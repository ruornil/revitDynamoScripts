""" Copyright(c) 2019, Mehmet Cenk Tunaboylu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. """

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
# .XLSX file inputted to IN has to have below column series.
# unique ID / room number / room name / area / level...
# .../ base finish / floor finish / wall finish / ceiling finish

dataEnteringNode = IN

ids = IN[0][0]
output = []

# assigning the current document
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication

TransactionManager.Instance.EnsureInTransaction(doc)

for i in range(len(ids)):
	room = doc.GetElement(ids[i])
	fb = room.get_Parameter(BuiltInParameter.ROOM_FINISH_BASE)
	fb.Set(IN[0][5][i])
	ff = room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR)
	ff.Set(IN[0][6][i])
	fw = room.get_Parameter(BuiltInParameter.ROOM_FINISH_WALL)
	fw.Set(IN[0][7][i])
	fc = room.get_Parameter(BuiltInParameter.ROOM_FINISH_CEILING)
	fc.Set(IN[0][8][i])
	department = room.getParameter(BuiltInParameter.ROOM_DEPARTMENT)
	department.Set(IN[0[9]])

# end transaction
TransactionManager.Instance.TransactionTaskDone()
# Assign your output to the OUT variable.
OUT = 0
