from django.shortcuts import render
from .data_processor import qr_maker, sid_finder


def index(request):
    context = {
        'list_qr_images': qr_maker(),
        'list_sid': sid_finder()
    }

    return render(request, "index.html", context)

