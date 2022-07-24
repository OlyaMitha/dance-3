from project_app.views import index, page, based_directions, based_contact, based_home, based_trainer, based_lesson_trainer, my_lesson, add_lesson, RegisterFormView, LoginFormView, LogoutView, \
    update_lesson, delete_lesson, based_description, delete_name, delete_direction, update_name, update_direction, search, like, dislike, unlike, add_to_list, delete_from_list, drop_from_list, do_list, get_past_list, get_my_lists
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('page/', page),
    path('directions/', based_directions, name='based_directions'),
    path('contact/', based_contact, name='based_contact'),
    path('home/', based_home, name='based_home'),
    path('trainer/', based_trainer, name='based_trainer'),
    path('lesson/<int:id>/', based_lesson_trainer, name='based_lesson_trainer'),
    path('mylesson/', my_lesson, name='my_lesson'),
    path('addlesson/', add_lesson, name='add_lesson'),
    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('updatelesson/<int:id>/', update_lesson, name='update_lesson'),
    path('dellesson/<int:id>/', delete_lesson, name='delete_lesson'),
    path('description/<int:id>/', based_description, name='based_description'),
    path('delname/<int:id>/', delete_name, name='delete_name'),
    path('deldirection/<int:id>/', delete_direction, name='delete_direction'),
    path('updatename/<int:id>/', update_name, name='update_name'),
    path('updatedirection/<int:id>/', update_direction, name='update_direction'),
    path('search/', search, name='search'),
    path('like/<int:id>/', like, name='like'),
    path('dislike/<int:id>/', dislike, name='dislike'),
    path('unlike/<int:id>/', unlike, name='unlike'),

    path('addtolist/<int:id>', add_to_list, name='add_to_list'),
    path('deletefromlist/<int:id>', delete_from_list, name='delete_from_list'),
    path('dropfromlist/<int:id>', drop_from_list, name='drop_from_list'),

    path('dolist/', do_list, name='do_list'),
    path('getpastlist/<int:id>', get_past_list, name='get_past_list'),
    path('getmylists/', get_my_lists, name='get_my_lists'),
]