from board.models import Post
from django.http import request
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'board/board.html'
    context_object_name = 'posts'
    paginate_by=2

    def get_queryset(self):
        self.filters = dict()
        for key in ['position']:
            if self.request.GET.get(key) != None:
                self.filters[key] = self.request.GET.get(key)
        return Post.objects.filter(**self.filters)
    

class UserView(generic.ListView):
    template_name = 'board/user.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
    