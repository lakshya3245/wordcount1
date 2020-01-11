from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html')
    
def count(request):
    data = request.GET['fullTextArea']
    wordlist=data.split()
    wordlength=len(wordlist)

    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    sorted_list=sorted(worddictionary.items(), key=operator.itemgetter(1))
    return render(request, 'count.html',{'textarea':data, 'no_of_words':wordlength ,'worddict':sorted_list} )
