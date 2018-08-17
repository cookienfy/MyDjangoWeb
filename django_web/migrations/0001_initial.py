# Generated by Django 2.0.7 on 2018-08-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('libraryId', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('fun', models.CharField(max_length=50)),
                ('doubt', models.CharField(max_length=50)),
                ('doubtDesc', models.CharField(max_length=500)),
                ('processDoubtWay', models.CharField(max_length=500)),
                ('difficultyTypeId', models.IntegerField()),
                ('contributor', models.CharField(max_length=100)),
                ('contributeDate', models.DateTimeField()),
                ('lastUpdateDate', models.DateTimeField()),
                ('lcv', models.BooleanField()),
            ],
            options={
                'db_table': 'library',
            },
        ),
    ]