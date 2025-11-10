# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Author(models.Model):

    #__Author_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    biograghy = models.TextField(max_length=255, null=True, blank=True)
    date of birth = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Author_FIELDS__END

    class Meta:
        verbose_name        = _("Author")
        verbose_name_plural = _("Author")


class Category(models.Model):

    #__Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Book(models.Model):

    #__Book_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    available = models.IntegerField(null=True, blank=True)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")


class Member(models.Model):

    #__Member_FIELDS__
    user = models.TextField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    join_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Member_FIELDS__END

    class Meta:
        verbose_name        = _("Member")
        verbose_name_plural = _("Member")


class Issue(models.Model):

    #__Issue_FIELDS__
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    return_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fine = models.IntegerField(null=True, blank=True)

    #__Issue_FIELDS__END

    class Meta:
        verbose_name        = _("Issue")
        verbose_name_plural = _("Issue")



#__MODELS__END
