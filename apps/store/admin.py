from django.contrib import admin

from .models import Category, Product, ProductImage, ProductReview

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_featured', 'num_available']
    list_editable = ['price', 'is_featured', 'num_available']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}

    class Meta:
        ordering = ['name']
admin.site.register(ProductImage)
admin.site.register(ProductReview)