from django.shortcuts import render


from blog.models import Post
from .models import StaticInfo


def index(request):
    staticinfo = StaticInfo.objects.get(pk=1)

    newslist = Post.objects.all().order_by('-id')[:3]

    return render(request, 'pages/' + request.tenant + '/index.html',
                  {'staticinfo': staticinfo,'newslist': newslist,})


def about(request):
    staticinfo = StaticInfo.objects.get(pk=1)
    return render(request, 'pages/about.html', {'staticinfo': staticinfo})


def terms(request):
    staticinfo = StaticInfo.objects.get(pk=1)
    return render(request, 'pages/terms.html', {'staticinfo': staticinfo})


def privacy(request):
    staticinfo = StaticInfo.objects.get(pk=1)
    return render(request, 'pages/privacy.html', {'staticinfo': staticinfo})


def notfound(request, exception):
    staticinfo = StaticInfo.objects.get(pk=1)
    return render(request, 'pages/404.html', {'staticinfo': staticinfo})
