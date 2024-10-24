# Generated by Django 4.2.16 on 2024-10-18 01:33

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='instagram',
            new_name='linkedin',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='foto',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='equipe', variations={'thumb': {'crop': True, 'height': 500, 'width': 500}}),
        ),
    ]
