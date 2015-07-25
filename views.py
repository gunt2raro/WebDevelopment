from django.shortcuts import render
from .models import Parentitem
from .utils import Utils

def home( request ) : 

    context = {
        
        'title' : 'Home',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Home' )
    
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
    
def marketing( request ) :
    
    context = {
    
        'title' : 'Marketing',
        'menu_gen' : ''#Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "marketing/index.html" )
    
def portfolio( request ) :
    
    context = {
    
        'title' : 'Portfolio',
        'menu_gen' : ''#Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "portfolio/index.html" )
    
def products( request ) :
    
    context = {
    
        'title' : 'Products',
        'menu_gen' : ''#Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "products/index.html" )
    
def about( request ) :
    
    context = {
    
        'title' : 'About Us',
        'menu_gen' : ''#Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "about/index.html" )
    
def contact( request ) :
    
    context = {
    
        'title' : 'Contact',
        'menu_gen' : ''#Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "contact/index.html" )