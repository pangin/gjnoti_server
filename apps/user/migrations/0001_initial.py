# Generated by Django 3.2.6 on 2021-08-21 08:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('univ', '0001_initial'),
        ('keywords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', models.ManyToManyField(blank=True, to='keywords.Keyword')),
                ('univ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='univ.univ')),
            ],
        ),
    ]
