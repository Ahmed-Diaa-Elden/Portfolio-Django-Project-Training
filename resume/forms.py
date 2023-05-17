  # import form class from django
from django import forms
from django.forms import ModelForm
from .models import Contact

# deﬁne the class of a form
class ContactForm(ModelForm):
  class Meta:
    # write the name of models for which the form is made
    model = Contact
    # Custom ﬁelds
    ﬁelds =["name", "gender", "number"]
    # this function will be used for the validation
  def clean(self):
    # data from the form is fetched using super function
    super(ContactForm, self).clean()
    # extract the name, gender and number ﬁelds from the data
    name = self.cleaned_data.get('name')
    number = self.cleaned_data.get('number')
    # conditions to be met for the name length
    if len(name) < 5:
      self._errors['name'] = self.error_class(['Minimum 5 characters required'])
    if len(number) <5:
      self._errors['number'] = self.error_class(['Number Should Contain a minimum of 5 Numbers'])
    # return any errors if found
    return self.cleaned_data