###########################################################################################
# Module with the functions to compute or visualise parameters of a rectangular section in Jupyter Notebook using Bokeh.
# Carmine Schipani, 2022
###########################################################################################


import numpy as np 
from cienpy import javascriptcodes as js


def compute_area(b, h):
    """
    Function that computes the area of a rectangular section.

    @param b (float): Width in mm.
    @param h (float): Height in mm.

    @returns float: Area in mm^2.
    """
    return b*h


def implement_compute_areaJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_area() in a Javascript code.
    The implemented function can compute the area of a rectangular section.

    @returns str: Javascript code to implement the function compute_area().
    
    JS function:

    @paramJS b (float): Width in mm.
    @paramJS h (float): Height in mm.
    
    @returnsJS float: Area in mm^2.
    """
    code = """
    function compute_area(b, h) {
        return b*h
    }
    """
    return code


def compute_inertia_y(b, h):
    """
    Function that computes the inertia with respect to the y axis (strong axis) of a rectangular section.

    @param b (float): Width in mm.
    @param h (float): Height in mm.

    @returns float: Inertia with respect to the y axis in mm^4.
    """
    return b*h**3/12


def implement_compute_inertia_yJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_inertia_y() in a Javascript code.
    The implemented function can compute the inertia with respect to the y axis (strong axis) of a rectangular section.

    @returns str: Javascript code to implement the function compute_inertia_y().
    
    JS function:

    @paramJS b (float): Width in mm.
    @paramJS h (float): Height in mm.
    
    @returnsJS float: Inertia with respect to the y axis in mm^4.
    """
    code = """
    function compute_inertia_y(b, h) {
        return b*h**3/12
    }
    """
    return code


def compute_inertia_z(b, h):
    """
    Function that computes the inertia with respect to the z axis (weak axis) of a rectangular section.
    
    @param b (float): Width in mm.
    @param h (float): Height in mm.

    @returns float: Inertia with respect to the z axis in mm^4.
    """
    return b**3*h/12


