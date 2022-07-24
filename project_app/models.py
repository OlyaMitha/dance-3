from django.db import models
from django.db.models import Avg

# Create your models here.


class Direction(models.Model):
    name_dance = models.CharField(max_length=30)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.name_dance


class Trainer(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)



    def __str__(self):
        return self.name

    @property
    def mark_avg(self):
        if Likemark.objects.filter(name=self).exists():
            return Likemark.objects.filter(name=self).aggregate(Avg('mark'))['mark__avg']
        else:
            return 0

    @property
    def mark_count(self):
        if Likemark.objects.filter(name=self).exists():
            return Likemark.objects.filter(name=self).count()
        else:
            return 0


class Lesson(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    subscription = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', default=1, on_delete=models.CASCADE, verbose_name='user')
    image = models.ImageField(upload_to='project_app/images/', default='static/project_app/images/default.jpg')

    def __str__(self):
        return self.trainer.name+':'+ self.direction.name_dance

class Likemark(models.Model):
    name = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='user')
    mark = models.PositiveSmallIntegerField(default=5)

# фиксируем закрытие списка (аналог чека/заказа)
class Order(models.Model):
    state = models.BooleanField(default=True)
# # набираем список избранное
class List(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='user')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    count = models.PositiveSmallIntegerField(default=1)
