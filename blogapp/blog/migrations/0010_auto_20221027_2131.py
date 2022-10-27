# Generated by Django 3.2.9 on 2022-10-27 18:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211120_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basvurular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('onyazi', ckeditor.fields.RichTextField()),
                ('cv', models.ImageField(upload_to='blogs')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
    ]
