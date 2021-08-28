from rest_framework import viewsets
from apps.univ.models import Univ
from apps.univ.serializers import UnivSerializer


# Create your views here.
class UnivViewSet(viewsets.ModelViewSet):
    queryset = Univ.objects.all()
    serializer_class = UnivSerializer
