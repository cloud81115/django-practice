from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Article(models.Model):
	title=models.CharField("標題",max_length=50)
	writer=models.CharField("作者",max_length=50)
	created_date=models.DateField("創建日期",auto_now_add=True)
	modify_date=models.DateField("創建日期",auto_now=True)
	content=models.TextField()
	is_show=models.BooleanField()

	class Meta:
		db_table="article"

	def __str__(self):
		return self.title
class Myuser (AbstractUser):
   
    score= models.IntegerField('積分',default=0)

    class Meta:
    	db_table='MyUser'
    def __str__(self):
    		return self.id