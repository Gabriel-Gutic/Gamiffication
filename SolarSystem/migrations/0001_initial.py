# Generated by Django 3.0.5 on 2020-04-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('variant_1', models.CharField(max_length=200)),
                ('variant_2', models.CharField(max_length=200)),
                ('number_of_votes', models.IntegerField()),
            ],
        ),
    ]