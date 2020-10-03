from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster_url = models.TextField()
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    description = models.TextField()
    grade = models.CharField(max_length=50)
    running_time = models.IntegerField()
    score = models.FloatField()
    released_date = models.IntegerField(null=True)
    genre = models.ForeignKey(Genre, related_name="movie", on_delete = models.CASCADE)
    # 제외 / 상영확정
    is_excepted = models.BooleanField(default=False)
    is_rereleased = models.BooleanField(default=False)
    # 투표 관련
    voted_users = models.ManyToManyField(UserExtension, blank=True, related_name='voted_users')
    total_num = models.IntegerField(default=0)
    # 지역
    # {'서울':1, '경기북부':2, '경기남부':3, '인천':4. '강원':5, '대전':6, '충청':7, '대구':8, '부산':9, '울산':10, '경상':11, '광주':12, '전라':13, '제주':14}
    Seoul =  models.IntegerField(default=0)
    North_GyeonGi = models.IntegerField(default=0)
    South_GyeonGi = models.IntegerField(default=0)
    Incheon = models.IntegerField(default=0)
    Gangwon = models.IntegerField(default=0)
    Daejeon = models.IntegerField(default=0)
    ChungCheong = models.IntegerField(default=0)
    Daegu = models.IntegerField(default=0)
    Busan = models.IntegerField(default=0)
    Ulsan = models.IntegerField(default=0)
    GyeongSang = models.IntegerField(default=0)
    Gwangju = models.IntegerField(default=0)
    JeonRa = models.IntegerField(default=0)
    Jeju = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    
    