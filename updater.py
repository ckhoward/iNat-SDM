import datetime
import Observation_Getter
import csv

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
        new_year = datetime.date.today().year
        new_month = datetime.date.today().month
        new_day = datetime.date.today().day

    else:
        new_year = int(requested_day.split()[2])
        new_month = int(requested_day.split()[1])
        new_day = int(requested_day.split()[0])
        
        new_date = datetime.date(int(new_year), int(new_month), int(new_day))
        
    
    date_lst = []
    index = 0
    
    while(True):
        if past_year >= new_year:
            if past_month >= new_month:
                break
        current_date_dict = {}
        current_date_dict['month'] = str(past_month)
        current_date_dict['year'] = str(past_year)
        
        past_month += 1
        
        if past_month >= 13:
            past_month = 1
            past_year += 1
        
        date_lst.append(current_date_dict)
        index += 1
            
    return date_lst
    
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
        

def clean_requests(request_lst):
    '''
        Cleans the request list and forms it into something that can be translated into a csv
        
        params:
            request_lst: the list that would be retrieved from Observation_Getter.ObsGrabber.get_all_obs_for_id()
            primary key: the string of the primary key, in this case it would be taxon id
            
        returns:
            a list of orderd dictionaries
    '''
    output_lst = []
    for i in request_lst:
        output_lst.extend(i)
    
    return output_lst

def write_to_csv(lst, fname_out):
    if len(lst) < 1:
        return None

    
    fieldnames = lst[0]
    with open(fname_out, 'w', newline='') as ptr:
        od_writer = csv.DictWriter(ptr, fieldnames=fieldnames)
        od_writer.writeheader()
        for i in lst:
            od_writer.writerow(i)
        
    
def main():
    date1 = '9 10 2017'
    date2 = ''
    
    calls_delta = .01
    fname = 'taxon_list.txt'
    
    id_species = parse_tax_file(fname)
    
    lst_dates = calculate_datetime_difference(date1)
    
    lst_all_taxon_obs = []
    
    for taxon_id in id_species:
        
        current = Observation_Getter.ObsGrabber(calls_delta, id_species[taxon_id], taxon_id)
        
        for date in lst_dates:
            lst_all_taxon_obs.append(current.get_all_obs_for_id(taxon_id, date['month'], date['year']))
        
    lst_all_taxon_obs = clean_requests(lst_all_taxon_obs)
    write_to_csv(lst_all_taxon_obs, 'out.csv')
    
    
main()
