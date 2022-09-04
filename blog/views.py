from django.shortcuts import render

# Create your views here.
# ListViewはオブジェクトをリスト表示するための機能←今回で言えば、ブログ記事を一覧表示できるようになる
from django.views.generic import ListView, DetailView
from blog.models import Post

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
