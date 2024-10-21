from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    glavnoe_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото', default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT ,related_name='products', default=None)
    categoryid = models.CharField(max_length=6, verbose_name='Номер категории' , null=True, default=None)
    stock = models.PositiveIntegerField(null=True , default=1)
    name = models.CharField(max_length=200, db_index=True, default=None)
    slug = models.SlugField(max_length=200, db_index=True, default=None)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    dopolnitelnie_xapakteristiki = models.CharField( verbose_name='Дополнительные характеристики',max_length=2550,null=True, default=None)
    polnoe_opisanie = models.CharField( verbose_name='Полное описание',max_length=10000, default=None)
    description = models.CharField(max_length=150, verbose_name='Мета описание',blank=True, default=None)
    keywords = models.CharField(max_length=150, verbose_name='Мета слова',blank=True, default=None)
    glavnoe_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')
    photo_na_slider = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото на слайдер',default=None,null=True)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])
      




class Pages(models.Model):
    
    podcherk = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка подчёркивания', blank=True)
    text = models.CharField(max_length=35000, verbose_name='Текст внизу' , null=True)
    title = models.CharField(max_length=150, verbose_name='Название страницы')
    description = models.CharField(max_length=150, verbose_name='Мета описание')
    keywords = models.CharField(max_length=150, verbose_name='Мета слова')
    fotertitle = models.CharField(max_length=350, verbose_name='Заголовок в футере')
    fotercontent = models.CharField(max_length=550, verbose_name='Слова в футере')
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Логотип', blank=True)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Slider(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок 1 слайда')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото 1 слайда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['title']


class Photos(models.Model):
    title = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, verbose_name='Товар') 
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    num = models.CharField(max_length=10, verbose_name='Номер слайда', null=True)
 
    # def __str__(self):
    #     return self.title
    def photo_img(self):
        if self.photo:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.photo.url)
        else:
            return '(Нет изображения)'
    photo_img.short_description = 'Картинка'
    photo_img.allow_tags = True
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['title']













# Дабавление записи:
#     Выбераем категорию
#     Ставим её айдишник ( считая сверху вниз: 1, 2, 3, 4, 5... )
#     Пишем найменование товара
#     Ставим цену только цифрами
#     В полное описание записываем:

# Размер: 190 х 540 мм
# Рамка: 
# Техника: Вышивка бисером 
# Бисер: 
# Тематика: Пейзаж
# Тип ткани: Габардин

# *Цвет последний слева

#     В дополнительные характеристики - что-то интересное
#     Главное фото должно быть без отступов сверху