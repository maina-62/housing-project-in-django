# Generated by Django 3.1.5 on 2021-02-01 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.IntegerField(default=0)),
                ('county', models.CharField(default='Nyeri', max_length=30)),
                ('name', models.CharField(default='none', max_length=30)),
                ('phone', models.CharField(default='none', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='none', max_length=30)),
                ('second_name', models.CharField(default='none', max_length=30)),
                ('location', models.CharField(default='none', max_length=30)),
                ('phone', models.CharField(default='none', max_length=30)),
                ('email', models.CharField(default='none', max_length=30)),
                ('amount', models.IntegerField(default=0)),
                ('payment_method', models.CharField(default='none', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=30)),
                ('house_type', models.CharField(default='none', max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('owner', models.IntegerField(default=0)),
                ('location', models.CharField(default='none', max_length=30)),
                ('detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalsapp.detail')),
            ],
        ),
    ]