# Виртуальная стажировка SkillFactory
## Описание

На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами.
ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

### Требования к мобильному приложению и REST API.

* Внесение информации о новом объекте (перевале) в карточку объекта;
* Редактирование в приложении неотправленных на сервер ФСТР данных об объектах. На перевале не всегда работает Интернет;
* Заполнение ФИО и контактных данных (телефон и электронная почта) с последующим их автозаполнением при внесении данных о новых объектах;
* Отправка данных на сервер ФСТР;
* Получение уведомления о статусе отправки (успешно/неуспешно);
* Согласие пользователя с политикой обработки персональных данных в случае нажатия на кнопку «Отправить» при отправке данных на сервер.

_Пользователь с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:_

* Координаты перевала и его высота;
* Имя пользователя;
* Почта и телефон пользователя;
* Название перевала;
* Несколько фотографий перевала.

### Содержание проекта.

* Проект выполнен на языке программирования [Python](https://www.python.org/) с использованием фреймворка [Django](https://www.djangoproject.com/) и [Django Rest Framework](https://www.django-rest-framework.org/);
* В качестве СУБД для локального сервера выбран [PostgreSQL](https://www.postgresql.org/), а для облачного [SQLite](https://www.sqlite.org/index.html);
* Проект развернут в облаке благодаря ресурсу [pythonanywhere](https://www.pythonanywhere.com/);
* Сгенерирована документация SWAGGER с помощью [DRF_YASG](https://drf-yasg.readthedocs.io/en/stable/readme.html);
* Присутствует покрытие кода тестами.

### Модели проекта.

_Модель пользователя `User` содержит 5 полей для заполнения данных о пользователе:_

* Поля `Фамилия`, `Имя`, `Отчество`, `Телефон` c типом `CharField`;
* Поле Email для указания электронной почты с типом `EmailField`.

_Модель `Coords` служит для указания координат объекта, имеет 3 поля:_

* Поля `Широта` и `Долгота` с типом `FloatField`;
* Поле `Высота` с типом `IntegerField`.

_Модель `Level` служит для указания категории сложности объекта, имеет 4 поля:_

* Поля `Зима`, `Лето`, `Осень`, `Весна` с типом `CharField`.

_Модель `Images` служит для добавления фото горного перевала, имеет 3 поля:_

* Поле `pereval` для связи с основной моделью;
* Поле `Изображение` с типом URLField;
* Поле `Название` с типом CharField.

_Основная модель `Pereval`, включающая в себя поля для связи с предыдущими моделями, а также новые:_

* Поля `Форма рельефа`, `Название`, `Альтернативное название`, `Соединяет`, `Статус объекта` с типом CharField;
* Поле `Дата` с типом `DateTimeField`;
* Поля `coords`, `level`, `user` для связи с предыдущими моделями.

### Представление проекта.

В проекте используется `ModelViewSet`, т.к. в нем реализуются все методы `CRUD`.

### Сериализаторы проекта.

Сериализаторы служат для конвертирования сложных данных (querysets, models) в родные для Python типы данных, которые могут быть отображены в JSON, XML или в другие типы содержимого.

_Основной сериализатор содержащий в себе остальные:_

```
class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)
```

### [Пример](https://github.com/Vesoff/SprintPereval/blob/master/JSON%20raw_data%20example) JSON данных:

```
{
    "user": {
        "fam": "G",
        "name": "V",
        "otc": "S",
        "email": "test@mail.ru",
        "phone": "+7777777"
    },
    "coords": {
        "latitude": "37.2222",
        "longitude": "37.6666",
        "height": "2345"
    },
    "level": {
        "winter": "1a",
        "summer": "a",
        "autumn": "a",
        "spring": "a"
    },
    "images": [{"data":"https://www.zynovo.com/wp-content/uploads/2016/10/Magento_Success.jpg", "title":"Success"}],
    "beautyTitle": "G",
    "title": "s",
    "other_titles": "w",
    "connect": "s",
    "status": "new"
}
```

### Развертывание приложения в облаке.

Проект развернут в облаке благодаря ресурсу [pythonanywhere](https://www.pythonanywhere.com/) с использованием SQLite бд.

Проект доступен по адресу: http://vesoff.pythonanywhere.com/

### Сгенерированная документация SWAGGER c помощью DRF_YASG.

Доступна по адресу: https://vesoff.pythonanywhere.com/redoc/