###########################################################################################
# Module with functions that compute plastic stresses and strains inside a rectangular section.
# Carmine Schipani, 2022
###########################################################################################


import math
import numpy as np
import cienpy.stress_strain_elastic as stst


# private
def __check_limit(M_norm, N_norm):
    """
    Private function that checks the if the section is completely yielded.

    @param M_norm (float): Positive bending moment normalised.
    @param N_norm (float): Positive axial force normalised.

    @returns bool: Check response.
    """
    tmp = 2/3*M_norm+N_norm**2
    if tmp>1:
        return False
    else:
        return True


def __compute_M_norm(M, My):
    """
    Private function that computes the bending momnet normalised (absolute value).

    @param M (float): Bending moment in kNm.
    @param My (float): Elastic resisting bending moment in kNm.

    @returns float: Positive normalised bending moment.
    """
    return abs(M/My)

    
def __compute_N_norm(N, Ny):
    """
    Private function that computes the normalised axial force (absolute value).

    @param N (float): Axial force in kN.
    @param Ny (float): Elastic resisting axial force in kN.

    @returns float: Positive normalised axial force.
    """
    return abs(N/Ny)


def __compute_strain_pl(y, yNA, chi):
    """
    Private function that computes the plastic strain.

    @param y (float or array): Vertical position of the section analysed in mm.
    @param yNA (float): Vertical position of the plastic neutral axis strarting from the bottom in mm.
    @param chi (float): Curvature in 1/mm.

    @returns float or array: Plastic strain in [-].
    """
    return -(y-yNA)*chi


def __compute_stress_pl(epsilon, fy, E):
    """
    Private function that computes the plastic stress.

    @param epsilon (float or array): Plastic strain in [-].
    @param fy (float): Yield strength in MPa.
    @param E (float): Young modulus in MPa.

    @returns float or array: Plastic stress in MPa.
    """
    if len(epsilon) == 1:
        sigma = epsilon*E
        if sigma > fy:
            sigma = fy
        if sigma < -fy:
            sigma = -fy
    else:
        sigma = np.zeros(len(epsilon))
        for i, eps in enumerate(epsilon):
            tmp = -eps*E
            if tmp > fy:
                sigma[i] = fy
            elif tmp < -fy:
                sigma[i] = -fy
            else:
                sigma[i] = tmp
    return sigma
    

# double yield
def __compute_h_2Y(N_norm):
    """
    Private function that computes the normalised parameter h for the double yields case.

    @param N_norm (float): Positive normalised axial force.

    @returns float: h.
    """
    return (1-N_norm)/2

    
def __compute_k_2Y(M_norm, N_norm):
    """
    Private function that computes the normalised parameter k for the double yields case.

    @param M_norm (float): Positive normalised bending moment.
    @param N_norm (float): Positive normalised axial force.

    @returns float: k.
    """
    return math.sqrt((1+2*N_norm+N_norm**2) / (3-3*N_norm**2-2*M_norm))

    
def __compute_k_prime_2Y(k, h):
    """
    Private function that computes the normalised parameter k' for the double yields case.

    @param k (float): k parameter.
    @param h (float): h parameter.

    @returns float: k'.
    """
    return k*h / (1-h)


def __compute_chi_2Y(k, fy, E, H, yNA):
    """
    Private function that computes the curvature chi for the double yields case.

    @param k (float): k parameter.
    @param fy (float): Yield strength in MPa.
    @param E (float): Young modulus in MPa.
    @param H (float): Depth of the section in mm.
    @param yNA (float): Vertical position of the plastic neutral axis strarting from the bottom in mm.

    @returns float: Curvature in 1/mm.
    """
    return k*fy/(E*(H-yNA))

    
# single yield (yNA inside)
def __check_validity_yNA(h, N_norm):
    """
    Private function that checks the validity of the given plastic neutral axis for the single yield, yNA inside case.

    @param h (float): h parameter.
    @param N_norm (float): Positive normalised axial force.

    @returns bool: Check response.
    """
    tmp = (1-N_norm)**2 -2*h*(1-N_norm)
    if tmp<0:
        return False
    else:
        return True

    
