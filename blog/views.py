import random

from django.shortcuts import render, get_object_or_404

from blog.models import Post
from blog.models import Wanted
from spending_money.models import Spend


def home(request):
    return render(request, "blog/home.html", {
        'y': Wanted.objects.count(),
        'x': Post.objects.count(),
        'object_list': Post.objects.order_by('-id').all(),
        'object_spend_list': Spend.objects.order_by('date').all(),
        'object_wanted_list': Wanted.objects.order_by('-id').all(),
    })


def single_post(request, pk):
    return render(request, "blog/post.html", {
        #'object': Post.objects.get(pk=int(pk)),
        'object': get_object_or_404(Post, pk=int(pk)),
    })

def single_wanted(request, pk):
    return render(request, "blog/wanted.html", {
        #'object': Post.objects.get(pk=int(pk)),
        'object': get_object_or_404(Wanted, pk=int(pk)),
    })