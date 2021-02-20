from django.shortcuts import render
from .models import plantPromModel
from .forms import plantPromForm
from code import plantPromClassifier

# Create your views here.
def plantPromApp(request):
    form = plantPromForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')   
            print(sent)
            print(len(sent))
            textAns = plantPromClassifier(sent)
            context['text'] = textAns
        else:
            form = plantPromForm()
    
    context['form'] = form
    return render(request, 'app.html', context=context)