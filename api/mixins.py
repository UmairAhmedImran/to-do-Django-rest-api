from rest_framework import permissions
from .permission import isTodoEditor


class TodoEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, isTodoEditor]
