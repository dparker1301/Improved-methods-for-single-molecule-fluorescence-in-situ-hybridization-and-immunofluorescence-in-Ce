#The purpose of this script is to take smFISH spot data produced by the Matlab implementation of FISHquant in __spots.txt files and convert it to a form that can be used by the web-based Python/ImJoy implementation

#Import stuff

import csv			#Import csv to allow export as .csv files
import os			#Import os to permit system navigation


#Navigate a directory to find all __spots.txt files in all subdirectories and make a list of them.

directory = input("Enter the file path you want to convert")			#Ask the user which directory they want to convert from __spots.txt files to ImJoy compatible .csv files.
listofiles = []			#Initialize list for each of the __spots.txt files
for subdir, dirs, files in os.walk(directory):			#Loop to scan for __spots.txt files in the user specified directory.
    for filename in files:			#Loop over all the files in the directories
        filepath = subdir + os.sep + filename			#Define the file path as the filename plus the full file path.
        if filename.endswith("__spots.txt"):			#If the file is a __spots.txt file ->
            listofiles.append(filepath)			#Add it to the file list to convert.


#Set up the csv writer to convert the data to a .csv file.

from csv import writer			#Import csv writer.
def append_list_as_row(file_name, list_of_elem):			#Define a function to append lists as rows in the new .csv file using the same file name as the __spots.txt file and a list defined later.
    with open(file_name, 'a+', newline='') as write_obj:			#Open the new .csv file using the same name as the __spots.txt file and set it up to append data
        csv_writer = writer(write_obj)			#Set up csv_writer to writer to the new file.
        csv_writer.writerow(list_of_elem)			#Use csv_writer to add the list to a new row.


#Set up the ZYX data converter to extract RNA spot coordinates and swap data from YXZ ordering to ZYX.

def ZYX_spot_convert( strs ):			#Define the ZYX converter function

	#Make header
    
    with open(savefilename, 'w', newline='') as file:			#Open a user file.
        wr = csv.writer(file)			#Set up wr to write to the new file.
        header = ['Z', 'Y', 'X']			#Define the headers.
        wr.writerow(header)			#Write the headers to the .csv file
        
	#Extract and convert data
    
    with open(anyfile, newline = '') as spotfile:			#Open the file to be converted.                                                                                    
        spot_reader = csv.reader(spotfile, delimiter='\t')			#Set up spot_reader to read the tab delimited file.
        spotfile_line_count = 0			#Initialize spotfile_line_count to count the number of lines in the RNA spot data
        spots_data_start = 0			#Initialize spots_data_start to use later to set the spotfile_line_count to the line data starts on once it gets through the __spots.txt preamble.
        spots_data_end = 1000000000000000			#Set the spots_data_end to a ridiculously high number. I couldn't get the spots_data_end variable to reinitialize later without this.
        for line in spot_reader:			#Iterate through the file
            spotfile_line_count += 1			#Add 1 to the line count for each line to keep track of where data will begin and end.
            if "SPOTS_END" in line:			#Find where the data ends
                    spots_data_end = (spotfile_line_count)			#Then set the spots_data_end to where the data ends
            if spotfile_line_count != spots_data_end:			#Now that the end is defined, iterate through all the data
                if "SPOTS_START" in line:			#And find where the data actually starts
                    spots_data_start = (spotfile_line_count)			#Then set the beginning of the data to this line
                if  spots_data_start > 0:			#Now that the spots_data_start variable shows where the data starts
                    if spotfile_line_count > (spots_data_start+1):			#Start looking at the data on the next line
                        ZYX_list = []			#And initialize the ZYX_list within this line
                        ZYX_list.append(line[18])			#Then reorder the coordinate data in Z, Y, X form
                        ZYX_list.append(line[16])			#Then reorder the coordinate data in Z, Y, X form
                        ZYX_list.append(line[17])			#Then reorder the coordinate data in Z, Y, X form
                        append_list_as_row(savefilename, ZYX_list)			#Append this coordinate to the new spots.csv file as a row.

        
for anyfile in listofiles:			#Run through all of the files in the user specified folder.
    print(anyfile)			#List the file being converted
    savefilename = anyfile.replace(".txt", ".csv")			#Set the savefile name to be the same as the original, with a .csv suffix instead of .txt.
    ZYX_spot_convert(anyfile)			#Convert the RNA spot coordinate data
        