from django.shortcuts import render
from user.models import UserExtension, Movie, Genre
import json
# Create your views here.
def total(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-total_num')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].total_num))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'total.html', context=context)

def seoul(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Seoul')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Seoul))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'seoul.html', context=context)

def north_gyeongi(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-North_GyeonGi')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].North_GyeonGi))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'north_gyeongi.html', context=context)

def south_gyeongi(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-South_GyeonGi')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].South_GyeonGi))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'south_gyeongi.html', context=context)        

def incheon(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Incheon')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Incheon))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'incheon.html', context=context)

def gangwon(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Gangwon')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Gangwon))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'gangwon.html', context=context)

def daejeon(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Daejeon')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Daejeon))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'daejeon.html', context=context)

def chungcheong(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-ChungCheong')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].ChungCheong))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'chungcheong.html', context=context)

def daegu(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Daegu')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Daegu))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'daegu.html', context=context)

def busan(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Busan')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Busan))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'busan.html', context=context)

def ulsan(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Ulsan')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Ulsan))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'ulsan.html', context=context)
    
def gyeongsang(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-GyeongSang')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].GyeongSang))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'gyeongsang.html', context=context)
    
def gwangju(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Gwangju')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Gwangju))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'gwangju.html', context=context)

def jeonra(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-JeonRa')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].JeonRa))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'jeonra.html', context=context)

def jeju(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Jeju')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Jeju))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'jeju.html', context=context)


def staff_main(request):
    if 'query' in request.GET:
        query = request.GET['query']
        results = Movie.objects.all().filter(title__contains=query)
        is_searched = True
    else:
        ordered_movies = Movie.objects.order_by('-total_num')
        top_twenty_list = []

        for i in range(0,20):
            top_twenty_list.append(ordered_movies[i])

        results = top_twenty_list
        is_searched = False 

    # if 'deletion' in request.GET or 're-release_confirmed' in request.GET:

    return render(request, 'staff_main.html', {'results' : results, 'is_searched' : is_searched})