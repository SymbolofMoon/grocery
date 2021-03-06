# Generated by Django 3.1.4 on 2020-12-31 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('NOT AVAILABLE', 'Not Available'), ('BOUGHT', 'Bought')], default='PENDING', max_length=20)),
                ('added_date', models.DateField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
            ],
        ),
    ]
