from django.contrib import admin
from .models import Category, Brand, Product

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'imageUrl')  # Customize the list display
    search_fields = ('title',)  # Add search capability

# Register the Brand model
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'imageUrl')  # Customize the list display
    search_fields = ('title',)  # Add search capability

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_featured', 'category')  # Customize the list display
    search_fields = ('title',)  # Add search capability
    list_filter = ('category', 'is_featured')  # Add filters to the right side
    prepopulated_fields = {'title': ('title',)}  # Auto-populate the title field based on the title value

