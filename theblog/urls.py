from django.urls import path
from .views import CategoryView, LikeView,HomeView, ArticleDetailView, AddPostView, UserEditView,UserDeleteView, AddCommentView
urlpatterns = [
    path('', HomeView.as_view(), name = 'home' ),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail' ),
    path('article/edit/<int:pk>', UserEditView.as_view(), name = 'update-article' ),
    path('article/delete/<int:pk>', UserDeleteView.as_view(), name = 'delete-article' ),
    path('add_post/', AddPostView.as_view(), name = 'add_post' ),
    path('likes/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment' ),
]