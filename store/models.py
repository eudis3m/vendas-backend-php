from django.db import models # type: ignore

class Product(models.Model):
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stockQuantity = models.IntegerField()

    def __str__(self):
        return self.description

class Sale(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.description} - {self.quantity}'
