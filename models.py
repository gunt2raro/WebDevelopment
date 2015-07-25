from django.db import models

#Menu Class model
class Parentitem( models.Model ) : 
    
    #parameters
    name = models.CharField( max_length=50 )#the name of the menu item
    description = models.CharField( max_length = 200 )#description of the menu item
    url = models.CharField( max_length=200, default = True )#url in case it needs an especific url
    position = models.IntegerField( default = 0 )#date of position on the menu
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    #unicode return
    def __unicode__( self ) :
	    return self.name
	
#End of menu class model

#Menu child item class model
class Childitem( models.Model ) :
    
    #parameters
    name = models.CharField( max_length = 50 )
    description = models.CharField( max_length = 200 )
    url = models.CharField( max_length = 200, default = 'url' )
    position = models.IntegerField( default = 0 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    parentitem = models.ForeignKey( Parentitem, default=1 )
    
    #unicode return
    def __unicode__( self ) :
	    return self.name
	    
#End of Child_menu_item Class Model