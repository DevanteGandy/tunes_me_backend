from django.urls import path
from .views import ListMusicView , PostMusicView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('music/', ListMusicView.as_view(), name="music-all"),
    path('music1/', csrf_exempt(PostMusicView.as_view()), name="music-all")

]