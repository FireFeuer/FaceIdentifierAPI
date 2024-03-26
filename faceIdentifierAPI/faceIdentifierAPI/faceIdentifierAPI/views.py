from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadedImageSerializer
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import ListAPIView



class UploadImageView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Привет, картинка!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





