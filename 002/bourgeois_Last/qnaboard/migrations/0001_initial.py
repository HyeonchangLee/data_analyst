# Generated by Django 4.0.5 on 2022-06-17 05:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freeboard',
            fields=[
                ('f_no', models.AutoField(primary_key=True, serialize=False)),
                ('f_title', models.CharField(max_length=1000)),
                ('f_content', models.TextField()),
                ('f_group', models.IntegerField(default=0)),
                ('f_step', models.IntegerField(default=0)),
                ('f_indent', models.IntegerField(default=0)),
                ('f_hit', models.IntegerField(default=1)),
                ('f_createdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 17, 14, 34, 20, 320458))),
                ('f_updatedate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 17, 14, 34, 20, 320458))),
                ('f_file', models.ImageField(blank=True, upload_to='')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='membership.bourgeoismember')),
            ],
        ),
    ]
