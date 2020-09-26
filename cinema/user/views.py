from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
# from datetime import datetime, timedelta
from .models import UserExtension, Movie, Genre, Vote
from django.http import HttpResponse
import requests
import json
import time
# import ssl

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
    return redirect('/')

def update_DB(request):
    PAGE = 40
    base_url = "https://movie.naver.com"
    genre_name = {'드라마':1, '판타지':2, '서부':3, '공포':4, '로맨스':5, '모험':6, '스릴러':7, '느와르':8, '컬트':9, '다큐멘터리':10, '코미디':11, '가족':12, '미스터리':13, '전쟁':14, '애니메이션':15, '범죄':16, '뮤지컬':17, 'SF':18, '액션':19, '무협':20, '에로': 21, '서스펜스':22, '서사':23, '블랙코미디':24, '실험':25, '영화카툰':26, '영화음악':27, '영화패러디포스터':28, '멜로/로맨스':29}

    for now in range(1, PAGE):
        url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200924&page=" + str(now)
        response = requests.get(url)
        time.sleep(0.05)
        html = bs(response.text, 'html.parser')
        movies = html.select("div.tit5 a")
        score = html.find("td", {"class" : "point"}).text
        for moive in movies:
            try:
                movie_url = moive['href']
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

    '''
    # 기본 설정
    baseurl = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList"
    movies = {}
    NAVER_URL = "https://openapi.naver.com/v1/search/movie.json"
    secrets = json.loads(open(SECRET_FILE).read())
    API_KEY = secrets["KOBIS"]["API_KEY"]
    CLIENT_ID = secrets["NAVER"]["CLIENT_ID"]
    CLIENT_SECRET = secrets["NAVER"]["CLIENT_SECRET"]
    HEADERS = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
    }  

    # 영화진흥위원회
    all_movies = Movie.objects.all()
    for i in range(11, 52): # 1년당 52주 // 0~51까지 처리
        targetDt = datetime(2018, 12, 31) - timedelta(weeks=i)
        targetDt = targetDt.strftime('%Y%m%d')
        key = API_KEY              
        api_url = f'{baseurl}?key={key}&targetDt={targetDt}&weekGb=1'
        response = requests.get(api_url).json()
        result = response.get('boxOfficeResult').get('weeklyBoxOfficeList')
        for value in result:
            flag = 0
            if movies.get(value['movieCd']) == None:  # 영화 정보가 없으면
                for i in range(len(all_movies)): # 모든 영화를 탐색해서 중복을 검사한다
                    if str(all_movies[i]) == value['movieNm']:
                        flag = 1
                        break
                if flag == 0:
                    movies[value['movieCd']] = [value['movieNm'], value['audiAcc'], value['openDt']]  
                    # movies[영화번호] = [영화 이름, 누적관객수, 개봉일]  

    # 네이버
    for movie_code in movies.keys():
        query = movies[movie_code][0]  # 검색어 = 영화 이름
        API_URL = f'{NAVER_URL}?query={query}'
        time.sleep(0.05)
        response_naver = requests.get(API_URL, headers = HEADERS).json()
        result = response_naver['items']
        for datas in result:
            if int(datas['pubDate']) <= 2018:
                try:
                    # 포스터
                    naver_code = datas['link']
                    naver_code = naver_code.split('=')[1]
                    image_url = f'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={naver_code}'
                    time.sleep(0.05)
                    response = requests.get(image_url)
                    new = response.text
                    soup = BeautifulSoup(new, 'html.parser')
                    html = BeautifulSoup(response.text, 'html.parser')
                    img = html.select('img')[0]['src']
                    # 설명
                    des = datas['link']
                    context = ssl._create_unverified_context()  # 의존성 문제 
                    html = urlopen(des, context = context)
                    source = html.read()
                    html.close()
                    soup = BeautifulSoup(source, 'html.parser')
                    description = soup.find('p', class_='con_tx')
                    step = soup.find('dl', 'info_spec')
                    genre = step.find('a').text
                    genre_name = {'드라마':1, '판타지':2, '서부':3, '공포':4, '로맨스':5, '모험':6, '스릴러':7, '느와르':8, '컬트':9, '다큐멘터리':10, '코미디':11, '가족':12, '미스터리':13, '전쟁':14, '애니메이션':15, '범죄':16, '뮤지컬':17, 'SF':18, '액션':19, '무협':20, '에로': 21, '서스펜스':22, '서사':23, '블랙코미디':24, '실험':25, '영화카툰':26, '영화음악':27, '영화패러디포스터':28, '멜로/로맨스':29}
                    grade = step.find_all('dd')[3].find('a').text
                    running = int(step.find('dd').find_all('span')[2].text[:-2])
                    movies[movie_code].extend([datas['director'], datas['actor'], datas['userRating'], img, description.get_text(), genre_name.get(genre), grade, running])
                    movie = Movie()
                    movie.title = movies[movie_code][0]
                    movie.total_audience = movies[movie_code][1]
                    movie.released_date = movies[movie_code][2]
                    movie.director = movies[movie_code][3]
                    movie.actor = movies[movie_code][4]
                    movie.score = movies[movie_code][5]
                    movie.poster_url = movies[movie_code][6]
                    movie.description = movies[movie_code][7]
                    movie.genre = get_object_or_404(Genre, num = movies[movie_code][8])
                    movie.grade = movies[movie_code][9]
                    movie.running_time = movies[movie_code][10]
                    movie.save()
                    print("Added one movie...")
                    break
                except:
                    break
    print("done!")
    '''

def index(request):
    return render(request, 'index.html')