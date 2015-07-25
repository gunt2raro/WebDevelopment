from django import forms
from .models import Parentitem
from .models import Childitem

class ParentitemForm( forms.ModelForm ) :
    
    description = forms.CharField(widget=forms.Textarea)
    
    class Meta : 
        
        model = Parentitem
        fields = [ 'name', 'position', 'description', 'url' ]
    
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

class ChilditemForm( forms.ModelForm ) :
    
    description = forms.CharField(widget=forms.Textarea)
    
    class Meta : 
        
        model = Childitem
        fields = [ 'name', 'position', 'description', 'url', 'parentitem' ]
    
    def clean_description( self ) :
        
        description = self.cleaned_data.get( 'description' )
    
        if not description :
            
            raise forms.ValidationError( 'Please add a description to the child menu item.' )
        
        return description
    
    def clean_name( self ) :
        
        name = self.cleaned_data.get( 'name' )
        
        if not name :
            
            raise forms.ValidationError( 'Pelase add a Name to child menu item.' )

        return name
