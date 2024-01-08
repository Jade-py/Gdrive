from rest_framework.serializers import ModelSerializer
from .models import Storage_Folder, Storage_File


class Storage_Folder_Serializer(ModelSerializer):
    class Meta:
        model = Storage_Folder
        fields = '__all__'


class Storage_File_Serializer(ModelSerializer):
    folder = Storage_Folder_Serializer()
    class Meta:
        model = Storage_File
        fields = '__all__'