from django.contrib.auth.models import AbstractBaseUser
from SharingBookBE.settings import AVATAR_URI_PREFIX
from django.db import models
from books.models import Book
from categories.models import Category
from tags.models import Tag


class AdminType(object):
    REGULAR_USER = "Regular User"
    ADMIN = "Admin"
    SUPER_ADMIN = "Super Admin"
    TYPES = [REGULAR_USER, ADMIN, SUPER_ADMIN]


class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class User(AbstractBaseUser):
    created = models.DateTimeField(auto_now_add=True)

    # Profiles
    username = models.TextField(unique=True)
    email = models.TextField(null=True)

    # One of UserType
    admin_type = models.TextField(choices=AdminType.TYPES, default=AdminType.REGULAR_USER)

    reset_password_token = models.TextField(null=True)
    reset_password_token_expire_time = models.DateTimeField(null=True)

    # SSO auth token
    auth_token = models.TextField(null=True)
    session_keys = models.TextField(null=True)

    # open api key
    open_api = models.BooleanField(default=False)
    open_api_appkey = models.TextField(null=True)
    is_disabled = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def is_admin(self):
        return self.admin_type == AdminType.ADMIN

    def is_super_admin(self):
        return self.admin_type == AdminType.SUPER_ADMIN

    def is_admin_role(self):
        return self.admin_type in [AdminType.ADMIN, AdminType.SUPER_ADMIN]

    class Meta:
        ordering = ['created', ]


class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.TextField(null=True)
    credit = models.PositiveIntegerField(default=0)

    avatar = models.TextField(default=f"{AVATAR_URI_PREFIX}/default.png")

    # use json format
    books_read = models.TextField(null=True)
    books_reading = models.TextField(null=True)
    books_donated = models.TextField(null=True)
    favorite_books = models.TextField(null=True)
    favorite_tags = models.TextField(null=True)
    favorite_categories = models.TextField(null=True)

    class Meta:
        ordering = ['created']
