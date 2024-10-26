from django.db import models


class Author(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    example = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
