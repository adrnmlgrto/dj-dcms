from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


@login_required
def homepage(request: HttpRequest):
    return render(request, 'base.html')
