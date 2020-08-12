# Generated by Django 3.1 on 2020-08-11 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='catalogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='catalogos.catalogo'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='fabricante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='catalogos.fabricante'),
        ),
    ]
