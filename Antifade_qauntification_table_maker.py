#Import stuff and set parameters.
import csv							#Import csv so I can write to .csv files
import os							#Import os for general OS navigation


#Ask for user inputs
directory = input("Enter the file path you want to tabulate")		#Get user input for data. This script will tabulate any files contained within the user input folder.
userfilename = input("What would you like your .csv file to be named? ")					#Assign save file name


#Get the list of files to tabulate
listofiles = []			#Initialize file list to analyze later
for subdir, dirs, files in os.walk(directory):			#Iterate through files in user directory
    for filename in files:			#Loop through file list to find Results.csv files
        filepath = subdir + os.sep + filename			#Get full path name so the directory info can be split up later
        if subdir.endswith("C1"):								#Search for C1 directory (output from split_image_for_antifade_analysis.ijm)
            if filename.endswith("Results.csv"):			#Search for the results.csv file in the C1 directory
                listofiles.append(filepath)			#Add results files to list of files
        if subdir.endswith("C2"):			#Search for C2 directory
            if filename.endswith("Results.csv"):			#Search for the results.csv file in the C2 directory
                listofiles.append(filepath)			#Add results files to list of files
                
                
#Set up the csv writer to convert the data to a .csv file.                
from csv import writer			#Import csv writer.
def append_list_as_row(file_name, list_of_elem):			#Define function that takes the user file name and the tabulated output to add to a .csv file
    with open(file_name, 'a+', newline='') as write_obj:			#Open user defined file in append mode
        csv_writer = writer(write_obj)								#Set up csv_writer to writer to the new file.
        csv_writer.writerow(list_of_elem)							#Use csv_writer to add the list to a new row.
                

