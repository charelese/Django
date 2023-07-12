from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from Pro.views import HomeHuman, HumanByProfession, ViewHuman, AddHuman
# from Pro.views import pro, get_profession, view_human, add_human, test, register, user_login, user_logout

urlpatterns = [
    # path('', pro, name='Human'),
    # path('profession/<int:profession_id>', get_profession, name='Profession'),
    # path('human/<int:pk>', view_human, name='View_human'),
    # path('human/add_human', add_human, name='Add_human'),
    # path('test/', test, name='Test'),
    path('', HomeHuman.as_view(), name='Human'),
    path('profession/<int:profession_id>/', HumanByProfession.as_view(), name='Profession'),
    path('human/<int:pk>/', ViewHuman.as_view(), name='View_human'),
    path('human/add_human', AddHuman.as_view(), name='Add_human'),
#     path('register/', register, name='Register'),
#     path('login/', user_login, name='Login'),
#     path('logout/', user_logout, name='Logout'),
]

