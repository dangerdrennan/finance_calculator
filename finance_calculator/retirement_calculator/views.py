from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm

def retirement_calulator(request):
    retirement_savings = None

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            years_to_retirement = profile.calculate_years_to_retirement()
            retirement_savings = profile.calculate_return(years_to_retirement)
            ## saves user. Uncomment after log-in feature implemented
            # profile.user = request.user
            # profile.save()
    else:
        form = ProfileForm()

    context = {'form': form, 'retirement_savings': retirement_savings}
    return render(request, 'retirement_calculator/calculator.html', context)
