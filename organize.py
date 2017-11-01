import csv
taxon_dict={}
year_keys=[]
taxonID=[]
month_list=['01','02','03','04','05','06','07','08','09','10','11','12','all']

def get_organized(file):
	file=open(file, 'r')
	with open('taxon_list.csv','w') as csv_file:
		csvwriter = csv.writer(csv_file, delimiter=',')
		for line in file:
			line=line.split()
			names = ' '.join(line[1:])
			taxon_dict[line[0]]=names
			taxonID.append(line[0])
			csvwriter.writerow([line[0],names])
			
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
						'''
						Checking that entries have Lat/long coords
						'''
						if len(row['decimalLatitude']) > 4 or len(row['decimalLongitude']) > 4:
							data_dict[row['taxonID']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])

					else:
						if len(row['decimalLatitude']) > 4 or len(row['decimalLongitude']) > 4:

							data_dict[row['taxonID']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
				

			
get_data('observations.csv')
print('Processing Complete, beginning file creation')
#id, year, month, lat/long
'''
Writing data in format needed to new TXT file for SDM format
'''
with open('data_for_sdm.txt','w') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',')

	csvwriter.writerow(['taxonId','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

					
print('data_for_sdm.txt created successfully')
'''					
Writing data in format needed to new CSV file for easier user viewing
'''
with open('data_for_sdm.csv','w') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',')

	csvwriter.writerow(['taxonId','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

#print(taxonID)
print('data_for_sdm.csv created successfully. This is useful for visualizing the data in a clean excel form')
print('Beginning file creation for each Taxon ID for each month')
'''
making files for each taxonid for each month and all years
'''
for each in taxonID:
	if each!= 'taxonID':
		for month in month_list:
			filename = str(each + '-' + month + '-iNaturalist.txt')
			with open(filename,'w') as csv_file:
				csvwriter = csv.writer(csv_file, delimiter=',')
				csvwriter.writerow(['taxonId','year','month','latitude','longitude'])
				for id in data_dict:
					if id == each:
						if month == 'all':
							for year in data_dict[id]:
								for months in data_dict[id][year]:
									for coords in data_dict[id][year][months]:
										csvwriter.writerow([id,year, months,coords[0], coords[-1]])
						if month != 'all':
							for year in data_dict[id]:
								for months in data_dict[id][year]:
									if month == months:
										for coords in data_dict[id][year][month]:
											csvwriter.writerow([id,year, month,coords[0], coords[-1]])

		
		
print('File creation complete')


'''
The below can be used to update the list of taxonID's in the 
sdm R script by replaceing the list there with the printed output 
of the below function

check = []
for each in taxonID:
	word = str('"' + each + '" ' )
	check.append(word)

newlist =  ' '.join(check)
print(newlist)
'''
