# Generated by Django 4.2.7 on 2023-11-27 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0003_dealergameadmin'),
        ('agent', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='dealer_game_admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dealer.dealergameadmin'),
        ),
    ]