
from typing import Match
from django.shortcuts import render
from pythainlp import word_tokenize
from pythainlp import pos_tag

# Create your views here.

def index(request):
    return render(request, 'index.html')


def detect(request):

    name = request.GET['name']
    text = request.GET['text']

    Referential = 0
    Coordination = 0
    Scope = 0
    Vague = 0

    test = pos_tag(word_tokenize(text,keep_whitespace=False))
    print(pos_tag(word_tokenize(text,keep_whitespace=False)))
    print(len(test))

    count = len(pos_tag(word_tokenize(text,keep_whitespace=False)))

    print(count)
    for word in test:
        if word[0] == '\r\n':
            count=count-1
        elif word[1] == 'PRON' :
            Referential = Referential+1
        elif word[1] == 'PPRS' :
            Referential = Referential+1
        elif word[1] == 'PDMN' :
            Referential = Referential+1
        elif word[1] == 'PNTR' :
            Referential = Referential+1
        elif word[1] == 'PROPN' :
            Referential = Referential+1
        elif word[1] == 'NPRP' :
            Referential = Referential+1
        elif word[1] == 'DDAN' :
            Referential = Referential+1
        elif word[1] == 'PREL':
            Referential = Referential+1
        elif word[1] == 'CCONJ':
            Coordination = Coordination+1
        elif word[1] == 'JCRG':
            Coordination = Coordination+1
        elif word[1] == 'SCONJ':
            Coordination = Coordination+1
        elif word[1] == 'JSBR':
            Coordination = Coordination+1
        elif word[1] == 'JCMP':
            Coordination = Coordination+1
        elif word[1] == 'DET':
            Scope = Scope+1
        elif word[1] == 'DIAQ':
            Scope = Scope+1
        elif word[1] == 'DDAC':
            Scope = Scope+1
        elif word[1] == 'DDBQ':
            Scope = Scope+1
        elif word[1] == 'DDAQ':
            Scope = Scope+1
        elif word[1] == 'DIAC':
            Scope = Scope+1
        elif word[1] == 'DIBQ':
            Scope = Scope+1
        elif word[1] == 'ADJ':
            Vague = Vague+1
        elif word[1] == 'NONM':
            Vague = Vague+1
        elif word[1] == 'VATT':
            Vague = Vague+1
        elif word[1] == 'DONM':
            Vague = Vague+1
        elif word[1] == 'ADV':
            Vague = Vague+1
        elif word[1] == 'ADVN':
            Vague = Vague+1
        elif word[1] == 'ADVI':
            Vague = Vague+1
        elif word[1] == 'ADVP':
            Vague = Vague+1
        elif word[1] == 'ADVS':
            Vague = Vague+1

    pVague = round(Vague/count*100, 2)
    pCoordination = round(Coordination/count*100, 2)
    pScope = round(Scope/count*100, 2)
    pReferential = round(Referential/count*100, 2)

    print("Vague is ", Vague)
    print("Coordination is ", Coordination)
    print("Scope is ", Scope)
    print("Referential is ", Referential)
    result = Vague+Coordination+Scope+Referential
    print("Vague : ", pVague)
    print("Coordination : ", pCoordination)
    print("Scope : ", pScope)
    print("Referential : ", pReferential)
    presult = round(pVague+pCoordination+pScope+pReferential,2)

    args = {'name': name, 'req': test, 'vague': Vague, 'coordination': Coordination, 'scope': Scope, 'referential': Referential, 'pvague': pVague,
            'pcoordination': pCoordination, 'pscope': pScope, 'preferential': pReferential, 'count': count, 'result': result, 'presult': presult}
    return render(request, 'detect.html', args)
