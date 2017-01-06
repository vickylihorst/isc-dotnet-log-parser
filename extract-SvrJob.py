# This program takes the list of unique server jobs, extract all the lines in the original .Net log that contains that SrvJob number, and creates new files for each unique SvrJob numbers
# The program runs the following line for each unique SrvJob numbers:
# grep "SvrJob=6920]" Net.txt > SvrJob6920.txt
# note I needed to add "]" to the grep command as otherwise grepping "SvrJob=70" would aslo get "SvrJob=7012"
# Author: Vicky Li Horst

import subprocess 
import shlex
import os

workingDirectory = "/Users/mli/Projects/isc-dotnet-log-parser/files/"
uniqueSvrJobFile = "uniqueSvrJob.txt"
dotNetLogFile = "Net.txt"
outputDirectory = workingDirectory + "output/"

# check if the output directory already exists, if not, create a new one
if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)


with open(workingDirectory + uniqueSvrJobFile, 'r') as uniqueSvrJob:
	for line in uniqueSvrJob:
		# The following line runs a grep command that looks like:
		# grep "SvrJob=8160]" /Users/mli/Projects/isc-dotnet-log-parser/files/Net.txt > /Users/mli/Projects/isc-dotnet-log-parser/files/output/SvrJob=8160.txt
		cmd = subprocess.check_output('grep \"'+ line.rstrip()  + ']\" ' + workingDirectory + dotNetLogFile + ' > ' + outputDirectory + line.strip() + ".txt", shell=True);
	
	


