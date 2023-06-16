from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_age = models.IntegerField(default=33)
    retirement_age = models.IntegerField(default=65)
    current_salary = models.FloatField(default=87477)
    current_savings = models.FloatField(default=10330)
    percent_contribution = models.FloatField(default=20)
    rate_of_return = models.FloatField(default=4)
    projected_yearly_salary_increase = models.FloatField(default=3.25)
    max_salary = models.IntegerField(default=143000)

    def calculate_years_to_retirement(self):
        return self.retirement_age - self.current_age
    
    def calculate_return(self, years):
        # Normalize the percentages for calculation
        percent_contribution = self.percent_contribution / 100
        rate_of_return = self.rate_of_return / 100
        yearly_salary_increase = self.projected_yearly_salary_increase / 100

        # Initial conditions
        total = self.current_savings
        salary = self.current_salary

        for year in range(years):
            # Add this year's contribution
            
            total += salary * percent_contribution

            # Grow the total amount and salary by their respective rates
            total *= (1 + rate_of_return)
            salary *= (1 + yearly_salary_increase)
            # Never outpace max salary
            salary = min(salary, self.max_salary)
        return total



    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
