from django.db import models


class User(models.Model):
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    email = models.CharField(max_length=50, unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=50, verbose_name='Телефон')


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


class Level(models.Model):
    winter = models.CharField(max_length=2, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=2, verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=2, verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=2, verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = 'Категория трудности'
        verbose_name_plural = 'Категория трудности'


class Pereval(models.Model):  # pereval_added
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'
    TYPE = [
        (new, 'новый объект'),
        (pending, 'объект рассматривается'),
        (accepted, 'объект принят'),
        (rejected, 'отказано'),
    ]

    beautyTitle = models.CharField(max_length=255, verbose_name='Форма рельефа', default=None)
    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    other_titles = models.CharField(max_length=255, verbose_name='Альтернативное название')
    connect = models.TextField(null=True, blank=True, verbose_name='Соединяет')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=TYPE, default=new, verbose_name='Статус объекта')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.pk} {self.beautyTitle}'

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевал'


class Images(models.Model):  # pereval_images
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    data = models.URLField(null=True, blank=True, verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'
