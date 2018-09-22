from django import forms

from .models import Post, Descriptions

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'categorie', 'image')
		
class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Descriptions
        fields = ('corp',)
		
class ConnexionForm(forms.Form):
         username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm validate'}))
         password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)