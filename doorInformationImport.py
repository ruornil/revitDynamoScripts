"""MIT License

Copyright (c) 2019 M. Cenk Tunaboylu

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
from Autodesk.Revit.DB import *

# import document and transaction managers
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

ids = IN[0][0]
output = []

# assigning the current document
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication

TransactionManager.Instance.EnsureInTransaction(doc)

# user need to check the correct parameter name to change...
for i in range(len(ids)-1):
	door = doc.GetElement(ids[i+1])
	for p in door.Parameters:
		if p.Definition.Name == 'Hardware':
			hw = door.get_Parameter(p.GUID)
			hw.Set(IN[0][3][i+1])

# end transaction
TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = 0