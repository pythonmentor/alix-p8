# Generated by Django 2.0 on 2019-03-21 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_purbeurre', '0005_auto_20190320_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.AddField(
            model_name='product',
            name='rep_nutritionnel',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='savedsubstitute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_prod', to='app_purbeurre.Product', verbose_name='related prod'),
        ),
        migrations.AlterField(
            model_name='savedsubstitute',
            name='substitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_sub', to='app_purbeurre.Product', verbose_name='related sub'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
