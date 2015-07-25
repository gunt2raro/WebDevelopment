from django.shortcuts import render
from .models import Parentitem
from .utils import Utils

def home( request ) : 

    context = {
        
        'title' : 'Home',
        'menu_gen' : '',#Utils().create_menu( Parentitem.objects.all(), 'Home' )
    
    }

    return render( request, "home/index.html", context )
    
def development( request ) :
    
    context = {
    
        'title' : 'Development',
        'menu_gen' : '',#Utils().create_menu( Parentitem.objects.all(), 'Development' )
        
    }

    return render( request, "development/index.html" )
    
def design( request ) :
    
    context = {
    
        'title' : 'Design',
        'menu_gen' : ''#Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "design/index.html" )