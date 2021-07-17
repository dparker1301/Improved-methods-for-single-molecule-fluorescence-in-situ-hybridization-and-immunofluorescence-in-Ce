#Import stuff and set parameters.
import csv							#Import csv so I can write to .csv files
import os							#Import os for general OS navigation
import statistics			#Import statistics to do statistical analysis
import math			#Import math for some other analysis


#Set up the csv writer to convert the data to a .csv file.                
from csv import writer			#Import writer
def append_list_as_row(file_name, list_of_elem):			#Define function that takes the user file name and the tabulated output to add to a .csv file
    with open(file_name, 'a+', newline='') as write_obj:			#Open user defined file in append mode (Idk what as write_obj does)
        csv_writer = writer(write_obj)								#Set up csv_writer to writer to the new file.
        csv_writer.writerow(list_of_elem)							#Add new row to .csv using defined list     


#Write file and add header
with open('OUTPUT_FILE_GOES_HERE', 'w', newline='') as file:			#Open user file name
    wr = csv.writer(file)			#Set up wr to write to the file
    header = ['Antifade', 'Transcript', 'Stack_No', 'Avg_Max', 'Std_Max', 'SEM_Max', 'Avg_Min', 'Std_Min', 'SEM_Min', 'Avg_Mean', 'Std_Mean', "SEM_Mean", 'Norm_avg_Max', 'Norm_std_Max', 'Norm_SEM_Max', 'Norm_avg_Min', 'Norm_std_Min', 'Norm_SEM_Min', 'Norm_avg_Mean', 'Norm_std_Mean', "Norm_SEM_Mean"]			#generate a header for each column
    wr.writerow(header)			#Write the header


#Open file, determine which antifade/trancript combos exist, and make a dictionary for each set    
with open('INPUT_FILE_GOES_HERE', newline = '') as antifile:			#Opens the second antifade data file
    anti_reader = csv.reader(antifile, delimiter=',')			#Splits the file by commas
    antifile_line_count = -1			#Initialize the line counter
    
    data_list = []			#Initialize the list of data
    for line in anti_reader:			#Iterate over the data
        antifile_line_count += 1			#Add to the line count variable
        if antifile_line_count > 0:			#Once into the data ->
            if str(line[0]+"_"+line[1]) not in data_list:			#Look to see if a string of Antifade_transcript exists
                data_list.append(str(line[0]+"_"+line[1]))			#If it doesn't add it to the list of data
    
                
    dictionaries = {}			#Initialize a dictionary
    for dataset in data_list:			#Iterate over the data list
        dictionaries[dataset] = {}			#And make each data list a new dictionary
        
        
