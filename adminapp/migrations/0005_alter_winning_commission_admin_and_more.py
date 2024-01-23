# Generated by Django 4.2.7 on 2023-11-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_winning_commission_admin_winning_prize_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winning',
            name='commission_admin',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='winning',
            name='prize_admin',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='winning',
            name='total_admin',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
