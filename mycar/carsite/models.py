from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    STATUS_CHOICE = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='simple')

    def __str__(self):
        return f' {self.first_name} - {self.last_name} '


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.model_name} - {self.marca_name}'


class Car(models.Model):
    car_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='car', on_delete=models.CASCADE)
    year = models.DateField(max_length=10)
    active = models.BooleanField(default=True, verbose_name='в наличий')
    product_video = models.FileField(verbose_name='видео', null=True, blank=True)
    body = models.CharField(max_length=32)  #кузов
    color = models.CharField(max_length=32)
    engine = models.CharField(max_length=32)  #двигатель
    box = models.CharField(max_length=32)  #коробка_передач
    drive = models.CharField(max_length=32)  #привод
    fuel_consumption = models.CharField(max_length=32)  #расход топлива
    acceleration = models.CharField(max_length=32)  #разгон
    model_name = models.CharField(max_length=16, unique=True)
    marca_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.car_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class CarPhotos(models.Model):
    car = models.ForeignKey(Car, related_name='car', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')


class Rating(models.Model):
    car = models.ForeignKey(Car, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.car} - {self.user} - {self.stars} stars'


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    car = models.ForeignKey(Car, related_name='reviews', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.car}'
