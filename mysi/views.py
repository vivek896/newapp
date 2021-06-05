# made by me
from django.http import HttpResponse, request
from django.shortcuts import render

def index(request):
   
    return render(request,'index.html')


    



def newapp(request):
    tex = request.POST.get('bittu', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyazed = ""
        for char in tex:
            if char not in punctuations:
                analyazed = analyazed + char
        params = {'purpose': 'Remove punc' , 'anaylazed_text': analyazed}
         
        tex = analyazed
    if fullcaps == "on":
        analyazed = ""
        for char in tex:
            analyazed = analyazed + char.upper()
        
        params = {'purpose': 'changed to upper case' , 'anaylazed_text': analyazed}
         
    
    if removepunc != "on" and fullcaps != "on":
        return HttpResponse("please select any option")

    return render(request, 'anaylaze.html', params)
    
    

    

  