from storages.backends.s3boto3 import S3ManifestStaticStorage, S3Boto3Storage


class StaticStorage(S3ManifestStaticStorage):
    location = "static"
    default_acl = "public-read"


class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