def __compute_k_1Y_in(h, N_norm):
    """
    Private function that computes the normalised parameter k for the sigle yield, yNA inside case.

    @param h (flaot): h parameter.
    @param N_norm (float): Positive normalised axial force.

    @returns float: k.
    """
    return (h-1)*((h-1+N_norm) + math.sqrt((1-N_norm)**2 -2*h*(1-N_norm)) ) / h**2


def __compute_err_1Y_in(h, k, M_norm, N_norm):
    """
    Private function that computes the normalised error for the sigle yield, yNA inside case.

    @param h (float): h parameter.
    @param k (float): k parameter.
    @param M_norm (float): Positive normalised bending moment.
    @param N_norm (float): Positive normalised axial force.

    @returns flaot: Error in [-].
    """
    return abs(M_norm + 3*N_norm*(1-2*h) - 2*k*h**3/(1-h) - (3*k**2-1)/k**2*(1-h)**2)

    
def __compute_chi_1Y_in(k, fy, E, H, yNA):
    """
    Private function that computes the curvature for the sigle yield, yNA inside case.

    @param k (flaot): k parameter.
    @param fy (float): Yield strength in MPa.
    @param E (float): Young modulus in MPa.
    @param H (float): Depth of the section in mm.
    @param yNA (float): Vertical position of the plastic neutral axis strarting from the bottom in mm.

    @returns float: Curvature in 1/mm.
    """
    # unit: 1/mm
    return k*fy/(E*(H-yNA))


# signle yield (yNA outside)
def __compute_h_1Y_out(N_norm, k):
    """
    Private function that computes the normalised parameter h for the sigle yield, yNA outside case.

    @param N_norm (float): Positive normalised axial force.
    @param k (float): k parameter.

    @returns float: h.
    """
    return (k*(2-N_norm)-1-k*math.sqrt((k-N_norm)**2-(k-1)**2)) / (k-1)**2

    
def __compute_chi_1Y_out(k, fy, E, H, yNA):
    """
    Private function that computes the curvature for the sigle yield, yNA outside case.

    @param k (float): k parameter.
    @param fy (float): Yield strength in MPa.
    @param E (float): Young modulus in MPa.
    @param H (float): Depth of the section in mm.
    @param yNA (float): Vertical position of the plastic neutral axis strarting from the bottom in mm.

    @returns flaot: Curvature in 1/mm.
    """
    return k*fy/(E*(H+yNA))


def __compute_err_1Y_out(k, h, M_norm, N_norm):
    """
    Private function that computes the curvature for the sigle yield, yNA outside case.

    @param k (float): k parameter.
    @param h (float): h parameter.
    @param M_norm (float): Positive normalised bending moment.
    @param N_norm (float): Positiv normalised axial force.

    @returns float: Error in [-].
    """
    return abs( M_norm + 3*(N_norm-1) + (1+h-k*h)**3 / (k**2*(1+h)) )


