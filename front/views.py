from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from front.models import Auto, Make
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from front.forms import CarcreateForm


def index(request):
    #return HttpResponse("Hello, world. You're at the front index.")
	context={"test":"test"}
	return render(request, 'front/index.html', context)



class MakeView(View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'front/make_list.html', ctx)



class CarView(View):
	def get(self, request):
		bc = Make.objects.count()
		ml = Auto.objects.all()
		ctx = {'car_list': ml, 'brand_count':bc}
		return render(request, 'front/car_list.html', ctx)


class MakeCreate(CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('make_list')

class MakeUpdate(UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('index')

class MakeDelete(DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('make_list') 


# class CarCreate(CreateView):
# 	model = Auto
# 	fields = '__all__'

# 	#brand = ModelChoiceField(queryset=Make.objects.none())

# 	def __init__(self, *args, **kwargs):
# 		#self.my_var = kwargs.pop('my_var2')
# 		#super(self).__init__(*args, **kwargs)
# 		#self.fields['brand'].queryset = Make.objects.filter(type=self.my_var)
# 		self.fields['brand'].queryset = Make.objects.all()

# 	def form_valid(self, form):
# 		return super(CarCreate, self).form_valid(form)

# 	def get_context_data(self, **kwargs):
# 		"""Insert the form into the context dict."""
# 		print(self.get_form())
# 		if 'form' not in kwargs:
# 			form = self.get_form()
# 			#form= form.replace('brand', 'brand2')
# 			kwargs['form'] = form
# 		print(kwargs)
# 		return super().get_context_data(**kwargs)

# 	# def get_form_kwargs(self):
# 	# 	kwargs = super(CarCreate, self).get_form_kwargs()
# 	# 	kwargs.update({'my_var2': 'my value'})
# 	# 	return kwargs	
	
	
# 	success_url = reverse_lazy('car_list')


class CarCreate(View):
	template = 'front/make_form.html'
	success_url = reverse_lazy('index')

	def get(self, request):
		form = CarcreateForm()
		print(form)
		ctx = {'form': form}
		return render(request, self.template, ctx)

	def post(self, request):
		form = CarcreateForm(request.POST)
		if not form.is_valid():
			ctx = {'form': form}
			return render(request, self.template, ctx)

		make = form.save()
		return redirect(self.success_url)


class CarUpdate(View):
	model = Auto
	template = 'front/auto_form.html'
	success_url = reverse_lazy('car_list')

	def get(self, request, pk):
		car = get_object_or_404(self.model, pk=pk)
		form = CarcreateForm(instance=car,brand='')
		#form.fields['brand'].queryset = Make.objects.filter(id=pk)
		print(car.brand)
		ctx = {'form': form, 'brand': car.brand}
		return render(request, self.template, ctx)

	def post(self, request, pk):
		car = get_object_or_404(self.model, pk=pk)
		form = CarcreateForm(request.POST, instance=car)
		if not form.is_valid():
			ctx = {'form': form}
			return render(request, self.template, ctx)

		Auto = form.save()
		return redirect(self.success_url)


class CarDelete(View):
    model = Auto
    success_url = reverse_lazy('car_list')
    template = 'front/car_confirm_delete.html'

    def get(self, request, pk):
        car = get_object_or_404(self.model, pk=pk)
        form = CarcreateForm(instance=car)
        ctx = {'car': car}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        car = get_object_or_404(self.model, pk=pk)
        car.delete()
        return redirect(self.success_url)


	
# class CarDelete(View):
# 	def get(self, request):
# 		return 'ok'