from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    modi_len = len(text.replace(' ',''))
    count_word = len(wordlst(text))

    return render(request, 'result.html', {
        'total_len':total_len,
        'text':text,
        'modi_len': modi_len,
        'count_word': count_word,
    })

def wordlst(text):
        return text.replace('.', ' ').replace(',', ' ').split()
