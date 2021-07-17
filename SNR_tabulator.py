#The purpose of this script is to tabulate all of the signal to noise SNR.csv files


#Import modules
import csv			#Import csv to make and read the table
import os			#Import os to navigate the file directory
import numpy		#Import numpy for calculations
import pandas		#Import pandas, also for calculations.


# Get user inputs
directory = input("Enter the file path you want to convert")			#Ask the user for the directory to tabulate
listofiles = []			#Initialize the list of files to tabulate
for subdir, dirs, files in os.walk(directory):			#Loop over the directory
    for filename in files:			#And look at all the files
        filepath = subdir + os.sep + filename		#Get the full file path to use in adding some of the data later based on the file structure
        if filename.endswith("SNR.csv"):			#Find all of the SNR.csv files with SNR data
            listofiles.append(filepath)			#And append them to the list of files to tabulate
 

input_string = input("Enter a list of transcripts to be quantified separated by commas: ")			#Ask the user for the transcripts that are being tabulated
userList = input_string.split(', ')			#Split the transcripts into a list

input_conditions = input("Enter a list of conditions separated by commas: ")			#Ask the user for conditions, IE Stellaris or homebrew
userconditions = input_conditions.split(', ')			#Make a list of conditions

userfilename = input("What would you like your .csv file to be named? ")			#Ask the user to make the output file name



from csv import writer			#Import writer
def append_list_as_row(file_name, list_of_elem):			#Define function that takes the user file name and the tabulated output to add to a .csv file
    with open(file_name, 'a+', newline='') as write_obj:			#Open user defined file in append mode (Idk what as write_obj does)
        csv_writer = writer(write_obj)			#Set up csv_writer to writer to the new file.
        csv_writer.writerow(list_of_elem)			#Add new row to .csv using defined list     


#Open output file and write header
with open(userfilename, 'w', newline='') as file:			#Open the users output file in write mode
    wr = csv.writer(file)			#Set up wr to write to that file
    header = ['image_name', 'buffer', 'transcript', 'average_snr', 'snr_stdv', 'lower_95_confidence', 'upper_95_confidence']			#Specify the header
    wr.writerow(header)			#Write the header to the file


#Write the snr_tabulate function to collect all of the data
def snr_tabulate( strs ):			#Set up the function to work on a file path
    
    
    #Use the file path to extract some data into a dictionary
    filename = strs			#Set the filename as the file input to the function
    splitlist = filename.split("/")			#Split the file path by directory and save it as a list
    t = 0			#Set a counter to count directory depth
    filedict = {}			#Initialize a dictionary to take the file path info
    for line in splitlist:			#Iterate over the file path list
        t += 1			#And count for each directory
        filedict[t] = line			#Then save the directory name as the value to a key corresponding to its path depth.
    
    
    #Set up transcript variables
    transcript = ''			#Initialize transcript variable
    first_tran = ''			#Initialize variable to identify first transcript
    second_tran = ''			#Initialize variable to identify second transcript
    trans = ''			#Initialize the trans variable to use in splitting the two transcript names
    for tran in userList:			#Iterate through user defined transcripts
            if tran in filedict[7]:			#If the user defined transcripts are in the file path name
                trans = filedict[7].split("_")			#Split the two transcripts, ie nos-2_erm-1 becomes nos-2, erm-1
                first_tran = trans[0]			#Set first transcript to be the first listed
                second_tran = trans[1]			#Set second transcript to be the second listed
            if 'C1' in filedict[10]:			#Then check whether the downstream analysis is from channel 1
                transcript = first_tran			#If so, the transcript is the first one listed
            if 'C2' in filedict[10]:			#Then check whether the downstream analysis is from channel 2
                transcript = second_tran			#If so, the transcript is the second one listed
     
     
    #Look for the image number data           
    for name in filedict:			#Iterate through path data
        if 'image' in filedict[name].lower():			#And if the word image is in the path
            image_number = filedict[name]			#Set image number to that string
    
        
    cond = filedict[8]			#Get the buffer condition from the file dictionary
    
    
    #Extract the snr data
    col_list = ["#  snr", " signal", " background", " noise"]			#Set up the column names
    df = pandas.read_csv(filename, usecols=col_list)			#Us pandas to generate a frame from the file using the above column names
    snr_values = df["#  snr"]			#Define the snr values from the data frame
    
    
    #Do some math/statistics
    snr = numpy.mean(snr_values)			#Take the mean of the snr
    snr_dev = numpy.std(snr_values)			#Find the standard deviation of the snr
    
    
    #Confidence intervals
    import statsmodels.stats.api as sms			#Load statsmodels.stats so the confidence intervals can be found
    snr_95 = sms.DescrStatsW(snr_values).tconfint_mean()			#Find the 95% confidence intervals
    snr_lower = snr_95[0]			#Set the lower value of the 95% confidence interval
    snr_upper = snr_95[1]			#Set the upper value of the 95% confidence interval
    
    
    #Set up the list to be added to the tabulated data file as a row
    quantified = []			#Initialize the list
    quantified.append(image_number)			#Append the image number
    quantified.append(cond)			#Append the buffer condition
    quantified.append(transcript)			#Append the transcript name
    quantified.append(snr)			#Append the snr value
    quantified.append(snr_dev)			#Append the standard deviation
    quantified.append(snr_lower)			#Append the lower 95% confidence value
    quantified.append(snr_upper)			#Append the upper 95% confidence value


	#Add the list as a row to the data file    
    append_list_as_row(userfilename, quantified) 


#Iterate through the entire list of files to be tabulated    
for anyfile in listofiles:			#Iterate through the files
    print(anyfile)			#Print the file being tabulated
    snr_tabulate(anyfile)			#and run the tabulation function
        
        
        