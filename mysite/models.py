from django.db import models
#see classes
class Search(models.Model):
  search = models.CharField(maxlength=500)
  create = models.DateTimeField(auto_now= True)

  def  __str__(self):
    return '{}'.format(self.search)

  class Meta:
    verbose_name_plural= 'Searches'

