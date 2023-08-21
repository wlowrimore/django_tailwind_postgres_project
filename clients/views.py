from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Client
from .forms import ClientForm


def view_clients(request):
    all_clients = Client.objects.all().order_by('last_name')

    context = {'all_clients': all_clients}
    return render(request, 'view_clients.html', context)


def search_clients(request):
    query_dict = request.GET
    query = query_dict.get("q")
    client_obj = None
    if query is not None:
        client_obj = Client.objects.get(email=query)
    context = {
        "client": client_obj
    }
    return render(request, "search_clients.html", context)


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The client was successfully added!')
            return redirect('view_clients')
        context = {'form': form}
        return render(request, 'create_client.html', context)

    context = {'form': ClientForm}
    return render(request, 'create_client.html', context)

