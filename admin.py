from django.contrib import admin
from .forms import ParentitemForm
from .forms import ChilditemForm
from .models import Parentitem
from .models import Childitem

#ManuForm
#The Menu Item Admin
class ParentitemAdmin( admin.ModelAdmin ) :
    
    list_display = [ "__unicode__", "url", "timestamp", "updated" ]
    form = ParentitemForm
    
class ChilditemAdmin( admin.ModelAdmin ) : 
    
    list_display = [ "__unicode__", "url", "timestamp", "updated", "parentitem" ]
    form = ChilditemForm
    
admin.site.register( Parentitem, ParentitemAdmin )
admin.site.register( Childitem, ChilditemAdmin )