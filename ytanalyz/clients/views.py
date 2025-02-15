from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ClientForm
from .models import UsersClients, Clients, ClientsStatus


@login_required
def clients_list(request):
    current_user = request.user
    user_clients = UsersClients.objects.filter(users=current_user).values_list('clients', flat=True)
    clients = Clients.objects.filter(id__in=user_clients)
    statuses = ClientsStatus.objects.all()
    return render(request, 'clients/clients_list.html', {'clients': clients, 'statuses': statuses})


@login_required
def add_client(request):
    if request.method == 'POST':
        # Обработка данных формы
        client_name = request.POST.get('client_name')
        project_name = request.POST.get('project_name')
        city = request.POST.get('city')
        photo = request.POST.get('photo')
        contact = request.POST.get('contact')
        start_date = request.POST.get('start_date')
        status_id = request.POST.get('status')

        # Создание нового клиента
        status = ClientsStatus.objects.get(id=status_id)
        new_client = Clients.objects.create(
            client_name=client_name,
            project_name=project_name,
            city=city,
            photo=photo,
            contact=contact,
            start_date=start_date,
            status=status
        )

        # Создание новой связи Пользователь:Клиент
        UsersClients.objects.create(
            users=request.user,
            clients=new_client
        )

        return redirect('clients_list')
    else:
        # Получение списка статусов для выпадающего списка
        statuses = ClientsStatus.objects.all()
        return render(request, 'clients/add_client_modal.html', {'statuses': statuses})


@login_required
def client_detail(request, client_id):
    client = get_object_or_404(Clients, id=client_id)  # Получаем клиента по ID
    return render(request, 'clients/client_detail.html', {'client': client})