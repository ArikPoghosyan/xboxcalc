from django.shortcuts import render

def calculate_conversion(request):
    result = None
    total_with_ultimate = None
    unit = "days"  # Default unit is days
    
    if request.method == "POST":
        subscription = request.POST.get("subscription")
        days_remaining = int(request.POST.get("days", 0))
        month_remaining = int(request.POST.get("months", 0))
        unit = request.POST.get("unit", "days")  # Get selected unit (days or months)

        # Conversion ratios (for converting to Ultimate days)
        conversion_ratios = {
            "core": 2,       # Game Pass Core: 2:1
            "pc": 1.5,       # PC Game Pass: 3:2
            "standard": 1.33, # Standard/Console Game Pass: 4:3
            "ea": 3,         # EA Play: 3:1
        }

        # Calculate converted Ultimate days
        if subscription in conversion_ratios:
            if unit == "months" and month_remaining > 0:
                # Convert months to days and then apply the conversion ratio
                converted_days = month_remaining * 30  # 1 month = 30 days
                result = converted_days / conversion_ratios[subscription]  # Convert to Ultimate days
            else:
                # Convert directly from days to Ultimate days using the conversion ratio
                converted_days = days_remaining / conversion_ratios[subscription]
                result = converted_days

            # Add 1 month of Ultimate (30 days) to the converted days
            
    return render(
        request,
        'calculator/index.html',
        {'result': result, 'total_with_ultimate': total_with_ultimate, 'unit': unit}
    )
