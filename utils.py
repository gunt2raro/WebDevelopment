import HTMLParser

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
                    
                str_gen.append( active_str )
                str_gen.append( '<a href="#" class="dropdown-toggle" data-toggle="dropdown">' )
                str_gen.append( item.name )
                str_gen.append( '</a>' )
                str_gen.append( '</li> <!-- dropdown -->' )
            
            s = HTMLParser.HTMLParser( )
        
        return s.unescape( '' . join( str_gen ) )
        
#End of utils class