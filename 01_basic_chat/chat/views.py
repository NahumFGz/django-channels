from rest_framework.generics import ListCreateAPIView

from .models import Message
from .serializers import MessageSerializer


class MessageListCreateAPIView(ListCreateAPIView):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerializer
