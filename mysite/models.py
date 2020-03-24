from django.db import models

class NewPerson(models.Model):
  added_name=models.CharField(max_length=200, null=True, default=None)
  added_email=models.CharField(max_length=200, null=True, default=None)
  added_phone=models.CharField(max_length=200, null=True, default=None)
  added_msg=models.CharField(max_length=200, null=True, default=None)

  def __str__(self):
        return '{}'.format(self.added_name,self.added_email,self.added_phone,self.added_msg)

   
   



#  class Meta:
#    verbose_name_plural= 'Searches'



