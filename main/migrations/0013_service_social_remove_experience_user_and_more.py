# Generated by Django 4.2.3 on 2024-02-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_experience_user_portfolio_git_hub_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='service',
            field=models.ManyToManyField(blank=True, to='main.service'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social',
            field=models.ManyToManyField(blank=True, to='main.social'),
        ),
    ]
