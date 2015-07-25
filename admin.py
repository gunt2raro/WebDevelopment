from django.contrib import admin
from .forms import ParentitemForm
from .models import Parentitem

#ManuForm
#The Menu Item Admin
class ParentitemAdmin( admin.ModelAdmin ) :
    
    list_display = [ "__unicode__", "timestamp", "updated" ]
    form = ParentitemForm
    
admin.site.register( Parentitem, ParentitemAdmin )