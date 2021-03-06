# Generated by Django 3.2.12 on 2022-03-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name:')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='E-mail:')),
                ('department', models.CharField(choices=[('-', '-----'), ('T', 'Tester'), ('D', 'Developer'), ('R', 'RH')], max_length=1, verbose_name='Name:')),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registers',
            },
        ),
    ]
