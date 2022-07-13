###########################################################################################
# Module with functions that compute elastic stresses and strains inside a section.
# Carmine Schipani, 2022
###########################################################################################


def compute_sigma_axial(y, N, A):
    """
    Function that computes the stress sigma axial at the section x and vertical position y.

    @param y (float or np.array): Vertical position from the bottom in mm.
    @param N (float): Axial force in kN.
    @param A (float): Area in mm^2.

    @returns float: Stress in kN/m^2.
    """
    return N*1000/A+y*0


def implement_compute_sigma_axialJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_sigma_axial() in a Javascript code.
    The implemented function can compute the stress sigma axial at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_sigma_axial().
    
    JS function:

    @paramJS N (float): Axial force in kN.
    @paramJS A (float): Area in mm^2.

    @returnsJS float: Stress in kN/m^2.
    """
    code = """
    function compute_sigma_axial(N, A) {
        return N*1000/A
    }
    """
    return code


def compute_sigma_bending(y, M, Iy, yG):
    """
    Function that computes the stress sigma bending at the section x and vertical position y.

    @param y (float or np.array): Vertical position from the bottom in mm.
    @param M (float): Bending momwnt in kNm.
    @param Iy (float): Inertia with respect to the strong axis in mm^4.
    @param yG (float): Centroid position from the bottom in mm.

    @returns float: Stress in kN/mm^2.
    """
    return M*1e6/Iy*(y-yG)


def implement_compute_sigma_bendingJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_sigma_bending() in a Javascript code.
    The implemented function can compute the stress sigma bending at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_sigma_bending().
    
    JS function:

    @paramJS y (float or np.array): Vertical position from the bottom in mm.
    @paramJS M (float): Bending momwnt in kNm.
    @paramJS Iy (float): Inertia with respect to the strong axis in mm^4.
    @paramJS yG (float): Centroid position from the bottom in mm.

    @returnsJS float: Stress in kN/mm^2.
    """
    code = """
    function compute_sigma_bending(y, M, Iy, yG) {
        return M*1e6/Iy*(y-yG)
    }
    """
    return code


def compute_tau_shear(y, V, S, Iy, b_or_t):
    """
    Function that computes the stress tau shear at the section x and vertical position y.

    @param y (float or np.array): Vertical position from the bottom in mm.
    @param V (float): Shear force in kN.
    @param S (float): First moment of area in mm^3.
    @param Iy (float): Inertia with respect to the strong axis in mm^4.
    @param b_or_t (float): Width or thickness of the section in mm.

    @returns float: Stress in kN/mm^2.
    """
    return V*1000*S/(Iy*b_or_t)+y*0


def implement_compute_tau_shearJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_tau_shear() in a Javascript code.
    The implemented function can compute the stress tau shear at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_tau_shear().
    
    JS function:

    @paramJS V (float): Shear force in kN.
    @paramJS S (float): First moment of area in mm^3.
    @paramJS Iy (float): Inertia with respect to the strong axis in mm^4.
    @paramJS b_or_t (float): Width or thickness of the section in mm.

    @returnsJS float: Stress in kN/mm^2.
    """
    code = """
    function compute_tau_shear(V, S, Iy, b_or_t) {
        return V*1000*S/(Iy*b_or_t)
    }
    """
    return code


def compute_epsilon_axial(y, sigma_bending, E):
    """
    Fuction that computes the strain epsilon axial at the section x and vertical position y.

    @param y (float or np.array): Vertical position from the bottom in mm.
    @param sigma_bending (float): Stress due to pure flexure in kN/mm^2.
    @param E (float): Young modulus in MPa.

    @returns float: Strain in %.
    """
    return sigma_bending/E*100+y*0


def implement_compute_epsilon_axialJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_epsilon_axial() in a Javascript code.
    The implemented function can compute the strain epsilon axial at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_epsilon_axial().
    
    JS function:

    @paramJS sigma_bending (float): Stress due to pure flexure in kN/mm^2.
    @paramJS E (float): Young modulus in MPa.

    @returnsJS float: Strain in %.
    """
    code = """
    function compute_epsilon_axial(sigma_axial, E) {
        return sigma_axial/E*100
    }
    """
    return code


def compute_epsilon_bending(y, sigma_axial, E):
    """
    Function that computes the strain epsilon bending at the section x and vertical position y.

    @param y (float or np.array): Vertical position from the bottom in mm.
    @param sigma_axial (float): Stress due to axial force in MPa.
    @param E (float): Young modulus in MPa.

    @returns float: Strain in %.
    """
    return sigma_axial/E*100+y*0