#Write file and add header
with open(userfilename, 'w', newline='') as file:			#Open user file name
    wr = csv.writer(file)			#Set up wr to write to the file
    header = ['Antifade', 'Transcript', 'Image', 'Area', 'Max1', 'Max2', 'Max3', 'Max4', 'Max5', 'Max6', 'Max7', 'Max8', 'Max9', 'Max10', 'Max11', 'Max12', 'Max13', 'Max14', 'Max15', 'Max16', 'Max17', 'Max18', 'Max19', 'Max20', 'Max21', 'Max22', 'Max23', 'Max24', 'Max25', 'Max26', 'Max27', 'Max28', 'Max29', 'Max30', 'Max31', 'Max32', 'Max33', 'Max34', 'Max35', 'Max36', 'Max37', 'Max38', 'Max39', 'Max40', 'Max41', 'Max42', 'Max43', 'Max44', 'Max45', 'Max46', 'Max47', 'Max48', 'Max49', 'Max50', 'Max51', 'Max52', 'Max53', 'Max54', 'Max55', 'Max56', 'Max57', 'Max58', 'Max59', 'Max60', 'Max61', 'Max62', 'Max63', 'Max64', 'Max65', 'Max66', 'Max67', 'Max68', 'Max69', 'Max70', 'Max71', 'Max72', 'Max73', 'Max74', 'Max75', 'Max76', 'Max77', 'Max78', 'Max79', 'Max80', 'Max81', 'Max82', 'Max83', 'Max84', 'Max85', 'Max86', 'Max87', 'Max88', 'Max89', 'Max90', 'Max91', 'Max92', 'Max93', 'Max94', 'Max95', 'Max96', 'Max97', 'Max98', 'Max99', 'Max100', 'Min1', 'Min2', 'Min3', 'Min4', 'Min5', 'Min6', 'Min7', 'Min8', 'Min9', 'Min10', 'Min11', 'Min12', 'Min13', 'Min14', 'Min15', 'Min16', 'Min17', 'Min18', 'Min19', 'Min20', 'Min21', 'Min22', 'Min23', 'Min24', 'Min25', 'Min26', 'Min27', 'Min28', 'Min29', 'Min30', 'Min31', 'Min32', 'Min33', 'Min34', 'Min35', 'Min36', 'Min37', 'Min38', 'Min39', 'Min40', 'Min41', 'Min42', 'Min43', 'Min44', 'Min45', 'Min46', 'Min47', 'Min48', 'Min49', 'Min50', 'Min51', 'Min52', 'Min53', 'Min54', 'Min55', 'Min56', 'Min57', 'Min58', 'Min59', 'Min60', 'Min61', 'Min62', 'Min63', 'Min64', 'Min65', 'Min66', 'Min67', 'Min68', 'Min69', 'Min70', 'Min71', 'Min72', 'Min73', 'Min74', 'Min75', 'Min76', 'Min77', 'Min78', 'Min79', 'Min80', 'Min81', 'Min82', 'Min83', 'Min84', 'Min85', 'Min86', 'Min87', 'Min88', 'Min89', 'Min90', 'Min91', 'Min92', 'Min93', 'Min94', 'Min95', 'Min96', 'Min97', 'Min98', 'Min99', 'Min100', 'Mean1', 'Mean2', 'Mean3', 'Mean4', 'Mean5', 'Mean6', 'Mean7', 'Mean8', 'Mean9', 'Mean10', 'Mean11', 'Mean12', 'Mean13', 'Mean14', 'Mean15', 'Mean16', 'Mean17', 'Mean18', 'Mean19', 'Mean20', 'Mean21', 'Mean22', 'Mean23', 'Mean24', 'Mean25', 'Mean26', 'Mean27', 'Mean28', 'Mean29', 'Mean30', 'Mean31', 'Mean32', 'Mean33', 'Mean34', 'Mean35', 'Mean36', 'Mean37', 'Mean38', 'Mean39', 'Mean40', 'Mean41', 'Mean42', 'Mean43', 'Mean44', 'Mean45', 'Mean46', 'Mean47', 'Mean48', 'Mean49', 'Mean50', 'Mean51', 'Mean52', 'Mean53', 'Mean54', 'Mean55', 'Mean56', 'Mean57', 'Mean58', 'Mean59', 'Mean60', 'Mean61', 'Mean62', 'Mean63', 'Mean64', 'Mean65', 'Mean66', 'Mean67', 'Mean68', 'Mean69', 'Mean70', 'Mean71', 'Mean72', 'Mean73', 'Mean74', 'Mean75', 'Mean76', 'Mean77', 'Mean78', 'Mean79', 'Mean80', 'Mean81', 'Mean82', 'Mean83', 'Mean84', 'Mean85', 'Mean86', 'Mean87', 'Mean88', 'Mean89', 'Mean90', 'Mean91', 'Mean92', 'Mean93', 'Mean94', 'Mean95', 'Mean96', 'Mean97', 'Mean98', 'Mean99', 'Mean100']			#generate a header for each column
    wr.writerow(header)			#Write the header
    

