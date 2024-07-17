from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name="post-detail-view")
]
