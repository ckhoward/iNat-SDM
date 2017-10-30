
# coding: utf-8

# In[1]:

import requests
import json
from IPython.display import display
import time


class obs_grabber:
    '''
        Grabs the observations for a specific species (with the taxonomy id) and a request delta. The request delta
        is the time in seconds to wait inbetween each request. 
    
    '''
    
    def __init__(self, request_delta=0, species_name=''):
        self.request_delta = request_delta
        self.species_name = species_name
        return self
    
    
    def get_observations_for_page(data):
        '''
            This is a private method for the purpose of grabbing the observation list from the 
            given data.
            
            Params:
                data: a json soup of data
                
            returns: a list of dictionaries with the information mapped to the keyword that is 
            associated with it
        '''
        
        obs_lst = []
    
        for i in data:
            specific_obs = i
        
        d = {}
        d["species name"] = self.species_name
        d["year"] = specific_obs['observed_on_details']['year']
        d["month"] = specific_obs['observed_on_details']['month']
        d['lat'] = specific_obs['geojson']['coordinates'][1]
        d['long'] = specific_obs['geojson']['coordinates'][0]
        
        obs_lst.append(d)

    
        return obs_lst
    
        
    def get_count_one_month(id_no_lst, month, year):
        
        count = 0
        for i in id_no_lst:
            count += int(get_observation(i, month, year)['total_results'])
        return count


    
    def get_all_obs_for_id(idno, month, year):
        '''
            This method finds all of the observations for one month and returns a list of dictionaries 
            that contains the associated information mapped to the keyword that was found in the json.
            
            params:
                idno: a taxonomy ID that can be found on iNaturalist, this should be a string
                month: a string month number 1-12 starting with january and ending with december
                year: a string year number 0000-9999 (but should realistically be 1990-20XX. 
                
           returns:
               a dictionary with the information mapped to the associated keyword
        '''
        
        base_url = "http://api.inaturalist.org/v1/observations?"
        end_url = "&order=desc&order_by=created_at"
        
        url = base_url  + 'taxon_id=' + str(idno) + '&page=1' + "&per_page=200" + "&quality_grade=research" + '&month=' + month + '&year' + year + end_url
        
        idno = str(idno)
        request = requests.get(url)
        data = request.json()
        page = 1
        
        taxon_lst = []
        
        
        
        while(len(data['results']) > 0):
            
            
            obs_out = obs_grabber.get_observations_for_page(data['results'])
            
            for i in obs_out:
                taxon_lst.append(i)
            
            
            #Url builder, for the request
            page += 1
            base_url = "http://api.inaturalist.org/v1/observations?"
            end_url = "&order=desc&order_by=created_at"
            
            url = base_url  + 'taxon_id=' + str(idno) + '&page=' + str(page) + "&per_page=200" + "&quality_grade=research" + '&month=' + month + '&year' + year + end_url
                            
            request = requests.get(url)
            data = request.json()
            
            # Limit the number of calls to prevent blacklisting
            time.sleep(self.request_delta)
        
        return {idno : taxon_lst}

    


