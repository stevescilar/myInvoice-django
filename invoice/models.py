from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(null=True,blank=True,max_length=200)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return ''
    
    def get_absolute_url(self):
        return reverse ('client-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('')

        self.slug = slugify('')
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)
        
