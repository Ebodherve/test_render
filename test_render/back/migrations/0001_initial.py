# Generated by Django 4.2.3 on 2023-07-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnythingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att1', models.CharField(max_length=255)),
                ('att2', models.CharField(max_length=255)),
            ],
        ),
    ]
