from django.http import request
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

import urllib
import json

from urllib.parse import quote

# Create your views here.
def index(request):
    if (request.GET.get('page') != None) :
        next_page = int(request.GET.get('page')) + 1
        prev_page = next_page - 2
    else: next_page = 2

    url = 'https://api.hh.ru/vacancies?area=40&text={}&page={}'.format(quote("разработчик"), next_page-1)
    serialized_data = urllib.request.urlopen(url).read()
    data = json.loads(serialized_data)
    posts = [x['name'] for x in data['items']]

    context = {'posts': posts, 'next_page': next_page, 'prev_page': prev_page}
    return render(request, 'hhboard/board.html', context)
