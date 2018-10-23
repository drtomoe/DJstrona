from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
# '.' oznacza aktualny katalog

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #pierwsze to ścieżka '/home/', adres skąd ją wziąść i nazwać
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   #<pk> primary key dla danego posta
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #tu ten sam .html co post-create
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),  # nazwa do wywoływania href="{% url 'blog-home'%}"
]