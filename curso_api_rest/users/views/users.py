"""users api views
"""

import logging

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

from curso_api_rest.users.models.users import User

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()