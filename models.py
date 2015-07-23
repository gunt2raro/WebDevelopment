from django.db import models

#Menu Class model
class Menu( models.Model ) : 
    
    #parameters
    id = models.AutoField( primary_key=True )
    name = models.CharField( max_length=50, null = False )
    description = models.CharField( max_length = 200 )
    url = models.CharField( max_length=200, null = True, default='url' )
    position = models.IntegerField()
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    #unicode return
    def __unicode__( self ) :
	    return self.name