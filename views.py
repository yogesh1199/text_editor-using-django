from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzed(request):
    djtext=request.POST.get('text','default')
    djunwant=request.POST.get('unwanted_text','default')
    removet=request.POST.get('cheak','off')
    upper=request.POST.get('caps','off')
    nline=request.POST.get('newline','off')
    spaceremover=request.POST.get('space','off')
    word_counter=request.POST.get('count','off')
    n=len(djtext)-djtext.count(' ')
    params={}
    #print(chekbox)
    #print(djtext)
    if(removet=='on'):
        analyzed = ""
        for char in djtext:
            if char not in djunwant:
                analyzed = analyzed + char
        n=len(analyzed)
        params = {'purpose': 'remove unwanted text', 'analyze_text': analyzed,'length': n}
        djtext=analyzed
        #return render(request,'index.html',params)

    if(upper=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params={'purpose':'convert to capitle','analyze_text': analyzed,'length': n}

        djtext=analyzed
        #return render(request,'index.html',params)

    if(nline=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        #print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyze_text': analyzed,'length': n}
        djtext = analyzed
        #print(params)
        # Analyze the text
        #return render(request, 'index.html', params)

    if(spaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char



        params = {'purpose': 'Removed NewLines' ,'analyze_text': analyzed,'length': n}
        djtext=analyzed
        # Analyze the text
        #return render(request, 'index.html', params)
    if(removet!='on' and upper!='on' and nline=='on' and spaceremover!='on'):
        params = {'purpose': 'please seslect option and try again', 'analyze_text': 'error'}
        return render(request, 'index.html', params)
    #else:
     #   params = {'purpose': 'please seslect option', 'analyze_text': 'error'}

    return render(request, 'index.html', params)
'''
def capitalize(request):
    return HttpResponse('capital text')

def newline(request):
    return HttpResponse('newline')

def space(request):
    return HttpResponse('space')

'''
