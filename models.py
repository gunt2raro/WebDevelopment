from django.db import models

#Menu Class model
class Parentitem( models.Model ) : 
    
    #parameters
    name = models.CharField( max_length=50, null = False, unique=True )#the name of the menu item
    description = models.CharField( max_length = 200 )#description of the menu item
    url = models.CharField( max_length=200, null = True, default='url' )#url in case it needs an especific url
    position = models.IntegerField()#date of position on the menu
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    #unicode return
    def __unicode__( self ) :
	    return self.name
	
#End of menu class model

#Menu child item class model
class Childitem( models.Model ) :
    
    #parameters
    name = models.CharField( max_length = 50, null = False, unique = True )
    description = models.CharField( max_length = 200, null = True, default = '' )
    url = models.CharField( max_length = 200, null = True, default = 'url' )
    position = models.IntegerField( null = True, default = 0 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    
    #unicode return
    def __unicode__( self ) :
	    return self.name
	    
#End of Child_menu_item Class Model