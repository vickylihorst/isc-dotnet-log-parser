# isc-dotnet-log-parser

a program to parse ISC .NET log

## These are the steps:

### 1. In the same directory where the .Net log file is, execute the following command to extract all the fields that match `SvrJob=[0-9]*\|SvrJob=[a-zA-Z]*`:

	`grep -o 'SvrJob=[0-9]*\|SvrJob=[a-zA-Z]*' Net.txt > OnlySvrJob.txt`

	As you may have expected, the output file contain duplicated fields because of the nature of the .NET log, so we need get the unique SvrJob ID's.

### 2. Sort the unique lines using the following command:

	`sort onlySvrJob.txt | uniq > uniqueSvrJob.txt`

### 3. Run the included `extract-SvrJob.py` to create individual files that contain all entries from the .Net log for a given a the SvrJob number

	The output files will be created in the specified `Output/` directory

### 4. Run the included `time-duration-calc.py` to go through the files created from the previous step and outputs file that contains the time duration of each SrvJob sorted by the duration.

