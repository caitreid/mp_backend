from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.theme import Theme
from ..serializers import ThemeSerializer

# Create your views here.
class Themes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ThemeSerializer
    def get(self, request):
        """Index request"""
        # Get all the themes:
        # themes = Theme.objects.all()
        # Filter the themes by owner, so you can only see your owned themes
        themes = Theme.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ThemeSerializer(themes, many=True).data
        return Response({ 'themes': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['theme']['owner'] = request.user.id
        # Serialize/create theme
        theme = ThemeSerializer(data=request.data['theme'])
        # If the theme data is valid according to our serializer...
        if theme.is_valid():
            # Save the created theme & send a response
            theme.save()
            return Response({ 'theme': theme.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(theme.errors, status=status.HTTP_400_BAD_REQUEST)

class ThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the theme to show
        theme = get_object_or_404(Theme, pk=pk)
        # Only want to show owned themes?
        if request.user != theme.owner:
            raise PermissionDenied('Unauthorized, you do not own this theme')

        # Run the data through the serializer so it's formatted
        data = ThemeSerializer(theme).data
        return Response({ 'theme': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate theme to delete
        theme = get_object_or_404(Theme, pk=pk)
        # Check the theme's owner against the user making this request
        if request.user != theme.owner:
            raise PermissionDenied('Unauthorized, you do not own this theme')
        # Only delete if the user owns the  theme
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Theme
        # get_object_or_404 returns a object representation of our Theme
        theme = get_object_or_404(Theme, pk=pk)
        # Check the theme's owner against the user making this request
        if request.user != theme.owner:
            raise PermissionDenied('Unauthorized, you do not own this theme')

        # Ensure the owner field is set to the current user's ID
        request.data['theme']['owner'] = request.user.id
        # Validate updates with serializer
        data = ThemeSerializer(theme, data=request.data['theme'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
