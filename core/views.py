from django.views import View
from django.shortcuts import render,redirect, get_object_or_404
from .models import TicketModel, AdvertModel
from .forms import TicketForm , AdvertForm
from django.core.mail import send_mail


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from docx import Document
from docx.shared import Inches
import random


# text file 

def add_advert(request):
    if request.method == "POST":
       data = request.POST
       imo = request.FILES.get('image')
       AdvertModel.objects.get_or_create(
               name = data['name'],
               title = data['title'],
               image =imo,
               desc = data['desc'],
               url = data['url'],
           )
       return redirect('home')
    
    adverts = AdvertModel.objects.all()
    return render(request,'core/add_advert.html',{
        'adverts':adverts,
        })    


def text(request, id):
    doc = HttpResponse(content_type='docx/plain')
    doc['Content-Disposition'] = 'attachment; filename=yourticket.docx'
  
    doc.writelines('Ticket Online')
    doc.writelines('welcome to our online serves\n \n')
    doc.writelines('this is your ticket \n \n \n \n ')
    
    lines = []
    tickests = TicketModel.objects.get(id = id)
    lines.append(f"mr/mis {tickests.name} \n your ticket from {tickests.to}\n mack showr you pay {tickests.cost}$  ")
    
    doc.writelines(lines)
    
    
    
    
    return doc
    
    
    



# the templates

def home(request):
    detail= TicketModel.objects.all()
    num = AdvertModel.objects.all().values_list('id',flat=True)
    print(num)
    ad =random.choice(num)
    print(ad)
    adverts = AdvertModel.objects.get(id=ad)
    return render(request,'core/home.html', {
        'detail':detail,
        'a':adverts,
        })


@login_required
def tickets_detail(request):
    tickets = TicketModel.objects.all().order_by('-id')
    
   
    

    for tick in tickets:
        costs = tick.to 
        global y
        y = ''
        if costs == 'bosaso to qardho' :
                y =10
               
            
        elif costs== 'bosaso to garowe' :
                y =20
                
        
        elif costs == 'bosaso to galkacyo':
                 y =30
               
            
        elif costs== 'bosaso to lascano':
                 y =40
                
        else: 
            y = 0
        tick.cost = y
        tick.save()
   
    return render(request,'core/ticket_details.html',{
        'tickets':tickets,
        
                })



def get_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            i =form.cleaned_data.get('to')
            name=form.cleaned_data.get('name')
            
            email = form.cleaned_data.get('email')
            tickets = TicketModel.objects.all()
            for tick in tickets:
                if tick.to == i:
                        costs = tick.to 
                        global y
                        y = ''
                        if costs == 'bosaso to qardho' :
                                y ='10'
                            
                            
                        elif costs== 'bosaso to garowe' :
                                y ='20'
                                
                        
                        elif costs == 'bosaso to galkacyo':
                                y ='30'
                            
                            
                        elif costs== 'bosaso to lascano':
                                y ='40'
                                
                        else: 
                            y = None
                        tick.cost = y
                        tick.save()
            
            print(tick)

            cost = tick.cost
                
            
          
                
            print(cost)
            # co = TicketModel.objects.all()
            
            # for c in co:
            #     if c.name == name:
                    
            #         print(c.name)
            #         o=(c.cost)
            # print(o)
            # cost = o
            send_mail(
                f'mudane/murow {name}  ',
                f"Fdlan kudir A/C 50000  qimaha ticket ka oo ah {cost}$   mahadsanid.." ,
                'bus1ticket101@gmail.com',
                [email],
            )
            send_mail(
                f"name  {name} want ticket form  {form.cleaned_data.get('to')}",
                f"pay {cost} $ on {form.cleaned_data.get('date')}",
                email,
                ['bus1ticket101@gmail.com'],
            )
            
            

            return redirect('home')
    form = TicketForm()
    return render(request,'core/add_ticket.html',{'form':form,
                                                   } )        
    
# class Add_ticket(generic.CreateView):
#     model= TicketModel
#     form_class= TicketForm
#     template_name= 'core/add_ticket.html'
#     success_url= 'detail'            

@login_required
def update_ticket(request, id):
    toUp = TicketModel.objects.get(pk=id)
    if request.method == "POST":
        form = TicketForm(request.POST or None, instance=toUp)
        if form.is_valid():
            
            form.save()
            return redirect('details')
    form = TicketForm(instance=toUp)        
    return render(request,'core/update.html',{'form':form,
                                              'toUp':toUp})
    
@login_required    
def deleteticket(request, id):
    toDe=TicketModel.objects.get(pk=id)
    toDe.delete()
    return redirect('details')

@login_required
def costumer_detail(request, id):
    costumer = TicketModel.objects.get(pk = id)
    return render(request,'core/costumer_detail.html',{'costumer':costumer})


