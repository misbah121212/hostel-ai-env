def grade(predicted, actual):
    if predicted == actual:
        return 1.0
    
    # partial credit example
    if predicted in ["Plumbing", "Electricity", "Cleaning", "Other"]:
        return 0.2
    
    return 0.0