from django import forms

from exam.main.models import Profile, Album


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age',)
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
        }

class DeleteProfileForm(forms.ModelForm):
    def save(self, commit = True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model=Profile
        fields=()



class CreateAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre','description', 'image_URL', 'price')
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),

            'image_URL': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),
        }
        labels = {
            'album_name': 'Album Name'
        }

class EditAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields='__all__'
        labels = {
            'album_name': 'Album Name'
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
            self.fields[field].required = False

    def save(self, commit = True):
        self.instance.delete()
        return self.instance

    class Meta:
        model=Album
        fields = '__all__'

        labels = {
            'album_name': 'Album Name'
        }
