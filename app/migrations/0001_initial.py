# Generated by Django 2.2.2 on 2020-11-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]