# Generated by Django 2.1.5 on 2021-06-21 08:18

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
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('order_field', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=155)),
                ('type', models.CharField(choices=[('survey', 'Survey'), ('discussion', 'Discussion'), ('diary', 'Diary')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('live', 'Live'), ('pending', 'Pending'), ('archived', 'Archived')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.Tile'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]