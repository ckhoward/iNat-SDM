# iNaturalist SDM

## Basic Overview

This application provides a full data pipeline for getting and cleaning iNaturalist butterfly data, and running this data through Jeff Oliver's species distribution model, which creates rasters and image files that help scientists visualize how different butterfly species are distributed across the country, given the month of the year.

![input output](https://github.com/ckhoward/iNat-SDM/blob/master/imgs/inputoutput.jpg?raw=true "Input to output")

## System Requirements:
    Software: Python 3.6, R, Git, Anaconda(install as Admin), Bash on Ubuntu
    R packages: dismo, sp, raster, maptools

[Install Ubuntu Bash on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/install-win10)

[Install R on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-16-04-2)

Install R Packages by typing the following into Bash:
1. R
2. install.packages('raster')
3. install packages('sp')
4. install.packages('maptools')
5. install.packages('dismo')
    

Or you can Download a pre-analysis virtual image containing all of the system requirements, all of the project, file paths, and code for you, all you have to do is start from ## How To Use: 

VM Link: https://drive.google.com/file/d/0BxVqlUplrcsfalhDZlBxWHdIYjQ/view?usp=sharing

VM Username: User

VM Password: Butterfly (this is the same for sudo in Bash)

## Getting started:

1. Clone the required projects
 * Get Jeff Oliver's SDM with ```git clone https://github.com/jcoliver/ebutterfly-sdm.git```
 * Get this program with ```git clone https://github.com/ckhoward/ebutterfly-sdm.git```

2. Get your data
 * If downloading [GBIF Observations](http://www.inaturalist.org/observations/gbif-observations-dwca.zip), unzip the downloaded file, and move observations.csv into the directory ebutterfly-sdm/data/ (warning: many input files will be generated here)
 * If using updater.py and observation_getter.py..

3. Organize your files
 * Place inat_request.ipynb into the directory ebutterfly-sdm/ (this notebook will act as command and control)
 * Place organize.py into the directory ebutterfly-sdm/data/
 * Move taxon_list.txt from ebutterfly-sdm/data/gbif/ to ebutterfly-sdm/data/inaturalist


## How to use:
Run organize.py with ```python organize.py``` from the command line. This script:
 * Cleans the observations.csv data by removing extraneous and/or missing data (IDs not listed in Jeff's taxon_list file, for instance);
 * Creates a user-friendly file, data_for_sdm.csv, containing all observations, with data for taxonId, year, month, latitude, and longitude. A text copy is created too, just in case it is preferred. This makes it easier for users to sift through the data of interest, to find any glaring issues;
 * Creates 13 text files for every species listed in data_for_sdm.csv, one for each month, and one for all months, to be used as input for the SDM, as the format [taxonid-month-iNaturalist].

Run inat_request.ipynb with ```jupyter notebook``` from the command line.
Navigate to the header **Running the R Scripts through Bash**, then find the block:


    %%bash
    start=$(date +%s.%N)
    months=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12" "all")
    ids=("214017")

    for id in "${ids[@]}"; do
        for month in "${months[@]}"; do
            Rscript --vanilla scripts/run-sdm.R data/inaturalist/$id-$month-iNaturalist.txt $id-$month output/
        done
    done
    end=$(date +%s.%N)    
    runtime=$(python -c "print(${end} - ${start})")

    echo "Runtime was $runtime"

This code iterates on every species contained in the ```ids``` array, and for every month (and all observations), the run-sdm.R script takes in each species, by each month, and creates associated images and raster files.

Notice that the IDs are hardcoded. We know this is not ideal and are working on a fix. In the meantime, we have created a massive list of space separated IDs that can be plugged in as necessary. The list can be found [here](https://pastebin.com/sYdqyXqL). Additionally, organize.py contains a commented out function that takes taxon_list.txt and provides an output that can be copied and pasted into the bash ID array contained in the notebook. Thus, you're given the flexibility to choose what specific IDs you want to observe.

## Output:

![Species Distributions](https://github.com/ckhoward/iNat-SDM/blob/master/imgs/species.png?raw=true "October, November, December, All")



## Warnings

#### Data integrity:

From iNaturalist:
> "Our export system is a bit flawed, though: if you alter the filters to get more than 10,000 records
it may start omitting data, so the above techniques would probably be better. Plus, if you use GBIF,
your [users] can benefit from even more records from museums and such."

Anyone using iNaturalist data should perhaps use our API access code, Jeff's, or download the DwC-A that iNaturalist makes for GBIF.

Some of the research-grade observations did not have latitude and longitude entries. Our script takes care of this by omitting these data.

#### Runtimes:

Approximate run time for organization.py to clean and organize/write needed files for the SDM : ~5minutes

Approximate run time for SDM/R Script to fully run 5 Taxon ID's and recieve Raster Images: ~3minutes

Estimated run time for SDM/R Script to fully run all 760-780 Taxon ID's and recieve Raster Images: ~6.5hours


#### Space requirement:

When running the SDM on 760 species, the output produced is approximately 16 GBs in total. Consider your hard drive space before utilizing the SDM on large numbers of species.


## License

This program is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contribution

Have an issue? The repository is currently public, but this may change in the future. If you suddenly find that you do not have access to make alterations, file an issue and we will quickly respond. Our current list of to-dos:
 * Make the bash array dynamically access taxon IDs
 * Create titling for each output image generated by the SDM
 * Restructure output directory to organize output files by month (and all observations)

#### Alternative projects:

[Blue](https://github.com/Dtruong77/ua-acic-2017-midterm)
[Monarch](https://github.com/jetjr/HPC-inaturalist-sdm)
[JJARVIS](https://github.com/Sithyphus/Acic2017)
[JJARVIS2](https://github.com/jhanson3/ista-422-midterm) 
 
#### Contributors

Phillip Johnson, Daniel Phillips, Michael Reid, Jacob Smith, Chris Howard
