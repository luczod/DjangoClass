from tag.models import Tag
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


from django.db.models import F,  Value
from django.db.models.functions import Concat

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
# srt(recipes.query)


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self) -> str:  # __ __ call thunder
        return self.name


class RecipeManager(models.Manager):
    # add new personal function to the objects
    def get_published(self):
        return self.filter(
            is_published=True
        ).annotate(
            author_full_name=Concat(
                F('author__first_name'), Value(' '),
                F('author__last_name'), Value(' ('),
                F('author__username'), Value(')'),
            )
        ).order_by('-id')[:100]


class Recipe(models.Model):
    # add new personal objects Manager to class
    objects = RecipeManager()
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # add datatime to update
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', null=True, blank=True)  # noqa: E501 path to images dir
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('recipes:recipe', args=(self.id,))

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug
        # ao sobreescrever retorna o que deveria tervindo
        return super().save(*args, **kwargs)


# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)
