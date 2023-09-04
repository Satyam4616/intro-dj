from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies':[
        {
            'id': 5,
            'title' : 'qwerty',
            'year' : 1500

        },
        {  
            'id': 6,
            'title' : 'asdf',
            'year' : 1550

        },
        {
            'id': 7,
            'title' : 'zxcv',
            'year' : 1600

        }
    ]
}
def movies(request):
    return render(request, 'movies/movies.html',data)

def home(request):
    return HttpResponse("home page")