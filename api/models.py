from django.db import models

# Create your models here.
class Order(models.Model):
    # Add your model here
    order_num = models.CharField(max_length=30, unique=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User)
    
    def __str__(self):
        return '訂單編號：{} 總價：{}'.format(self.order_num, self.total_price)

    class Meta:
        db_table = "orders"
        
    #pass

class Product(models.Model):
    product_num = models.CharField(max_length=30, unique=True)
    product_name = models.CharField(max_length=50, default="Unknown")
    price = models.DecimalField(max_digits=15,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    # orders = models.ManyToManyField(Order)

    # orders = models.ManyToManyField(Order)
    def __str__(self):
        return '產品編號：{} 產品名稱：{} 價格：{}'.format(self.product_num, self.product_name, self.price)

    class Meta:
        db_table = "products"
        unique_together = ('product_num', 'product_name')


class DataManagement(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '訂單：{} 產品：{}'.format(self.order, self.product)

    class Meta:
        db_table = "management"