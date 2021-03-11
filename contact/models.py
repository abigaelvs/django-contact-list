from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    relation = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Profile, self).save(*args, **kwargs)