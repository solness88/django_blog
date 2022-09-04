from django.urls import path
from blog.views import PostList, PostDetail

#トップページにアクセスしたら、PostListで設定されている内容が反映される
urlpatterns = [
    path("", PostList.as_view(), name = "post_list"),
    path("post/<int:pk>/", PostDetail.as_view(), name = "post_detail"),
]