#Define the quantification function
def antifade_quantifier( strs ):			#Initialize the quantification function using a string as the only input.
    
    #Split the path name into individual words for use in the table
    filename = (strs)			#Set the file path up as the string
    splitlist = filename.split("/")			#Split the filename up by level.
    t = 0			#Initialize variable to make file levels into dictionary for searching
    filedict = {}			#Initialize file dictionary
    for line in splitlist:			#Parse filename list to make dictionary
        t += 1			#Raise key by 1
        filedict[t] = line			#Assign keys to dictionary values

    #Define column values  
    with open(anyfile, newline = '') as antifile:			#Open user file
        anti_reader = csv.reader(antifile, delimiter=',')			#Split the csv file by commas
        antifile_line_count = -1			#Initialize line counter at -1 (so the counter below starts at 0)
        
        Antifade = ""			#Initialize Antifade variable
        Antifade = filedict[6]			#Define Antifade based on it's location in the file path dictionary
    
        Transcript = ""			#Initialize Transcript variable
        if filedict[7] == 'nos-2_set-3':			#Check which transcripts are being probed for.
            if filedict[9] == 'C1':			#If the path name has C1 in it, that means the transcript is ->
                Transcript = "nos-2"			#nos-2
            if filedict[9] == 'C2':			#If the path name has C2 in it, that means the transcript is ->
                Transcript = "set-3"			#set-3
        if filedict[7] == 'imb-2_erm-1':			#Check which transcripts are being probed for.
            if filedict[9] == 'C1':			#If the path name has C1 in it, that means the transcript is ->
                Transcript = "imb-2"			#imb-2
            if filedict[9] == 'C2':			#If the path name has C2 in it, that means the transcript is ->
                Transcript = "erm-1"			#erm-1
            
    
        Image = ""			#Initialize the image string
        Image = filedict[8]			#Take the image name from the path dictionary
        
        Area_var = ''			#Initialize the Area_var string
        
        Max_dict = {}			#Initialize the Max_dict dictionary
        Max_var = ''			#Initialize the Max_var string
        Max_stack_max = ''			#Initialize the Max_stack_max string
        Max_list = []			#Initialize the Max_list list
        
        Mean_dict = {}			#Initialize the Mean_dict dictionary
        Mean_var = ''			#Initialize the Mean_var string
        Mean_stack_max = ''			#Initialize the Mean_stack_max string
        Mean_list = []			#Initialize the Mean_list list
        
        Min_dict = {}			#Initialize the Min_dict dictionary
        Min_var = ''			#Initialize the Min_var string
        Min_stack_max = ''		#Initialize the Min_stack_max string
        Min_list = []			#Initialize the min_list string
        
        
        for line in anti_reader:			#Iterate through the lines of the file
            antifile_line_count += 1			#Add to the line counter
            if antifile_line_count == 2:			#On the second data line ->
                    Area_var = line[1]			#Take the area of the region of interest as the Area_var
            if antifile_line_count > 0:			#Once data lines start ->
                Max_var = ("Max" + str(antifile_line_count))			#Set the max_var string to the maximum intensity and the image number, ie Max1 - Max100
                Max_stack_max = line[4]			#Get the maximum intensity from that stack
                Max_dict[Max_var] = Max_stack_max			#Add the maximum intensity from that stack to a dictionary with the corresponding stack label key from Max_var
                
                Mean_var = ("Mean" + str(antifile_line_count))			#For the Mean and Min blocks the code functions identically to the previous three lines, changing only which measurements are being logged.
                Mean_stack_max = line[2]
                Mean_dict[Mean_var] = Mean_stack_max
                
                Min_var = ("Min" + str(antifile_line_count))
                Min_stack_max = line[3]
                Min_dict[Min_var] = Min_stack_max
                
        Max_list = list(Max_dict.values())			#Convert the Max_dict to an ordered list
        Mean_list = list(Mean_dict.values())		#Convert the Mean_dict to an ordered list
        Min_list = list(Min_dict.values())			#Convert the Min_dict to an ordered list
            
        quantified = []			#Initialize the quantified list as the list to be appended to the file
        quantified.append(Antifade)			#Add the antifade as the first item of the list
        quantified.append(Transcript)			#Add the transcript as the second item of the list
        quantified.append(Image)			#Add the Image info as the third item of the list
        quantified.append(Area_var)			#Add the area of the ROI as the fourth item of the list
        quantified = quantified + Max_list			#Add the entire list of maximum values to the list
        quantified = quantified + Min_list			#Add the entire list of minimum values to the list
        quantified = quantified + Mean_list			#Add the entire list of mean values to the list
        
        append_list_as_row(userfilename, quantified)			#Add the data list to the user file as a row

        
for anyfile in listofiles:			#Iterate through all of the user files in the directory supplied
    print(anyfile)			#Print the files being tabulated
    antifade_quantifier(anyfile)			#Tabulate the files