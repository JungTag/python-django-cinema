from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
# from datetime import datetime, timedelta
from .models import UserExtension, Movie, Genre
from django.contrib.auth.models import User
from django.contrib import auth
import requests
import json
import time
import ssl
import asyncio
from django.http import HttpResponse
from django.db.models import Max
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Q

# 가입 시 이메일 인증 관련
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_FILE = BASE_DIR / 'secrets.json'

def make_genre(request):
    genre_name = {'드라마':1, '판타지':2, '서부':3, '공포':4, '로맨스':5, '모험':6, '스릴러':7, '느와르':8, '컬트':9, '다큐멘터리':10, '코미디':11, '가족':12, '미스터리':13, '전쟁':14, '애니메이션':15, '범죄':16, '뮤지컬':17, 'SF':18, '액션':19, '무협':20, '에로': 21, '서스펜스':22, '서사':23, '블랙코미디':24, '실험':25, '영화카툰':26, '영화음악':27, '영화패러디포스터':28, '멜로/로맨스':29}
    for i in range(1,30):
        for name, value in genre_name.items():
            if i == value:
                genre = Genre()
                genre.name = name
                genre.num = i
                genre.save()
    return redirect('main')

def update_DB(request):
    # PAGE = 40
    PAGE = 9
    base_url = "https://movie.naver.com"
    genre_name = {'드라마':1, '판타지':2, '서부':3, '공포':4, '로맨스':5, '모험':6, '스릴러':7, '느와르':8, '컬트':9, '다큐멘터리':10, '코미디':11, '가족':12, '미스터리':13, '전쟁':14, '애니메이션':15, '범죄':16, '뮤지컬':17, 'SF':18, '액션':19, '무협':20, '에로': 21, '서스펜스':22, '서사':23, '블랙코미디':24, '실험':25, '영화카툰':26, '영화음악':27, '영화패러디포스터':28, '멜로/로맨스':29}
    checker = Movie.objects.filter(title='가벼나움')
    if not checker.exists():
        for now in range(1, PAGE):
            url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200924&page=" + str(now)
            response = requests.get(url)
            time.sleep(0.05)
            html = bs(response.text, 'html.parser')
            movies = html.select("div.tit5 a")
            score = html.find("td", {"class" : "point"}).text
            for movie in movies:
                try:
                    movie_url = movie['href']
                    print(movie_url)
                    movie_url = base_url + movie_url
                    response = requests.get(movie_url)
                    html = bs(response.text, 'html.parser')
                    # image
                    naver_code = movie_url.split('=')[1]
                    image_url = f'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={naver_code}'
                    time.sleep(0.05)
                    response = requests.get(image_url)
                    soup = bs(response.text, 'html.parser')
                    img = soup.select('img')[0]['src']            
                    # desc
                    title_tag = html.find('h3', {'class' : "h_movie"})
                    title = title_tag.find('a').text
                    description = html.find('p', class_='con_tx')
                    step = html.find('dl', 'info_spec')
                    date = step.find_all('dd')[0].find('p').find_all('span')[-1].find('a')
                    if date:
                        released_date = int(date.text.strip())
                        print(released_date)
                        if released_date > 2019:
                            continue
                    else:
                        print("no date")
                    director = step.find_all('dd')[1].find('a').text
                    actor = step.find_all('dd')[2].find('a').text
                    genre = step.find('a').text
                    genre = genre_name.get(genre)
                    grade = step.find_all('dd')[-1].find('a').text
                    running = int(step.find('dd').find_all('span')[2].text[:-2])
                    new_movie = Movie()
                    new_movie.title = title
                    new_movie.poster_url = img
                    new_movie.director = director
                    new_movie.actor = actor
                    new_movie.description = description.get_text()
                    new_movie.grade = grade
                    new_movie.running_time = running
                    new_movie.score = score
                    new_movie.released_date = released_date
                    new_movie.genre = get_object_or_404(Genre, num = genre)
                    new_movie.save()
                except:
                    print(f'error: {movie_url}')
                    continue
        print("done!")
        return HttpResponse(200)
    else:
        redirect('main')

