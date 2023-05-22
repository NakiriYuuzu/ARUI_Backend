from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from feature_api.serializer import *


class SkuView(APIView):
    @staticmethod
    def get(request):
        serializer = SKUListSerializer(SKU.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        sku_name = request.data.get('sku_name', None)
        sku_image = request.data.get('sku_image', None)

        if sku_name and sku_image:
            sku = SKU.objects.update_or_create(
                sku_name=sku_name,
                defaults={'sku_image': sku_image}
            )
            return Response({'message': 'SKU added successfully', 'sku_id': sku.sku_id}, status=status.HTTP_201_CREATED)

        return Response({'message': 'SKU name and image are required'}, status=status.HTTP_400_BAD_REQUEST)


class ButtonView(APIView):
    @staticmethod
    def get(request):
        serializer = ButtonListSerializer(Button.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        pass

    @transaction.atomic
    def delete(self, request):
        return Response({'message': 'Button deleted successfully'}, status=status.HTTP_200_OK)


class SKUBtnView(APIView):
    @staticmethod
    def get(request):
        serializer = SKUBtnListSerializer(SKUBtn.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        pass

    @transaction.atomic
    def delete(self, request):
        pass