def implement_compute_epsilon_bendingJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_epsilon_bending() in a Javascript code.
    The implemented function can compute the strain epsilon bending at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_epsilon_bending().
    
    JS function:

    @paramJS sigma_axial (float): Stress due to axial force in MPa.
    @paramJS E (float): Young modulus in MPa.

    @returnsJS float: Strain in %.
    """
    code = """
    function compute_epsilon_bending(sigma_bending, E) {
        return sigma_bending/E*100
    }
    """
    return code


def compute_total_sigma(sigma_axial, sigma_bending):
    """
    Function that computes the total stress sigma at the section x and vertical position y.

    @param sigma_axial (float or np.array): Axial stress in MPa.
    @param sigma_bending (float or np.array): Bending stress in MPa.

    @returns float or np.array: Total stress sigma in MPa.
    """
    return sigma_bending+sigma_axial


def implement_compute_total_sigmaJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_total_sigma() in a Javascript code.
    The implemented function can compute the total stress sigma at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_total_sigma().
    
    JS function:
    
    @paramJS sigma_axial (float): Axial stress in MPa.
    @paramJS sigma_bending (float): Bending stress in MPa.

    @returnsJS float: Total stress sigma in MPa.
    """
    code = f"""
    function compute_total_sigma(sigma_axial, sigma_bending) {{
        return sigma_bending+sigma_axial
    }}
    """
    return code


def compute_total_tau(tau_shear, tau_torsion=0):
    """
    Function that computes the total stress tau at the section x and vertical position y.

    @param tau_shear (float or np.array): Shear stress in MPa.
    @param tau_torsion (float or np.array): Torsion stress in MPa.

    @returns float or np.array: Total stress tau in MPa.
    """
    return tau_shear + tau_torsion


def implement_compute_total_tauJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_total_tau() in a Javascript code.
    The implemented function can compute the total stress tau at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_total_tau().
    
    JS function:
    
    @paramJS tau_shear (float): Shear stress in MPa.
    @paramJS tau_torsion (float): Torsion stress in MPa.

    @returnsJS float: Total stress tau in MPa.
    """
    code = f"""
    function compute_total_tau(tau_shear, tau_torsion=0) {{
        return tau_shear + tau_torsion
    }}
    """
    return code


def compute_neutral_axis(N, A, Iy, M, yG):
    """
    Function that computes the vertical position of the neutral axis at the section x and vertical position y.

    @param N (float): Axial force in kN.
    @param A (float): Area in mm^2.
    @param Iy (float): Inertia with respect to the strong axis in mm^4.
    @param M (float): Bending moment in kNm.
    @param yG (float): Centroid vertical position in mm.

    @returns float: Neutral axis vertical position in mm.
    """
    if M == 0:
        return yG
    else:
        return yG - N/A*Iy/M/1000


def implement_compute_neutral_axisJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_neutral_axis() in a Javascript code.
    The implemented function can compute the vertical position of the neutral axis at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_neutral_axis().
    
    JS function:

    @paramJS N (float): Axial force in kN.
    @paramJS A (float): Area in mm^2.
    @paramJS Iy (float): Inertia with respect to the strong axis in mm^4.
    @paramJS M (float): Bending moment in kNm.
    @paramJS yG (float): Centroid vertical position in mm.

    @returnsJS float: Neutral axis vertical position in mm.
    """
    code = """
    function compute_neutral_axis(N, A, Iy, M, yG) {
        if (M == 0) {
            return yG
        }
        else {
            return yG - N/A*Iy/M/1000
        }
    }
    """
    return code


def compute_total_epsilon(epsilon_axial, epsilon_bending):
    """
    Function that computes the total strain epsilon at the section x and vertical position y.

    @param epsilon_axial (float or np.array): Axial strain in %.
    @param epsilon_bending (float or np.array): Bending strain in %.

    @returns float or np.array: Total strain epsilon in %.
    """
    return epsilon_axial+epsilon_bending


def implement_compute_total_epsilonJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_total_epsilon() in a Javascript code.
    The implemented function can compute the total strain epsilon at the section x and vertical position y.

    @returns str: Javascript code to implement the function compute_total_epsilon().
    
    JS function:
    
    @paramJS epsilon_axial (float or np.array): Axial strain in %.
    @paramJS epsilon_bending (float or np.array): Bending strain in %.

    @returnsJS float: Total strain epsilon in %.
    """
    code = f"""
    function compute_total_epsilon(epsilon_axial, epsilon_bending) {{
        return epsilon_axial+epsilon_bending
    }}
    """
    return code