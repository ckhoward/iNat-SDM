import csv
taxon_dict={}
def get_organized(file):
	file=open(file, 'r')
	for line in file:
		line=line.split()
		taxon_dict[line[0]]=' '.join(line[1:])
		#print(taxon_dict[line[0]])
	file.close()
	return taxon_dict
		
hello = get_organized('taxon_list.txt')
#print(taxon_dict)
data_dict={}
def get_data(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
			if row['taxonID'] not in data_keys and row['datasetName'] == 'iNaturalist research-grade observations':
				data_dict[row['taxonID']]= {}				
				'''
				organizing dictionary input into format {{taxonID}, {year}, {month}, [lat, long]}
				'''
				if row['eventDate'][4]=='-':
					data_dict[row['taxonID']][row['eventDate'][0:4]]={}
					data_dict[row['taxonID']][row['eventDate'][0:4]]['01']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['02']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['03']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['04']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['05']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['06']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['07']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['08']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['09']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['10']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['11']=[]
					data_dict[row['taxonID']][row['eventDate'][0:4]]['12']=[]
					
					
					#format is Latitude, longitude
					data_dict[row['taxonID']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
					#print(data_dict[row['taxonID']][row['eventDate'][0:4]])
					
					
			elif row['datasetName'] == 'iNaturalist research-grade observations':	
				'''
				This gets rid of all non research grade observations
				'''	
				if len(row['eventDate'])>0 and row['eventDate'][4]=='-':
					year_key = data_dict[row['taxonID']].keys()
					if row['eventDate'][0:4]not in year_key:
						data_dict[row['taxonID']][row['eventDate'][0:4]]={}
						data_dict[row['taxonID']][row['eventDate'][0:4]]['01']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['02']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['03']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['04']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['05']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['06']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['07']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['08']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['09']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['10']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['11']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]]['12']=[]
						data_dict[row['taxonID']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])

					else:
						data_dict[row['taxonID']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
				
						#print(row['taxonID'])
		
			
get_data('observations.csv')
display(data_dict['27818'])				
