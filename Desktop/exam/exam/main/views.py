from django.shortcuts import render, redirect

from exam.main.forms import ProfileForm, CreateAlbumForm, EditAlbumForm, DeleteProfileForm, \
    DeleteAlbumForm
from exam.main.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None



def show_home(request):
    if get_profile():
        profile = get_profile()
        albums = list(Album.objects.all())
        context = {
            'profile': profile,
            'albums': albums,
        }
        return render(request, 'home-with-profile.html', context)
    return create_profile(request)

def show_profile(request):
    profile = get_profile()
    albums = list(Album.objects.all())

    context ={
        'profile': profile,
        'albums': albums,
        'albums_numb': len(albums),
    }

    return render(request, 'profile-details.html', context)




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
    return profile_action(request, DeleteProfileForm, 'home', get_profile(), 'profile-delete.html')


#albums:
def album_action(request, form_class, success_url, instance, template_name):
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
        'album': instance,
        'profile': profile,
    }
    return render(request, template_name, context)

def create_album(request):
    return album_action(request, CreateAlbumForm, 'home', Album(), 'add-album.html')

def edit_album(request, pk):
    return album_action(request, EditAlbumForm, 'home', Album.objects.get(pk=pk), 'edit-album.html')

def delete_album(request, pk):
    return album_action(request, DeleteAlbumForm, 'home', Album.objects.get(pk=pk), 'delete-album.html')

def details_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
        'profile': profile
    }

    return render(request, 'album-details.html', context)