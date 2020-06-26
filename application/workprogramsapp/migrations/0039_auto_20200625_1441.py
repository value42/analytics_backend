# Generated by Django 2.2.6 on 2020-06-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workprogramsapp', '0038_merge_20200625_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='workprogram',
            name='approval_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='workprogram',
            name='authors',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='workprogram',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='workprogram',
            name='video',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
