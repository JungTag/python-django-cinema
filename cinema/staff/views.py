from django.shortcuts import render, redirect
from user.models import UserExtension, Movie, Genre
import json
from django.db.models import Max
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required
def total(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-total_num')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].total_num))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'total.html', context=context)

@staff_member_required
def seoul(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Seoul')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Seoul))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'seoul.html', context=context)

@staff_member_required
def north_gyeongi(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-North_GyeonGi')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].North_GyeonGi))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'north_gyeongi.html', context=context)

@staff_member_required
def south_gyeongi(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-South_GyeonGi')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].South_GyeonGi))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'south_gyeongi.html', context=context)        

@staff_member_required
def incheon(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Incheon')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Incheon))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'incheon.html', context=context)

@staff_member_required
def gangwon(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Gangwon')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Gangwon))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'gangwon.html', context=context)

@staff_member_required
def daejeon(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Daejeon')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Daejeon))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'daejeon.html', context=context)

@staff_member_required
def chungcheong(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-ChungCheong')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].ChungCheong))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'chungcheong.html', context=context)

@staff_member_required
def daegu(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Daegu')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Daegu))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'daegu.html', context=context)

@staff_member_required
def busan(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Busan')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Busan))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'busan.html', context=context)

@staff_member_required
def ulsan(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Ulsan')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Ulsan))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'ulsan.html', context=context)

@staff_member_required    
def gyeongsang(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-GyeongSang')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].GyeongSang))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'gyeongsang.html', context=context)

@staff_member_required    
def gwangju(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Gwangju')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Gwangju))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'gwangju.html', context=context)

@staff_member_required
def jeonra(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-JeonRa')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].JeonRa))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'jeonra.html', context=context)

@staff_member_required
def jeju(request):
    movie_list = []
    vote_count = []
    ordered_movies = Movie.objects.order_by('-Jeju')
    for i in range(10):
        movie_list.append(str(ordered_movies[i]))
        vote_count.append(int(ordered_movies[i].Jeju))
    context = {'vote_count' : json.dumps(vote_count), 'movie_list' : json.dumps(movie_list)}
    return render(request, 'jeju.html', context=context)

@staff_member_required
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

    return render(request, 'staff_main.html', {'results' : results, 'is_searched' : is_searched})

@staff_member_required
def reset(request):
    max_id = Movie.objects.all().aggregate(max_id=Max('id'))['max_id']
    for i in range(1, max_id+1):
        movie = Movie.objects.get(id=i)
        movie.is_excepted = False
        movie.is_rereleased = False
        movie.save()
        if movie.total_num == 0:
            continue
        
        movie.total_num = 0
        movie.Seoul = 0
        movie.North_GyeonGi = 0
        movie.South_GyeonGi = 0
        movie.Incheon = 0
        movie.Gangwon = 0
        movie.Daejeon = 0
        movie.ChungCheong = 0
        movie.Daegu = 0
        movie.Busan = 0
        movie.Ulsan = 0
        movie.GyeongSang = 0
        movie.Gwangju = 0
        movie.JeonRa = 0
        movie.Jeju = 0
        movie.voted_users.clear() 
        movie.save()

    return redirect('staff_main')