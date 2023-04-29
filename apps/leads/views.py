from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead


@login_required
def lead_add(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.create_by = request.user
            lead.save()
            return redirect('dashboard:main')
    else:
        form = AddLeadForm()
    return render(request, 'leads/add.html', {'form': form})


@login_required
def lead_list(request):
    leads = Lead.objects.filter(create_by=request.user)
    return render(request, 'leads/list.html', {'leads': leads})


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, create_by=request.user, pk=pk)
    return render(request, 'leads/detail.html', {'lead': lead})
