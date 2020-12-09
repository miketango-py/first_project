from django.db import models

# Create your models here.
class Genre_TM(models.Model):
    genre = models.CharField(max_length = 50)
    def __str__(self):
        return self.genre
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
class Author_TM(models.Model):
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 30)
    def __str__(self):
        return self.name + ' ' + self.surname
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
class Book_TM(models.Model):
    title = models.CharField(max_length = 30)
    author = models.ForeignKey(Author_TM, on_delete = models.CASCADE, related_name = 'authors')
    genre = models.ManyToManyField(Genre_TM)
    def __str__(self):
        return self.title + ' ' + self.author + ' ' + self.genre
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'