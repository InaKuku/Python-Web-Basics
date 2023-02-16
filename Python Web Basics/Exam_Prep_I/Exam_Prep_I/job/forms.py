import os

from django import forms

from Exam_Prep_I.job.models import Profile, Expense


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image',)

        widgets={
            'profile_image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-file'
                }
            )
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }
        widgets={
            'profile_image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-file'
                }
            )
        }

class DeleteProfileForm(forms.ModelForm):
    def save(self, commit = True):
        image_path = self.instance.profile_image.path
        os.remove(image_path)
        self.instance.delete()
        Expense.objects.all().delete()
        return self.instance

    class Meta:
        model=Profile
        fields=()

class CreateExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields='__all__'
        labels = {
            'expense_image': 'Link to Image'
        }


class EditExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields='__all__'
        labels = {
            'expense_image': 'Link to Image'
        }


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
            self.fields[field].required = False

    def save(self, commit = True):
        self.instance.delete()
        return self.instance

    class Meta:
        model=Expense
        fields = '__all__'
        labels = {
            'expense_image': 'Link to Image'
        }
