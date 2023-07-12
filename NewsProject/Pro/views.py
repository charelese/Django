from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, logout

from .models import Human, Profession
from .forms import HumanForm
# , UserRegisterForm, UserLoginForm



# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Регистрация успешна')
#             user = form.save()
#             login(request, user)
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'Pro/register.html', {'form': form})
#
# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('Home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'Pro/login.html', {'form': form})
#
#
# def user_logout(request):
#     logout(request)
#     return redirect('Login')


class HomeHuman(ListView, MyMixin):
    model = Human
    context_object_name = 'human'
    template_name = 'Pro/home_human_list.html'
    extra_context = {'name': 'Главная'}
    paginate_by = 4

    def get_context_data2(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Главная страница'
        return context

    def get_queryset2(self):
        return Human.objects.filter(birthday=True).select_related('profession')

class HumanByProfession(ListView):
    model = Human
    template_name = 'Pro/home_human_list.html'
    context_object_name = 'human'
    allow_empty = False
    paginate_by = 3

    def get_context_data2(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Profession.objects.get(pk=self.kwargs['profession_id'])
        return context

    def get_queryset2(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id'], birthday=True).select_related('profession')

class ViewHuman(DetailView):
    model = Human
    context_object_name = 'human_item'
    template_name = 'Pro/view_human.html'

class AddHuman(CreateView):
    form_class = HumanForm
    template_name = 'Pro/add_human.html'
    login_url = '/admin/'

# def test(request):
#     objects = ['john', 'paul', 'george', 'ringo', 'john2', 'paul2', 'george2', 'ringo2',]
#     paginator = Paginator(object, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'Pro/test.html', {'page_obj': page_objects})

# def pro(request):
#     human = Human.objects.all()
#     professions = Profession.objects.all()
#     context = {
#         'human': human,
#         'name': 'Имена сотрудников'
#     }
#     return render(request, 'Pro/index_pro.html', context=context)
#
# def get_profession(request, profession_id):
#     human = Human.objects.filter(profession_id=profession_id)
#     professions = Profession.objects.all()
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'human': human,
#         'profession': profession
#     }
#     return render(request, 'Pro/profession.html', context=context)
#
# def view_human(request, human_id):
#     # human_item = Pro.objects.get(pk=human_id)
#     human_item = get_object_or_404(Human, pk=human_id)
#     context = {
#         'human_item': human_item
#     }
#     return render(request, 'Pro/view_human.html', context=context)
#
# def add_human(request):
#     if request.method == 'POST':
#         form = HumanForm(request.POST)
#         if form.is_valid():
#             human = Human.objects.create(**form.cleaned_data)
#             return redirect(human)
#     else:
#         form = HumanForm()
#     return render(request, 'Pro/add_human.html', {'form': form})
