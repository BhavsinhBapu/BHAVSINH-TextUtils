# This Is Created By Mee- Bhavsinh
from django.http import HttpResponse
from django.shortcuts import render

# # -----------------------------------------------------TUT 5--------------------------------------------
# def index(request):
#     return HttpResponse("<h1><b>JAY MATAJI BAPU <b><h1>")
#
# def About(request):
#     return HttpResponse("JAY MATAJI BHAVSINH BAPU")
#
# def tut5(request):
#     with open("C:\\Users\\pm\\PycharmProjects\\NewProjects/textfile.txt") as f:
#         a=f.read()
#     return HttpResponse(a)
# # ----------------------------------------------------------TUT 6--------------------------------
# def tut6(request):
#      return HttpResponse('''Click Here To Open <a href="https://www.goodhealthmarketing.in/login.php"> GOOD HEALTH MARKETING <a> <p>
#      Click Here To Open <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww">CODE WITH HARRY YOUTUBE CHANNEL </a> <p>
#      Click Here To      <a href="https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110">LOGIN FACEBOOK </a> <p>
#      Click Here To Open <a href="https://www.google.co.in/">GOOGLE </a> <p>
#      Click Here To Open <a href="https://www.youtube.com/"> YOUTUBE </a>''')


# ----------------------------------------------------TUT 7----------------------------------------------
#
# def tut7(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse("remove punc <p><a href='/'>Back </a>")
#
# def capitalizefirst(request):
#     return HttpResponse("capitalize first <p><a href='/'>Back </a>")
#
# def newlineremove(request):
#     return HttpResponse("newline remove <p><a href='/'>Back </a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove <p><a href='/'>Back </a>")
# def charcount(request):
#     return HttpResponse("char count <p><a href='/'>Back </a>")
# -----------------------------------------------------------------------Tut 8---------------------------
# def index(request):
#     params={'name':'Bhavsinh','place' :'Delpura'}
#     return render(request,'index.html',params)
#
# def removepunc(request):
#     return HttpResponse("remove punc <p><a href='/'>Back </a>")
#
# def capitalizefirst(request):
#     return HttpResponse("capitalize first <p><a href='/'>Back </a>")
#
# def newlineremove(request):
#     return HttpResponse("newline remove <p><a href='/'>Back </a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove <p><a href='/'>Back </a>")
# def charcount(request):
#     return HttpResponse("char count <p><a href='/'>Back </a>")

# --------------------------------------------------------------------------TUT 9-----------------------------
#
# def index(request):
#     params={'name':'Bhavsinh','place' :'Delpura'}
#     return render(request,'index.html',params)
#
# def removepunc(request):
#     djtxt=request.GET.get('text','default')
#     print(djtxt)
#     return HttpResponse("remove punc <p><a href='/'>Back </a>")
#
# def capitalizefirst(request):
#     return HttpResponse("capitalize first <p><a href='/'>Back </a>")
#
# def newlineremove(request):
#     return HttpResponse("newline remove <p><a href='/'>Back </a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove <p><a href='/'>Back </a>")
# def charcount(request):
#     return HttpResponse("char count <p><a href='/'>Back </a>")

# -------------------------------------------------------------------TUT 10------------------
#
#
# def index(request):
#     params={'name':'Bhavsinh','place' :'Delpura'}
#     return render(request,'index.html',params)
#
# def analyze(request):
#     djtxt=request.GET.get('text','default')
#     removepunc=request.GET.get('removepunc','off')
#     print(removepunc)
#     print(djtxt)
#     if removepunc == "on":
#         # analyzed=djtxt
#         punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         analyzed = ""
#         for character in djtxt:
#             if character not in punctuation:
#                 analyzed = analyzed + character
#         params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
#         return render(request,'analyze.html',params)
#     else:
#         return HttpResponse("Error")

# -------------------------------------------------------------------TUT 11------------------------------------
# EXERCISE 1 SOLUTION       TUT 6

# -----------------------------------------------------------------TUT 12---------------------------
#
# def index(request):
#     params={'name':'Bhavsinh','place' :'Delpura'}
#     return render(request,'index.html',params)
#
# def analyze(request):
#     djtxt=request.GET.get('text','default')
#     removepunc=request.GET.get('removepunc','off')
#     capitalize=request.GET.get('capitalize','off')
#     newlineremove=request.GET.get('newlineremove','off')
#     extraspaceremover=request.GET.get('extraspaceremover','off')
#     charcount=request.GET.get('charcount','off')
#
#     if removepunc == "on":
#         # analyzed=djtxt
#         punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         analyzed = ""
#         for character in djtxt:
#             if character not in punctuation:
#                 analyzed = analyzed + character
#         params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
#         return render(request,'analyze.html',params)
#
#
#
#     elif(capitalize=="on"):
#         analyzed=""
#
#         for character in djtxt:
#             analyzed=analyzed + character.upper()
#         params = {'purpose': 'Your UPPER CASE', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#     elif (newlineremove == "on"):
#         analyzed = ""
#
#         for character in djtxt:
#             if character != "\n" and character !="\r":
#                 analyzed = analyzed + character
#         params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#     elif (extraspaceremover == "on"):
#         analyzed = ""
#
#         for index,character in enumerate(djtxt):
#             if not (djtxt[index] == " " and djtxt[index+1] ==" "):
#                 analyzed = analyzed + character
#         params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#     elif (charcount == "on"):
#         analyzed = len(djtxt)
#
#         params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#
#     else:
#         return HttpResponse("Error!!! Please Select Any One")

