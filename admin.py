from django.contrib import admin
from .forms import MenuForm
from .models import Menu

#ManuForm
#The Menu Item Admin
class MenuAdmin( admin.ModelAdmin ) :
    
    list_display = [ "id", "__unicode__", "timestamp", "updated", "position" ]
    form = MenuForm
    
    
    
admin.site.register( Menu, MenuAdmin )