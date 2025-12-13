from django.conf import settings
from django.contrib.staticfiles.storage import ManifestFilesMixin
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(ManifestFilesMixin, S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    default_acl = "public-read"
    file_overwrite = True
    manifest_strict = False


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    default_acl = "public-read"
    file_overwrite = False
