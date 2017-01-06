# This program 
# 1) goes through each file in the output directory created by extract-SvrJob.py
# 2) calculate the time difference of the first entry and the last entry for each SvrJob file
# 3) outputs a sorted file with the format: Duration|SvrJob|StartTime|EndTime
# Author: Vicky Li Horst

import os
import re
import subprocess
from datetime import datetime

workingDirectory = "/Users/mli/Projects/isc-dotnet-log-parser/files/"
fileFolder = workingDirectory + "output/"
resultFile = workingDirectory + "result.txt"
sortedResultFile = workingDirectory + "resultSorted.txt"
timestamp = r'\d{2}:\d{2}:\d{2}:\d{3}'
timestampFormat = '%H:%M:%S:%f'

#open the result file for writing
with open(resultFile, "w") as result:
	# write the header with column names
	result.write("Duration|SvrJob|StartTime|EndTime" + "\n")
	# loop through all the files in fileFolder
	for filename in os.listdir(fileFolder):
		file = fileFolder + filename # the complete path to file
		#open each file in the fileFolder
		with open(file, 'r') as f:
			firstLine = f.readline()
			# find the timestamp in the firstLine
			initialTimeObject = re.search(timestamp,firstLine)
			if initialTimeObject: # because of the nature of the log, there will always be a timestamp for each entry. Thus, I'm not handling the ELSE situation here due to time strains
				initialTime = initialTimeObject.group(0)
			# find the lastLine in the file
			f.seek(-2,2) # jump to the second last byte, which is the last character before the EOL. the whence parameter is set to 2 because my reference point is the end of the file. 
			while f.read(1) != b"\n": # the while loop moves the cursor back 2 characters at a time and reads one character forward until it finds EOL
				f.seek(-2,1) # the whence parameter is 1 because the reference point is the current position
			#now the cursor is at the EOL of the second to the last line
			lastLine = f.readline()
			finalTime = re.search(timestamp,lastLine).group(0)
			# now find the time duration beween finalTime and initialTime
			duration = datetime.strptime(finalTime,timestampFormat) - datetime.strptime(initialTime,timestampFormat)
			result.write(str(duration) + "|" + filename + "|" + initialTime + "|" + finalTime + "\n") # this is the unsorted result

# Now write to the resultSorted.txt file after sorting result.txt by the time duration
cmd = subprocess.check_output("sort -r " + resultFile + " > " + sortedResultFile, shell=True)


