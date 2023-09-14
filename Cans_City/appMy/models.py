from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Platform (models.Model):
    title = models.CharField(
        ("Platform"), max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Edition (models.Model):
    title = models.CharField(("Edition"), max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Game (models.Model):
    title = models.CharField(("Game Name"), max_length=50)
    platform = models.ForeignKey(Platform, verbose_name=(
        "Platform"), on_delete=models.CASCADE, null=True, blank=True)
    edition = models.ForeignKey(Edition, verbose_name=(
        "Edition"), on_delete=models.CASCADE, null=True, blank=True)
    editionImage = models.ImageField(
        ("Edition Image"), upload_to='background_images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    backgroundImage = models.ImageField(
        ("Background Image"), upload_to='background_images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    iframe = models.CharField(
        ("Iframe"), max_length=100, null=True, blank=True)
    leftPng = models.ImageField(("Left Png"), upload_to='background_images/',
                                height_field=None, width_field=None, max_length=None, null=True, blank=True)
    rightPng = models.ImageField(("Right Png"), upload_to='background_images/',
                                 height_field=None, width_field=None, max_length=None, null=True, blank=True)
    pngShadowColor = models.CharField(
        ("Png Shadow Color"), max_length=50, null=True, blank=True)
    aboutImage = models.ImageField(("About Image"), upload_to='background_images/',
                                   height_field=None, width_field=None, max_length=None, null=True, blank=True)
    about = models.CharField(("About"), max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField(
        ("Price"), default=0, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name=("liked_games"))
    likes_count = models.PositiveIntegerField(default=0)
    basket = models.ManyToManyField(User, related_name=("basket_games"))
    basket_amount = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    def __str__(self) -> str:
        return str(self.platform) + " - " + self.title + " - " + str(self.edition)


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "User"), on_delete=models.CASCADE, null=True, blank=True)
    gameComment = models.ForeignKey(Game, verbose_name=(
        "Game Comment"), on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(("Comment"))
    commentTime = models.DateTimeField(
        (""), auto_now=False, auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user) + " - " + str(self.gameComment)


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "User"), on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profileImg = models.ImageField(("Profil Image"), upload_to='background_images/', height_field=None,
                                   width_field=None, max_length=None, null=True, blank=True)
    

