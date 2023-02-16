from django.shortcuts import render, redirect

from pattern.main.forms import ProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from pattern.main.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None



def show_home(request):
    if get_profile():
        profile = get_profile()
        notes = list(Note.objects.all())
        context = {
            'profile': profile,
            'notes': notes,
            'notes_numb': len(notes),
        }
        return render(request, 'home-with-profile.html', context)
    return create_profile(request)

def show_profile(request):
    profile = get_profile()
    notes = list(Note.objects.all())

    context ={
        'profile': profile,
        'notes': notes,
        'notes_numb': len(notes),
    }

    return render(request, 'profile.html', context)




#profile:
def profile_action(request, form_class, success_url, instance, template_name):
    profile = get_profile()
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, template_name, context)

def create_profile(request):
    return profile_action(request, ProfileForm, 'home', Profile(), 'home-no-profile.html')

def delete_profile(request):
    profile = get_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home')


#expenses:
def note_action(request, form_class, success_url, instance, template_name):
    profile = get_profile()
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'note': instance,
        'profile': profile,
    }
    return render(request, template_name, context)

def create_note(request):
    return note_action(request, CreateNoteForm, 'home', Note(), 'note-create.html')

def edit_note(request, pk):
    return note_action(request, EditNoteForm, 'home', Note.objects.get(pk=pk), 'note-edit.html')

def delete_note(request, pk):
    return note_action(request, DeleteNoteForm, 'home', Note.objects.get(pk=pk), 'note-delete.html')

def details_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
        'profile': profile
    }

    return render(request, 'note-details.html', context)