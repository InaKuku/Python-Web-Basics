from django.shortcuts import render, redirect

from Exam_Prep_IV.main.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Exam_Prep_IV.main.models import Recipe


def show_home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
        'recipes_numb': len(recipes),
    }
    return render(request, 'index.html', context)



def details_recipe(request, pk):

        recipe = Recipe.objects.get(pk=pk)
        recipe_ingrediens = []
        recipe_ingrediens = recipe.ingredients.split(', ')
        context = {
            'recipe': recipe,
            'recipe_ingrediens': recipe_ingrediens
        }

        return render(request, 'details.html', context)


#recipes:
def recipe_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'recipe': instance,
    }
    return render(request, template_name, context)

def create_recipe(request):
    return recipe_action(request, CreateRecipeForm, 'home', Recipe(), 'create.html')

def edit_recipe(request, pk):
    return recipe_action(request, EditRecipeForm, 'home', Recipe.objects.get(pk=pk), 'edit.html')

def delete_recipe(request, pk):
    return recipe_action(request, DeleteRecipeForm, 'home', Recipe.objects.get(pk=pk), 'delete.html')

