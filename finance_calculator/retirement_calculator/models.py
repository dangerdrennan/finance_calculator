from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_age = models.IntegerField()
    retirement_age = models.IntegerField()
    current_salary = models.FloatField()
    current_savings = models.FloatField()
    percent_contribution = models.FloatField()
    rate_of_return = models.FloatField()

    def calculate_years_to_retirement(self):
        return self.retirement_age - self.current_age
    
    def calculate_return(self, years):
        # normalize the percentages for calculation
        percent_contribution = self.percent_contribution / 100
        rate_of_return = self.rate_of_return / 100
        # calculate annual contribution
        annual_contribution = self.current_salary * percent_contribution
        # return future value of the series formula
        return (self.current_savings * (1 + rate_of_return) ** years) + (annual_contribution * (((1 + rate_of_return) ** years) - 1) / rate_of_return)


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
