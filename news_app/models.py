#from -- import
from django.db import models
#code
class Journalist(models.Model):#start Journalist
    #local variables
    #code
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    association = models.CharField(max_length = 30)#associaton where the journalist writes articles
    def __str__(self):#start __str__
        #local variables
        #code
        return self.name + ' ' + self.surname + '\nAssociation: ' + self.association
    #end __str__
    class Meta:#start class Meta
        verbose_name = 'Journalist'
        verbose_name_plural = 'Journalists'
    #end class Meta
#end Journalist

class Article(models.Model):#start Article
    #local variables
    #code
    """generic model"""
    title = models.CharField(max_length = 100)
    context = models.TextField()
    journalist = models.ForeignKey(Journalist, on_delete = models.CASCADE, related_name = 'articles')#creating a foreign key
    def __str__(self):#start __str__
        #local variables
        #code
        return self.title
    #end __str__
    class Meta:#start class Meta
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    #end class Meta
#end Article