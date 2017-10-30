import datetime
import Observation_Getter

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
    
def parse_tax_file(fname):
    """
    Parses the tax file to build a dictionary with the taxonomy ID 
    This is an extremely hardcoded function and should not be used normally
    
    params:
        fname: a string representing a file name
    
    returns: a dictionary with the taxonomy id mapped to the species name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    
    """
    
    tax_spec = {}
    with open(fname, 'r') as ptr:
        ptr.readline() #skip the header line
        
        for line in ptr:
            lst = line.split()
            tax_spec[lst[0]] = ' '.join(lst[1:])
            
    return tax_spec
        

def main():
    date1 = ''
    date2 = ''
    
    calls_delta = 0
    fname = ''
    
    id_species = parse_tax_file(fname)
    
    lst_dates = calculate_datetime_difference(date1, date2)
    
    lst_all_taxon_obs = []
    
    for taxon_id in id_species:
        
        current = obs_grabber(calls_delta, id_species[taxon_id])
        
        for date in lst_dates:
            lst.append(current.get_all_obs_for_id(taxon_id, date['month'], date['year']))
        
    
    print(lst_all_taxon_obs)
    
    

main()