from rest_framework import permissions


class Appoint(permissions.BasePermission):

    def can_appoint(self, request, view, obj):
        return obj.creator == request.user
