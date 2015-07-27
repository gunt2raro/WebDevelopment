import HTMLParser

from .models import Childitem

#Utils
#Helper document for the WebDevelopment application

#Utils class
class Utils :
    
    #Create menu
    #Class that returns a made menu
    #recieves a list of menu items
    #returns an html string
    @staticmethod
    def create_menu( items, active ) : 
        
        str_gen = []     
         
        if items :
            
            for item in items :
            
                active_str = '<li class="dropdown" >'
                
                if item.name == active :
                    
                    active_str = '<li class="dropdown active" >'
                
                children =  Childitem.objects.all().filter( parentitem = item )
                
                str_gen.append( active_str )
                str_gen.append( '<a href="/' )
                str_gen.append( item.url )
                str_gen.append( '/"  >' )
                str_gen.append( item.name )
                
                if children :
                    
                    str_gen.append( ' <b class="caret"></b></a>' )
                    str_gen.append( '<ul class="dropdown-menu">' )
                    
                    for child in children :
                        
                        str_gen.append( '<li><a href="/' ) 
                        str_gen.append( child.url )
                        str_gen.append( '/">' )
                        str_gen.append( child.name )
                        str_gen.append( '</a></li>' )
                    
                    str_gen.append( '</ul>' )
                    
                else :
                    
                    str_gen.append( '</a>' )
                    
                str_gen.append( '</li> <!-- dropdown -->' )
       
        return( '' . join( str_gen ) )
        
#End of utils class