###########################################################################################
# Module with the models and functions developed for Jupyter Notebook using Bokeh.
# For Javascript counterparts, see javascriptcodes module.
# Carmine Schipani, 2022
###########################################################################################


import math
import numpy as np 
from bokeh.plotting import ColumnDataSource
from bokeh.models import Arrow
from bokeh.models.tickers import AdaptiveTicker
from bokeh.models.arrow_heads import VeeHead


def implement_check_stateJS():
    """
    Function that creates the Javascript code for the implementation of the function check_state() in a Javascript code.
    The implemented function can check the state (IDLE, R_SEC, L_SEC).

    @returns str: Javascript code to implement the function check_state().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    """
    code = """
    function check_state(data) {
        const FBD = data['FBD'][0]
        const pos = data['x'][0]
        const L = data['L'][0]
        if (FBD == 0 && pos != L) {
            data['state'][0] = 'R_SEC'
        } else if (FBD == 1 && pos != 0) {
            data['state'][0] = 'L_SEC'
        } else {
            data['state'][0] = 'IDLE'
        }
    }
    """
    return code


def define_curvedArrow(fig, a, b, c, size_head=15, arrow_color='red', arrow_alpha=1, arrow_width=3, discr=10, center = [0, 0]):
    """
    Function that defines a curved arrow. The arrow follows a symmetric quadratic curve.
    It uses the line renderer for the main body of the arrow and a scatter point with the triangle symbol as the head.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas of the arrow.
    @param a (float): First curve parameter: defines the horizontal position of the head and tail.
    @param b (float): Second curve parameter: defines the horizontal position of the center of the arrow.
    @param c (float): Third curve parameter: defines half of the height if the arrow.
    @param size_head (int, optional): Size of the head in pixel. Defaults to 15.
    @param arrow_color (str, optional): Color of the arrow (body and head). Defaults to 'red'.
    @param arrow_alpha (int, optional): Transparency of the arrow (body and head). Defaults to 1.
    @param arrow_width (int, optional): Width of the body of the arrow. Defaults to 3.
    @param discr (int, optional): Number of points for the discretisation of the curved body. Defaults to 10.
    @param center (array of dimension 2, optional): Horizontal and vertical position of the center. Defaults to [0, 0].

    @returns tuple: Tuple with the renderer of the curved line, the scatter point with triangular shape and the source with the coordinates.
    """
    # compute the coordinates of the parabola
    x_loc = np.linspace(-c, c, discr)
    if c == 0:
        y_loc = x_loc
        theta = 0
    else:
        a1 = b
        a2 = 0
        a3 = (a-b)/c**2
        y_loc = a1 + a2*x_loc + a3*x_loc**2
        theta = -math.atan(2/c*(a-b))
    if c < 0:
        theta = theta+math.pi
    
    # create source
    x = y_loc+center[0]
    y = x_loc+center[1]
    source = ColumnDataSource(data=dict(
        x=x,
        y=y
    ))
    
    # parabola
    arrow = fig.line('x', 'y', source=source, line_color=arrow_color, alpha=arrow_alpha, line_width=arrow_width)
    
    # head (patch), alternative
    # sh = 2; # size head not in pixel
    # x_head = [sh/2*math.sin(theta)+c, -sh/2*math.sin(theta)+c, sh/2*math.sqrt(3)*math.cos(theta)+c]
    # y_head = [sh/2*math.cos(theta)+a, -sh/2*math.cos(theta)+a, -sh/2*math.sqrt(3)*math.sin(theta)+a]
    # head = f.patch(x_head, y_head, line_color='green', fill_color='green')
    
    # head (triangle point)
    head = fig.scatter(x=[x[-1]],y=[y[-1]], marker='triangle',
                     size=size_head, angle=theta,
                     line_color=arrow_color, fill_color=arrow_color, alpha=arrow_alpha)
    
    return (arrow, head, source)


