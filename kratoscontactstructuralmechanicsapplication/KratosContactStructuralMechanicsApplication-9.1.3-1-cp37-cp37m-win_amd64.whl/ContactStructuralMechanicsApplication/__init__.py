# Application dependent names and paths
from KratosMultiphysics import _ImportApplication
import KratosMultiphysics.StructuralMechanicsApplication
from KratosContactStructuralMechanicsApplication import *
application = KratosContactStructuralMechanicsApplication()
application_name = "KratosContactStructuralMechanicsApplication"

_ImportApplication(application, application_name)
