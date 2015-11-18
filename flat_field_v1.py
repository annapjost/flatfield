from ij import IJ, ImagePlus
from ij import WindowManager as WM
from ij.gui import ProfilePlot as PP
from script.imglib.math import Min, Max
from ij.process import ImageStatistics as IS
from ij.measure import ResultsTable

projname = "AVG_test"

#WM.setCurrentWindow('test')

IJ.run("Z Project...", "projection=[Average Intensity]")

# plot the diagonal profile
imp = WM.getImage(projname)
IJ.run("Line Width...", "line=3")
IJ.makeLine(0, 0, imp.width, imp.height)
IJ.run("Plot Profile")

# bring back the projection, run Measure to get max and min
WM.putBehind()
IJ.run("Measure")  #this method reports the actual max and min, not averaged across 3 px...
rt = ResultsTable.getResultsTable()
max2 = rt.getValue("Max", 0)
min2 = rt.getValue("Min", 0)

#print max
#print min
#print max2
#print min2

