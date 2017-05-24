from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from blog.models import BlogPage

'''
Run each time the model is changed:
python manage.py makemigrations
python manage.py migrate
'''


class HomePage(Page):
    body = RichTextField(blank=True)

    def blogs(self):
        # Get list of live blog pages that are descendants of the ResourceIndexPage page
        blogs = BlogPage.objects.all()

        # Order by most recent date first
        # blogs = blogs.live().order_by('-first_published_at')
        blogs = blogs.live().order_by('-date')

        # return only last 5 entries
        return blogs[:5]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
