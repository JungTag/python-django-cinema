# Generated by Django 3.1.1 on 2020-10-03 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('num', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('poster_url', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('grade', models.CharField(max_length=50)),
                ('running_time', models.IntegerField()),
                ('score', models.FloatField()),
                ('released_date', models.IntegerField(null=True)),
                ('is_excepted', models.BooleanField(default=False)),
                ('is_rereleased', models.BooleanField(default=False)),
                ('total_num', models.IntegerField(default=0)),
                ('Seoul', models.IntegerField(default=0)),
                ('North_GyeonGi', models.IntegerField(default=0)),
                ('South_GyeonGi', models.IntegerField(default=0)),
                ('Incheon', models.IntegerField(default=0)),
                ('Gangwon', models.IntegerField(default=0)),
                ('Daejeon', models.IntegerField(default=0)),
                ('ChungCheong', models.IntegerField(default=0)),
                ('Daegu', models.IntegerField(default=0)),
                ('Busan', models.IntegerField(default=0)),
                ('Ulsan', models.IntegerField(default=0)),
                ('GyeongSang', models.IntegerField(default=0)),
                ('Gwangju', models.IntegerField(default=0)),
                ('JeonRa', models.IntegerField(default=0)),
                ('Jeju', models.IntegerField(default=0)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='user.genre')),
                ('voted_users', models.ManyToManyField(blank=True, null=True, related_name='voted_users', to='user.UserExtension')),
            ],
        ),
    ]
