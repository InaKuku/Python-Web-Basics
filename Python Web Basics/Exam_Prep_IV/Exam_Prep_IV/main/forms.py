from django import forms

from Exam_Prep_IV.main.models import Recipe



class CreateRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields=('title', 'image_url', 'description', 'ingredients', 'time')

        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }


class EditRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')

        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }

class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
            self.fields[field].required = False

    def save(self, commit = True):
        self.instance.delete()
        return self.instance

    class Meta:
        model=Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')