def define_doubleArrow(fig, x_start, x_end, y_start, y_end, size_head=15, arrow_color='red', arrow_alpha=1, arrow_width=3, pixel2unit=10):
    """
    Function that defines a curved arrow. The arrow follows a symmetric quadratic curve.
    It uses the line renderer for the main body of the arrow and a scatter point with the triangle symbol as the head.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas of the arrow.
    @param x_start (float): X position of the tail.
    @param x_end (float): X position of the head.
    @param y_start (float): Y position of the tail.
    @param y_end (float): Y position of the head.
    @param size_head (int, optional): Size of the head in pixel. Defaults to 15.
    @param arrow_color (str, optional): Color of the arrow (body and head). Defaults to 'red'.
    @param arrow_alpha (int, optional): Transparency of the arrow (body and head). Defaults to 1.
    @param arrow_width (int, optional): Width of the body of the arrow. Defaults to 3.
    @param pixel2unit (int, optional): Value to change the pixel head size in the units of the plot. Defaults to 10.

    @returns tuple: Tuple with the renderer of the straight line, the scatter points with triangular shape and the source with the coordinates.
    """
    # compute the angle of the line
    delta_x = x_end-x_start
    if delta_x==0:
        if y_end-y_start > 0:
            theta = math.pi/2
        else:
            theta = math.pi*3/2
    elif delta_x > 0:
        theta = math.atan((y_end-y_start)/delta_x)
    else:
        theta = math.atan((y_end-y_start)/delta_x)+math.pi
    
    
    # head adjust
    head_x = size_head/pixel2unit*math.cos(theta)
    head_y = size_head/pixel2unit*math.sin(theta)
    
    # create source
    source = ColumnDataSource(data=dict(
        x=[x_start, x_end],
        y=[y_start, y_end]
    ))
    
    # line
    arrow = fig.line('x', 'y', source=source, line_color=arrow_color, alpha=arrow_alpha, line_width=arrow_width)
    
    # heads (triangle point)
    heads = fig.scatter(x=[x_end-head_x/2, x_end-head_x/2*3],y=[y_end-head_y/2, y_end-head_y/2*3], marker='triangle',
                     size=size_head, angle=theta+math.pi/6,
                     line_color=arrow_color, fill_color=arrow_color, alpha=arrow_alpha)
    
    return (arrow, heads, source)


def force_vector(fig, intensity, x_start, x_end, y_start, y_end, color, AHF=7):
    """
    Function that initialises the glyph of a straight arrow.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas of the arrow.
    @param intensity (float): Parameter that controls the size of the arrow's head and the width of the arrow's body.
    @param x_start (float): X position of the tail.
    @param x_end (float): X position of the head.
    @param y_start (float): Y position of the tail.
    @param y_end (float): Y position of the head.
    @param color (str): String with the color name choosen.
    @param AHF (int, optional): Arrow Head Factor. Defaults to 7.

    @returns bokeh.models.renderers.GlyphRendere: Arrow glyph.
    """
    force = Arrow(end=VeeHead(size=arrow_growth(abs(intensity))*AHF, line_color=color, fill_color=color), line_color=color,
              x_start=x_start, y_start=y_start, x_end=x_end, y_end=y_end, line_width=arrow_growth(intensity))
    fig.add_layout(force)
    return force


def define_pinned(fig, x, y, b_supp, ratio, supp_opt: dict):
    """
    Function that defines the patch with a triangular shape to represent a pinned support.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas of the support.
    @param x (float): Horizontal position of the apex.
    @param y (float): Vertical position of the apex.
    @param b_supp (float): Length of the equilateral triangle.
    @param ratio (float): Ratio of the figure (interval_y/height*100). Use 1.0 if match_aspect is used (correctly).
    @param supp_opt (dict): Options for the rendering of the glyph.

    @returns bokeh.models.renderers.GlyphRenderer: The renderer for the support.
    """
    return fig.patch([x, b_supp/2+x, -b_supp/2+x],
                     [y, y-b_supp/2*math.sqrt(3)*ratio, y-b_supp/2*math.sqrt(3)*ratio],
                    **supp_opt)
    

