# Generated by Django 3.0.3 on 2020-03-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200304_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('position', models.CharField(max_length=128)),
                ('telephone', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'unique_together': {('telephone', 'email')},
            },
        ),
    ]
