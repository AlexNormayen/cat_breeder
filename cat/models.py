from django.db import models

# Create your models here.




class Cat(models.Model):
    breed = models.CharField(max_length=255, unique = True)
    name_cat = models.CharField(max_length=16, null=True, blank=True, unique = True)
    description = models.TextField(null=True, blank=True)
    age = models.PositiveIntegerField(default = 0, blank=True)
    group = models.ForeignKey('cat.Group', on_delete = models.PROTECT, null=True)
    parametrs = models.ManyToManyField('cat.Parametr')
    
    
    def __str__(self):
        if self.name_cat is None:
            return '{1} (000) {0}'.format(self.breed, self.pk)
        else:
            return '{2} ({0}) {1}'.format(self.name_cat, self.breed, self.pk)



class Group(models.Model):
    title = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True)
    scoro = models.NullBooleanField()
    
    @property
    def full_title(self):
        return '({0}) {1}'.format(self.code, self.title)
    
    def __str__(self):
        return self.full_title
    
    
class Parametr(models.Model):
    title = models.CharField(max_length=32, primary_key=True)
    
    def __str__(self):
        return self.title
        
    
