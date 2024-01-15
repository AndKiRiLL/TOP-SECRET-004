from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=30, default='---')

    def __str__(self):
        return self.name

class Publishing(models.Model):
    name = models.CharField(max_length=30)
    adres = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    publishing = models.ManyToManyField(Publishing, through="AuthorPublishing")

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class AuthorPublishing(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE)


class Post(models.Model):
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    img = models.TextField()
    date = models.CharField(max_length=30, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)