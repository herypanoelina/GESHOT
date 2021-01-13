# Generated by Django 3.1.5 on 2021-01-12 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='CHAMBREARR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.IntegerField()),
                ('Client_id', models.IntegerField()),
                ('Num_chambre', models.IntegerField()),
                ('nameChambre', models.CharField(max_length=200)),
                ('date_arr', models.DateTimeField()),
                ('date_dep', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CHAMBREDEP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.IntegerField()),
                ('Client_id', models.IntegerField()),
                ('Num_chambre', models.IntegerField()),
                ('nameChambre', models.CharField(max_length=200)),
                ('date_arr', models.DateTimeField()),
                ('date_dep', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CHAMBREHORS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('Num_chambre', models.IntegerField()),
                ('nameChambre', models.CharField(max_length=200)),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('Motif', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CHAMBRERESERV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.IntegerField()),
                ('Client_id', models.IntegerField()),
                ('Num_chambre', models.IntegerField()),
                ('nameChambre', models.CharField(max_length=200)),
                ('date_arr', models.DateTimeField()),
                ('date_dep', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.IntegerField()),
                ('Client_id', models.IntegerField()),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=100)),
                ('transport', models.CharField(max_length=50)),
                ('Adresse', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.AddField(
            model_name='employees',
            name='Mot_pass',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
