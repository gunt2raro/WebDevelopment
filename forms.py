from django import forms
from .models import Menu

class MenuForm( forms.ModelForm ) :
    
    description = forms.CharField(widget=forms.Textarea)
    
    class Meta : 
        
        model = Menu
        fields = [ 'id', 'position', 'name', 'description' ]
       
    def clean_description( self ) :
        
        description = self.cleaned_data.get( 'description' )
    
        if not description :
            
            raise forms.ValidationError( 'Please add a description to the menu item.' )
        
        return description
        
    def clean_name( self ) :
        
        name = self.cleaned_data.get( 'name' )
        
        if not name :
            
            raise forms.ValidationError( 'Pelase add a Name to menu item.' )

        return name
