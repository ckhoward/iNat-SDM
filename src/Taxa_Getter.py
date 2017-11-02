
import requests
import json
"""
This module contains only a single function. Its purpose is to 
get the suspected taxa ids for a particular species name

"""

def get_taxa_id(species_name):
    '''
    This function returns the taxon_id when given the species name.
    
    Parameters:
    species_name: a string object representing a species name, e.g. "Danaus plexippus"
    
    Returns: ids, a list object containing integer id's for the species
    '''
    
    base_url = "http://api.inaturalist.org/v1/taxa/autocomplete?q="

    
    request = requests.get(base_url + "%20".join(species_name.split()))
    data = request.json()

    ids = []
    for i in data['results']:
        ids.append(i['id'])

    return ids
