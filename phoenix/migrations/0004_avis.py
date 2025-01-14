# Generated by Django 5.1 on 2024-09-04 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0003_profil_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField()),
                ('note', models.PositiveIntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phoenix.produit')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phoenix.profil')),
            ],
        ),
    ]
