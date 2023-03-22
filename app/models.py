from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT', 'IT'),
                                                    ('Non IT', 'Non IT'),
                                                    ('Insurance', 'Insurance')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
   
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager', 'manager'),
                                                        ('Sofware Developer', 'sofware developer'),
                                                        ('Designer', 'Designer')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)                            
    
        
    def __str__(self):
        return self.name