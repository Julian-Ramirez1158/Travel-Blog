from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.about, name="about"),
    path('faq', views.faq, name="faq"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]