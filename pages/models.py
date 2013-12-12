from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Page(models.Model):
    word = models.CharField(max_length=30)
    text = models.TextField()


    def __unicode__(self):
        return self.word
        

    def get_absolute_url(self):
        return reverse('pages.views.details', args=[str(self.word)])


    def text_with_hrefs(self):
        all_words = Page.objects.all()
        text = self.text
        for word in all_words:
            text = text.replace(word.word, '<a href="{}">{}</a>' \
                .format(word.get_absolute_url(), word.word))
            text = text.replace(word.word.lower(), '<a href="{}">{}</a>' \
                .format(word.get_absolute_url(), word.word.lower()))
        return text
