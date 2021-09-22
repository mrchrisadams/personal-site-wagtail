# Generated by Django 3.0 on 2020-04-15 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailperson", "0006_auto_20200416_1603"),
        ("wagtailpress", "0008_auto_20191001_1317"),
    ]

    operations = [
        migrations.RemoveField(model_name="blogarticleauthor", name="person",),
        migrations.AddField(
            model_name="blogarticleauthor",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="article_authors",
                to="wagtailperson.Person",
                verbose_name="Author",
            ),
        ),
    ]