def implement_support_function_plasticJS():
    """
    Function that creates the Javascript code for the implementation of various supporting function in a Javascript code.
    The implemented function are used for the computation of the plastic state in a rectangular section.
    For more information on each function, check the Python counterpart inside this module.

    @returns str: Javascript code to implement the various supporting functions.
    """
    code = f"""
    function __check_limit(M_norm, N_norm) {{
        const tmp = 2/3*M_norm+N_norm**2
        if (tmp>1) {{
            return false
        }}else{{
            return true
        }}
    }}
        
    function __compute_M_norm(M, My){{
        return Math.abs(M/My)
    }}
        
    function __compute_N_norm(N, Ny){{
        return Math.abs(N/Ny)
    }}

    function __compute_strain_pl(y, yNA, chi){{
        return y.map(x => -(x-yNA)*chi) 
    }}

    function __compute_stress_pl(epsilon, fy, E){{
        const sigma = new Array(epsilon.length).fill(0)
        for (var i = 0; i < epsilon.length; i++) {{
            var tmp = epsilon[i]*E
            if (tmp > fy){{
                sigma[i] = fy
            }}else if (tmp < -fy){{
                sigma[i] = -fy
            }}else{{
                sigma[i] = tmp
            }}
        }}
        return sigma
    }}
    
    // double yield
    function __compute_h_2Y(N_norm){{
        return (1-N_norm)/2
    }}
    
    function __compute_k_2Y(M_norm, N_norm){{
        return Math.sqrt((1+2*N_norm+N_norm**2) / (3-3*N_norm**2-2*M_norm))
    }}
    
    function __compute_k_prime_2Y(k, h){{
        return k*h / (1-h)
    }}

    function __compute_chi_2Y(k, fy, E, H, yNA){{
        return k*fy/(E*(H-yNA))
    }}

    
    // one yield (yNA inside)
    function __check_validity_yNA(h, N_norm){{
        const tmp = (1-N_norm)**2 -2*h*(1-N_norm)
        if (tmp<0) {{
            return false
        }}else{{
            return true
        }}
    }}
        
    function __compute_k_1Y_in(h, N_norm){{
        return (h-1)*( (h-1+N_norm) + Math.sqrt((1-N_norm)**2 -2*h*(1-N_norm)) ) / h**2
    }}

    function __compute_err_1Y_in(h, k, M_norm, N_norm){{
        return Math.abs(M_norm + 3*N_norm*(1-2*h) - 2*k*h**3/(1-h) - (3*k**2-1)/k**2*(1-h)**2)
    }}
        
    function __compute_chi_1Y_in(k, fy, E, H, yNA){{
        // unit: 1/mm
        return k*fy/(E*(H-yNA))
    }}

    // one yield (yNA outside)
    function __compute_h_1Y_out(N_norm, k){{
        return (k*(2-N_norm)-1-k*Math.sqrt((k-N_norm)**2-(k-1)**2)) / (k-1)**2
    }}
        
    function __compute_chi_1Y_out(k, fy, E, H, yNA){{
        return k*fy/(E*(H+yNA))
    }}

    function __compute_err_1Y_out(k, h, M_norm, N_norm){{
        return Math.abs( M_norm + 3*(N_norm-1) + (1+h-k*h)**3 / (k**2*(1+h)) )
    }}
    """
    return code


# public
def compute_Ny(fy, A):
    """
    Function that computes the elastic resisting axial force.

    @param fy (float): Yield strength in MPa.
    @param A (flaot): Area of the section in mm^2.

    @returns flaot: Elastic resisting axial force in kN.
    """
    return fy*A/1e3
    
    
def implement_compute_NyJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_Ny() in a Javascript code.
    The implemented function can compute the elastic resisting axial force.

    @returns str: Javascript code to implement the function compute_Ny().
    
    JS function:

    @paramJS fy (float): Yield strength in MPa.
    @paramJS A (flaot): Area of the section in mm.

    @returnsJS float: Elastic resisting axial force in kN.
    """
    code = f"""
    function compute_Ny(fy, A) {{
        return fy*A/1e3
    }}
    """
    return code


def compute_My(fy, Iy, yG, H):
    """
    Function that computes the elastic resisting bending moment.

    @param fy (float): Yield strength in MPa.
    @param Iy (float): Inertia with respect to the strong axis in mm^4.
    @param yNA (float): Vertical position of the plastic neutral axis strarting from the bottom in mm.
    @param H (float): Depth of the section in mm.

    @returns float: Elastic resisting bending moment in kNm.
    """
    extreme_fiber = yG if yG >= H-yG else H-yG
    return Iy/extreme_fiber*fy/1e6


def implement_compute_MyJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_My() in a Javascript code.
    The implemented function can compute the elastic resisting bending moment.

    @returns str: Javascript code to implement the function compute_My().
    
    JS function:

    @paramJS fy (float): Yield strength in MPa.
    @paramJS Iy (float): Inertia with respect to the strong axis in mm^4.
    @paramJS yNA (float): Vertical position of the plastic neutral axis strarting from the bottom in mm.
    @paramJS H (float): Depth of the section in mm.

    @returnsJS float: Elastic resisting bending moment in kNm.
    """
    code = f"""
    function compute_My(fy, Iy, yG, H) {{
        if (yG >= H-yG) {{
            var extreme_fiber = yG
        }} else {{
            var extreme_fiber = H-yG
        }}
        return Iy/extreme_fiber*fy/1e6
    }}
    """
    return code


