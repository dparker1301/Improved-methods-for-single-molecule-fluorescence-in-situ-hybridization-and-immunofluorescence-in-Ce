// The purpose of this macro is to split antifade optimization data into a form amenable to downstream analysis.

name = getTitle()

 //Auto level so you can see where to make the box
 
 run("Enhance Contrast", "saturated=0.35");
 
 
 //Select a rectangle to crop
 
setTool (0); // Set tool to rectangle
myImageID = getImageID();  //IDK what this does, I found it somewhere
beep (); // Alert user
waitForUser("select a rectangle");
selectImage(myImageID);  // make sure you have the right image
if (selectionType() != 0)   // Make sure the selection is a rectangle
exit ("No rectangle");
run("Crop");

//split the colors

run("Split Channels");

 
//Make file structure needed for GMM/DBSCAN/Antifade analysis

parentdir = getDirectory("Choose a directory");
C1 = parentdir + "/C1/";
C2 = parentdir + "/C2/";
File.makeDirectory(C1);
File.makeDirectory(C2);

//Autolevel the rest and save in the file structure need for GMM/DBSCAN

selectWindow("C1-" + name); 
saveAs("Tiff", C1 + "C1-" + name);
close();
selectWindow("C2-" + name);
run("Enhance Contrast", "saturated=0.35");
saveAs("Tiff", C2 + "C2-" + name);
close();
selectWindow("C3-" + name);
run("Enhance Contrast", "saturated=0.35");
saveAs("Tiff", parentdir + "C3-" + name);
close();
selectWindow("C4-" + name);
run("Enhance Contrast", "saturated=0.35");
saveAs("Tiff", parentdir + "C4-" + name);
close();
selectWindow("C5-" + name);
close();
