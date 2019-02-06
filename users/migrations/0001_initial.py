# Generated by Django 2.1.2 on 2019-02-06 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveProcess',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('date_posted',),
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Clubber',
            fields=[
                ('student_number', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('committee', models.CharField(choices=[('Executive', 'Executive'), ('Academics', 'Academics'), ('Externals', 'Externals'), ('Extracurricular', 'Extracurricular'), ('Finance', 'Finance'), ('Internals', 'Internals'), ('Membership', 'Membership'), ('Publicity', 'Publicity'), ('TBA', 'TBA')], default='', max_length=100)),
                ('position', models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Executive Secretary', 'Executive Secretary'), ('Associate Secretary', 'Associate Secretary'), ('Director', 'Director'), ('Project Manager', 'Project Manager'), ('Member', 'Member'), ('TBA', 'TBA')], default='', max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('degree_program', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('present_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('emergency_name', models.CharField(max_length=100)),
                ('emergency_relationship', models.CharField(max_length=100)),
                ('emergency_contact', models.CharField(max_length=100)),
                ('carpool_capacity', models.IntegerField(default=0)),
                ('av_equipment', models.CharField(default='', max_length=100)),
                ('sports_equipment', models.CharField(default='', max_length=100)),
                ('instruments', models.CharField(default='', max_length=100)),
                ('current_subjects', models.CharField(default='', max_length=255)),
                ('closest_friends', models.CharField(default='', max_length=255)),
                ('ieaid_company', models.CharField(default='', max_length=100)),
                ('ieaid_contactperson', models.CharField(default='', max_length=100)),
                ('ieaid_contactdetails', models.CharField(default='', max_length=100)),
                ('candy', models.CharField(choices=[('Chocnut', 'Chocnut'), ('Choco Choco', 'Choco Choco'), ('Flat Tops', 'Flat Tops'), ('Potchi', 'Potchi')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('student_number', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('committee', models.CharField(choices=[('Executive', 'Executive'), ('Academics', 'Academics'), ('Externals', 'Externals'), ('Extracurricular', 'Extracurricular'), ('Finance', 'Finance'), ('Internals', 'Internals'), ('Membership', 'Membership'), ('Publicity', 'Publicity'), ('TBA', 'TBA')], default='', max_length=100)),
                ('position', models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Executive Secretary', 'Executive Secretary'), ('Associate Secretary', 'Associate Secretary'), ('Director', 'Director'), ('Project Manager', 'Project Manager'), ('Member', 'Member'), ('TBA', 'TBA')], default='', max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('degree_program', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('present_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('emergency_name', models.CharField(max_length=100)),
                ('emergency_relationship', models.CharField(max_length=100)),
                ('emergency_contact', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('carpool_capacity', models.IntegerField(default=0)),
                ('av_equipment', models.CharField(default='', max_length=100)),
                ('sports_equipment', models.CharField(default='', max_length=100)),
                ('instruments', models.CharField(default='', max_length=100)),
                ('current_subjects', models.CharField(default='', max_length=255)),
                ('closest_friends', models.CharField(default='', max_length=255)),
                ('ieaid_company', models.CharField(default='', max_length=100)),
                ('ieaid_contactperson', models.CharField(default='', max_length=100)),
                ('ieaid_contactdetails', models.CharField(default='', max_length=100)),
                ('candy', models.CharField(choices=[('Chocnut', 'Chocnut'), ('Choco Choco', 'Choco Choco'), ('Flat Tops', 'Flat Tops'), ('Potchi', 'Potchi')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('clubber', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.Clubber')),
                ('password', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('clubber',),
            },
        ),
        migrations.CreateModel(
            name='ReaffedClubber',
            fields=[
                ('clubber', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.Clubber')),
                ('last_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(default='', max_length=100)),
                ('updated_db', models.BooleanField()),
                ('submitted_docs', models.BooleanField()),
                ('paid_fee', models.BooleanField()),
                ('read_contract', models.BooleanField(default=False)),
                ('ew_participation', models.BooleanField(default=False)),
                ('ew_jersey', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='clubber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Clubber'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('event', 'clubber')},
        ),
    ]
