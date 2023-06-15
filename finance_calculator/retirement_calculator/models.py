from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_age = models.IntegerField()
    retirement_age = models.IntegerField()
    current_salary = models.FloatField()
    current_savings = models.FloatField()
    rate_of_return = models.FloatField()

    def calculate_years_to_retirement(self):
        return self.retirement_age - self.current_age
    
    def calculate_return(self, years):
        return self.current_savings * ((1 + self.rate_of_return) ** years) - self.current_savings

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
