from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=2)
    number_of_page = models.PositiveIntegerField()
    published_on = models.DateField()

    def __str__(self):
        return f'{self.title} by {self.author}'


