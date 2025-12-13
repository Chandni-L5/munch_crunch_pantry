from django.contrib.staticfiles.storage import ManifestFilesMixin
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(ManifestFilesMixin, S3Boto3Storage):
    location = "static"
    default_acl = None
    file_overwrite = True
    manifest_strict = True


class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = None
    file_overwrite = False
