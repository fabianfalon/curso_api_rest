"""Profile model."""

# Django
from django.db import models

# Utilities
from curso_api_rest.utils.models import BaseModel


class Profile(BaseModel):
    """Profile model."""

    STATUS_CHOICES = (
        (1, 'active'),
        (2, 'inactive'),
    )

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    picture = models.ImageField(
        "profile picture",
        upload_to="users/pictures/",
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, db_index=True)
    address = models.CharField("address", max_length=255, blank=True)

    class Meta:
        db_table = "profile"
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)