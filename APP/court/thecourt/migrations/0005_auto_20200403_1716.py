# Generated by Django 3.0.2 on 2020-04-03 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thecourt', '0004_auto_20200403_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='password',
            field=models.CharField(default=123, max_length=50),
        ),
        migrations.AlterField(
            model_name='chat',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='thecourt.Players'),
        ),
    ]
