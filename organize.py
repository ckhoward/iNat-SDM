import csv
taxon_dict={}
year_keys=[]
taxonID=[]

def get_organized(file):
	file=open(file, 'r')
	for line in file:
		line=line.split()
		names = ' '.join(line[1:])
		taxon_dict[line[0]]=names
		taxonID.append(line[0])
	file.close()
	return (taxon_dict, taxonID)
hello = get_organized('taxon_list.txt')
data_dict={}
def get_data(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
			if row['taxonID'] not in data_keys and row['datasetName'] == 'iNaturalist research-grade observations':
				data_dict[row['taxonID']]= {}				
				'''
				organizing dictionary input into format {{year}, {month}, [lat, long]}
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
					
					
			elif row['datasetName'] == 'iNaturalist research-grade observations':	
				'''
				This gets rid of all non research grade observations
				'''	
				if len(row['eventDate'])>0 and row['eventDate'][4]=='-':
					year_key = data_dict[row['taxonID']].keys()
					if row['eventDate'][0:4]not in year_key:
						year_keys.append([row['eventDate'][0:4]])
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
				

			
get_data('observations.csv')
#id, year, month, lat/long
'''
Writing data in format needed to new CSV
'''
with open('data_for_sdm.csv','w') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',')
	csvwriter.writerow(['TaxonId','Year','Month','Latitude','Longitude'])
	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])


	
	


		
		
	