def compute_total_stress_strain(discr, H, fy, E, N, M, A, Iy, yG):
    """
    Function that computes the total stress, strain and the plastic neutral axis position at the section x (plastic included).

    @param discr (float): Discretisation factor of the depth of the section.
    @param H (float): Depth of the section in mm.
    @param fy (float): Yield strength in MPa.
    @param E (float): Young modulus in MPa.
    @param N (flaot): Axial force N in the section in kN.
    @param M (float): Bending moment M in the section in kNm.
    @param A (float): Area of the section in mm^2.
    @param Iy (float): Inertia with respect to the strong axis in mm^4.
    @param yG (float): Vertical position of the centroid strarting from the bottom in mm.

    @returns tuple: Array with plastic stress in MPa, array with plastic strain in %, array with discretised depth in mm and vertical position of the plastic neutral axis in mm.
    """
    # initialization
    scale_discr_o = 20
    y_discr = np.linspace(0, H, discr)
    Ny = compute_Ny(fy, A)
    My = compute_My(fy, Iy, yG, H)
    M_norm = __compute_M_norm(M, My)
    N_norm = __compute_N_norm(N, Ny)
    err_inside = np.ones(discr)*math.inf
    err_outside = np.ones(discr*scale_discr_o)*math.inf

    # compute state (elastic)
    sigma_N_el = stst.compute_sigma_axial(y_discr, N, A)
    sigma_M_el = stst.compute_sigma_bending(y_discr, M, Iy, yG)
    stress_el = sigma_M_el + sigma_N_el
    strain_el = stst.compute_epsilon_axial(y_discr, sigma_N_el, E)/100 + stst.compute_epsilon_bending(y_discr, sigma_M_el, E)/100
    if abs(stress_el[0]) > fy or abs(stress_el[-1]) > fy:
        if __check_limit(M_norm, N_norm):
            # double yield check
            h = __compute_h_2Y(N_norm)
            yNA = h*H
            k = __compute_k_2Y(M_norm, N_norm)
            chi = __compute_chi_2Y(k, fy, E, H, yNA)
            k_prime = __compute_k_prime_2Y(k, h)
            if k>=1 and k_prime>=1:
                # DOUBLE YIELD CASE
                if (N>=0 and M<0) or (N<0 and M>0):
                    yNA_F = H-yNA
                else:
                    yNA_F = yNA
                if (N>=0 and M>0) or (N<0 and M>0):
                    chi_F = -chi
                else:
                    chi_F = chi
                
                strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                stress_pl = __compute_stress_pl(strain_pl, fy, E)
                return (stress_pl, strain_pl*100, y_discr, yNA_F)
            else:
                # one yield, yNA inside check
                for i, yNA in enumerate(y_discr[1:-1]):
                    i = i+1
                    h = yNA/H
                    if __check_validity_yNA(h, N_norm):
                        k = __compute_k_1Y_in(h, N_norm)
                        err_inside[i] = __compute_err_1Y_in(h, k, M_norm, N_norm)
                index_min_i = np.argmin(err_inside)
                yNA = y_discr[index_min_i]
                k = __compute_k_1Y_in(yNA/H, N_norm)
                chi = __compute_chi_1Y_in(k, fy, E, H, yNA)
                if (N>=0 and M<0) or (N<0 and M>0):
                    yNA_F = H-yNA
                else:
                    yNA_F = yNA
                if (N>=0 and M>0) or (N<0 and M>0):
                    chi_F = -chi
                else:
                    chi_F = chi
                
                if index_min_i != 1:
                    # ONE YIELD (YNA INSIDE) CASE
                    strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                    stress_pl = __compute_stress_pl(strain_pl, fy, E)
                    return (stress_pl, strain_pl*100, y_discr, yNA_F)
                
                else:
                    # check if it's inside (edge case) or outside
                    yNA_F_in = yNA_F
                    chi_F_in = chi_F
                    err_in = err_inside[index_min_i]
                    
                    k_discr = np.linspace(1, 20, discr*scale_discr_o)
                    for i, k in enumerate(k_discr[1:]):
                        i = i+1
                        h = __compute_h_1Y_out(N_norm, k)
                        err_outside[i] = __compute_err_1Y_out(k, h, M_norm, N_norm)
                    index_min_o = np.argmin(err_outside)
                    k = k_discr[index_min_o]
                    h = __compute_h_1Y_out(N_norm, k)
                    yNA = h*H
                    chi = __compute_chi_1Y_out(k, fy, E, H, yNA)
                    err_o = err_outside[index_min_o]
                    if (N>=0 and M<0) or (N<0 and M>0):
                        yNA_F_o = H+yNA
                    else:
                        yNA_F_o = -yNA
                    if (N>=0 and M>0) or (N<0 and M>0):
                        chi_F_o = -chi
                    else:
                        chi_F_o = chi
                    
                    if err_in < err_o:
                        # ONE YIELD (YNA INSIDE) CASE
                        yNA_F = yNA_F_in
                        chi_F = chi_F_in
                        strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                        stress_pl = __compute_stress_pl(strain_pl, fy, E)
                        return (stress_pl, strain_pl*100, y_discr, yNA_F)
                    
                    else:
                        # ONE YIELD (YNA OUTSIDE) CASE
                        yNA_F = yNA_F_o
                        chi_F = chi_F_o
                        strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                        stress_pl = __compute_stress_pl(strain_pl, fy, E)
                        return (stress_pl, strain_pl*100, y_discr, yNA_F)
                        
        else:
            # PLASTIC LIMIT CASE
            yNA = __compute_h_2Y(N_norm)*H
            if (N>=0 and M<0) or (N<0 and M>0):
                yNA_F = H-yNA
            else:
                yNA_F = yNA
            if (N>=0 and M>=0) or (N<0 and M>0):
                strain_pl = np.ones(len(y_discr))*fy/E
                strain_pl[y_discr<yNA_F] = fy/E
            else:
                strain_pl = -np.ones(len(y_discr))*fy/E
                strain_pl[y_discr<yNA_F] = -fy/E
            
            stress_pl = __compute_stress_pl(strain_pl, fy, E)
            strain_pl = [min(strain_el), max(strain_el)]
            y_discr =  [yNA_F, yNA_F]
            return (stress_pl, strain_pl*100, y_discr, yNA_F)
        
    else:
        # ELASTIC CASE
        strain_pl = strain_el
        stress_pl = __compute_stress_pl(strain_pl, fy, E)
        return (stress_pl, strain_pl*100, y_discr, yG)


