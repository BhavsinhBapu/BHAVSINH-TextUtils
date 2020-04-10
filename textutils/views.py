# This Is Created By Mee- Bhavsinh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Bhavsinh','place' :'Delpura'}
    return render(request,'index.html',params)

def analyze(request):
    djtxt=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for character in djtxt:
            if character not in punctuation:
                analyzed = analyzed + character
        params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
        djtxt=analyzed

    if(capitalize=="on"):
        analyzed=""
        for character in djtxt:
            analyzed=analyzed + character.upper()
        params = {'purpose': 'Your UPPER CASE', 'analyzed_text': analyzed}
        djtxt=analyzed

    if (newlineremove == "on"):
        analyzed = ""
        for character in djtxt:
            if character != "\n" and character !="\r":
                analyzed = analyzed + character
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtxt=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,character in enumerate(djtxt):
            if not (djtxt[index] == " " and djtxt[index+1] ==" "):
                analyzed = analyzed + character
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtxt=analyzed

    if(removepunc!="on" and capitalize!="on" and extraspaceremover!="on" and newlineremove!="on"):
        return HttpResponse("Error!!! Please Select Any One")

    return render(request, 'analyze.html', params)
