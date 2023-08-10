from django.db import models

# Create your models here.

class Product(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
  #quantity = models.PositiveIntegerField(default=1)
  product_picture = models.ImageField(null=True, blank=True, default='place_holder_book.png')

  def __str__(self):
    return f"{self.title}"

#this is the shopping cart
class Cart(models.Model):
  #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) // don't use user beccause we will use session?
  cart_id = models.CharField(primary_key=True, max_length=255)
  ordered = models.BooleanField(default=False)
  quantity = models.PositiveIntegerField(default = 0)
  total = models.DecimalField(default= 0.00, max_digits=5, decimal_places=2)
  def __str__(self):
    return f"{self.cart_id}" #not sure what to return here
