# Generated by Django 4.1.1 on 2022-09-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('author_name', models.CharField(max_length=30)),
                ('published', models.DateField()),
                ('edition', models.CharField(max_length=20)),
            ],
        ),
    ]