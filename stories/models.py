from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from django_ckeditor_5.fields import CKEditor5Field


class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = CKEditor5Field("Content", config_name="default")
    is_published = models.BooleanField(default=False)
    featured_image = models.ImageField(
        upload_to='stories/',
        blank=True, null=True
    )

    origin_country = CountryField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Stories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
