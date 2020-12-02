from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Account
from .forms import AccForm

def index(request):
    account_list = Account.objects.order_by('id')[:5]
    template = loader.get_template('feedback/index.html')
    context = {
        'account_list': account_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'feedback/detail.html', {'account': account})

def edit(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = AccForm (request.POST, instance=account)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/')
    else:
        form = AccForm(instance=account)
    return render (request, 'feedback/edit.html', {
        'account':account, 'form':form
    })
