from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, get_object_or_404
from .models import Storage_Folder, Storage_File
from .serializers import Storage_Folder_Serializer, Storage_File_Serializer


# Create your views here.
class FolderView(ListCreateAPIView):
    queryset = Storage_Folder.objects.all()
    serializer_class = Storage_Folder_Serializer


class FileView(ListCreateAPIView):

    def get_queryset(self):
        folder_name = self.kwargs['folder']
        folder = get_object_or_404(Storage_Folder, folder=folder_name)
        return Storage_File.objects.filter(folder=folder)


    serializer_class = Storage_File_Serializer
