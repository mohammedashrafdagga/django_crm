from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm


@login_required
def add_leads(request):
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
