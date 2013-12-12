from django.shortcuts import render_to_response, get_object_or_404, \
                             redirect
from django.http import HttpResponse
from pages.models import Page

# Create your views here.
def home(request):
    return render_to_response('pages/home.html', dict())

    
def list(request):
    context = dict(words=Page.objects.all())
    return render_to_response('pages/list.html', context)


def details(request, word_name):

    # check if the the page is in the database, add it if not
    if len(Page.objects.filter(word=word_name)) == 0:
        return redirect('add_word')
    else:
        page = get_object_or_404(Page, word=word_name)

    context = dict(word=page)
    return render_to_response('pages/details.html', context)


def edit(request, word_name):
    page = get_object_or_404(Page, word=word_name)
    context = dict(word=page)
    return render_to_response('pages/edit.html', context)


def add_word(request):
    return render_to_response('pages/add_word.html', dict())


def update_view(request):
    word_name = request.GET.get('word_name').capitalize()

    # check if the the page is in the database, add it if not
    if len(Page.objects.filter(word=word_name)) == 0:
        page = Page(word=word_name)
    else:
        page = get_object_or_404(Page, word=word_name)

    new_text = request.GET.get('new_text')
    page.text = new_text
    page.save()
    context = dict(word=page)
    return redirect('details', word_name)
