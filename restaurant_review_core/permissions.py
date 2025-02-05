from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class IsOwnerAdminOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object or admin users to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_permission(self, request, view):
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        # Let GET, HEAD, or OPTIONS requests pass to allowed read permissions to any request.
        if request.method in SAFE_METHODS:
            return True

        # Allow write permissions only if the user is the author or an admin.
        else:
            return bool(
                request.user and (request.user == obj.author or request.user.is_staff)
            )
