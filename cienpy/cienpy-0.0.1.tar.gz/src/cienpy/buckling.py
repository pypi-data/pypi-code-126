###########################################################################################
# Module with the functions that computes different parameters for buckling.
# Carmine Schipani, 2022
###########################################################################################


import math
import numpy as np
from cienpy import javascriptcodes as js


def compute_N_buckling_y(E, Iy, L, n_bracey):
    """
    Function that computes the critical buckling axial force in the y direction.

    @param E (float): Young modulus in MPa.
    @param Iy (float): Inertia with respect to the y axis in mm^4.
    @param L (float): Length of the beam in m.
    @param n_bracey (int): Number of braces in the y direction (equally spaced).

    @returns float: N critical buckling in the y direction in kN.
    """
    return ((n_bracey+1)*math.pi)**2*E*Iy/L**2/1e9


def compute_N_buckling_z(E, Iz, L, n_bracez):
    """
    Function that computes the critical buckling axial force in the z direction.

    @param E (float): Young modulus in MPa.
    @param Iz (float): Inertia with respect to the z axis in mm^4.
    @param L (float): Length of the beam in m.
    @param n_bracez (int): Number of braces in the z direction (equally spaced).

    @returns float: N critical buckling in the z direction in kN.
    """
    return ((n_bracez+1)*math.pi)**2*E*Iz/L**2/1e9


def implement_compute_N_buckling_yJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_N_buckling_y() in a Javascript code.
    The implemented function can compute the critical buckling axial force in the y direction.

    @returns str: Javascript code to implement the function compute_N_buckling_y().
    
    JS function:

    @paramJS E (float): Young modulus in MPa.
    @paramJS Iy (float): Inertia with respect to the y axis in mm^4.
    @paramJS L (float): Length of the beam in m.
    @paramJS n_bracey (int): Number of braces in the y direction (equally spaced).

    @returnsJS float: N critical buckling in the y direction in kN.
    """
    code = f"""
    function compute_N_buckling_y(E, Iy, L, n_bracey) {{
        return ((n_bracey+1)*Math.PI)**2*E*Iy/L**2/1e9
    }}
    """
    return code


def implement_compute_N_buckling_zJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_N_buckling_z() in a Javascript code.
    The implemented function can compute the critical buckling axial force in the z direction.

    @returns str: Javascript code to implement the function compute_N_buckling_z().
    
    JS function:

    @paramJS E (float): Young modulus in MPa.
    @paramJS Iz (float): Inertia with respect to the z axis in mm^4.
    @paramJS L (float): Length of the beam in m.
    @paramJS n_bracez (int): Number of braces in the z direction (equally spaced).

    @returnsJS float: N critical buckling in the z direction in kN.
    """
    code = f"""
    function compute_N_buckling_z(E, Iz, L, n_bracez) {{
        return ((n_bracez+1)*Math.PI)**2*E*Iz/L**2/1e9
    }}
    """
    return code 


def compute_mode_shape_N_buckling(x, L, n_brace, C=1):
    """
    Function that computes the buckling mode shape.

    @param x (float or np.array): Horizontal position along the beam in m.
    @param L (float): Length of the beam in m.
    @param n_brace (int): Number of braces (equally spaced).
    @param C (int, optional): Constant of integration. Defaults to 1.

    @returns float or np.array: Mode shape.
    """
    f_ms = lambda x : C*math.sin((n_brace+1)*math.pi*x/L)
    if len(x) == 1:
        return f_ms(x)
    else:
        res = np.zeros(len(x))
        for i, x_i in enumerate(x):
            res[i] = f_ms(x_i)
        return res


