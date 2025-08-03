from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from comman.models import BaseModel
from users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("email"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=15)
    first_name = models.CharField(_("First name"), max_length=30, null=True, blank=True)
    last_name = models.CharField(_("Last name"), max_length=30, null=True, blank=True)
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
    )
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
