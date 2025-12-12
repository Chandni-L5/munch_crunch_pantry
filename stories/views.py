from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from .models import Story


def stories_intro(request):
    """ A view to return the origin stories index page """
    stories = Story.objects.filter(is_published=True).order_by("title")
    return render(
        request, "stories/stories_intro.html", {"stories": stories}
    )


def story_detail(request, slug):
    """ A view to return the details of a specific story """
    story = get_object_or_404(Story, slug=slug, is_published=True)
    return render(request, "stories/story.html", {"story": story})


@staff_member_required
def story_preview(request, slug):
    """Preview any story (published or not) for staff/admin only."""
    story = get_object_or_404(Story, slug=slug)
    return render(
        request,
        "stories/story.html",
        {"story": story, "is_preview": True}
    )
