from django.shortcuts import render, redirect
from django.http import HttpResponse
from project_app.models import Direction, Lesson, Trainer, Likemark, List, Order
from project_app.forms import LessonForm, TrainerForm, DirectionForm, SearchForm, LikemarkForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.views.generic.base import View
from django.db.models import Count

from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.




def based_contact(request):
    return render(request, 'project_app/contact.html')

def based_trainer(request):
    return render(request, 'project_app/trainer.html')

def based_home(request):
    data = dict()
    data['tel'] = '+ 375-29-1234567'
    data['address'] = 'Minsk, Mir, 1'
    return render(request, 'project_app/home.html', {'data': data})

def index(request):
    data = Direction.objects.all()
    return render(request, 'project_app/index.html', {'data': data})

def based_directions(request):
    data = Direction.objects.all()
    return render(request, 'project_app/directions.html', {'data': data})

def based_lesson_trainer(request, id):
    data = Trainer.objects.filter(id=id)
    form = LikemarkForm()
    return render(request, 'project_app/lesson.html', {'data': data, 'form': form})

def based_description(request, id):
    data = Direction.objects.filter(id=id)
    return render(request, 'project_app/description.html', {'data': data})


def based_trainer(request):
    data = Trainer.objects.all()
    print(data)
    #print(data, 'hello')
    return render(request, 'project_app/trainer.html', {'data': data})

def my_lesson(request):
    if request.user.username=='projectadmin':
        data = Lesson.objects.all()
    else:
        data = Lesson.objects.filter(user=request.user)
    return render(request, 'project_app/my_lesson.html', {'data': data})

def page(request):
    return HttpResponse('<h2>Страница с текстом</>')

def add_lesson(request):
    my_form = LessonForm()
    msg = ''
    if request.method == 'POST':
        #direction = Direction.objects.get(id=request.POST['direction'])
        #trainer = Trainer.objects.get(id=request.POST['trainer'])
        #lesson = Lesson.objects.create(direction=direction, trainer=trainer,
                                    #subscription=request.POST['subscription'], price=request.POST['price'],
                                    #user=request.user)
        #lesson.save()
        my_form = LessonForm(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
        msg = 'ok'
    return render(request, 'project_app/add_lesson.html', {'my_form': my_form, 'msg': msg})

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "project_app/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "project_app/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('index')


def update_lesson(request, id):
    obj = Lesson.objects.get(id=id)
    my_form = LessonForm(instance=obj)

    if request.method == 'POST':
        #direction = Direction.objects.get(id=request.POST['direction'])
        #trainer = Trainer.objects.get(id=request.POST['trainer'])
        #Lesson.objects.filter(id=id).update(direction=direction, trainer=trainer,
                                    #subscription=request.POST['subscription'], price=request.POST['price'])
        #obj = Lesson.objects.get(id=id)
        #my_form = LessonForm(instance=obj)
        my_form = LessonForm(request.POST, request.FILES, instance=obj)
        if my_form.is_valid():
            my_form.save()


    return render(request, 'project_app/update_lesson.html', {'my_form': my_form })

def delete_lesson(request, id):
    obj = Lesson.objects.get(id=id).delete()
    return redirect('my_lesson')

def delete_name(request, id):
    obj = Trainer.objects.get(id=id).delete()
    return redirect('based_trainer')

def delete_direction(request, id):
    obj = Direction.objects.get(id=id).delete()
    return redirect('based_directions')

def update_name(request, id):
    obj = Trainer.objects.get(id=id)
    my_form = TrainerForm(instance=obj)

    if request.method == 'POST':
        Trainer.objects.filter(id=id).update(name=request.POST['name'])

    return render(request, 'project_app/update_name.html', {'my_form': my_form})

def update_direction(request, id):
    obj = Direction.objects.get(id=id)
    my_form = DirectionForm(instance=obj)

    if request.method == 'POST':
        Direction.objects.filter(id=id).update(name_dance=request.POST['name_dance'], about=request.POST['about'])


    return render(request, 'project_app/update_direction.html', {'my_form': my_form})

def search(request):
    my_form = SearchForm()
    data = []
    if request.method == 'POST':
        if request.POST['where'] == '0':
            data = Direction.objects.filter(name_dance__icontains=request.POST['searchtext'])
        elif request.POST['where'] == '1':
            data = Direction.objects.filter(about__icontains=request.POST['searchtext'])

        print(data)
    return render(request, 'project_app/search.html', {'my_form': my_form, 'data': data})



def like(request, id):
    if request.method == 'POST':
        name = Trainer.objects.get(id=id)
        if Likemark.objects.filter(user=request.user, name=name).exists():
           Likemark.objects.filter(user=request.user, name=name).update(mark=int(request.POST['mark']))
        else:
            obj = Likemark.objects.create(user=request.user, mark=int(request.POST['mark']),name=name)
            obj.save()
    return redirect('based_lesson_trainer',id)


def dislike(request, id):
    if request.method == 'POST':
        name = Trainer.objects.get(id=id)
        if Likemark.objects.filter(user=request.user, name=name).exists():
           Likemark.objects.filter(user=request.user, name=name).update(mark=0)
        else:
            obj = Likemark.objects.create(user=request.user, mark=0, name=name)
            obj.save()
    return redirect('based_lesson_trainer', id)

def unlike(request, id):
    if request.method == 'POST':
        name = Trainer.objects.get(id=id)
        if Likemark.objects.filter(user=request.user, name=name).exists():
           Likemark.objects.filter(user=request.user, name=name).delete()

    return redirect('based_lesson_trainer', id)


def add_to_list(request, id):
    direction = Direction.objects.get(id=id)
    if List.objects.filter(user=request.user,direction=direction, order__isnull=True).exists():
        obj = List.objects.get(user=request.user,direction=direction, order__isnull=True)
        obj.count = obj.count + 1
        obj.save()
    else:
        obj = List.objects.create(user=request.user,direction=direction)
        obj.save()
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def delete_from_list(request, id):
    direction = Direction.objects.get(id=id)
    obj = List.objects.get(user=request.user,direction=direction, order__isnull=True)
    if obj.count > 1:
        obj.count = obj.count - 1
        obj.save()
    else:
        List.objects.get(user=request.user,direction=direction, order__isnull=True).delete()
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def drop_from_list(request, id):
    direction = Direction.objects.get(id=id)
    List.objects.get(user=request.user,direction=direction, order__isnull=True).delete()
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)



def do_list(request):
    order = Order.objects.create()
    List.objects.filter(user=request.user,order__isnull=True).update(order=order)
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)

def get_past_list(request, id):
    menu = Direction.objects.all()
    pastlist = Order.objects.get(id=id)
    data = List.objects.filter(order=pastlist)
    return render(request, 'project_app/get_past_list.html', {'data': data, 'menu': menu})


def get_my_lists(request):
    menu = Direction.objects.all()
    current = List.objects.filter(user=request.user,order__isnull=True)
    data = List.objects.filter(user=request.user,order__isnull=False).values('order').annotate(total=Count('id'))
    return render(request, 'project_app/get_my_lists.html', {'data': data, 'menu': menu,'current': current})






