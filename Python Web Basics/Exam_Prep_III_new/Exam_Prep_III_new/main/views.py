from django.shortcuts import render, redirect

from Exam_Prep_III_new.main.forms import ProfileForm, CreateBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from Exam_Prep_III_new.main.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def show_home(request):
    if get_profile():
        profile = get_profile()
        books = list(Book.objects.all())
        first_books = []

        if books:
            for ind, book in enumerate(books):
                if ind % 3 == 0:
                    first_books.append(book)
            context = {
                'profile': profile,
                'books': books,
                'first_book': books[0],
                'first_books': first_books
            }
        else:
            context = {
                'profile': profile,
                'books': books,
            }
        return render(request, 'home-with-profile.html', context)
    return create_profile (request)

def show_profile(request):
    if get_profile():
        profile = get_profile()
        books = list(Book.objects.all())

        context = {
            'profile': profile,
            'books': books,
            'books_numb': len(books),
        }

        return render(request, 'profile.html', context)

def details_book(request, pk):
    if get_profile():
        profile = get_profile()
        book = Book.objects.get(pk=pk)
        context = {
            'book': book,
            'profile': profile
        }

        return render(request, 'book-details.html', context)



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

def edit_profile(request):
    return profile_action(request, EditProfileForm, 'show profile', get_profile(), 'edit-profile.html')

def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'home', get_profile(), 'delete-profile.html')


#expenses:
def book_action(request, form_class, success_url, instance, template_name):
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
        'book': instance,
        'profile': profile
    }
    return render(request, template_name, context)

def create_book(request):
    return book_action(request, CreateBookForm, 'home', Book(), 'add-book.html')

def edit_book(request, pk):
    return book_action(request, EditBookForm, 'home', Book.objects.get(pk=pk), 'edit-book.html')

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')