def implement_compute_mode_shape_N_bucklingJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_mode_shape_N_buckling() in a Javascript code.
    The implemented function can compute the buckling mode shape.

    @returns str: Javascript code to implement the function compute_mode_shape_N_buckling().
    
    JS function:

    @paramJS x (float): Horizontal position along the beam in m.
    @paramJS L (float): Length of the beam in m.
    @paramJS n_brace (int): Number of braces (equally spaced).
    @paramJS C (int, optional): Constant of integration. Defaults to 1.

    @returnsJS float: Mode shape.
    """
    code = f"""
    function compute_mode_shape_N_buckling(x, L, n_brace, C=1) {{
        return C*Math.sin((n_brace+1)*Math.PI*x/L)
    }}
    """
    return code


def div_text_buckling(P, Rx, N, Ncrity, Ncritz, str_insta):
    """
    Function that creates the text with buckling information for a Div Widget.

    @param P (float): Externa axial force in kN.
    @param Rx (float): Horizontal reaction force in kN.
    @param N (float): Axial force N in kN.
    @param Ncrity (float): Critical buckling axial force in the y direction in kN.
    @param Ncritz (float): Critical buckling axial force in the z direction in kN.
    @param str_insta (str): Dynamic text ("yes" or "no") for the question "Is there buckling instability?".

    @returns str: The text.
    """
    return f"""
    <p style='font-size:14px'><b>Forces and Instability:</b></p>
    P = {P} kN<br>
    Rx = {Rx} kN<br>
    N = {N} kN<br>
    V = 0 kN<br>
    M = 0 kNm<br>
    N<sub>crit,y</sub> = {Ncrity} kN<br>
    N<sub>crit,z</sub> = {Ncritz} kN<br>
    Instability: {str_insta}
    """


def implement_update_div_bucklingJS():
    """
    Function that creates the Javascript code for the implementation of the function update_div_buckling() in a Javascript code.
    The implemented function can update the text of the buckling Div.

    @returns str: Javascript code to implement the function update_div_buckling().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS div (bokeh.models.widgets.markups.Div): Div widget.
    """
    div_text = js.multiline_code_as_stringJS(div_text_buckling(
                    js.var_in_strJS('P'),
                    js.var_in_strJS('Rx'),
                    js.var_in_strJS('N'),
                    js.var_in_strJS('Ncrity'),
                    js.var_in_strJS('Ncritz'),
                    js.var_in_strJS('str_insta')))
        
    return f"""
    function update_div_buckling(data, div) {{
        const P = data['P'][0]
        const Rx = data['Rx'][0]
        const N = data['N'][0]
        const Ncrity = Math.round(data['Ncrity'][0]*10)/10
        const Ncritz = Math.round(data['Ncritz'][0]*10)/10
        if ((-N<Ncrity) && (-N<Ncritz)) {{
            var str_insta = "No"
        }} else {{
            var str_insta = "Yes"
        }}
        div.text = {div_text}
    }}
    """


def implement_update_point_braceJS():
    """
    Function that creates the Javascript code for the implementation of the function update_point_brace() in a Javascript code.
    The implemented function can dynamically plot a variable number of red dots in the graph to show the position of the braces.

    @returns str: Javascript code to implement the function update_point_brace().
    
    JS function:

    @paramJS point_brace (bokeh.models.renderers.GlyphRenderer): Glyph for the red dots.
    @paramJS n_brace (int): Number of braces (equally spaced).
    """
    code = f"""
    function update_point_brace(point_brace, n_brace) {{
        switch(n_brace) {{
            case 0:
                var x_ = []
                var y_ = []
                break
            case 1:
                var x_ = [L/2]
                var y_ = [0]
                break
            case 2:
                var x_ = [L/3, 2*L/3]
                var y_ = [0, 0]
                break
            default:
                console.error("Number of braces "+n_brace+" exceeds the implemented limit (2)")
        }}
        const src_point = point_brace.data_source
        src_point.data.x = x_
        src_point.data.y = y_
        src_point.change.emit()
    }}
    """
    return code


def implement_update_mode_shape_N_bucklingJS(discr, C=1):
    """
    Function that creates the Javascript code for the implementation of the function update_mode_shape_N_buckling() in a Javascript code.
    The implemented function can dynamically change the buckling mode shape with instability or without it.

    @param discr (int): Discretisation factor.
    @param C (int, optional): Constant of integration. Defaults to 1.

    @returns str: Javascript code to implement the function update_mode_shape_N_buckling().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_ms_y (bokeh.models.renderers.GlyphRenderer): Glyph for the bucklind mode shape in y direction.
    @paramJS glyph_ms_z (bokeh.models.renderers.GlyphRenderer): Glyph for the bucklind mode shape in z direction.
    @paramJS n_brace (int): Number of braces (equally spaced).
    @paramJS discr (int, optional): Discretisation factor. Default to discr (args).
    @paramJS C (int, optional): Constant of integration. Defaults to C (args).
    """
    code = f"""
    function update_mode_shape_N_buckling(data, glyph_ms_y, glyph_ms_z, discr={discr}, C={C}) {{
        const L = data['L'][0]
        const n_bracey = data['n_bracey'][0]
        const n_bracez = data['n_bracez'][0]
        const N = -data['N'][0]
        const Ncrity = data['Ncrity'][0]
        const Ncritz = data['Ncritz'][0]
        const x_discr = linspace(0, L, discr)
        let mode_shape_y = new Array(discr)
        let mode_shape_z = new Array(discr)
        
        // compute the arrays
        if (N >= Ncrity) {{
            for (var i = 0; i < discr; i++) {{
                mode_shape_y[i] = compute_mode_shape_N_buckling(x_discr[i], L, n_bracey, C)
            }}
        }} else {{
            mode_shape_y = new Array(discr).fill(0)
        }}
        if (N >= Ncritz) {{
            for (var i = 0; i < discr; i++) {{
                mode_shape_z[i] = compute_mode_shape_N_buckling(x_discr[i], L, n_bracez, C)
            }}
        }} else {{
            mode_shape_z = new Array(discr).fill(0)
        }}
        debugger
        // update the mode shape
        const src_ms_y = glyph_ms_y.data_source
        src_ms_y.data.x = x_discr
        src_ms_y.data.y = mode_shape_y
        src_ms_y.change.emit()
        const src_ms_z = glyph_ms_z.data_source
        src_ms_z.data.x = x_discr
        src_ms_z.data.y = mode_shape_z
        src_ms_z.change.emit()
    }}
    """
    return code