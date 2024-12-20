# Generated by Django 4.2.16 on 2024-10-25 00:55

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_instagram_funcionario_linkedin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=500)),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='servicos', variations={'thumb': {'crop': True, 'height': 300, 'width': 300}})),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]
