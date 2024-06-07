from django.db import models

# Create your models here.

class Book(models.Model):

    GENRES_OF_BOOKS = (
        ("FANTASY", "FANTASY"),
        ("FICTION", "FICTION"),
        ("THRILLER", "THRILLER"),
        ("ROMANCE", "ROMANCE"),
        ("HORROR", "HORROR")
    )

    title = models.CharField(max_length=100, verbose_name='Введите название книги')
    image = models.ImageField(upload_to='books/' , verbose_name='Загрузите фото')
    author = models.CharField(max_length=100, verbose_name='Введите автора книги')
    genres_of_books = models.CharField(max_length=100, verbose_name='Выберите жанр книги', choices=GENRES_OF_BOOKS)
    content = models.TextField(verbose_name='Напишите содержание')
    review = models.TextField(verbose_name='Напишите отзывы об этой книге')
    part = models.IntegerField(verbose_name='Напишите какая у вас часть книги')
    page = models.IntegerField(verbose_name='Напишите сколько страниц у книги')
    publication_date = models.DateField(verbose_name='Укажите дату публикации книги')


    def __str__(self):
        return f'{self.title}-{self.genres_of_books}'
    

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'


