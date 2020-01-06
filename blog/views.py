from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post

app_name = 'news'


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    # tag = None

    # if tag_slug:
    #   tag = get_object_or_404(Tag, slug=tag_slug)
    #  object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)  # 3 post in each page.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if it aint no integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if the page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/post/list.html', {'page': page, 'posts': posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'news/post/list.html'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    # list of active comments for this posts
    # comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # some sick ass dude made a comment
        pass
        """comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create comment object but dont save it
            new_comment = comment_form.save(commit=False)
            # assign current post to the comment
            new_comment.post = post
            # save the comment to the db
            new_comment.save()"""
    else:
        # comment_form = CommentForm()
        pass

    # list of similar posts
    # post_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    # similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'news/' + request.tenant + '/post/detail.html', {'post': post})


