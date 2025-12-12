from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField


class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(max_length=5000, blank=True)
    is_published = models.BooleanField(default=False)
    featured_image = models.ImageField(
        upload_to='stories/',
        blank=True, null=True
    )

    origin_country = CountryField(blank=True)
    origin_region = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
