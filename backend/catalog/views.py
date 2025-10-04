from rest_framework import viewsets, permissions
from .models import ClothingItem
from .serializers import ClothingItemSerializer

class ClothingItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clothing items to be viewed or edited.
    """
    serializer_class = ClothingItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the clothing items
        for the currently authenticated user.
        """
        return self.request.user.clothing_items.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Assign the current user as the owner of the new clothing item.
        """
        serializer.save(owner=self.request.user)