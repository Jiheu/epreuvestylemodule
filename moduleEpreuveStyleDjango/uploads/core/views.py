from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from reportlab.pdfgen import canvas


def home(request):

    documents = Document.objects.all()

    return render(request, 'core/home.html', {'documents': documents})


def upload(request):

    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            return render(request, 'core/upload.html', {'form': form})
    else:
        form = DocumentForm()
    return render(request, 'core/upload.html', {'form': form})
    """
    return HttpResponse("UPLOAD")


def vote(request):

    return HttpResponse("VOTE")


def classement(request):

    return HttpResponse("CLASSEMENT")
