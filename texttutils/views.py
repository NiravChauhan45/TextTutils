from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):

    # Get The Text
    text = request.POST.get('text','defualt')

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    countchar = request.POST.get('countchar','off')
   
#    Check which checkbox is on 
    if removepunc == "on":      
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed+=char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        text = analyzed
    
    if fullcaps =="on":
        analyzed = ''
        for char in text:
            analyzed=analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        text = analyzed

    if (newlineremover) =="on":
        analyzed = ''
        for char in text:
            if char !='\n' and char!='\r':
                analyzed=analyzed + char
        params = {'purpose':'Removed New Lines','analyzed_text':analyzed}
        text = analyzed

    if extraspaceremover == "on":
        analyzed='' 
        for index,char in enumerate(text):
            if text[index]==" " and text[index+1]==" ":
                pass
            else:
                analyzed=analyzed + char
        params = {'purpose':'Removed Extra Spaces','analyzed_text':analyzed}
        text = analyzed

    if countchar == "on":
        analyzed=""
        for char in text:
            analyzed+=char
        params = {'purpose':'Count Characters','analyzed_text':len(analyzed)}
        return render(request,"analyze.html",params)
    
    if(removepunc != 'on' and fullcaps!= 'on' and newlineremover!= 'on' and extraspaceremover!= 'on'):
        return HttpResponse('Error - 404')
    
    return render(request,"analyze.html",params)