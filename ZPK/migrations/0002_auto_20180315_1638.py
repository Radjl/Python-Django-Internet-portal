# Generated by Django 2.0.3 on 2018-03-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZPK', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]