# -----------------------------------------------------------------TUT 13-------------------------------------

# THIS IS EXERCISE

# --------------------------------------------------------------------TUT 14--------------------------------------
#
# def index(request):
#     params={'name':'Bhavsinh','place' :'Delpura'}
#     return render(request,'index.html',params)
#
# def analyze(request):
#     djtxt=request.GET.get('text','default')
#     removepunc=request.GET.get('removepunc','off')
#     capitalize=request.GET.get('capitalize','off')
#     newlineremove=request.GET.get('newlineremove','off')
#     extraspaceremover=request.GET.get('extraspaceremover','off')
#     charcount=request.GET.get('charcount','off')
#
#     if removepunc == "on":
#         # analyzed=djtxt
#         punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         analyzed = ""
#         for character in djtxt:
#             if character not in punctuation:
#                 analyzed = analyzed + character
#         params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
#         return render(request,'analyze.html',params)
#
#
#
#     elif(capitalize=="on"):
#         analyzed=""
#
#         for character in djtxt:
#             analyzed=analyzed + character.upper()
#         params = {'purpose': 'Your UPPER CASE', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#     elif (newlineremove == "on"):
#         analyzed = ""
#
#         for character in djtxt:
#             if character != "\n" and character !="\r":
#                 analyzed = analyzed + character
#         params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#     elif (extraspaceremover == "on"):
#         analyzed = ""
#
#         for index,character in enumerate(djtxt):
#             if not (djtxt[index] == " " and djtxt[index+1] ==" "):
#                 analyzed = analyzed + character
#         params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#     elif (charcount == "on"):
#         analyzed = len(djtxt)
#
#         params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#
#     else:
#         return HttpResponse("Error!!! Please Select Any One")





# -----------------------------------------------------------------TUT 16-------------------------------------



# def index(request):
#     params={'name':'Bhavsinh','place' :'Delpura'}
#     return render(request,'index.html',params)
#
# def analyze(request):
#     djtxt=request.POST.get('text','default')
#     removepunc=request.POST.get('removepunc','off')
#     capitalize=request.POST.get('capitalize','off')
#     newlineremove=request.POST.get('newlineremove','off')
#     extraspaceremover=request.POST.get('extraspaceremover','off')
#     charcount=request.POST.get('charcount','off')
#
#     if removepunc == "on":
#         # analyzed=djtxt
#         punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         analyzed = ""
#         for character in djtxt:
#             if character not in punctuation:
#                 analyzed = analyzed + character
#         params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
#         return render(request,'analyze.html',params)
#
#
#
#     elif(capitalize=="on"):
#         analyzed=""
#
#         for character in djtxt:
#             analyzed=analyzed + character.upper()
#         params = {'purpose': 'Your UPPER CASE', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#     elif (newlineremove == "on"):
#         analyzed = ""
#
#         for character in djtxt:
#             if character != "\n" and character !="\r":
#                 analyzed = analyzed + character
#         params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#     elif (extraspaceremover == "on"):
#         analyzed = ""
#
#         for index,character in enumerate(djtxt):
#             if not (djtxt[index] == " " and djtxt[index+1] ==" "):
#                 analyzed = analyzed + character
#         params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#     elif (charcount == "on"):
#         analyzed = len(djtxt)
#
#         params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#
#
#
#     else:
#         return HttpResponse("Error!!! Please Select Any One")



# --------------------------------------------------------TUT 17------EXR 2 SOLUTION------------------------------

def index(request):
    params={'name':'Bhavsinh','place' :'Delpura'}
    return render(request,'index.html',params)

def analyze(request):
    djtxt=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc == "on":
        # analyzed=djtxt
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for character in djtxt:
            if character not in punctuation:
                analyzed = analyzed + character
        params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
        djtxt=analyzed
        # return render(request,'analyze.html',params)



    if(capitalize=="on"):
        analyzed=""

        for character in djtxt:
            analyzed=analyzed + character.upper()
        params = {'purpose': 'Your UPPER CASE', 'analyzed_text': analyzed}
        djtxt=analyzed
        # return render(request, 'analyze.html', params)


    if (newlineremove == "on"):
        analyzed = ""

        for character in djtxt:
            if character != "\n" and character !="\r":
                analyzed = analyzed + character
            else:
                print("no")
        print("pre",analyzed)
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtxt=analyzed
        # return render(request, 'analyze.html', params)



    if (extraspaceremover == "on"):
        analyzed = ""

        for index,character in enumerate(djtxt):
            if not (djtxt[index] == " " and djtxt[index+1] ==" "):
                analyzed = analyzed + character
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtxt=analyzed
        # return render(request, 'analyze.html', params)



    if (charcount == "on"):
        analyzed = len(djtxt)

        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if(removepunc!="on" and capitalize!="on" and extraspaceremover!="on" and newlineremove!="on" and charcount!="on"):
        return HttpResponse("Error!!! Please Select Any One")


    return render(request, 'analyze.html', params)