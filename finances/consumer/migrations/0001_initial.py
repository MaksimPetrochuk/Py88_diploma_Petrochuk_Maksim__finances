# Generated by Django 4.2.6 on 2023-10-28 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('default_currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.currency')),
            ],
        ),
        migrations.CreateModel(
            name='CostGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cost_group_name', models.CharField(max_length=255)),
                ('consumer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='CostRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('consumer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer.consumer')),
                ('cost_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer.costgroup')),
                ('currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.currency')),
            ],
        ),
    ]
