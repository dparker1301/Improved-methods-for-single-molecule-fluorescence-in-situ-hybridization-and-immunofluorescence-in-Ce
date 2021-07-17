//dir1 = getDirectory("Choose Destination Directory");
//list = getFileList(dir1);

setTool (2); // Set tool to polygon
myImageID = getImageID();  //Set image ID
beep (); // Alert user
waitForUser("outline your cell");
selectImage(myImageID);  // make sure you have the right image
if (selectionType() != 2)   // Make sure the selection is a polygon
exit ("No outline");
roiManager("add")	//Adds selection to ROI manager
roiManager("multi measure")   //Measure all under the ROI for all exposures


