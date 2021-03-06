# Generated by Django 3.0.5 on 2020-06-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='Aadhar_Card',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='cover',
            new_name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='Income',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='Pan_Card',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
