from django.shortcuts import render
from .forms import UserRegister


users = ['user1', 'user2', 'admin']


def sign_up_by_django(request):
    info = ''
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            if password != repeat_password:
                info = "Пароли не совпадают."
            elif age < 18:
                info = "Возраст должен быть не менее 18 лет."
            elif username in users:
                info = "Пользователь с таким именем уже существует."
            else:
                info = f"Приветствуем, {username}!"
                users.append(username)

    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    info = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info = "Пароли не совпадают."
        elif age < 18:
            info = "Возраст должен быть не менее 18 лет."
        elif username in users:
            info = "Пользователь с таким именем уже существует."
        else:
            info = f"Приветствуем, {username}!"
            users.append(username)

    return render(request, 'fifth_task/registration_page.html', {'info': info})
