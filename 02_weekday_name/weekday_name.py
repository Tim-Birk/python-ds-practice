def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if not type(day_of_week) == int:
        return None
    elif not (day_of_week >= 1 and day_of_week <= 7):
        return None

    if day_of_week == 1:
        return "Sunday"
    elif day_of_week == 2:
        return "Monday"
    elif day_of_week == 3:
        return "Tuesday"
    elif day_of_week == 4:
        return "Wednesday"
    elif day_of_week == 5:
        return "Thursday"
    elif day_of_week == 6:
        return "Friday"
    elif day_of_week == 7:
        return "Saturday"

print(f"weekday_name(1) should return Sunday, result: {weekday_name(1)}")
print(f"weekday_name(7) should return Saturday, result: {weekday_name(7)}")