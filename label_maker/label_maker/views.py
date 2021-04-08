from django.shortcuts import render
from .data_processor import qr_maker


def index(request):
    context = {
        'list_qr_images': qr_maker()
    }

    return render(request, "index.html", context)

