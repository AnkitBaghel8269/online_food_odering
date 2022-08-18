from django.db import models

# Create your models here.



class RestaurantUser(models.Model):
    r_name = models.CharField(max_length=50,null=True)
    r_image = models.ImageField(upload_to = 'images/',null=True)
    r_number = models.IntegerField(default=0)
    r_manager_name = models.CharField(max_length=50,null=True)
    r_manager_number = models.IntegerField(default=0)
    r_email = models.EmailField(max_length=50,null=True)
    address = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50,blank=True, null=True)



    def __str__(self):
        return f"{self.r_name}"


FOOD_TYPE = (
        ('Fruit and vegetables' , 'Fruit and vegetables'),
        ('Starchy food' , 'Starchy food'),
        ('Dairy' , 'Dairy'),
        ('Protein' ,'Protein'),
        ('Fat' , 'Fat'),
    )
   


class OurMenu(models.Model):
    food_name = models.CharField(max_length=100)
    f_type = models.CharField(max_length=50,choices= FOOD_TYPE , default='vagetarian')
    food_price = models.FloatField()
    food_image = models.ImageField(upload_to = 'images/food_image', blank = True)
    food_description = models.TextField(max_length=200,blank=True)
    r_name = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE,related_name='rest_name')

    def __str__(self):
        return self.food_name



class CustomerReviews(models.Model):
    name = models.CharField(max_length=50)
    
    review = models.TextField(max_length=200)

    def __str__(self):
        return self.name


    


    