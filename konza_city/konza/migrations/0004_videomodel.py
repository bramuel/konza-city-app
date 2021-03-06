# Generated by Django 2.2 on 2021-03-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konza', '0003_post_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(null=True, upload_to='videos/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
