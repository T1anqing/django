from django.db import models


# Create your models here.

class Ctrip(models.Model):
    in_place = models.CharField(max_length=32)
    inplace_pinyin = models.CharField(max_length=32)
    notice = models.TextField(null=True)
    title = models.CharField(max_length=32)
    title_pinyin = models.CharField(max_length=100)
    title_url = models.CharField(max_length=100, primary_key=True)
    score = models.CharField(max_length=32)
    place = models.CharField(max_length=50)
    comment_nums = models.CharField(max_length=100)
    image_urls = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Mafengwo(models.Model):
    in_place = models.CharField(max_length=32)
    inplace_pinyin =models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    title_pinyin = models.CharField(max_length=100)
    title_url = models.CharField(max_length=100, primary_key=True)
    comment_nums = models.CharField(max_length=100)
    comment_mains = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Place(models.Model):
    name = models.CharField(max_length=32)
    name_pinyin = models.CharField(max_length=32)
    image_urls = models.CharField(max_length=350)

    def __str__(self):
        return self.name_pinyin