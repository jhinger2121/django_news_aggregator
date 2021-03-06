# Generated by Django 3.1 on 2020-08-25 11:09

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Website')),
            ],
            options={
                'verbose_name': 'Website',
                'verbose_name_plural': 'Websites',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Title')),
                ('link', models.URLField(max_length=1000, verbose_name='Link')),
                ('favourit', models.BooleanField(default=False, verbose_name='Favorit')),
                ('read_latter', models.BooleanField(default=False, verbose_name='Read Latter')),
                ('author', models.CharField(blank=True, max_length=50, verbose_name='Author')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Rating')),
                ('comments', models.PositiveIntegerField(blank=True, null=True, verbose_name='Comments')),
                ('visits', models.PositiveIntegerField(blank=True, null=True, verbose_name='Visits')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.website')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
    ]
