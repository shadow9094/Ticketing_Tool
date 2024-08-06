# Generated by Django 5.0.1 on 2024-07-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=2000)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('In-progress', 'In-progress'), ('Closed', 'Closed')], default='Open', max_length=100)),
                ('category', models.CharField(choices=[('Hardware', 'Hardware'), ('Software', 'Software'), ('Cloud', 'Cloud')], max_length=100)),
                ('sub_category', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
