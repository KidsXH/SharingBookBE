# Generated by Django 2.2.1 on 2019-05-15 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.TextField(unique=True)),
                ('email', models.TextField(null=True)),
                ('admin_type', models.TextField(default='Regular User')),
                ('reset_password_token', models.TextField(null=True)),
                ('reset_password_token_expire_time', models.DateTimeField(null=True)),
                ('auth_token', models.TextField(null=True)),
                ('session_keys', models.TextField(null=True)),
                ('open_api', models.BooleanField(default=False)),
                ('open_api_appkey', models.TextField(null=True)),
                ('is_disabled', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created'],
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.TextField(null=True)),
                ('credit', models.PositiveIntegerField(default=0)),
                ('avatar', models.TextField(default='/default.png')),
                ('books_read', models.TextField(null=True)),
                ('books_reading', models.TextField(null=True)),
                ('books_donated', models.TextField(null=True)),
                ('favorite_books', models.TextField(null=True)),
                ('favorite_tags', models.TextField(null=True)),
                ('favorite_categories', models.TextField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
                'ordering': ['created'],
            },
        ),
    ]
