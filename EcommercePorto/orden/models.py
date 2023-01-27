from django.db import models
from producto.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo electonico')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    postal_code = models.CharField(max_length=20, verbose_name='Código Postal')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'orden'
        verbose_name_plural = 'ordenes'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Código de Orden')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Productos')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Cantidad')

    class Meta:
        verbose_name = 'producto ordenado'
        verbose_name_plural = 'productos ordenados'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
