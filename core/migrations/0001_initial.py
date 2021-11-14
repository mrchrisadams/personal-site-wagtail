# Generated by Django 3.2.9 on 2021-11-14 11:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0023_add_choose_permissions"),
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogArticlePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.datetime(
                            2021, 11, 14, 11, 2, 9, 790705, tzinfo=utc
                        ),
                        help_text="Only for visitor display",
                        verbose_name="Publication date",
                    ),
                ),
                (
                    "intro",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Introduction"
                    ),
                ),
                (
                    "content",
                    wagtail.core.fields.StreamField(
                        [
                            ("paragraph", wagtail.core.blocks.RichTextBlock()),
                            (
                                "markdown",
                                wagtailmarkdown.blocks.MarkdownBlock(icon="code"),
                            ),
                            ("quote", wagtail.core.blocks.BlockQuoteBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(),
                            ),
                            ("embed", wagtail.embeds.blocks.EmbedBlock()),
                        ],
                        blank=True,
                        verbose_name="content",
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="header image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog article",
                "verbose_name_plural": "Blog articles",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="BlogArticlePageTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="core.blogarticlepage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="core_blogarticlepagetag_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="blogarticlepage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.BlogArticlePageTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
