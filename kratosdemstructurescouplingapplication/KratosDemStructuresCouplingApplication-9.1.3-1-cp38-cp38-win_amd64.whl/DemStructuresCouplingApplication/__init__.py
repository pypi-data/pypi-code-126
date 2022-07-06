# Application dependent names and paths
from KratosMultiphysics import _ImportApplication
import KratosMultiphysics.StructuralMechanicsApplication
import KratosMultiphysics.DEMApplication
from KratosDemStructuresCouplingApplication import *
application = KratosDemStructuresCouplingApplication()
application_name = "KratosDemStructuresCouplingApplication"

_ImportApplication(application, application_name)