from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead


@login_required
def leads_add(request):
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
def leads_list(request):
    leads = Lead.objects.filter(create_by=request.user)
    return render(request, 'leads/list.html', {'leads': leads})
