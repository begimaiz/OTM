from django.shortcuts import HttpResponse


def index(request):

    return HttpResponse('hey, this is NOtes')
