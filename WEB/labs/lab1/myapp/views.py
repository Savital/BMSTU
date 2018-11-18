from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    notes = Note.objects
    template = loader.get_template('index.html')
    context = {'notes': notes}
    return render(request, 'index.html', context)
    #return render_to_response('index.html')

# Create your views here.
#def home(request):
#    notes = Note.objects
#    template = loader.get_template('index.html')
#    context = {'notes': notes}
#    return render(request, 'note.html', context)
#    # return render_to_response("note.html", notes)