def main(request):
    ordered_movies = Movie.objects.order_by('-total_num')
    top_ten_list = []
    for i in range(0,10):
        top_ten_list.append(ordered_movies[i])
    return render(request, 'main.html', {'first' : top_ten_list[0], 'second' : top_ten_list[1], 'third' : top_ten_list[2], 'fourth' : top_ten_list[3], 'fifth' : top_ten_list[4], 'sixth' : top_ten_list[5], 'seventh' : top_ten_list[6], 'eighth' :top_ten_list[7], 'ninth' : top_ten_list[8], 'tenth' : top_ten_list[9]})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error' : '아이디 혹은 비밀번호가 올바르지 않습니다.'})
    
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(email = request.POST['email_address'])
                return render(request, 'signup.html', {'error' : '이미 사용 중인 이메일입니다.'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    email = request.POST['email_address'],
                )

                userextension = UserExtension()
                userextension.user = user
                userextension.location = request.POST['location']
                user.is_active = False
                user.save()
                userextension.save()

                current_site = get_current_site(request)
                message = render_to_string('activation_email.html', {
                    'user' : user,
                    'domain' : current_site.domain,
                    'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                    'token' : account_activation_token.make_token(user),
                })
                mail_title = "Confirm your Signup!"
                mail_to = request.POST['email_address']
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()

                return render(request, 'login.html')
        else:
            return render(request, 'signup.html', {'error' : '비밀번호가 일치하지 않습니다.'})
        

    return render(request, 'signup.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('main')
    else:
        return render(request, 'login.html', {'error' : '계정 활성화 오류'})


def get_random_movies(*nums):
    # 영화 DB 받아오고 장르 구분 수정 고려
    if len(nums) == 1:
        movies_by_genre = Movie.objects.filter(genre__num=nums[0])
    elif len(nums) == 2:
        movies_by_genre = Movie.objects.filter(Q(genre__num=nums[0]) | Q(genre__num=nums[1]))
    elif len(nums) == 3:
        movies_by_genre = Movie.objects.filter(Q(genre__num=nums[0]) | Q(genre__num=nums[1]) | Q(genre__num=nums[2]))
    else:
        movies_by_genre = Movie.objects.filter(Q(genre__num=nums[0]) | Q(genre__num=nums[1]) | Q(genre__num=nums[2]) | Q(genre__num=nums[3]) | Q(genre__num=nums[4]) | Q(genre__num=nums[5]) | Q(genre__num=nums[6]) | Q(genre__num=nums[7]) | Q(genre__num=nums[8]))
    
    max_id = movies_by_genre.all().aggregate(max_id=Max('id'))['max_id']
    movie_list = []

    # 영화 DB 받아오면 갯수 수정하기!
    while len(movie_list) != 5:
        pk = random.randint(1, max_id)
        movie = movies_by_genre.filter(pk=pk).first()
        if movie:
            if movie not in movie_list:
                movie_list.append(movie)

    return movie_list


def recommend(request):
    # 영화 제목으로 검색
    if 'query' in request.GET:
        query = request.GET['query']
        #results = Movie.objects.all().filter(genre__name__contains=query)
        results = Movie.objects.all().filter(title__contains=query)
        is_searched =True
    else:
        results = {
            '드라마/가족/코미디' : get_random_movies(1, 11, 12),
            '판타지/모험/SF' : get_random_movies(2, 6, 18),
            '멜로/로맨스' : get_random_movies(5, 29),
            '공포/미스터리' : get_random_movies(4, 13, 9),
            '범죄/느와르' : get_random_movies(16, 8),
            '액션/무협' : get_random_movies(19, 20),
            '스릴러/서스펜스' : get_random_movies(7, 22),
            '다큐멘터리' : get_random_movies(10),
            '애니메이션' : get_random_movies(15),
            '전쟁' : get_random_movies(14),
            # '기타' : get_random_movies(3, 17, 21, 23, 24, 25, 26, 27, 28)
            }
        query = None
        is_searched = False
    
    return render(request, 'recommend.html', {'results' : results, 'is_searched' : is_searched, 'query' : query})


@login_required
def vote(request, movie_id): # 프론트에서 confirm 넣어줘야 함 -> yes일 때 실행되도록
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        next = request.POST["next"]
    else:
        next = 'main'
    # if request.user not in movie.voted_users.all(): # 첫 투표
    if not movie.voted_users.filter(user=request.user).exists():
        movie.voted_users.add(request.user.userextension)
        user_location = request.user.userextension.location
        if user_location == 1: movie.Seoul += 1
        elif user_location == 2: movie.North_GyeonGi += 1
        elif user_location == 3: movie.South_GyeonGi += 1
        elif user_location == 4: movie.Incheon += 1
        elif user_location == 5: movie.Gangwon += 1
        elif user_location == 6: movie.Daejeon += 1
        elif user_location == 7: movie.ChungCheong += 1
        elif user_location == 8: movie.Daegu += 1
        elif user_location == 9: movie.Busan += 1
        elif user_location == 10: movie.Ulsan += 1
        elif user_location == 11: movie.GyeongSang += 1
        elif user_location == 12: movie.Gwangju += 1
        elif user_location == 13: movie.JeonRa += 1
        else: movie.Jeju += 1
        movie.total_num += 1
        movie.save()
        return redirect(next)
    else: # 중복 투표 // alert있었으면 좋겠음
        return redirect(next)

def detail(request, movie_id):
    selected_movie = Movie.objects.get(id=movie_id)
    if 'next' in request.POST:
        next = request.POST['next']
    else:
        next = None
    return render(request, 'detail.html', {'movie' : selected_movie, 'next' : next})

def logout(request):
    auth.logout(request)
    return redirect('/')

def re_release(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if not movie.is_rereleased:
        movie.is_rereleased = True
    else:
        movie.is_rereleased = False
    movie.save()

    return redirect('detail', movie_id = movie.id)

def deletion(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if not movie.is_excepted:
        movie.is_excepted = True
    else:
        movie.is_excepted = False
    movie.save()

    return redirect('detail', movie_id = movie.id)