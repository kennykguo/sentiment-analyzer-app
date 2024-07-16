# # Import the models module from Django
# from django.db import models
# from django.contrib.auth.models import User

# # Define a model for Company
# class Company(models.Model):
#     # Define a CharField for the company name with a max length of 100 characters
#     name = models.CharField(max_length=100)
#     # Define a TextField for the company description
#     description = models.TextField()
#     # Define a DateTimeField that automatically sets the current datetime when a company is created
#     created_at = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)

#     # String representation of the Company model
#     def __str__(self):
#         return self.name

# # Define a model for Review
# class Review(models.Model):
#     # Define a ForeignKey to the Company model, with reviews being deleted if the company is deleted
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reviews')
#     # Define a TextField for the review text
#     review_text = models.TextField()
#     # Define a DateTimeField that automatically sets the current datetime when a review is created
#     created_at = models.DateTimeField(auto_now_add=True)

#     # String representation of the Review model
#     def __str__(self):
#         return self.review_text[:50]



# Import necessary modules
from django.db import models
from django.contrib.auth.models import User

# Define Company model
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Define Review model
class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text[:50]
