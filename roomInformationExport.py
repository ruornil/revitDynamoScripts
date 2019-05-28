#Copyright(c) 2015, Nathan Miller
# The Proving Ground, http://theprovingground.org
#Edited and modified by Mehmet Cenk Tunaboylu, to better suit his needs. Removed boundary curves extraction. Added department extraction.

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
rooms = ['TYPE']
names = ['ROOM NAME']
numbers = ['ROOM NUMBER']
areas = ['AREA']
levels = ['LEVEL']
locations = ['LOCATION']
elementids = ['ELEMENT ID']
uniqueids = ['UNIQUE ID']
roomStyles = ['ROOM STYLE']
baseFinishes = ['BASE FINISH']
floorFinishes = ['FLOOR FINISH']
wallFinishes = ['WALL FINISH']
ceilingFinishes = ['CEILING FINISH']

if toggle == True:

	collector = FilteredElementCollector(doc)
	collector.OfCategory(BuiltInCategory.OST_Rooms)
 
	famtypeitr = collector.GetElementIdIterator()
	famtypeitr.Reset()


	for item in famtypeitr:
		elmID = item
		eleminst = doc.GetElement(elmID)
    
		#print eleminst
		if eleminst.Area > 0:
			room = eleminst
			roomname = ''
			for p in room.Parameters:
				if p.Definition.Name == 'Name':		
					roomname = p.AsString()
				if p.Definition.Name == 'Level':			
					level = p.AsValueString()
					if (level is None):
						level = p.AsString()
				if p.Definition.Name == 'Base Finish':			
					baseFinish = p.AsValueString()
					if (baseFinish is None):
						baseFinish = p.AsString()
				if p.Definition.Name == 'Wall Finish':			
					wallFinish = p.AsValueString()
					if (wallFinish is None):
						wallFinish = p.AsString()
				if p.Definition.Name == 'Floor Finish':			
					floorFinish = p.AsValueString()
					if (floorFinish is None):
						floorFinish = p.AsString()
				if p.Definition.Name == 'Ceiling Finish':			
					ceilingFinish = p.AsValueString()
					if (ceilingFinish is None):
						ceilingFinish = p.AsString()
				if p.Definition.Name == 'Room Style':
					roomStyle = p.AsValueString()
					if (roomStyle is None):
						roomStyle = p.AsString()
						
					
			number = eleminst.Number
			area = eleminst.Area
			
			location = eleminst.Location.Point.ToPoint()
			elementid = eleminst.Id.ToString()
			uniqueid = eleminst.UniqueId
    	
			uniqueids.append(uniqueid)
			rooms.append(room)
			numbers.append("xxx_"+number)
			names.append(roomname)
			areas.append(area)
			levels.append(level)
			roomStyles.append(roomStyle)
			baseFinishes.append(baseFinish)
			floorFinishes.append(floorFinish)
			wallFinishes.append(wallFinish)
			ceilingFinishes.append(ceilingFinish)
			locations.append(location)
        
	output.append(uniqueids)
	output.append(rooms)
	output.append(numbers)	
	output.append(names)
	output.append(areas)
	output.append(levels)
	output.append(roomStyles)
	output.append(baseFinishes)
	output.append(floorFinishes)
	output.append(wallFinishes)
	output.append(ceilingFinishes)
	output.append(locations)
	
#Assign your output to the OUT variable
OUT = output