# Generated by Django 2.1.2 on 2018-12-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubber',
            name='committee',
            field=models.CharField(choices=[('execomm', 'Executive'), ('acadcomm', 'Academics'), ('externals', 'External Affairs'), ('extracomm', 'Extracurricular Affairs'), ('fincomm', 'Finance'), ('internals', 'Internal Affairs'), ('memcomm', 'Membership'), ('pubcomm', 'Publicity')], default='', max_length=100),
        ),
    ]