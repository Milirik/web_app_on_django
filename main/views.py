
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .forms import AuthUser, AttributesForm
from .models import User, Attributes, Task, Connection

import random


def generate_connections(users, tasks):
    connections = []

    for _ in range(0, len(users)):
        tmp = random.choice(users)
        tmp2 = random.choice(tasks)
        connections.append((tmp['name'], tmp2['name']))

    return connections


@login_required
def index(request):
    attr = get_object_or_404(Attributes, pk=request.user.attributes.pk)
    users = User.objects.all()
    tasks = Task.objects.all()
    connections = Connection.objects.all()

    if request.method == "POST":
        if request.user.status == 'admin':
            # clean Connections
            for con in Connection.objects.all():
                con.delete()

            # start algorithm here
            # generate users
            users_for_c = []
            for user in users:
                if user.status == 'user':
                    users_for_c.append({
                        'name': user.username,
                        'skills': [
                            int(user.attributes.mathematics),
                            int(user.attributes.russian),
                            int(user.attributes.literature),
                            int(user.attributes.history),
                            int(user.attributes.music),
                            int(user.attributes.chemistry),
                            int(user.attributes.biology),
                            int(user.attributes.physics),
                            int(user.attributes.ecology),
                            int(user.attributes.geography),
                            int(user.attributes.astronomy),
                            int(user.attributes.technology),
                        ]
                    })

            # generate tasks
            tasks_for_c = []
            for task in tasks:
                tasks_for_c.append({
                    'name': task.name,
                    'skills': [
                        int(task.attributes.mathematics),
                        int(task.attributes.russian),
                        int(task.attributes.literature),
                        int(task.attributes.history),
                        int(task.attributes.music),
                        int(task.attributes.chemistry),
                        int(task.attributes.biology),
                        int(task.attributes.physics),
                        int(task.attributes.ecology),
                        int(task.attributes.geography),
                        int(task.attributes.astronomy),
                        int(task.attributes.technology),
                    ]
                })

            for data in generate_connections(users_for_c, tasks_for_c):
                a = Connection()
                for user in users:
                    if data[0] == user.username:
                        a.user = user
                for task in tasks:
                    if data[1] == task.name:
                        a.task = task
                a.save()
            messages.add_message(request, messages.SUCCESS, 'Алгоритм выполнен')
            return redirect('main:index')

        else:
            form = AttributesForm(request.POST, instance=attr)
            if form.is_valid():
                attr1 = form.save()
                messages.add_message(request, messages.SUCCESS, 'Изменения сохранены')
                return redirect('main:index')

    else:

        attr = Attributes.objects.get(pk=request.user.attributes.pk)
        form = AttributesForm(instance=attr)
        context = {
            'form': form,
            'users': users,
            'tasks': tasks,
            'connections': connections
        }
        return render(request, 'main.html', context)


def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Вы успешно авторизовались')
            return redirect(reverse('main:index'))
        else:
            for u in User.objects.all():
                if u.username == username:
                    messages.add_message(request, messages.ERROR, 'Пользователь с таким ником уже зарегестрирован '
                                                                  'или вы указали неверно пароль')
                    return redirect(reverse('main:index'))
            attr = Attributes()
            attr.save()
            user_new = User.objects.create_user(username=username, password=password, attributes=attr)
            messages.add_message(request, messages.SUCCESS, 'Вы зарегистрировались ')
            login(request, user_new)
            return redirect(reverse('main:index'))
    else:
        if request.user.is_authenticated:
            return redirect(reverse('main:index'))
        else:
            form = AuthUser
            context = {
                'form': form,
            }
            return render(request, 'auth.html', context)
