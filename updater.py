import datetime

def calculate_datetime_difference(past, requested_day=""):
    """
        Calculates the difference in the datetime of the previous update
        and the current update
        
        params: 
            past: a string object that is a date of last update
            requested_day: an optional string object that is the newly requested day
            
        returns:
            a dictionary of dictionaries with an integer mapped to the dictionary 
            that contains the month mapped to an integer (1-12) and a year mapped to an 
            integer
    
    """
    past_year = int(past.split()[2])
    past_month = int(past.split()[0])
    past_day = int(past.split()[1])
    
    new_year = ''
    new_month = ''
    new_day = ''
    
    if requested_day == '':
        new_year = date.today().year
        new_month = date.today().month
        new_day = date.today().day

    else:
        new_year = int(requested_day.split()[2])
        new_month = int(requested_day.split()[1])
        new_day = int(requested_day.split()[0])
        
        new_date = datetime.date(int(new_year), int(new_month), int(new_day))
        
    
    date_dict = {}
    index = 0
    
    while(True):
        if past_year >= new_year:
            if past_month >= new_month:
                break
        current_date_dict = {}
        current_date_dict['month'] = past_month
        current_date_dict['year'] = past_year
        
        past_month += 1
        
        if past_month >= 13:
            past_month = 1
            past_year += 1
        
        date_dict[index] = current_date_dict
        index += 1
            
    return date_dict
    


def main():
    day = ''
    month = ''
    year = ''
    calls_min = ''
    
    
    print(calculate_datetime_difference('10 11 2015', '10 11 2016'))
    
    

main()