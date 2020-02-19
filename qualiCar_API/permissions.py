from rest_framework import permissions


class UpdateOwnProfile (permissions.BasePermission):
    """ Allow user to edit their own profile """

    def has_object_permission (self, request, view, obj):
        """ Check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True

        # Return the Boolean of the comparison
        # In this case, return true if the user is changing its own profile
        return obj.id == request.user.id
