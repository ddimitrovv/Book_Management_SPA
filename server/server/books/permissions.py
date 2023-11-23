from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    This permission checks whether the authenticated user is the owner of the object.

    Usage:
    - Attach this permission to a view or viewset where object ownership needs to be enforced.

    Example:
    ```python
    class YourApiView(APIView):
        permission_classes = [IsOwner, ]

        def get(self, request, *args, **kwargs):
            # Your view logic here
    ```
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the authenticated user is the owner of the object.

        Parameters:
        - request: The HTTP request object.
        - view: The Django Rest Framework view.
        - obj: The object being accessed.

        Returns:
        - bool: True if the user is the owner, False otherwise.
        """

        return obj.owner.user == request.user
