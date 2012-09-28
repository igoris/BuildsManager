from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Build(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=256)
    description = models.TextField()
    number = models.CharField(max_length=256)
    url = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title + " (" + self.number + ")" 
