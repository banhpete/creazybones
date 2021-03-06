# Generated by Django 3.0.7 on 2020-07-06 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cb',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='main_app.Crazybone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='cb_offered',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cb_offered', to='main_app.Crazybone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='cb_wanted',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='cb_wanted', to='main_app.Crazybone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='user_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='main_app.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='user_to',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='main_app.Profile'),
            preserve_default=False,
        ),
    ]
