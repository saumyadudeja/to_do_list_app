# Generated by Django 3.1.5 on 2021-01-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0004_auto_20210127_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion_status',
            field=models.CharField(choices=[('todo', 'todo'), ('doing', 'doing'), ('done', 'done')], default='todo', max_length=5),
        ),
    ]