def implement_compute_inertia_zJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_inertia_z() in a Javascript code.
    The implemented function can compute the inertia with respect to the z axis (weak axis) of a rectangular section.

    @returns str: Javascript code to implement the function compute_inertia_z().
    
    JS function:

    @paramJS b (float): Width in mm.
    @paramJS h (float): Height in mm.
    
    @returnsJS float: Inertia with respect to the z axis in mm^4.
    """
    code = """
    function compute_inertia_z(b, h) {
        return h*b**3/12
    }
    """
    return code


def draw_section(fig, b: float, h: float, center = [0, 0]):
    """
    Function that draws the cross-section of the beam in a figure for a rectangular section.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the plot.
    @param b (float): Width of the section.
    @param h (float): Height of the section.
    @param center (list, optional): Coordinates of the center of the section. Defaults to [0, 0].

    @returns bokeh.models.renderers.GlyphRenderer: Renderer of the section.
    """
    return fig.rect([center[0]], [center[1]], width=b, height=h,
                    fill_color='white', color='black', line_width=3,
                    hatch_pattern='/', hatch_color='black')


def div_text_geo(h, b, L, A, Iy, Iz):
    """
    Function that creates the text with geometrical and mechanical parameters for a Div widget for a rectangular section.

    @param b (float): Width in mm.
    @param h (float): Height in mm.
    @param L (float): Length of the beam in m.
    @param A (float): Area in mm^2.
    @param Iy (float): Inertia with respect to the y axis in mm^4.
    @param Iz (float): Inertia with respect to the z axis in mm^4.

    @returns str: The text.
    """
    return f"""
    <p style='font-size:14px'><b>Geometrical and mechanical parameters:</b></p>
    h = {h} mm<br>
    b = {b} mm<br>
    L = {L} m<br>
    A = {A} mm<sup>2</sup><br>
    Iy = {Iy} mm<sup>4</sup><br>
    Iz = {Iz} mm<sup>4</sup>"""


def implement_update_div_geoJS():
    """
    Function that creates the Javascript code for the implementation of the function update_div_geo() in a Javascript code.
    The implemented function can update the text of the geo Div for a rectangular section.

    @returns str: Javascript code to implement the function update_div_geo().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS div (bokeh.models.widgets.markups.Div): Div widget.
    """
    div_text = js.multiline_code_as_stringJS(div_text_geo(
                    js.var_in_strJS('h'),
                    js.var_in_strJS('b'),
                    js.var_in_strJS('L'),
                    js.var_in_strJS('A.toExponential(2)'),
                    js.var_in_strJS('Iy.toExponential(2)'),
                    js.var_in_strJS('Iz.toExponential(2)')
                ))
    code = f"""
    function update_div_geo(data, div) {{
        // compute the parameters and dimensions
        const L = Math.round(data['L'][0]*10)/10
        const b = Math.round(data['b'][0])
        const h = Math.round(data['h'][0])
        const A = data['A'][0]
        const Iy = data['Iy'][0]
        const Iz = data['Iz'][0]
        // change the div text
        div.text = {div_text}
    }}
    """
    return code


def implement_update_sectionJS():
    """
    Function that creates the Javascript code for the implementation of the function update_section() in a Javascript code.
    The implemented function can update the section draw in the figure for a rectangular section.

    @returns str: Javascript code to implement the function update_section().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_section (bokeh.models.renderers.GlyphRendere): Patch glyph.
    """
    code = f"""
    function update_section(data, glyph_section) {{
        // change the plot of the section
        glyph_section.glyph.width = data['b'][0]
        glyph_section.glyph.height = data['h'][0]
    }}
    """
    return code


def compute_centroid_y(h):
    """
    Function that computes the centroid vertical position of a rectangular section.

    @param h (float): Height of the section in mm.

    @returns float: Position from the bottom in mm.
    """
    return h/2


def implement_compute_centroid_yJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_centroid_y() in a Javascript code.
    The implemented function can compute the centroid vertical position of a rectangular section.

    @returns str: Javascript code to implement the function compute_centroid_y().
    
    JS function:

    @paramJS h (float): Height in mm.
    
    @returnsJS float: Position from the bottom in mm.
    """
    code = """
    function compute_centroid_y(h) {
        return h/2
    }
    """
    return code


def compute_first_moment_of_area(y, b, h, yG):
    """
    Function that computes the first moment of area at the section x and vertical position y of a rectangular section.

    @param y (float or np.array): Vertical position from the bottom in mm.
    @param b (float): Width of the section in mm.
    @param h (float): Height of the section in mm.
    @param yG (float): Centroid vertical position in mm.

    @returns float: First moment of area in mm^3.
    """
    return b/2*(h**2/4-(y-yG)**2)


def implement_compute_first_moment_of_areaJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_first_moment_of_area() in a Javascript code.
    The implemented function can compute the first moment of area at the section x and vertical position y of a rectangular section.

    @returns str: Javascript code to implement the function compute_first_moment_of_area().
    
    JS function:

    @paramJS y (float or np.array): Vertical position from the bottom in mm.
    @paramJS b (float): Width of the section in mm.
    @paramJS h (float): Height of the section in mm.
    @paramJS yG (float): Centroid vertical position in mm.

    @returnsJS float: First moment of area in mm^3.
    """
    code = """
    function compute_first_moment_of_area(y, b, h, yG) {
        return b/2*(h**2/4-(y-yG)**2)
    }
    """
    return code


def implement_compute_first_moment_of_area_implicitJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_first_moment_of_area_implicit() in a Javascript code.
    The implemented function can compute the first moment of area using compute_first_moment_of_area but without explicit arguments.

    @returns str: Javascript code to implement the function compute_first_moment_of_area_implicit().
    
    JS function:

    @paramJS y_ (float or np.array): Vertical position from the bottom in mm.
    @paramJS data (dict): Data from the source that stores every essential info.

    @returnsJS float: First moment of area in mm^3.
    """
    code = f"""
    function compute_first_moment_of_area_implicit(y_, data) {{
        return compute_first_moment_of_area(y_, data['b'][0], data['h'][0], data['yG'][0])
    }}
    """
    return code
