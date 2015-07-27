from django.shortcuts import render
from .models import Parentitem
from .utils import Utils

def home( request ) : 

    context = {
        
        'title' : 'Home',
        'subtitle' : 'You say it, we make it',
        'menu_gen' : Utils().create_menu( Parentitem.objects.order_by( 'position' ), 'Home' )
    
    }

    return render( request, "home/index.html", context )
    
def development( request ) :
    
    context = {
    
        'title' : 'Development',
        'subtitle' : 'Developers',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Development' )
    }

    return render( request, "development/index.html", context )
    
def design( request ) :
    
    context = {
    
        'title' : 'Design',
        'subtitle' : 'Spectacular design',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Design' )
        
    }
    
    return render( request, "design/index.html", context )
    
def marketing( request ) :
    
    context = {
    
        'title' : 'Marketing',
        'subtitle' : 'Be everywhere',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Marketing' )
        
    }
    
    return render( request, "marketing/index.html", context )
    
def portfolio( request ) :
    
    context = {
    
        'title' : 'Portfolio',
        'subtitle' : 'Portfolio',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Portfolio' )
        
    }
    
    return render( request, "portfolio/index.html", context )
    
def products( request ) :
    
    context = {
    
        'title' : 'Products',
        'subtitle' : 'Our creations',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Products' )
        
    }
    
    return render( request, "products/index.html", context )
    
def about( request ) :
    
    context = {
    
        'title' : 'About Us',
        'subtitle' : 'Us',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'About Us' )
        
    }
    
    return render( request, "about/index.html", context )
    
def contact( request ) :
    
    context = {
    
        'title' : 'Contact',
        'subtitle' : 'With you all the time',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Contact' )
        
    }
    
    return render( request, "contact/index.html", context )
    
def pricing( request ) :
    
    context = {
    
        'title' : 'Pricing',
        'subtitle' : 'Hire us in just a click',
        'menu_gen' : Utils().create_menu( Parentitem.objects.all(), 'Pricing' )
        
    }
    
    return render( request, "pricing/index.html", context )
    
def coming( request ) :
    
    context = {
    
        'title' : 'Under Construction',
        'subtitle' : 'Stay in contact with us, sorry for the inconvenience.'
        
    }
    
    return render( request, "coming/index.html", context )