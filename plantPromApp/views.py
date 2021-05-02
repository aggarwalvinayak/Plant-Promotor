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
            textAns = plantPromClassifier(sent)
            context['text'] = textAns[0]
            context['score'] = round(textAns[1],4)
            # runTest()
        else:
            form = plantPromForm()
    
    context['form'] = form
    return render(request, 'app.html', context=context)

def runTest():
    file = open('/Users/vinayak/Desktop/Misc/Personal/Plant-Promotor/testOsmotic.txt')
    array = []
    for line in file:
        textAns = plantPromClassifier(line)
        array.append(textAns)
    print(array)