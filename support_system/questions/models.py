from django.db import models


class Articles(models.Model):
    title = models.CharField('Вопрос', max_length=200)
    intro = models.CharField('Описание проблемы', max_length=300)
    full_text = models.TextField('Решение проблемы')
    date = models.DateTimeField('Дата появление вопрос')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/questions/{self.id}'

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'
