from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddClientForm
from .models import Client


@login_required
def client_add(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.create_by = request.user
            client.save()
            messages.success(request, 'The Client wes created successfully')
            return redirect('client:list')
    else:
        form = AddClientForm()
    return render(request, 'client/add.html', {'form': form})


@login_required
def client_list(request):
    clients = Client.objects.filter(create_by=request.user)
    return render(request, 'client/list.html', {'clients': clients})


@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, create_by=request.user, pk=pk)
    return render(request, 'client/detail.html', {'client': client})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, create_by=request.user, pk=pk)
    client.delete()
    messages.success(request, 'The client wes deleted.')
    return redirect('client:list')


@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, create_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Lead wes update successfully')
            return redirect('client:detail', pk=client.id)
    else:
        form = AddClientForm(instance=client)
    return render(request, 'client/edit.html', {'form': form})
