from django import forms



class InventAddForm(forms.Form):
    Id = forms.IntegerField(label='Id',required=False)
    Name = forms.CharField(label='Your name', max_length=100)
    Account = forms.IntegerField(label='Account',required=False)
    Lifetime = forms.IntegerField(label='Lifetime',required=False)
    Comissioning = forms.DateField(label='Comissioning',required=False)
    MOL = forms.CharField(label='MOL', required=False,max_length=100)
    InvNum = forms.CharField(max_length=50,label='InvNum', required=False)
    FactoryNum = forms.CharField(max_length=100,label='FactoryNum', required=False)
    Location = forms.CharField(label='Location', required=False,max_length=100)

    # Проверка , вытягиваем данные поля аккаунт и если там пусто присваиваем 0 иначе возвращаем переданное значение
    #def clean(self):
     #   acc = self.cleaned_data.get('Account')
     #   lf = self.cleaned_data.get('Lifetime')
     #   if acc is None:
      #      self.cleaned_data['Account'] = 0
       # else:
        #    if lf is None:
         #       self.cleaned_data['Lifetime'] = 0
          #  else:
           #     return self.cleaned_data









