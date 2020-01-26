"""Publications model."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

from curso_api_rest.publications.models.categories import Category

# Utilities
from curso_api_rest.utils.models import BaseModel


class Publication(BaseModel):
    """Publications model."""
    TYPE_OF_PUBLICATION = (
        (1, 'new'),
        (2, 'old'),
    )
    profile = models.ForeignKey(
        'users.Profile', on_delete=models.CASCADE,
        related_name='publications',
    )
    title = models.CharField(
        _('title'),
        max_length=255
    )

    description = models.CharField(
        _('description'),
        max_length=255
    )

    type_of_publication = models.IntegerField(
        choices=TYPE_OF_PUBLICATION, default=1, db_index=True
    )
    price = models.DecimalField(
        _('price'),
        default=0, max_digits=16, decimal_places=2
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )

    is_active = models.BooleanField(
        _('is active'), default=True,
    )

    class Meta:
        verbose_name = 'publication'
        verbose_name_plural = 'publications'

    def __str__(self):
        """Return publication title."""
        return "#{}".format(self.title)

    def get_pictures(self):
        """Get all images of the publication"""
        return self.pictures.all()


class PublicationPicture(BaseModel):
    """PublicationPicture model."""
    profile = models.ForeignKey(
        Publication,
        related_name='pictures',
        on_delete=models.CASCADE
    )
    picture = models.ImageField(
        _('publication picture'),
        upload_to='publications/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        """Return pictures."""
        return "{}".format(self.picture)