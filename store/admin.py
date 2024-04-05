from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','stock','price','category','modified_date','is_avaiable']
    prepopulated_fields = {'slug':('product_name',)}
    
    # def get_available_sizes(self, obj):
    #     return ", ".join([size.size for size in obj.availabel_size.all()])
    # get_available_sizes.short_description = 'Availabel Size'
  

# class AvailabelAdmin(admin.ModelAdmin):
#     list_display = ['size','price']
# # Register your models here.
# admin.site.register(AvailableSize,AvailabelAdmin)
admin.site.register(Product,ProductAdmin)
