#This script takes the output of Antifade_quantification_table_maker.py and converts it to a form that allows statistics to be performed more easily.

#Import stuff and set parameters.
import csv			#Import csv so I can write to .csv files
import os			#Import os for general OS navigation
import statistics			#Import statistics to do statistics


#Set up the csv writer to convert the data to a .csv file.             
from csv import writer				#Import writer
def append_list_as_row(file_name, list_of_elem):			#Define function that takes the user file name and the tabulated output to add to a .csv file
    with open(file_name, 'a+', newline='') as write_obj:			#Open user defined file in append mode
        csv_writer = writer(write_obj)			#Set up csv_writer to writer to the new file.
        csv_writer.writerow(list_of_elem)			#Use csv_writer to add the list to a new row.    


#Write file and add header
with open('OUTPUT_FILE_NAME_GOES_HERE', 'w', newline='') as file:			#Open user file name
    wr = csv.writer(file)			#Open user file name
    header = ['Antifade', 'Transcript', 'Stack_No', 'Max', 'Min', 'Mean', 'Max_norm', 'Min_norm', 'Mean_norm']			#generate a header for each column
    wr.writerow(header)			#Write the header
    

#Define column values
with open('INPUT_FILE_GOES_HERE', newline = '') as antifile: 			#Open user file
    anti_reader = csv.reader(antifile, delimiter=',')			#Split the csv file by commas
    antifile_line_count = -1			#Initialize line counter at -1 (so the counter below starts at 0)
    
    
    for line in anti_reader:			#Iterate through the lines of the file
        antifile_line_count += 1			#Add to the line counter
        if antifile_line_count > 0:			#Start taking data only once past the header
            for i in range(0,100):			#Iterate over the 100 images
                max_index = i+4			#And index the max values at column 5
                min_index = max_index + 100			#Start indexing the min values when they start
                mean_index = min_index + 100			#Start indexing the mean values when they start
                rowlist = []			#Initialize the list of data
                rowlist.append(line[0])			#Append the antifade info to the list
                rowlist.append(line[1])			#Append the transcript info to the list
                rowlist.append(i + 1)			#Append the image number to the list
                rowlist.append(line[max_index])			#Append the max intensity value from the region of interest to the list
                rowlist.append(line[min_index])			#Append the min intensity value from the region of interest to the list
                rowlist.append(line[mean_index])		#Append the mean intensity value of the region of interest to the list
                rowlist.append(int(line[max_index])/int(line[4]))			#Append the normalized max intensity value of the region of interest to the list
                rowlist.append(int(line[min_index])/int(line[104]))			#Append the normalized min intensity value of the region of interest to the list
                rowlist.append(float(line[mean_index])/float(line[204]))			#Append the normalized mean intensity value of the region of interest to the list
                append_list_as_row('OUTPUT_FILE_NAME_GOES_HERE', rowlist)			#Add the list to the new file as a row