from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@permission_classes([IsAuthenticated])  # Require authentication
@api_view(['GET'])
def handle_detrack_payload(request):
    return (request)