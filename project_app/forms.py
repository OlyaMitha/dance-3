from django.forms import ModelForm
from django import forms
from project_app.models import Lesson, Trainer, Direction, Likemark



class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['direction', 'trainer', 'subscription', 'price', 'image']

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = ['name']

class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields = ['name_dance', 'about']


class SearchForm(forms.Form):
    searchtext = forms.CharField(label='Search', max_length='100', initial='type here')
    where = forms.ChoiceField(label='Where', choices=((0, "name_dance"), (1, "about")))
    #class Meta:
        #model = Lesson
        #fields = ['trainer', 'subscription', 'price']

Mark_Type = (
    ('5','super'),
    ('4','good'),
    ('3','not bad'),
    ('2','so...so'),
    ('1','badly'),
)
class LikemarkForm(forms.Form):
    mark = forms.ChoiceField(initial=5, choices=Mark_Type)