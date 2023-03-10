# Generated by Django 4.1.7 on 2023-03-14 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(max_length=100)),
                ('button_style', models.CharField(max_length=100)),
                ('button_bg_color', models.CharField(max_length=100)),
                ('button_font_color', models.CharField(max_length=100)),
                ('shadow_color', models.CharField(max_length=100)),
                ('font_color', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
    ]
