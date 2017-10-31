# iNaturalist SDM 

System Requirements:
    Python 3.6
    R 
    

1. Download the Observations dump from http://www.inaturalist.org/observations/gbif-observations-dwca.zip This will alleviate some of the online calls to the iNaturalist server, ensuring that the server will not be overloaded by get requests for additional data. Unzip package and place observations.csv onto the designated folder where all data will be stored (GOTCHA.. do NOT place of desktop) (we focused our analysis to this download, due to the response we received from iNat. 
            
            "Our export system is a bit flawed, though: if you alter the filters to get more than 10,000 records
            it may start omitting data, so the above techniques would probably be better. Plus, if you use GBIF, 
            your students can benefit from even more records from museums and such."
            
Place organize.py and taxon_id.txt in the same directory as observations.csv. organize.py takes observations.csv, cleans the data, and outputs a user-friendly CSV, as well as the required text files to be used by the SDM, in a format of [taxonid-month-iNaturalist]. To run organize.py, open shell in the directory as the two folders and type <python organize.py>.

2. Place the Jupyter Notebook file (inat_request.ipynb) in the directory containing the R scripts. This notebook runs the input text files through the SDM and generates sets of raster and image files that correspond to the file: for every taxon id, there is a set for each month (12 in total), and a set for all observations.





# Approximate run times on laptop/desktop:
Approximate run time for organization.py to clean and organize/write needed files for the SDM : ~5minutes

Approximate run time for SDM/R Script to fully run 5 Taxon ID's and recieve Raster Images: ~3minutes

Estimated run time for SDM/R Script to fully run all 760-780 Taxon ID's and recieve Raster Images: ~6.5hours