def implement_compute_total_stress_strainJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_total_stress_strain() in a Javascript code.
    The implemented function can compute the total stress, strain and the plastic neutral axis position at the section x (plastic included).

    @returns str: Javascript code to implement the function compute_total_stress_strain().
    
    JS function:

    @paramJS H (float): Depth of the section in mm.
    @paramJS fy (float): Yield strength in MPa.
    @paramJS E (float): Young modulus in MPa.
    @paramJS N (flaot): Axial force N in the section in kN.
    @paramJS M (float): Bending moment M in the section in kNm.
    @paramJS A (float): Area of the section in mm^2.
    @paramJS Iy (float): Inertia with respect to the strong axis in mm^4.
    @paramJS yG (float): Vertical position of the centroid strarting from the bottom in mm.
    @paramJS discr (float): Discretisation factor of the depth of the section.

    @returnsJS array: Array with plastic stress in MPa, array with plastic strain in %, array with discretised depth in mm and vertical position of the plastic neutral axis in mm.
    """
    code = f"""
    function compute_total_stress_strain(H, fy, E, N, M, A, Iy, yG, discr) {{
        // initialization
        const scale_discr_o = 20
        var y_discr = linspace(0, H, discr)
        const Ny = compute_Ny(fy, A)
        const My = compute_My(fy, Iy, yG, H)
        const M_norm = __compute_M_norm(M, My)
        const N_norm = __compute_N_norm(N, Ny)
        const err_inside = new Array(discr).fill(1e30)
        const err_outside = new Array(discr*scale_discr_o).fill(1e30)

        // compute state (elastic)
        let strain_el = new Array(discr)
        let stress_el = new Array(discr)
        for (var i = 0; i < discr; i++) {{
            var sigma_N_el = compute_sigma_axial(N, A)
            var sigma_M_el = compute_sigma_bending(y_discr[i], M, Iy, yG)
            stress_el[i] = sigma_M_el + sigma_N_el
            strain_el[i] = compute_epsilon_axial(sigma_N_el, E)/100 + compute_epsilon_bending(sigma_M_el, E)/100
        }}
        if (Math.abs(stress_el[0]) > fy || Math.abs(stress_el.slice(-1)[0]) > fy) {{
            if (__check_limit(M_norm, N_norm)) {{
                // double yield check
                var h = __compute_h_2Y(N_norm)
                var yNA = h*H
                var k = __compute_k_2Y(M_norm, N_norm)
                var chi = __compute_chi_2Y(k, fy, E, H, yNA)
                var k_prime = __compute_k_prime_2Y(k, h)
                if (k>=1 && k_prime>=1) {{
                    // DOUBLE YIELD CASE
                    console.log("2 yield case")
                    if ((N>=0 && M<0) || (N<0 && M>0)) {{
                        var yNA_F = H-yNA
                    }} else {{
                        var yNA_F = yNA
                    }}
                    if ((N>=0 && M>0) || (N<0 && M>0)) {{
                        var chi_F = -chi
                    }} else {{
                        var chi_F = chi
                    }}
                    
                    var strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                    var stress_pl = __compute_stress_pl(strain_pl, fy, E)
                    return [stress_pl, strain_pl.map(x => x*100), y_discr, yNA_F]
                }} else {{
                    // one yield, yNA inside check
                    for (var i = 1; i < discr-1; i++) {{
                        var yNA = y_discr[i]
                        var h = yNA/H
                        if (__check_validity_yNA(h, N_norm)) {{
                            var k = __compute_k_1Y_in(h, N_norm)
                            err_inside[i] = __compute_err_1Y_in(h, k, M_norm, N_norm)
                        }}
                    }}
                    const index_min_i = err_inside.indexOf(Math.min(...err_inside))
                    var yNA = y_discr[index_min_i]
                    var k = __compute_k_1Y_in(yNA/H, N_norm)
                    var chi = __compute_chi_1Y_in(k, fy, E, H, yNA)
                    if ((N>=0 && M<0) || (N<0 && M>0)) {{
                        var yNA_F = H-yNA
                    }} else {{
                        var yNA_F = yNA
                    }}
                    if ((N>=0 && M>0) || (N<0 && M>0)) {{
                        var chi_F = -chi
                    }} else {{
                        var chi_F = chi
                    }}
                    
                    if (index_min_i != 1) {{
                        // ONE YIELD (YNA INSIDE) CASE
                        var strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                        var stress_pl = __compute_stress_pl(strain_pl, fy, E)
                        return [stress_pl, strain_pl.map(x => x*100), y_discr, yNA_F]
                    
                    }} else {{
                        // check if it's inside (edge case) or outside
                        const yNA_F_in = yNA_F
                        const chi_F_in = chi_F
                        const err_in = err_inside[index_min_i]
                        
                        const k_discr = linspace(1, 20, discr*scale_discr_o)
                        for (var i = 1; i < discr*scale_discr_o; i++) {{
                            var k = k_discr[i]
                            var h = __compute_h_1Y_out(N_norm, k)
                            err_outside[i] = __compute_err_1Y_out(k, h, M_norm, N_norm)
                        }}
                        const index_min_o = err_outside.indexOf(Math.min(...err_outside))
                        var k = k_discr[index_min_o]
                        var h = __compute_h_1Y_out(N_norm, k)
                        var yNA = h*H
                        var chi = __compute_chi_1Y_out(k, fy, E, H, yNA)
                        const err_o = err_outside[index_min_o]
                        if ((N>=0 && M<0) || (N<0 && M>0)) {{
                            var yNA_F_o = H+yNA
                        }} else {{
                            var yNA_F_o = -yNA
                        }}
                        if ((N>=0 && M>0) || (N<0 && M>0)) {{
                            var chi_F_o = -chi
                        }} else {{
                            var chi_F_o = chi
                        }}
                        
                        if (err_in < err_o) {{
                            // ONE YIELD (YNA INSIDE) CASE
                            console.log("1 yield, yNA in case")
                            var yNA_F = yNA_F_in
                            var chi_F = chi_F_in
                            var strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                            var stress_pl = __compute_stress_pl(strain_pl, fy, E)
                            return [stress_pl, strain_pl.map(x => x*100), y_discr, yNA_F]
                        
                        }} else {{
                            // ONE YIELD (YNA OUTSIDE) CASE
                            console.log("1 yield, yNA out case")
                            var yNA_F = yNA_F_o
                            var chi_F = chi_F_o
                            var strain_pl = __compute_strain_pl(y_discr, yNA_F, chi_F)
                            var stress_pl = __compute_stress_pl(strain_pl, fy, E)
                            return [stress_pl, strain_pl.map(x => x*100), y_discr, yNA_F]
                        
                        }}
                    }}
                }}
            }} else {{
                // PLASTIC LIMIT CASE
                console.log("limit case")
                var yNA = __compute_h_2Y(N_norm)*H
                if ((N>=0 && M<0) || (N<0 && M>0)) {{
                    var yNA_F = H-yNA
                }} else {{
                    var yNA_F = yNA
                }}
                let strain_pl = new Array(discr)
                if ((N>=0 && M>=0) || (N<0 && M>0)) {{
                    for (var i = 0; i < discr; i++) {{
                        if (y_discr[i]<yNA_F) {{
                            strain_pl[i] = -fy/E
                        }} else {{
                            strain_pl[i] = fy/E
                        }}
                    }}
                }} else {{
                    for (var i = 0; i < discr; i++) {{
                        if (y_discr[i]>yNA_F) {{
                            strain_pl[i] = -fy/E
                        }} else {{
                            strain_pl[i] = fy/E
                        }}
                    }}
                }}
                var stress_pl = __compute_stress_pl(strain_pl, fy, E)
                var strain_pl_ = [Math.min(...strain_el)*100, Math.max(...strain_el)*100]
                var y_discr =  [yNA_F, yNA_F]
                return [stress_pl, strain_pl_, y_discr, yNA_F]
            }}
        }}else {{
            // ELASTIC CASE
            console.log("elastic case")
            var strain_pl = strain_el
            var stress_pl = __compute_stress_pl(strain_pl, fy, E)
            return [stress_pl, strain_pl.map(x => x*100), y_discr, yG]
        }}
    }}
    """
    return code