#Open the input file again to collect data              
with open('INPUT_FILE_GOES_HERE', newline = '') as second_antifile:			#Opens the second antifade data file
    second_antifile_reader = csv.reader(second_antifile, delimiter=',')			#Splits the file by commas
    first_row = next(second_antifile_reader, None)			# skip the headers
    data = list(second_antifile_reader)			#Save each row of the file as an item in the list "data"	
    
    for thing in dictionaries:			#Iterate over each of the antifade/transcript dictionaries
        nameofdict = thing			#Set the name of the dictionary being iterated on to the antifade/transcript combo
        max_dicts = {}			#Initialize a dictionary for the maximum intensity values
        min_dicts = {}			#Initialize a dictionary for the minimum intensity values
        mean_dicts = {}			#Initialize a dictionary for the mean intensity values
        norm_max_dicts = {}			#Initialize a dictionary for the normalized max intensity values
        norm_min_dicts = {}			#Initialize a dictionary for the normalized min intensity values
        norm_mean_dicts = {}			#Initialize a dictionary for the normalized mean intensity values
        for numb in range(1,101):			#Iterate over each of the 100 values
            numbstr = str(numb)			#Turn the value into a string
            max_dicts[numbstr] = {}			#Add key values 1-100 to the max dictionary
            min_dicts[numbstr] = {}			#Add key values 1-100 to the min dictionary
            mean_dicts[numbstr] = {}			#Add key values 1-100 to the mean dictionary
            norm_max_dicts[numbstr] = {}			#Add key values 1-100 to the normalize max dictionary
            norm_min_dicts[numbstr] = {}			#Add key values 1-100 to the normalize min dictionary
            norm_mean_dicts[numbstr] = {}			#Add key values 1-100 to the normalize mean dictionary
            
        
        #Get the data from each individual line as 1 item lists
        for dataline in data:			#Now that the dictionaries are set up iterate over the data again
            score = dataline[2]			#Set score to the image number (ie 1-100)
            if nameofdict == str(str(dataline[0]+"_"+dataline[1])):			#Find the dictionary corresponding to the antifade and transcript written on the line
                namesaver1 = str(dataline[0])			#Save the antifade info as namesaver1
                namesaver2 = str(dataline[1])			#Save the transcript info as namesaver2
                maxlist = []			#Initialize a list for the maximum values in the line
                maxlist.append(int(dataline[3]))			#Append the maximum value for the image to the maxlist
                minlist = []			#Initialize a list for the mainimum values in the line
                minlist.append(int(dataline[4]))			#Append the minimum value for the image to the minlist
                meanlist = []			#Initialize a list for the mean values in the line
                meanlist.append(float(dataline[5]))			#Append the mean value for the image to the meanlist
                normmaxlist = []			#Initialize a list for the normalized maximum values in the line
                normmaxlist.append(float(dataline[6]))			#Append the normalized maximum value for the image to the normmaxlist
                normminlist = []			#Initialize a list for the normalized minimum values in the line
                normminlist.append(float(dataline[7]))			#Append the normalized minimum value for the image to the normalizedminlist
                normmeanlist = []			#Initialize a list for the normalized mean values in the line
                normmeanlist.append(float(dataline[8]))			#Append the normalize mean value for the image to the normmeanlist
                
                
                #Make a dictionary of all values for each exposure number (ie all max values from exposure 1 across every image)
                for numb2 in range(1,101):			#Iterate over 100 values
                    if str(numb2) == score:			#And if the number is the same as the score (exposure number)
                        try:			#Try to add the data to the dictionary if the key-value pair exists
                            max_dicts[numb2] += (maxlist)			#Append the max value to the dictionary key
                            min_dicts[numb2] += (minlist)			#Append the min value to the dictionary key
                            mean_dicts[numb2] += (meanlist)			#Append the mean value to the dictionary key
                            norm_max_dicts[numb2] += (normmaxlist)			#Append the normalized max value to the dictionary key
                            norm_min_dicts[numb2] += (normminlist)			#Append the normalized min value to the dictionary key
                            norm_mean_dicts[numb2] += (normmeanlist)			#Append the normalized mean value to the dictionary key
                        except KeyError:			#A KeyError will throw if you try to append a list to an key with no value, so these assign the initial key-value pair
                            norm_max_dicts[numb2] = (normmaxlist)			#Assign first normalized max key value
                            norm_min_dicts[numb2] = (normminlist)			#Assign first normalized min key value
                            norm_mean_dicts[numb2] = (normmeanlist)			#Assign first normalized mean key value
                            max_dicts[numb2] = (maxlist)			#Assign first max key value
                            min_dicts[numb2] = (minlist)			#Assign first min key value
                            mean_dicts[numb2] = (meanlist)			#Assign first mean key value
        
        
        #Set up lists to do calculations/statistics on                    
        avg_max_list = []
        std_max_list = []
        sem_max_list = []
        avg_min_list = []
        std_min_list = []
        sem_min_list = []
        avg_mean_list = []
        std_mean_list = []
        sem_mean_list = []
        norm_avg_max_list = []
        norm_std_max_list = []
        norm_sem_max_list = []
        norm_avg_min_list = []
        norm_std_min_list = []
        norm_sem_min_list = []
        norm_avg_mean_list = []
        norm_std_mean_list = []
        norm_sem_mean_list = []
        
        
        #Do calculations and statistics. Each block is essentially identical so only the first is annotated. Should have just made a function.
        for maxi in max_dicts:			#Loop over the max value dictionaries
            if len(max_dicts[maxi]) > 0:			#If there is data in the dictionary ->
                maxilist = list(map(float, max_dicts[maxi]))			#Turn the values in the dictionary into a list of floats
                avg_max = statistics.mean(maxilist)			#Take the average of the list
                std_max = statistics.stdev(maxilist)			#Find the standard deviation of the list
                sem_max = std_max/math.sqrt(len(max_dicts[maxi]))			#Find the standard error of the mean of the list
                avg_max_list.append(avg_max)			#Add the average of the list to the list of averages
                std_max_list.append(std_max)			#Add the standard deviation of the list to the list of standard deviations
                sem_max_list.append(sem_max)			#Add the standard error of the mean of the list to the list of standard error of means.
                
        for mini in min_dicts:
            if len(min_dicts[mini]) > 0:
                minilist = list(map(float, min_dicts[mini]))
                avg_min = statistics.mean(minilist)
                std_min = statistics.stdev(minilist)
                sem_min = std_min/math.sqrt(len(min_dicts[mini]))
                avg_min_list.append(avg_min)
                std_min_list.append(std_min)
                sem_min_list.append(sem_min)
        for meani in mean_dicts:
            if len(mean_dicts[meani]) > 0:
                meanilist = list(map(float, mean_dicts[meani]))
                avg_mean = statistics.mean(meanilist)
                std_mean = statistics.stdev(meanilist)
                sem_mean = std_mean/math.sqrt(len(mean_dicts[meani]))
                avg_mean_list.append(avg_mean)
                std_mean_list.append(std_mean)
                sem_mean_list.append(sem_mean)
        for normmaxi in norm_max_dicts:
            if len(norm_max_dicts[normmaxi]) > 0:
                normmaxilist = list(map(float, norm_max_dicts[normmaxi]))
                norm_avg_max = statistics.mean(normmaxilist)
                norm_std_max = statistics.stdev(normmaxilist)
                norm_sem_max = norm_std_max/math.sqrt(len(norm_max_dicts[normmaxi]))
                norm_avg_max_list.append(norm_avg_max)
                norm_std_max_list.append(norm_std_max)
                norm_sem_max_list.append(norm_sem_max)
        for norm_mini in norm_min_dicts:
            if len(norm_min_dicts[norm_mini]) > 0:
                norm_minilist = list(map(float, norm_min_dicts[norm_mini]))
                norm_avg_min = statistics.mean(norm_minilist)
                norm_std_min = statistics.stdev(norm_minilist)
                norm_sem_min = norm_std_min/math.sqrt(len(norm_min_dicts[norm_mini]))
                norm_avg_min_list.append(norm_avg_min)
                norm_std_min_list.append(norm_std_min)
                norm_sem_min_list.append(norm_sem_min)
        for norm_meani in norm_mean_dicts:
            if len(norm_mean_dicts[norm_meani]) > 0:
                norm_meanilist = list(map(float, norm_mean_dicts[norm_meani]))
                norm_avg_mean = statistics.mean(norm_meanilist)
                norm_std_mean = statistics.stdev(norm_meanilist)
                norm_sem_mean = norm_std_mean/math.sqrt(len(norm_mean_dicts[norm_meani]))
                norm_avg_mean_list.append(norm_avg_mean)
                norm_std_mean_list.append(norm_std_mean)
                norm_sem_mean_list.append(norm_sem_mean)
    
    	#Add all of these values to a list to add as a row in the output file
        for numb3 in range(0,100):			#Iterate over all 100 exposures
            appendtolist = []			#Initialize list of data to append
            appendtolist.append(namesaver1)			#Add the antifade
            appendtolist.append(namesaver2)			#Add the transcripts
            appendtolist.append(numb3+1)			#Add the exposure number
            appendtolist.append(avg_max_list[numb3])			#Add the average max to the list
            appendtolist.append(std_max_list[numb3])			#Add the standard deviation of the maximum to the list
            appendtolist.append(sem_max_list[numb3])			#Add the standard error of the mean of the maximum to the list
            appendtolist.append(avg_min_list[numb3])			#Add the average minimum to the list
            appendtolist.append(std_min_list[numb3])			#Add the standard deviation of the minimum to the list
            appendtolist.append(sem_min_list[numb3])			#Add the standard error of the mean of the minimum to the list
            appendtolist.append(avg_mean_list[numb3])			#Add the average mean to the list
            appendtolist.append(std_mean_list[numb3])			#Add the standard deviation of the mean to the list
            appendtolist.append(sem_mean_list[numb3])			#Add the standard error of the mean of the mean to the list
            appendtolist.append(norm_avg_max_list[numb3])			#Add the average normalized max to the list
            appendtolist.append(norm_std_max_list[numb3])			#Add the standard deviation of the normalized maximum to the list
            appendtolist.append(norm_sem_max_list[numb3])			#Add the standard error of the mean of the normalized maximum to the list
            appendtolist.append(norm_avg_min_list[numb3])			#Add the average normalized min to the list
            appendtolist.append(norm_std_min_list[numb3])			#Add the standard deviation of the normalized minimum to the list
            appendtolist.append(norm_sem_min_list[numb3])			#Add the standard error of the mean of the normalized minimum to the list
            appendtolist.append(norm_avg_mean_list[numb3])			#Add the average normalized mean to the list
            appendtolist.append(norm_std_mean_list[numb3])			#Add the standard deviation of the normalized mean to the list
            appendtolist.append(norm_sem_mean_list[numb3])			#Add the standard error of the mean of the normalized mean to the list
            append_list_as_row("OUTPUT_FILE_GOES_HERE", appendtolist)			#Add the list as a row to the final data file

        
            
