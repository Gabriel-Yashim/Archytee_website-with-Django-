from django.db import models

# Create your models here.
# Table for Recent Projects section in the Home page
class RecentProjects(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    box = models.CharField(max_length=1)
    position = models.CharField(max_length=20) # residential, commercial, designs, interior
    image = models.ImageField(upload_to='archytee/static/archytee/images/backgrounds/')
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
# Table for the Client Feedback seection n the Home page
class ClientFeedback(models.Model):
    clientName = models.CharField(max_length=90)
    clientDesignation = models.CharField(max_length=80)
    feedback = models.TextField(max_length=500)
    rating = models.IntegerField(max_length=1)
    slide = models.IntegerField(max_length=1)
    image = models.ImageField(upload_to='archytee/static/archytee/images/backgrounds/')
    
# Projects page tables

def get_image_upload_path(instance, filename):
    # Use the 'page' field value as part of the subdirectory path
    return f'archytee/static/archytee/images/{instance.page}/{filename}'

# interior design page table
class interiorProjects(models.Model):
    page = models.CharField(max_length=100, default='interior')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    position = models.IntegerField()
    slide = models.IntegerField()
    image1 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
# 3D-design page table
class designProjects(models.Model):
    page = models.CharField(max_length=100, default='design')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    position = models.IntegerField()
    slide = models.IntegerField()
    image1 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    
    
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
# Residential building page table
class residentialProjects(models.Model):
    page = models.CharField(max_length=100, default='residential')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    position = models.IntegerField()
    slide = models.IntegerField()
    image1 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
# Commercial building page table
class commercialProjects(models.Model):
    page = models.CharField(max_length=100, default='commercial')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    position = models.IntegerField()
    slide = models.IntegerField()
    image1 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
# Properties page table
class Properties(models.Model):
    page = models.CharField(max_length=100, default='properties')
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=250)
    LongText = models.TextField(max_length=2000)
    slide = models.IntegerField()
    slug = models.SlugField(unique=True)
    image1 = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
class ClientForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    

    
