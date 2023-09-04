from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('home/', views.home),
    path('about/', views.about),
    # Urls For Article
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_view'),
    path('article/create', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/Delete', views.ArticleDeleteView.as_view(), name='article_delete'),
    # Urls For Authors
    path('authors', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_view'),
    path('author/create', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/update', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author_delete'),
]