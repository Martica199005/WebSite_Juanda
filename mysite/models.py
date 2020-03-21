from django.db import models

class Search(models.Model):
  search = models.CharField(maxlength=500)
  create = models.DateTimeField(auto_now= True)

  def  __str__(self):
    return '{}'.format(self.search)

  class Meta:
    verbose_name_plural= 'Searches'

class Credential():
  account_sid= 'ACe668adfcf2fb50ebb2080b16d33ffde2'
  token= '69c7c8f0078e85288906d9a3ebbd0df7'
  my_cell= '+393420659648'
  my_twiliocell= '+14703157182'