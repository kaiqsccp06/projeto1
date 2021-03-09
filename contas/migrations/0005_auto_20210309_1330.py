# Generated by Django 3.0 on 2021-03-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_campos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.DecimalField(decimal_places=1, max_digits=1)),
                ('altura', models.DecimalField(decimal_places=1, max_digits=1)),
                ('peso', models.DecimalField(decimal_places=1, max_digits=1)),
                ('nomeclartura', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Caracteristicas',
            },
        ),
        migrations.DeleteModel(
            name='Campos',
        ),
    ]