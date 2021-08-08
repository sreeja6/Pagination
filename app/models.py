from django.db import models

class ProductModel(models.Model):
    pno = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='product_images/')