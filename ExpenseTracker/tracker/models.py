from django.db import models
import uuid 


# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key =True,default=uuid.uuid4,editable=False, unique = True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    
    class  Meta:
        abstract = True
        
class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    
    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ('description',)
        
    def isNegative(self):
        return self.amount < 0