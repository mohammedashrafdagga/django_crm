from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead
from apps.client.models import Client


@login_required
def lead_add(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.create_by = request.user
            lead.save()
            messages.success(request, 'The Lead wes created successfully')
            return redirect('leads:list')
    else:
        form = AddLeadForm()
    return render(request, 'leads/add.html', {'form': form})


@login_required
def lead_list(request):
    leads = Lead.objects.filter(
        create_by=request.user, converted_to_client=False)
    return render(request, 'leads/list.html', {'leads': leads})


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, create_by=request.user, pk=pk)
    return render(request, 'leads/detail.html', {'lead': lead})


@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, create_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, 'The Lead wes deleted.')
    return redirect('leads:list')


@login_required
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, create_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Lead wes update successfully')
            return redirect('leads:detail', pk=lead.id)
    else:
        form = AddLeadForm(instance=lead)
    return render(request, 'leads/edit.html', {'form': form})


@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, create_by=request.user, pk=pk)
    Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        create_by=request.user
    )
    lead.converted_to_client = True
    lead.save()
    return redirect('client:list')
