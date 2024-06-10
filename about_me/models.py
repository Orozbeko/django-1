from django.db import models


class Poster(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.name

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

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user_name} on {self.book}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='books')

    def __str__(self):
        return self.title


