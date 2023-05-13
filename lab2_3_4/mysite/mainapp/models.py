import uuid
from django.db import models
from django.urls import reverse


class Headquarter(models.Model):
    STATUS_HEADQUARTER = (
        ('o', 'Open'),
        ('n', 'No data.'),
        ('c', 'Closed'),
    )

    name = models.CharField(max_length=60, help_text='Enter field documentation')
    status = models.CharField(max_length=1, choices=STATUS_HEADQUARTER, blank=True, default='n')
    country = models.CharField(max_length=60, help_text='Enter field documentation')
    address = models.CharField(max_length=120, help_text='Enter field documentation')
    phone = models.CharField(max_length=20, help_text='Enter field documentation')
    email = models.CharField(max_length=40, help_text='Enter field documentation')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('office-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Manufacturer(models.Model):
    headquarter = models.OneToOneField(Headquarter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(help_text='Enter field documentation')
    years_on_market = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=20)

    class Meta:
        ordering = ['name', 'years_on_market']

    def get_absolute_url(self):
        return reverse('manufacturer-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class FurnitureType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    # Fields
    name = models.CharField(max_length=60, help_text='Enter field documentation')
    description = models.TextField(help_text='Enter field documentation')
    furniture_type = models.ManyToManyField(FurnitureType)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.RESTRICT, null=True)
    price = models.DecimalField(max_digits=10, help_text='Enter field documentation', decimal_places=2)
    image = models.ImageField(help_text='Enter field documentation', null=True)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    STATUS_PRODUCT = (
        ('a', 'Available'),
        ('m', 'Maintenance'),
        ('r', 'Reserved')
    )
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    status = models.CharField(max_length=1, choices=STATUS_PRODUCT, blank=True, default='m')
    buyer = models.CharField(max_length=120, help_text='Enter field documentation')

    # Methods
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id} ({self.product.name})'
