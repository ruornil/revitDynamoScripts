"""MIT License

Copyright (c) 2019 M. Cenk Tuanboylu

"""

import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# import Revit Nodes to wrap and unwrap elements between revit and dynamo.
# with wrapped elements dynamo can track which elements is driven by dynamo and which is by revit, unwrapped elements is needed to use with Revit API
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

# Import geometry conversion methods between Revit API and Dynamo
clr.ImportExtensions(Revit.GeometryConversion)

# import Revit API
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *
# import document and transaction managers
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
# from RevitServices.Transactions import TransactionManager

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
# you have use UnwrapElement(IN[0]) for dynamo inputs to convert them from
# dynamo type to to revit type
# rooms = UnwrapElement(IN[0])
roomBoundary = []
output = []

# assigning the currnet document
doc = DocumentManager.Instance.CurrentDBDocument
# get all elements from the current document
collector = FilteredElementCollector(doc)
roomFilter = ElementCategoryFilter(BuiltInCategory.OST_Rooms)
# filter rooms from current document
rooms = collector.WherePasses(roomFilter).toElements()
roomIds = collector.WherePasses(roomFilter).toElementIds()

# ##no transactions for this document
# start transaction
# TransactionManager.Instance.EnsureInTransaction(doc)

# add codes to use with API
resultBoundaries = []
bo = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
elementids = []
for room in rooms:
	if room.Area > 0:
		# ##have to check this code with code from lunchbox
		elementids.append(room.elementid())
		# tempBoundary.append(room.GetBoundarySegments(boptions))
		a = room.GetBoundarySegments(bo)
		crvs = []
		for b in a:
			for seg in b:
				tempCrv = seg.GetCurve()
				resCrv = Revit.GeometryConversion.RevitToProtoCurve.ToProtoType(tempCrv)
				crvs.append(resCrv)
#		joinedCurve
#		crvs = PolyCurve.Join(crvs[0],crvs[1:])
		resultBoundaries.append(crvs)

# have to find the correct syntax for
# 1. Selecting elements (rooms in this case) with elementids
# 2. Getting minimum points of boundingboxes of each rooms as list
# 3. Moving the first room boundary segments from x,y,z, to
# 0,0,0 (- minimumPoint)
# 4. Assign a y value bigger than the previous boundary segments max y value
# (a new bounding box is coming!)
# or should have deal with it in number 2
# 5. After all this a new script will be used before or after 1. to separate
# each room by department.


# end transaction
# TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = resultBoundaries