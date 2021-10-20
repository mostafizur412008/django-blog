from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:url>', views.post),
    path('category/<slug:url>', views.category),
    path('about/',views.about),
]