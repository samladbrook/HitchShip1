# Generated by Django 5.1 on 2024-08-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_accepted_by_job_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='name',
            new_name='item_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='approx_weight',
        ),
        migrations.AddField(
            model_name='job',
            name='SKU',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='total_weight',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10),
        ),
    ]
