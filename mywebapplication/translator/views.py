from django.shortcuts import render
from . import translator
# Create your views here.


def translator_views(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        target_lang = request.POST['selectLang']
        output = translator.translate(original_text, target_lang)
        return render(request, 'translator.html', {"output_text": output.text, "original_text": original_text})
    else:
        return render(request, 'translator.html')
