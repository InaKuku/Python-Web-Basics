from django.shortcuts import render, redirect

from Exam_Prep_I.job.forms import ProfileForm, CreateExpenseForm, EditExpenseForm, DeleteExpenseForm, EditProfileForm, \
    DeleteProfileForm
from Exam_Prep_I.job.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def show_home(request):
    if get_profile():
        profile = get_profile()
        expenses = list(Expense.objects.filter(expenses_creator=profile))
        context = {
            'profile': profile,
            'expenses': expenses,
            'expenses_numb': len(expenses),
            'all_expenses': sum(x.price for x in expenses),
            'budget_left': profile.budget - sum(x.price for x in expenses),
        }
        return render(request, 'home-with-profile.html', context)
    return create_profile(request)

def show_profile(request):
    profile = get_profile()
    expenses = list(Expense.objects.filter(expenses_creator=profile))

    context ={
        'profile': profile,
        'expenses': expenses,
        'expenses_numb': len(expenses),
        'all_expenses': sum(x.price for x in expenses),
        'budget_left': profile.budget - sum(x.price for x in expenses),
    }

    return render(request, 'profile.html', context)




#profile:
def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form
    }
    return render(request, template_name, context)

def create_profile(request):
    return profile_action(request, ProfileForm, 'home', Profile(), 'home-no-profile.html')

def edit_profile(request):
    return profile_action(request, EditProfileForm, 'show profile', get_profile(), 'profile-edit.html')

def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'home', get_profile(), 'profile-delete.html')


#expenses:
def expense_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'expense': instance,
    }
    return render(request, template_name, context)

def create_expense(request):
    return expense_action(request, CreateExpenseForm, 'home', Expense(), 'expense-create.html')

def edit_expense(request, pk):
    return expense_action(request, EditExpenseForm, 'home', Expense.objects.get(pk=pk), 'expense-edit.html')

def delete_expense(request, pk):
    return expense_action(request, DeleteExpenseForm, 'home', Expense.objects.get(pk=pk), 'expense-delete.html')


