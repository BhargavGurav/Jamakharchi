from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Record
# Create your views here.



def home(request):
    try:
        rec = list(Record.objects.all())
    except e:
        messages.error(request, e)
        return HttpResponsRedirect('/')

    if request.method == 'POST':
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        purpose = request.POST.get('purpose')
        closing_amount = request.POST.get('closing_amount')

        print(date)
        if (len(purpose.strip()) == 0) or (int(amount) < 0) or (int(closing_amount) < 0):
            messages.error(request, 'Wrong data or purpose not entered.')
            return HttpResponseRedirect('/')
        else:
            record = Record(date=date, amount=amount, purpose=purpose, closing=closing_amount)
            record.save()
            messages.success(request, 'Record saved.')
            return HttpResponseRedirect('/')
        

    return render(request, 'base.html', {'records' : rec})

def deleteEntry(request, id):
    entry = Record.objects.get(id=id)
    entry.delete()
    messages.success(request, 'Entry deleted successfully !')
    return HttpResponseRedirect('/')


def downloadRecords(request):
    
    if request.method == 'POST':
        start = request.POST.get('start-date')
        end = request.POST.get('end-date')

        record = Record.objects.filter(date__range=[start, end])
        file = open('App/Static/Statement.txt', 'w')
        for i in record:
            file.write(f"{i.date} {i.amount:10} {i.purpose:>30} {i.closing:10}\n")
        file.close()
        
        
        # messages.success(request, 'Downloading started.')
        return HttpResponseRedirect('/download')
    return render(request, 'download.html')
    
