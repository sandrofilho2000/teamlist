from django.views.generic import ListView
from stadiums.models import Stadium
from django.shortcuts import get_object_or_404, render
from django.views import View

# Create your views here.
def order_list(list=[], key="", order=""):
    if key:
        list = list.order_by(f"{order}{key}")
    return list


class StadiumListView(ListView):
    model = Stadium
    paginate_by = 20  

    def get_queryset(self):
        queryset = super().get_queryset()

        order_by_param = self.request.GET.get('field', 'build_value')
        order_dir_param = self.request.GET.get('order', 'desc')  
        if order_dir_param == 'desc':
            queryset = order_list(queryset, order_by_param, "-")
        else:
            queryset = order_list(queryset, order_by_param, "")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





class StadiumInfoView(View):
    model = Stadium
    template_name = 'stadiums/stadium_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        stadium = get_object_or_404(Stadium, pk=pk)
        
        imgs = ''
        
        if stadium.imgs:
            imgs = stadium.imgs.split("%%")
            imgs = [img for img in imgs if img]

        print("STADIUM: ", stadium)    
        
        context = {
            'stadium': stadium,
            'imgs': imgs
        }

        return render(request, self.template_name, context)
