from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .admin_mixins import ExportAsCSVMixin
from .models import Product, Order


# Register your models here.
class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description="Archive")
def mark_archived(modeladmin: admin.ModelAdmin, request:HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description="Unrchive")
def mark_unarchived(modeladmin: admin.ModelAdmin, request:HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [mark_unarchived, mark_archived, "export_csv"]
    inlines = [OrderInline, ]
    list_display = ["pk", "name", "description_short", "description_short_admin", "price", "discount", "created_at",
                    "archived"]
    list_display_links = ["pk", "name"]
    ordering = ["-pk", "name", ]
    search_fields = "name", "description",
    fieldsets = [
        ("Text", {"fields": ("name", "description", ), }),
        ("Price", {"fields": ("price", "discount", ), "classes": ("collapse","wide",), }),
        ("extra", {"fields": ("archived", ), "classes": ("collapse", "wide",),
                   "description":"Extra option" }),
    ]

    def description_short_admin(self, obj: Product) -> str:
        return obj.description if len(obj.description) < 20 else obj.description[:20] + "..."


class ProdictInlineT(admin.TabularInline):
    model = Order.products.through


class ProdictInlineS(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProdictInlineT, ProdictInlineS, ]
    list_display = ["pk", "delivery_address", "promocode", "created_at", "user_verbose"]
    list_display_links = ["pk", "delivery_address"]

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

    # ordering = ["-pk", "name",]
    # search_fields = "name", "description",

    # def description_short_admin(self, obj: Product) -> str:
    #    return obj.description if len(obj.description) < 20 else obj.description[:20] + "..."

# admin.site.register(Product, ProductAdmin)
