# Generated by Django 3.0.5 on 2020-09-20 08:23

from django.db import migrations, models
import djongo.models.fields
import restApi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('entity', models.CharField(max_length=255)),
                ('customerId', models.IntegerField()),
                ('law', models.CharField(max_length=255)),
                ('fields', djongo.models.fields.ArrayField(model_container=restApi.models.Fields, null=True)),
            ],
        ),
    ]
