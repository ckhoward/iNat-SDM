taxon_dict={}
def get_organized(file):
	file=open(file, 'r')
	for line in file:
		line=line.split()
		taxon_dict[line[0]]=' '.join(line[1:])
		print(taxon_dict[line[0]])
	return taxon_dict
		
hello = get_organized('taxon_list.txt')
print(taxon_dict)