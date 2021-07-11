from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.name

class Washer(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):


    serviceName = models.CharField(max_length=100)
    servicePrice = models.IntegerField()

    def __str__(self):
        return self.serviceName

class Package(models.Model):


    packageName = models.CharField(max_length=100)
    serviceName = models.ForeignKey('Service', on_delete=models.CASCADE)
    packagePrice = models.IntegerField()

    def __str__(self):
        return self.packageName

class Order(models.Model):

    listOfType = (
        ('Reguler', 'Reguler'),
        ('Express', 'Express'),
    )


    customerName = models.ForeignKey('Customer', on_delete=models.CASCADE)
    washerName = models.ForeignKey('Washer', on_delete=models.CASCADE)
    packageName = models.ForeignKey('Package', on_delete=models.CASCADE)
    serviceName = models.ForeignKey('Service', on_delete=models.CASCADE, blank=True)
    orderLocation = models.CharField(max_length=100)
    orderType = models.CharField(max_length=100, choices=listOfType)
    orderPrice = models.IntegerField()
    orderDate = models.DateField()
    orderTime = models.TimeField()


    def __str__(self):
        return self.id


class Rating(models.Model):


    orderId = models.ForeignKey('Customer', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.orderId

class nilai(models.Model):


    name = models.CharField(max_length=500)
    matkul = models.IntegerField()
    nilaimatkul = models.IntegerField()
    gpa = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return self.name

class buku(models.Model):


    judul = models.CharField(max_length=500)
    pengarang = models.CharField(max_length=500)
    tahunrilis = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.judul


class bantuan(models.Model):


    pertanyaan = models.CharField(max_length=1000)
    jawaban = models.CharField(max_length=1000)

    def __str__(self):
        return self.pertanyaan


class berita(models.Model):


    judul = models.CharField(max_length=1000)
    deskripsi = models.CharField(max_length=1000)
    rilis = models.CharField(max_length=1000)
    kategori = models.CharField(max_length=1000)

    def __str__(self):
        return self.judul
