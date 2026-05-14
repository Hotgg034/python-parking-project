def park_car(spaces):
    if spaces > 0:
        return "Parked successfully"
    return "No spaces available"

def calculate_fee(hours):
    if hours < 0:
        return "Error: Hours cannot be negative"
    if hours == 0:
        return "Error: No parking time recorded"
    return hours * 21~def calculate_fee(hours):
    if hours < 0:
        return "Error: Hours cannot be negative"
    if hours == 0:
        return "Error: No parking time recorded"
    return hours * 2
