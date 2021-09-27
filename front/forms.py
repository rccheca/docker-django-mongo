from django.forms import ModelForm, ModelChoiceField
from front.models import Auto, Make


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'


# class CarcreateForm2(ModelForm):
    
#     brands = ModelChoiceField(queryset=Make.objects.none())

#     def __init__(self, *args, **kwargs):
#         self.my_var = kwargs.pop('my_var2')
#         super(CarcreateForm, self).__init__(*args, **kwargs)
#         self.fields['brand'].queryset = Make.objects.filter(type=self.my_var)

#     class Meta:
#         model = Auto
#         fields = '__all__'


class CarcreateForm(ModelForm):

	brand = ModelChoiceField(queryset=Make.objects.none())
	

	def __init__(self, *args, **kwargs):
		print(kwargs)
		# print(kwargs["instance"].id)
		# ModelChoiceField(queryset=Make.objects.filter(id=kwargs["instance"].id))
		
		if 'brand' in kwargs:
			self.brand = kwargs.pop('brand')
		super(CarcreateForm, self).__init__(*args, **kwargs)
		#self.initial['brand'] = 'ford'
		#self.fields['brand'].queryset = Make.objects.filter(type=self.my_var)
		#self.fields['brand'].queryset = Make.objects.filter(id=kwargs["instance"].id)
		self.fields['brand'].queryset = Make.objects.all()
		#self.fields['brand'] = ModelChoiceField(queryset=Make.objects.all(), empty_label="(Nothing)", initial={'id': 2})

	class Meta:
		model = Auto
		fields = '__all__'