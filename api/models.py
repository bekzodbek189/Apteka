from django.db import models
from io import BytesIO
import qrcode
from PIL import Image, ImageDraw
from django.core.files import File
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Status_user = (
        (1, "Director"),
        (2, "Omborchi"),
        (3, "Sotuvchi"),
        (4, "User")
    )
    status = models.SmallIntegerField(default=4, choices=Status_user)
    phone = models.BigIntegerField(null=True, blank=True)



class Tablet(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=55, decimal_places=2)
    selling_price = models.DecimalField(max_digits=55, decimal_places=2)
    date_srg = models.DateField()
    img = models.ImageField(upload_to="Tablets/")
    qr = models.FileField(upload_to="Qr/", null=True, blank=True)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(f"{self.name}")
        canvas = Image.new("RGB", (290, 290), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.name} price{self.selling_price}sum.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class In(models.Model):
    product = models.ForeignKey(Tablet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)



class Order(models.Model):
    product = models.ForeignKey(Tablet, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=55, decimal_places=2)
    in_price = models.DecimalField(max_digits=55, decimal_places=2)