# Generated by Django 3.2.9 on 2021-11-21 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_blogarticlepage_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="blogarticlepage", name="date",),
        migrations.AddField(
            model_name="blogarticlepage",
            name="published_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Only for visitor display",
                verbose_name="Publication date",
            ),
        ),
        migrations.AlterField(
            model_name="blogarticlepagetag",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
