from django.test import TestCase
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from .models import Story


class StoryModelTests(TestCase):
    def test_defaults(self):
        """
        Test that default values are set correctly upon creation.
        """
        story = Story.objects.create(
            title="My First Story",
            content="Some content",
        )
        self.assertFalse(story.is_published)
        self.assertIsNotNone(story.created_at)

    def test_str_returns_title(self):
        """
        Test that the string representation of the Story model
        returns the title.
        """
        story = Story.objects.create(
            title="Readable Title",
            content="Some content",
        )
        self.assertEqual(str(story), "Readable Title")

    def test_slug_autogenerates_from_title_on_save(self):
        """
        Test that the slug is automatically generated
        from the title upon saving.
        """
        story = Story.objects.create(
            title="Hello World!",
            content="Some content",
        )
        self.assertEqual(story.slug, slugify("Hello World!"))

    def test_slug_not_overwritten_if_already_set(self):
        """
        Test that the slug is not overwritten if it is
        already set before saving.
        """
        story = Story.objects.create(
            title="Hello World!",
            slug="custom-slug",
            content="Some content",
        )
        story.title = "Changed Title"
        story.save()
        self.assertEqual(story.slug, "custom-slug")

    def test_ordering_is_by_title(self):
        """
        Test that the default ordering of Story instances
        is by title.
        """
        Story.objects.create(title="Banana", content="x")
        Story.objects.create(title="Apple", content="x")
        Story.objects.create(title="Cherry", content="x")

        titles = list(Story.objects.values_list("title", flat=True))
        self.assertEqual(titles, ["Apple", "Banana", "Cherry"])

    def test_origin_country_is_required(self):
        """
        Test that the origin_country field is required.
        """
        story = Story(title="No Country Story", content="Some content")
        with self.assertRaises(ValidationError):
            story.full_clean()
