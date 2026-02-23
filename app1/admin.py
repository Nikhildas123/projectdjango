from django.contrib import admin
from .models import book 
# Register your models here.
# class bookadmin(admin.ModelAdmin):
#     list_display=("title","author","price","pub_date")
#     list_filter=("author",)
#     search_fields=("title","author",)
#     ordering=("pub_date",)
    #   list_editable=("price",)

class bookadmin(admin.ModelAdmin):
    list_display=('title','author','price','pub_date')

    actions=['markfree']
    

    def markfree(self,request,queryset):

        queryset.update(price=0)
        self.message_user(request,"the book are now free")
    markfree.short_description="books are free"
    
    


admin.site.register(book,bookadmin)

