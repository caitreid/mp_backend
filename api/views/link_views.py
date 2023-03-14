from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.link import Link
from ..serializers import LinkSerializer

# Create your views here.
class Links(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = LinkSerializer
    def get(self, request):
        """Index request"""
        # Get all the links:
        # links = Link.objects.all()
        # Filter the links by owner, so you can only see your owned links
        links = Link.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = LinkSerializer(links, many=True).data
        return Response({ 'links': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['link']['owner'] = request.user.id
        # Serialize/create link
        link = LinkSerializer(data=request.data['link'])
        # If the link data is valid according to our serializer...
        if link.is_valid():
            # Save the created link & send a response
            link.save()
            return Response({ 'link': link.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(link.errors, status=status.HTTP_400_BAD_REQUEST)

class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the link to show
        link = get_object_or_404(Link, pk=pk)
        # Only want to show owned links?
        if request.user != link.owner:
            raise PermissionDenied('Unauthorized, you do not own this link')

        # Run the data through the serializer so it's formatted
        data = LinkSerializer(link).data
        return Response({ 'link': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate link to delete
        link = get_object_or_404(Link, pk=pk)
        # Check the link's owner against the user making this request
        if request.user != link.owner:
            raise PermissionDenied('Unauthorized, you do not own this link')
        # Only delete if the user owns the  link
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Link
        # get_object_or_404 returns a object representation of our Link
        link = get_object_or_404(Link, pk=pk)
        # Check the link's owner against the user making this request
        if request.user != link.owner:
            raise PermissionDenied('Unauthorized, you do not own this link')

        # Ensure the owner field is set to the current user's ID
        request.data['link']['owner'] = request.user.id
        # Validate updates with serializer
        data = LinkSerializer(link, data=request.data['link'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
