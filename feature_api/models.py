from django.db import models

# Create your models here.
from django.db import models


class SKU(models.Model):
    sku_id = models.AutoField(primary_key=True)
    sku_name = models.CharField(max_length=255)
    sku_image = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.sku_name

    class Meta:
        db_table = 'arui_sku'


class Button(models.Model):
    button_id = models.AutoField(primary_key=True)
    button_name = models.CharField(max_length=255)
    button_icon = models.CharField(max_length=255, null=True)
    button_function = models.CharField(max_length=255)

    def __str__(self):
        return self.button_name

    class Meta:
        db_table = 'arui_button'


class SKUBtn(models.Model):
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    button = models.ForeignKey(Button, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku.sku_name + ' - ' + self.button.button_name

    class Meta:
        db_table = 'arui_sku_btn'
        unique_together = (('sku', 'button'),)
