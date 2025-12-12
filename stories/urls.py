from django.urls import path
from . import views

urlpatterns = [
    path("", views.stories_intro, name="origin_stories_index"),
    path("origins/<slug:slug>/", views.story_detail, name="story_detail"),
    path("preview/<slug:slug>/", views.story_preview, name="story_preview"),
]
