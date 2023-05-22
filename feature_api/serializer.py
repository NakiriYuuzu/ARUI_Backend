from rest_framework import serializers

from feature_api.models import *


class SKUListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['sku_id', 'sku_name', 'sku_image']


class ButtonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = ['button_id', 'button_name', 'button_icon', 'button_function']


class SKUBtnListSerializer(serializers.ModelSerializer):
    sku = SKUListSerializer()
    button = ButtonListSerializer()

    class Meta:
        model = SKUBtn
        fields = ['sku', 'button']