def define_roller(fig, x, y, b_supp, ratio, supp_opt: dict):
    """
    Function that defines the glyph with a circluar shape to represent a roller support.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas of the support.
    @param x (float): Horizontal position of the center.
    @param y (float): Vertical position of the center.
    @param b_supp (float): Diameter of the circle.
    @param ratio (float): Ratio of the figure (interval_y/height*100). Use 1.0 if match_aspect is used (correctly).
    @param supp_opt (dict): Options for the rendering of the glyph.

    @returns bokeh.models.renderers.GlyphRenderer: The renderer for the support.
    """
    return fig.circle([x], [y-b_supp/2*ratio], radius=b_supp/2, **supp_opt)


# helpful functions
def arrow_growth(var):
    """
    Function that modulates a value.
    The derivative of the function is high with small values and exponentially smaller with high values.

    @param var (float): Variable.

    @returns float: Modulated variable.
    """
    return math.log(abs(var)+1)


def NVM_diagram(fig, x, y, L, source_beam, x_src='x', y_src='y'):
    """
    Function that prepares a figure for a N/V/M diagram.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the glyphs.
    @param x (list): Array from 0 to L.
    @param y (list): Array of N/V/M.
    @param L (float): Length in m.
    @param source_beam (bokeh.models.sources.ColumnDataSource): Source that stores the coordinates of the beam (diagram).
    @param x_src (str, optional): Key of the dictionary for the x array of source_beam. Defaults to 'x'.
    @param y_src (str, optional): Key of the dictionary for the y array of source_beam. Defaults to 'y'.

    @returns bokeh.models.renderers.GlyphRenderer: Glyph of the N/V/M diagram. 
    """
    diag = fig.line([0, *x, L], [0, *y, 0], line_width=2)
    fig.line(x=x_src, y=y_src, source=source_beam, line_width=3, color='black')
    return diag


def stress_diagram(fig, stress, h, src_section, opt_neutral_axis=False, neutral_axis_y=0, scale_x=0.5):
    """
    Function that prepares a figure for a stress diagram.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the glyphs.
    @param stress (list): Array of stresses from the bottom to the top of the section.
    @param h (float): Height of the section in mm.
    @param src_section (bokeh.models.sources.ColumnDataSource): Source that stores the coordinates of the vertical cross-section (diagram).
    @param opt_neutral_axis (bool, optional): Option to add a neutral axis glyph (return changes). Defaults to False.
    @param neutral_axis_y (float, optional): Vertical position of the neutral axis. Defaults to 0.
    @param scale_x (float, optional): Half the length of the neutral axis. Defaults to 0.5.

    @returns *depends*: Return the stress diagram glyph or return the stress diagram and the neutral axis glyphs if opt_neutral_axis is true.
    """
    tmp_y = np.linspace(0, h, len(stress))
    diag = fig.line([0, *stress, 0], [0, *tmp_y, h], color='blue')
    fig.line(x='x', y='y', source=src_section, color='black', line_width=1.5)
    if opt_neutral_axis:
        neutral_axis = fig.line([-scale_x*1.2, scale_x*1.2], [neutral_axis_y, neutral_axis_y], color='black',
                                line_dash='4 4')
        return (diag, neutral_axis)
    else:
        fig.line([-scale_x*1.2, scale_x*1.2], [0, 0], alpha=0)
        return diag


def strain_diagram(fig, strain, h, src_section, scale_x=1e-4):
    """
    Function that prepares a figure for a strain diagram.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the glyphs.
    @param strain (list): Array of strain from the bottom to the top of the section.
    @param h (float): Height of the section.
    @param src_section (bokeh.models.sources.ColumnDataSource): Source that stores the coordinates of the vertical cross-section (diagram).
    @param scale_x (float, optional): Scale of the strain for the interval ticker. Defaults to 1e-4.

    @returns bokeh.models.renderers.GlyphRendere: Strain diagram glyph.
    """
    diag = fig.line(strain, np.linspace(0, h, len(strain)), color='red')
    fig.line(x='x', y='y', source=src_section, color='black', line_width=1.5)
    fig.line([-scale_x*1.2, scale_x*1.2], [0, 0], alpha=0)
    fig.xaxis.ticker = AdaptiveTicker(desired_num_ticks=3, num_minor_ticks=2)
    return diag


