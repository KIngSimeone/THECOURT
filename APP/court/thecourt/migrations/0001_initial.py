# Generated by Django 3.0.2 on 2020-04-01 20:56

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chats', models.CharField(max_length=2000)),
                ('pub_time', models.DateTimeField(verbose_name='time published')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contct phone number', max_length=31)),
            ],
        ),
    ]