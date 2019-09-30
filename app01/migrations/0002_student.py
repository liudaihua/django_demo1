# Generated by Django 2.2.3 on 2019-09-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.BooleanField()),
                ('cs', models.ForeignKey(on_delete=True, to='app01.Classes')),
            ],
        ),
    ]