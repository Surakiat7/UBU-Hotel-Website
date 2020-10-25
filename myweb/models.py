from django.db import models


class PriceType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'


class RoomType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'


class Price(models.Model):
    price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE)
    pname = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.price_type} - {self.pname}'


class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    rname = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.room_type} - {self.rname}'

class inputfood(models.Model):
    img = models.CharField(max_length=200)
    namefood1 = models.CharField(max_length=200)
    namefood2 = models.CharField(max_length=1000)
    def __str__(self):
        return f'{self.img} - {self.namefood1} - {self.namefood2}'
