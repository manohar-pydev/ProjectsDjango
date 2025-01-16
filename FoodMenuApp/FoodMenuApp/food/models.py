from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://in.images.search.yahoo.com/images/view;_ylt=AwrPrWs.BGlnyCQbl1a9HAx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkA2JhNGE3ZTJkM2YyZTlmNTM3NjExNmQ2MTU0YzRkNzk1BGdwb3MDNDAEaXQDYmluZw--?back=https%3A%2F%2Fin.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dfood%2Bplaceholder%2Bimage%2Bcoming%2Bsoon%26ei%3DUTF-8%26type%3DE211IN1274G0%26fr%3Dmcafee%26fr2%3Dp%253As%252Cv%253Ai%252Cm%253Asb-top%26tab%3Dorganic%26ri%3D40&w=600&h=600&imgurl=www.food4fuel.com%2Fwp-content%2Fuploads%2Fwoocommerce-placeholder-600x600.png&rurl=https%3A%2F%2Fwww.food4fuel.com%2Fproduct%2F5-family-packs-6-servings%2F&size=22KB&p=food+placeholder+image+coming+soon&oid=ba4a7e2d3f2e9f5376116d6154c4d795&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&fr=mcafee&tt=5+family+packs+-+6+servings+-+Food+4+Fuel+-+Healthy+Meal+Plans+Crafted+...&b=0&ni=250&no=40&ts=&tab=organic&sigr=O6TCINlGWKie&sigb=C7SkDQUYJkC9&sigi=K2eEMsWUqFAp&sigt=TqOOw8YGv.3v&.crumb=8pexUTu/CHY&fr=mcafee&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&type=E211IN1274G0")
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})