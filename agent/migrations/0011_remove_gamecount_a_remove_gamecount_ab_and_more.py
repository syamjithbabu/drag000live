# Generated by Django 4.2.7 on 2023-12-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0010_gamecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamecount',
            name='a',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='ab',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='ac',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='b',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='bc',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='box',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='c',
        ),
        migrations.RemoveField(
            model_name='gamecount',
            name='super',
        ),
        migrations.AddField(
            model_name='gamecount',
            name='a_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='ab_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='ac_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='b_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='bc_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='box_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='c_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamecount',
            name='super_count',
            field=models.IntegerField(default=0),
        ),
    ]