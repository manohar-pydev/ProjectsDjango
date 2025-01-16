from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food\index.html')
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html',context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name ='item_list'
    


def item(request):
    return HttpResponse("This is an item view")

def detail_view(request, item_id):
    try:
        item_data = Item.objects.get(pk=item_id)
        context = {
            'item':item_data
        }
        return render(request,'food\detail.html',context)
    except Exception as e:
        return 

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
     
def create_item(request):
   form = ItemForm(request.POST or None)
   if form.is_valid():
       form.save()
       return redirect('food:index')
   return render(request, 'food/item-form.html',{'form':form})

# class based view for create Item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'
    
    def form_valid(self, form):
        # To get the user who has currently logged in
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
    
def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food\item-form.html',{'form':form,'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})