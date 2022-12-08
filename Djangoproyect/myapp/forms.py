from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200)
    description =forms.CharField(label = "descripcion de la tarea", widget=forms.Textarea())



class createNewProject(forms.Form):
    name = forms.CharField(label="nombre del projecto", max_length=200)







