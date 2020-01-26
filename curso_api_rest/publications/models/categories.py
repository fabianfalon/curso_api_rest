"""Publications model."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Utilities
from curso_api_rest.utils.models import BaseModel


class Category(BaseModel):
    """Category model."""

    name = models.CharField(
        _('name'), max_length=255
    )
    is_active = models.BooleanField(
        _('is active'), default=True,
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """Return category name."""
        return "Category: {}".format(self.name)
