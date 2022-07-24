from django.contrib import admin
from project_app.models import Direction, Lesson, Trainer, Likemark, Order, List

# Register your models here.
admin.site.register(Direction)
admin.site.register(Lesson)
admin.site.register(Trainer)
admin.site.register(Likemark)
admin.site.register(Order)
admin.site.register(List)