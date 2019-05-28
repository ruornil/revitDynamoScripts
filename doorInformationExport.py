"""MIT License

Copyright (c) 2019 M. Cenk Tunaboylu

"""

import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#The input to this node will be stored in the IN[0] variable.

doc =  DocumentManager.Instance.CurrentDBDocument
app =  DocumentManager.Instance.CurrentUIApplication.Application

toggle = IN[0]

output = []

marks = ['MARK']
types = ['TYPE']
hardwareSets = ['HARDWARE SET']
comments = ['COMMENTS']
remarks = ['REMARKS']
uniqueids = ['UNIQUEIDS']
elementids = ['ELEMENTIDS']
levels = ['LEVEL']
hardwares = ['HARDWARE SET']
hardwareTypes = ['HARDWARE TYPE']


if toggle == True:

	collector = FilteredElementCollector(doc)
	#check below statement in Revit API if correct move on!
	collector.OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType()
 
	famtypeitr = collector.GetElementIdIterator()
	famtypeitr.Reset()


	for item in famtypeitr:
		elmID = item
		eleminst = doc.GetElement(elmID)
		

		door = eleminst
		for p in door.Parameters:
			if p.Definition.Name == 'Mark':
				mark = p.AsValueString()
				if (mark is None):
					mark = p.AsString()
			if p.Definition.Name == 'Level':
				level = p.AsValueString()
				if (level is None):
					level = p.AsString()
			if p.Definition.Name == 'Hardware':
				hardware = p.AsValueString()
				if (hardware is None):
					hardware = p.AsString()	
			if p.Definition.Name == 'Hardware Type':
				hardwareType = p.AsValueString()
				if (hardwareType is None):
					hardwareType = p.AsString()			
			if p.Definition.Name == 'Comments':
				comment = p.AsValueString()
				if (comment is None):
					comment = p.AsString()
			if p.Definition.Name == 'Remark':
				remark = p.AsValueString()
				if (remark is None):
					remark = p.AsString()


		elementid = eleminst.Id.ToString()
		uniqueid = eleminst.UniqueId
	
		uniqueids.append(uniqueid)
		marks.append("xxx_"+str(mark))
		levels.append(level)
		hardwares.append(hardware)
		hardwareTypes.append(hardwareType)
		comments.append(comment)
		remarks.append(remark)

        
	output.append(uniqueids)
	output.append(marks)
	output.append(levels)
	output.append(hardwares)
	output.append(hardwareTypes)
	output.append(comments)
	output.append(remarks)
		
#Assign your output to the OUT variable
OUT = output
