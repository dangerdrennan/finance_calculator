from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm

def retirement_calulator(request):
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save
        
            years_to_retirement = profile.calculate_years_to_retirement()
            end_balance = profile.calculate_return(years_to_retirement)
            return render(request, 'calculator_result.html', {'retirement_savings': end_balance})
    else:
        form = ProfileForm()
    return render(request, 'retirement_calculator/calculator.html', {'form':form})