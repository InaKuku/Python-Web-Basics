from django import forms

from Exam_Prep_III_new.main.models import Profile, Book


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            ),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL'
        }


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url',)


        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL'
        }

class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
            self.fields[field].required = False

    def save(self, commit = True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    class Meta:
        model=Profile
        fields = ('first_name', 'last_name', 'image_url',)

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL'
        }

class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        # fieldsets = [
        #     ('main',
        #      {'fields': ['title', 'description', 'image', 'type'],
        #       'legend': 'Add New Book'})],
        fields=('title', 'description', 'image', 'type')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..'
                }
            ),
        }



class EditBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields=('title', 'description', 'image', 'type')