def section_diagram(fig):
    """
    Function that prepares a figure for a cross-section diagram with the N/V/M arrows.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the glyphs.
    """
    extreme = 10
    fig.line([-extreme/6, 0, 0, -extreme/6], [-extreme, -extreme, extreme, extreme], color='black', line_width=1.5)


def set_arrows_stress_state(fig, sigma_x0, sigma_y0, tau_0, width_element, scale_tau=1.0, center_x=0.0, theta_element=0.0):
    """
    Function that initialises the 8 arrows for a stress state element.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the glyphs.
    @param sigma_x0 (float): Intensity of the sigma x arrows.
    @param sigma_y0 (float): Intensity of the sigma y arrows.
    @param tau_0 (float): Intensity of the tau arrows.
    @param width_element (float): Width of the stress state element
    @param scale_tau (float, optional): Optional parameter to increase the size of the tau arrows (for illustrative purposes). Defaults to 1.0.
    @param center_x (float, optional): X position of the center of the stress state element. Defaults to 0.0.
    @param theta_element (float, optional): Angle of the element counterclockwise. Defaults to 0.0.

    @returns array: Array with the 8 arrow glyphs. 
    """
    offset_arrows = width_element/3
    col_arrow = 'blue'
    offset_sigma = width_element/2+offset_arrows
    offset_tau = width_element/2+offset_arrows/2
    sigma_y0 = sigma_y0
    tau_0 = tau_0*scale_tau
    if sigma_x0<0:
        sigma_x0 = -sigma_x0
        arrow_sigma_x1 = force_vector(fig, sigma_x0,
                                    (offset_sigma+center_x+sigma_x0)*math.cos(theta_element),
                                    (offset_sigma+center_x)*math.cos(theta_element),
                                    (offset_sigma+center_x+sigma_x0)*math.sin(theta_element),
                                    (offset_sigma+center_x)*math.sin(theta_element),
                                    col_arrow)
        arrow_sigma_x2 = force_vector(fig, sigma_x0,
                                    (-(offset_sigma+sigma_x0)+center_x)*math.cos(theta_element),
                                    (-offset_sigma+center_x)*math.cos(theta_element),
                                    (-(offset_sigma+sigma_x0)+center_x)*math.sin(theta_element),
                                    (-offset_sigma+center_x)*math.sin(theta_element),
                                    col_arrow)
    else:
        arrow_sigma_x1 = force_vector(fig, sigma_x0,
                                    (offset_sigma+center_x)*math.cos(theta_element),
                                    (offset_sigma+center_x+sigma_x0)*math.cos(theta_element),
                                    (offset_sigma+center_x)*math.sin(theta_element),
                                    (offset_sigma+center_x+sigma_x0)*math.sin(theta_element),
                                    col_arrow)
        arrow_sigma_x2 = force_vector(fig, sigma_x0,
                                    (-offset_sigma+center_x)*math.cos(theta_element),
                                    (-(offset_sigma+sigma_x0)+center_x)*math.cos(theta_element),
                                    (-offset_sigma+center_x)*math.sin(theta_element),
                                    (-(offset_sigma+sigma_x0)+center_x)*math.sin(theta_element),
                                    col_arrow)
        
    if sigma_y0<0:
        sigma_y0 = -sigma_y0
        arrow_sigma_y1 = force_vector(fig, sigma_y0,
                                    (center_x)*math.cos(theta_element)-(offset_sigma+sigma_y0)*math.sin(theta_element),
                                    (center_x)*math.cos(theta_element)-(offset_sigma)*math.sin(theta_element),
                                    (center_x)*math.sin(theta_element)+(offset_sigma+sigma_y0)*math.cos(theta_element),
                                    (center_x)*math.sin(theta_element)+(offset_sigma)*math.cos(theta_element),
                                    col_arrow)
        arrow_sigma_y2 = force_vector(fig, sigma_y0,
                                    (center_x)*math.cos(theta_element)+(offset_sigma+sigma_y0)*math.sin(theta_element),
                                    (center_x)*math.cos(theta_element)+(offset_sigma)*math.sin(theta_element),
                                    (center_x)*math.sin(theta_element)-(offset_sigma+sigma_y0)*math.cos(theta_element),
                                    (center_x)*math.sin(theta_element)-(offset_sigma)*math.cos(theta_element),
                                    col_arrow)
    else:
        arrow_sigma_y1 = force_vector(fig, sigma_y0,
                                    (center_x)*math.cos(theta_element)-(offset_sigma)*math.sin(theta_element),
                                    (center_x)*math.cos(theta_element)-(offset_sigma+sigma_y0)*math.sin(theta_element),
                                    (center_x)*math.sin(theta_element)+(offset_sigma)*math.cos(theta_element),
                                    (center_x)*math.sin(theta_element)+(offset_sigma+sigma_y0)*math.cos(theta_element),
                                    col_arrow)
        arrow_sigma_y2 = force_vector(fig, sigma_y0,
                                    (center_x)*math.cos(theta_element)+(offset_sigma)*math.sin(theta_element),
                                    (center_x)*math.cos(theta_element)+(offset_sigma+sigma_y0)*math.sin(theta_element),
                                    (center_x)*math.sin(theta_element)-(offset_sigma)*math.cos(theta_element),
                                    (center_x)*math.sin(theta_element)-(offset_sigma+sigma_y0)*math.cos(theta_element),
                                    col_arrow)
    arrow_tau_x1 = force_vector(fig, tau_0,
                                  (center_x+offset_tau)*math.cos(theta_element)+(tau_0/2)*math.sin(theta_element),
                                  (center_x+offset_tau)*math.cos(theta_element)-(tau_0/2)*math.sin(theta_element),
                                  (center_x+offset_tau)*math.sin(theta_element)-(tau_0/2)*math.cos(theta_element),
                                  (center_x+offset_tau)*math.sin(theta_element)+(tau_0/2)*math.cos(theta_element),
                                  col_arrow)
    arrow_tau_x2 = force_vector(fig, tau_0,
                                  (center_x-offset_tau)*math.cos(theta_element)-(tau_0/2)*math.sin(theta_element),
                                  (center_x-offset_tau)*math.cos(theta_element)+(tau_0/2)*math.sin(theta_element),
                                  (center_x-offset_tau)*math.sin(theta_element)+(tau_0/2)*math.cos(theta_element),
                                  (center_x-offset_tau)*math.sin(theta_element)-(tau_0/2)*math.cos(theta_element),
                                  col_arrow)
    arrow_tau_y1 = force_vector(fig, tau_0,
                                  (center_x-tau_0/2)*math.cos(theta_element)-(offset_tau)*math.sin(theta_element),
                                  (center_x+tau_0/2)*math.cos(theta_element)-(offset_tau)*math.sin(theta_element),
                                  (center_x-tau_0/2)*math.sin(theta_element)+(offset_tau)*math.cos(theta_element),
                                  (center_x+tau_0/2)*math.sin(theta_element)+(offset_tau)*math.cos(theta_element),
                                  col_arrow)
    arrow_tau_y2 = force_vector(fig, tau_0,
                                  (center_x+tau_0/2)*math.cos(theta_element)+(offset_tau)*math.sin(theta_element),
                                  (center_x-tau_0/2)*math.cos(theta_element)+(offset_tau)*math.sin(theta_element),
                                  (center_x+tau_0/2)*math.sin(theta_element)-(offset_tau)*math.cos(theta_element),
                                  (center_x-tau_0/2)*math.sin(theta_element)-(offset_tau)*math.cos(theta_element),
                                  col_arrow)
    return [arrow_sigma_x1, arrow_sigma_x2,
            arrow_sigma_y1, arrow_sigma_y2,
            arrow_tau_x1, arrow_tau_x2,
            arrow_tau_y1, arrow_tau_y2]