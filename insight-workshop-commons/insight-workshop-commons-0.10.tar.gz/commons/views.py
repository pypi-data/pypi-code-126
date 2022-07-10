from rest_framework.generics import CreateAPIView

from .serializers import FileSerializer
from .models import FileUpload


class FileView(CreateAPIView):
    serializer_class = FileSerializer
    queryset = FileUpload.objects.all()
