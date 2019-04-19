# Generated by Django 2.1.7 on 2019-04-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('chart_id', models.TextField(blank=True, db_column='CHART_ID', null=True)),
                ('title', models.TextField(blank=True, db_column='TITLE', null=True)),
                ('datasource', models.TextField(blank=True, db_column='DATASOURCE', null=True)),
                ('datayear', models.TextField(blank=True, db_column='DATAYEAR', null=True)),
                ('unit', models.TextField(blank=True, db_column='UNIT', null=True)),
                ('visualtype', models.TextField(blank=True, db_column='VISUALTYPE', null=True)),
                ('author', models.TextField(blank=True, db_column='AUTHOR', null=True)),
                ('keyword', models.TextField(blank=True, db_column='KEYWORD', null=True)),
                ('datatype', models.TextField(blank=True, db_column='DATATYPE', null=True)),
                ('filepath', models.TextField(blank=True, db_column='FILEPATH', null=True)),
            ],
            options={
                'db_table': 'chart',
                'managed': False,
            },
        ),
    ]
