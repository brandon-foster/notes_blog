from django.db import models
from django.core.urlresolvers import reverse

from redactor.fields import RedactorField

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = RedactorField(verbose_name=u'Text')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # order the Post class by the created field in descending order
    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
