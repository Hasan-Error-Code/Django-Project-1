# Generated by Django 4.2.7 on 2023-12-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_name', models.IntegerField()),
                ('T_Age', models.CharField(max_length=50)),
                ('T_Class', models.CharField(max_length=50)),
            ],
        ),
    ]
