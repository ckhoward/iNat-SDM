import csv
taxon_dict={}
def get_organized(file):
	file=open(file, 'r')
	for line in file:
		line=line.split()
		taxon_dict[line[0]]=' '.join(line[1:])
		#print(taxon_dict[line[0]])
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
				data_dict[row['taxonID']]['date'] = [row['eventDate']] 
				data_dict[row['taxonID']]['latitude'] = [row['decimalLatitude']]
				data_dict[row['taxonID']]['longitude'] = [row['decimalLongitude']]
			elif row['datasetName'] == 'iNaturalist research-grade observations':	
				data_dict[row['taxonID']]['date'].append(row['eventDate'])
				data_dict[row['taxonID']]['latitude'].append(row['decimalLatitude'])
				data_dict[row['taxonID']]['longitude'].append(row['decimalLongitude'])
			
			#print(row['taxonID'])
			
			
get_data('observations.csv')
print(data_dict['27818'])
