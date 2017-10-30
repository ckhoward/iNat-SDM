
# coding: utf-8

# In[1]:

import requests
import json
from IPython.display import display
import time


class obs_grabber:
    
    def __init__(self, request_delta):
        self.request_delta = request_delta
        return self
    
    @staticmethod
    def get_observations_for_page(data):
        obs_lst = []
    
        for i in data:
            specific_obs = i
        
        d = {}
        d["species name"] = ''
        d["year"] = specific_obs['observed_on_details']['year']
        d["month"] = specific_obs['observed_on_details']['month']
        d['lat'] = specific_obs['geojson']['coordinates'][1]
        d['long'] = specific_obs['geojson']['coordinates'][0]
        
        obs_lst.append(d)

    
        return obs_lst
    
    @staticmethod    
    def get_count_one_month(id_no_lst, month, year):
        
        count = 0
        for i in id_no_lst:
            count += int(get_observation(i, month, year)['total_results'])
        return count


    @staticmethod
    def get_all_obs_for_id(idno, month, year):
        
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

    


