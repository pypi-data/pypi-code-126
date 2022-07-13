###########################################################################################
# Module with the tools for the visualization of a simple supported beam in Jupyter Notebook using Bokeh.
# Carmine Schipani, 2022
###########################################################################################


import numpy as np 
from bokeh.plotting import figure
from bokeh.models.tickers import SingleIntervalTicker
from cienpy import models
from cienpy import javascriptcodes as js


# notebook demo 1
def define_fig_beam(x_range: tuple, y_range: tuple, options: dict,
                    y_visible = False, f_h = 200, f_b = 700):
    """
    Function that defines the figure for the beam.

    @param x_range (tuple): x range.
    @param y_range (tuple): y range.
    @param options (dict): Customisable options.
    @param y_visible (bool, optional): Option to show or hide the y axis. Defaults to False.
    @param f_h (int, optional): Height of the figure. Defaults to 200.
    @param f_b (int, optional): Width of the figure. Defaults to 700.

    @returns bokeh.plotting.figure.Figure: Figure.
    """
    fig = figure(**options,
        x_axis_label="Position [m]",
        plot_height=f_h,
        plot_width=f_b,
        x_range=x_range,
        y_range=y_range,
        title="Simple supported beam"
    )
    fig.xgrid.grid_line_alpha = 0
    fig.ygrid.grid_line_alpha = 0
    fig.yaxis.visible = y_visible
    fig.min_border_left = 0
    
    return fig


def define_fig_section(max_b: float, max_h: float, options: dict, fig_h: int):
    """
    Function that defines the figur for the section.

    @param max_b (float): Maximal width b.
    @param max_h (float): Maximal height h.
    @param options (dict): Customisable options.
    @param f_h (int): Height of the figure.

    @returns bokeh.plotting.figure.Figure: Figure.
    """
    fig = figure(**options,
        x_axis_label="Width b [mm]",
        y_axis_label="Height h [mm]",
        plot_height=fig_h,
        plot_width=int(fig_h/max_h*max_b),
        match_aspect=True,
        title="Cross-section of the beam"
    )
    fig.rect([0], [0], width=max_b, height=max_h, alpha=0, fill_alpha=0)
    fig.axis.ticker = SingleIntervalTicker(interval=50, num_minor_ticks=5)
    
    return fig


def draw_beam(fig, src, L: float, x = 'x', y = 'y', b_supp=0.3, ratio = 1.0):
    """
    Function that draws the simple beam in a figure.

    @param fig (bokeh.plotting.figure.Figure): Figure that will be the canvas for the plot.
    @param src (bokeh.models.sources.ColumnDataSource): Source of the coordinates.
    @param L (float): Length of the beam in m.
    @param x (str): Key for the x values. Defaults to 'x'.
    @param y (str): Key for the y values. Defaults to 'y'.
    @param b_supp (float, optional): Size of the supports in x. Defaults to 0.3.
    @param ratio (float, optional): Ratio of the figure (interval_y/height*100). Defaults to 1.0 (axis equal).
    
    @return tuple: Tuple with the renderers of the beam and supports.
    """
    beam = fig.line(x, y, source=src, line_width=6, color='black')
    supp_opt = dict(
        fill_color='white',
        line_color='black'
    )
    support_l = models.define_pinned(fig, 0, 0, b_supp, ratio, supp_opt)
    support_r = models.define_roller(fig, L, 0, b_supp, ratio, supp_opt)
    
    return (beam, support_l, support_r)


# notebook demo 2
def define_figure_scheme(L, scale, max_q, offset_q, options: dict,
                         f_h = 200, f_b = 700):
    """
    Function that defines the figures for the scheme.

    @param L (float): Length of the beam in m.
    @param scale (float): Scale m to kN.
    @param max_q (float): Maximal uniform load in kN.
    @param offset_q (float): Offset of the uniform load in kN.
    @param options (dict): Options for the figure.
    @param f_h (int, optional): Height of the figurew. Defaults to 200.
    @param f_b (int, optional): Width of the figure. Defaults to 700.

    @returns bokeh.plotting.figure.Figure: Figure.
    """
    fig = figure(**options,
        plot_height=f_h,
        plot_width=f_b,
        match_aspect=True,
        title="Forces and Moments Scheme"
    )
    fig.rect([L*scale/2], [0], width=L*scale*1.2, height=(max_q+offset_q)*2,
                    alpha=0, fill_alpha=0) # transparent rect
    fig.xgrid.grid_line_alpha = 0
    fig.ygrid.grid_line_alpha = 0
    fig.axis.visible = False
    return fig


def compute_N(x, P):
    """
    Function that computes the axial force in the section x.

    @param x (float): Position analyzed in m.
    @param P (float): External force in kN.

    @returns float: Axial force in kN.
    """
    return -P+x*0


def implement_compute_NJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_N() in a Javascript code.
    The implemented function can compute the axial force in the section x.

    @returns str: Javascript code to implement the function compute_N().
    
    JS function:

    @paramJS P (float): External force in kN.
    
    @returnsJS float: Axial force in kN.
    """
    code = """
    function compute_N(P) {
        return -P
    }
    """
    return code


def compute_V(x, q, L):
    """
    Function that computes the shear force in the section x.

    @param x (float): Position analyzed in m.
    @param q (float): External uniform load in kN/m.
    @param L (float): Length of the beam in m.

    @returns float: Shear force in kN.
    """
    return q*x-q*L/2


def implement_compute_VJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_V() in a Javascript code.
    The implemented function can compute the shear force in the section x.

    @returns str: Javascript code to implement the function compute_V().
    
    JS function:

    @paramJS x (float): Position analyzed in m.
    @paramJS q (float): External uniform load in kN/m.
    @paramJS L (float): Length of the beam in m.
    
    @returnsJS float: Shear force in kN.
    """
    code = """
    function compute_V(x, q, L) {
        return q*x-q*L/2
    }
    """
    return code


def compute_M(x, q, L):
    """
    Function that computes the bending moment in the section x.

    @param x (float): Position analyzed in m.
    @param q (float): External uniform load in kN/m.
    @param L (float): Lendth of the beam in m.

    @returns float: Bending moment in kNm.
    """
    return q*x/2*(x-L)


def implement_compute_MJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_M() in a Javascript code.
    The implemented function can compute the bending moment in the section x.

    @returns str: Javascript code to implement the function compute_M().
    
    JS function:

    @paramJS x (float): Position analyzed in m.
    @paramJS q (float): External uniform load in kN/m.
    @paramJS L (float): Lendth of the beam in m.

    @returnsJS float: Bending moment in kNm.
    """
    code = """
    function compute_M(x, q, L) {
        return q*x/2*(x-L)
    }
    """
    return code


def compute_Rx(P):
    """
    Function that computes the horizontal reaction.

    @param P (float): External force in kN.

    @returns float: Reaction in kN.
    """
    return P


def implement_compute_RxJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_Rx() in a Javascript code.
    The implemented function can compute the horizontal reaction.

    @returns str: Javascript code to implement the function compute_Rx().
    
    JS function:

    @paramJS P (float): External force in kN.

    @returnsJS float: Reaction in kN.
    """
    code = """
    function compute_Rx(P) {
        return P
    }
    """
    return code


def compute_Ry_l(q, L):
    """
    Function that computes the vertical reaction in the left support.

    @param q (float): External uniform load in kN/m.
    @param L (float): Length of the beam in m.

    @returns float: Reaction in kN.
    """
    return q*L/2


def implement_compute_Ry_lJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_Ry_l() in a Javascript code.
    The implemented function can compute the vertical reaction in the left support.

    @returns str: Javascript code to implement the function compute_Ry_l().
    
    JS function:

    @paramJS q (float): External uniform load in kN/m.
    @paramJS L (float): Length of the beam in m.

    @returnsJS float: Reaction in kN.
    """
    code = """
    function compute_Ry_l(q, L) {
        return q*L/2
    }
    """
    return code


def compute_Ry_r(q, L):
    """
    Function that computes the vertical reaction in the right support.

    @param q (float): External uniform load in kN/m.
    @param L (float): Length of the beam in m.

    @returns float: Reaction in kN.
    """
    return q*L/2


def implement_compute_Ry_rJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_Ry_r() in a Javascript code.
    The implemented function can compute the vertical reaction in the right support.

    @returns str: Javascript code to implement the function compute_Ry_r().
    
    JS function:

    @paramJS q (float): External uniform load in kN/m.
    @paramJS L (float): Length of the beam in m.

    @returnsJS float: Reaction in kN.
    """
    code = """
    function compute_Ry_r(q, L) {
        return q*L/2
    }
    """
    return code

    
def div_text_forces(P, Rx, Ryl, Ryr, string_section, N, V, M, T_opt=False, T=0):
    """
    Function that creates the text with actions for a Div Widget.

    @param P (float): Externa axial force in kN.
    @param Rx (float): Horizontal reaction force in kN.
    @param Ryl (float): Vertical reaction force in the left support in kN.
    @param Ryr (float): Vertical reaction force in the right support in kN.
    @param string_section (float): Dynamic text with info for the analyzed section.
    @param N (float): Axial force N in kN.
    @param V (float): Shear force V in kN.
    @param M (float): Bending moment M in kNm.
    @param T_opt (bool, optional): Option to have the torsion. Default to False.
    @param T (float, optional): Torsional moment T in kNm. Default to 0 (neglected).

    @returns str: The text.
    """
    if T_opt:
        str_T = f"<br>T = {T} kNm"
    else:
        str_T = ""
        
    return f"""
    <p style='font-size:14px'><b>Forces and Moments:</b></p>
    P = {P} kN<br>
    Rx = {Rx} kN<br>
    Ry (left) = {Ryl} kN<br>
    Ry (right) = {Ryr} kN<br>
    {string_section}<br>
    N = {N} kN<br>
    V = {V} kN<br>
    M = {M} kNm
    {str_T}
    """


def implement_update_reactionsJS():
    """
    Function that creates the Javascript code for the implementation of the function _NAME_() in a Javascript code.
    The implemented function can compute the _DESC_.

    @returns str: Javascript code to implement the function _NAME_().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_Rx (bokeh.models.renderers.GlyphRendere): Horizontal reaction glyph.
    @paramJS glyph_Ry_l (bokeh.models.renderers.GlyphRendere): Vertical left reaction glyph.
    @paramJS glyph_Ry_r (bokeh.models.renderers.GlyphRendere): Vertical right reaction glyph.
    @paramJS alpha (float, optional): Transparency parameters. Defaults to 0.3
    """
    return f"""
    function update_reactions(data, glyph_Rx, glyph_Ry_l, glyph_Ry_r, alpha=0.3) {{
        const P = data['P'][0]
        const L = data['L'][0]*data['SCALE'][0]
        const Ry_l = data['Ry_l'][0]
        const Ry_r = data['Ry_r'][0]
        
        // update visibility
        switch(data['state'][0]) {{
            case 'IDLE':
                arrow_alpha(glyph_Rx) // Rx
                arrow_alpha(glyph_Ry_l) // Ry left
                arrow_alpha(glyph_Ry_r) // Ry right
                break
            case 'R_SEC':
                arrow_alpha(glyph_Rx, 1) // Rx
                arrow_alpha(glyph_Ry_l, 1) // Ry left
                arrow_alpha(glyph_Ry_r, alpha) // Ry right
                break
            case 'L_SEC':
                arrow_alpha(glyph_Rx, alpha) //Rx
                arrow_alpha(glyph_Ry_l, alpha) //Ry left
                arrow_alpha(glyph_Ry_r, 1) // Ry right
                break
            default:
                console.error("State "+data['state'][0]+" in state machine not implemented")
        }}
        
        // update size
        update_arrow(glyph_Rx, -P, -P, 0, 0, 0) // Rx
        update_arrow(glyph_Ry_r, Ry_r, L, L, -Ry_r, 0) // Ry right
        update_arrow(glyph_Ry_l, Ry_l, 0, 0, -Ry_l, 0) // Ry left
    }}
    """


def implement_update_external_forcesJS():
    """
    Function that creates the Javascript code for the implementation of the function update_external_forces() in a Javascript code.
    The implemented function can update the external forces.

    @returns str: Javascript code to implement the function update_external_forces().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_P (bokeh.models.renderers.GlyphRendere): External force glyph.
    @paramJS div_P (bokeh.models.widgets.markups.Div): Div widget.
    @paramJS alpha (float, optional): Transparency parameters. Defaults to 0.3
    """
    return f"""
    function update_external_forces(data, glyph_P, div_P, alpha=0.3) {{
        const P = data['P'][0]
        const L = data['L'][0]*data['SCALE'][0]
        
        // update visibility
        switch(data['state'][0]) {{
            case 'IDLE':
                arrow_alpha(glyph_P) // P
                break
            case 'R_SEC':
                arrow_alpha(glyph_P, alpha) // P
                break
            case 'L_SEC':
                arrow_alpha(glyph_P, 1) //P
                break
            default:
                console.error("State "+data['state'][0]+" in state machine not implemented")
        }}
        
        // update size
        if (P==0) {{
            div_P.text = "Axial force P=0 kN (removed)"
            update_arrow(glyph_P) // P
        }} else {{
            div_P.text = "Axial force P="+P+" kN (applied)"
            update_arrow(glyph_P, P, L+P, L, 0, 0) // P
        }}
    }}
    """


def implement_update_scheme_positionJS():
    """
    Function that creates the Javascript code for the implementation of the function update_scheme_position() in a Javascript code.
    The implemented function can update the draw of the beam in the figure.

    @returns str: Javascript code to implement the function update_scheme_position().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS data_scheme_beamta (dict): Data from the source of the beam (scheme).
    @paramJS data_scheme_q (dict): Data from the source that stores the uniform load (scheme).
    """
    return f"""
    function update_scheme_position(data, data_scheme_beam, data_scheme_q) {{
        const L = data['L'][0]*data['SCALE'][0]
        const pos = data['x'][0]*data['SCALE'][0]
        
        // move position of the point
        data['xF'][0] = pos
        
        switch(data['state'][0]) {{
            case 'IDLE':
                // beam
                data_scheme_beam['x'][0] = 0
                data_scheme_beam['x'][1] = L
                // unif load
                data_scheme_q['x'][0] = 0
                data_scheme_q['x'][1] = 0
                data_scheme_q['x'][2] = L
                data_scheme_q['x'][3] = L
                break
            case 'R_SEC':
                // beam
                data_scheme_beam['x'][0] = 0
                data_scheme_beam['x'][1] = pos
                // unif load
                data_scheme_q['x'][0] = 0
                data_scheme_q['x'][1] = 0
                data_scheme_q['x'][2] = pos
                data_scheme_q['x'][3] = pos
                break
            case 'L_SEC':
                // beam
                data_scheme_beam['x'][0] = L
                data_scheme_beam['x'][1] = pos
                // unif load
                data_scheme_q['x'][0] = L
                data_scheme_q['x'][1] = L
                data_scheme_q['x'][2] = pos
                data_scheme_q['x'][3] = pos
                break
            default:
                console.error("State "+data['state'][0]+" in state machine not implemented")
        }}
    }}
    """


def implement_update_div_forcesJS(T_opt=False):
    """
    Function that creates the Javascript code for the implementation of the function update_div_forces() in a Javascript code.
    The implemented function can update the text of the forces Div.

    @param T_opt (bool, optional): Option to have the torsion. Default to False.

    @returns str: Javascript code to implement the function update_div_forces().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS div (bokeh.models.widgets.markups.Div): Div widget.
    """
    div_text = js.multiline_code_as_stringJS(div_text_forces(
                    js.var_in_strJS('P'),
                    js.var_in_strJS('Rx'),
                    js.var_in_strJS('Ry_r'),
                    js.var_in_strJS('Ry_l'),
                    js.var_in_strJS('str_sec'),
                    js.var_in_strJS('N'),
                    js.var_in_strJS('V'),
                    js.var_in_strJS('M'),
                    T_opt,
                    js.var_in_strJS('T')))
    if T_opt:
        str_T = "const T = Math.round(data['T'][0]*10)/10"
    else:
        str_T = ""
        
    return f"""
    function update_div_forces(data, div) {{
        switch(data['state'][0]) {{
            case 'IDLE':
                var str_sec = "No cross section analysed."
                break
            case 'R_SEC':
            case 'L_SEC':
                var str_sec = "Cross section at "+Math.round(data['x'][0]*10)/10+" m."
                break
            default:
                console.error("State "+data['state'][0]+" in state machine not implemented")
        }}
        const P = data['P'][0]
        const Rx = data['Rx'][0]
        const Ry_l = Math.round(data['Ry_l'][0]*10)/10
        const Ry_r = Math.round(data['Ry_r'][0]*10)/10
        const N = Math.abs(data['N'][0])
        const V = Math.round(Math.abs(data['V'][0])*10)/10
        const M = Math.round(data['M'][0]*10)/10
        {str_T}
        div.text = {div_text}
    }}
    """


def implement_update_internal_forcesJS():
    """
    Function that creates the Javascript code for the implementation of the function update_internal_forces() in a Javascript code.
    The implemented function can update the internal force arrows (scheme).

    @returns str: Javascript code to implement the function update_internal_forces().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_N (bokeh.models.renderers.GlyphRendere): Axial force glyph.
    @paramJS glyph_V (bokeh.models.renderers.GlyphRendere): Shear force glyph.
    @paramJS glyph_M_head (bokeh.models.renderers.GlyphRendere): Arrow's head glyph of the the bending moment.
    @paramJS source_M (bokeh.models.sources.ColumnDataSource): Source that stores the coordinates of the bending moment's arrow.
    @paramJS lambda (float, optional): Parameter that defines the curvature of the bending moment's arrow (0 = straight). Defaults to 0.25.
    @paramJS offset_N (float, optional): Horizontal offset of the N arrow from the designated position. Defaults to 1.5.
    @paramJS offset_V (float, optional): Horizontal offset of the V arrow from the designated position. Defaults to 1.
    """
    return f"""
    function update_internal_forces(data, glyph_N, glyph_V, glyph_M_head, source_M, lambda=0.25, offset_N=1.5, offset_V=1) {{
        const pos = data['x'][0]
        const SCALE = data['SCALE'][0]
        const N = data['N'][0]
        const V = data['V'][0]
        const M = data['M'][0]
        switch(data['state'][0]) {{
            case 'IDLE':
                // internal forces
                update_arrow(glyph_N)
                update_arrow(glyph_V)
                update_curvedArrow(0, 0, 0, 0, 0, source_M, glyph_M_head)
                break;
            case 'R_SEC':
                // internal forces
                update_arrow(glyph_N, -N, pos*SCALE-N+offset_N, pos*SCALE+offset_N, 0, 0)
                update_arrow(glyph_V, -V, pos*SCALE+offset_V, pos*SCALE+offset_V, -V/2, V/2)
                var b = 6
                var c = -M/2*0.8
                var a = b-lambda*c
                update_curvedArrow(a, b, c, pos*SCALE, 0, source_M, glyph_M_head)
                break;
            case 'L_SEC':
                // internal forces
                update_arrow(glyph_N, N, pos*SCALE+N-offset_N, pos*SCALE-offset_N, 0, 0)
                update_arrow(glyph_V, V, pos*SCALE-offset_V, pos*SCALE-offset_V, V/2, -V/2)
                var b = -6
                var c = -M/2*0.8
                var a = b+lambda*c
                update_curvedArrow(a, b, c, pos*SCALE, 0, source_M, glyph_M_head)
                break;
            default:
                console.error("State "+data['state'][0]+" in state machine not implemented")
        }}
    }}
    """


def implement_update_u_loadJS(OFFSET_Q):
    """
    Function that creates the Javascript code for the implementation of the function update_u_load() in a Javascript code.
    The implemented function can update the uniform load's patch (scheme).

    @param OFFSET_Q (float): Value of the optional parameter OFFSET_Q in the JS function.
    
    @returns str: Javascript code to implement the function update_u_load().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS source_q (bokeh.models.sources.ColumnDataSource): Source that stores the coordinates of the uniform load's patch.
    @paramJS OFFSET_Q (float, optional): Vertical offset of the uniform load q from the beam. Defaults to OFFSET_Q (args).
    """
    code = f"""
    function update_u_load(data, source_q, OFFSET_Q={OFFSET_Q}) {{
        const q = data['q'][0]
        source_q.data['y'][1] = OFFSET_Q+q
        source_q.data['y'][2] = OFFSET_Q+q
        source_q.change.emit()
    }}
    """
    return code


# notebook demo 3
def implement_update_N_diagramJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_N_diagram() in a Javascript code.
    The implemented function can update the N diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_N_diagram().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph (bokeh.models.renderers.GlyphRendere): Axial force diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    return f"""
        function update_N_diagram(data, glyph, discr={discr}) {{
            const P = data['P'][0]
            const N_discr = Array.from({{length: discr}}, (_, i) => compute_N(P))
            update_NVM_diagram(glyph, N_discr)
        }}
    """

    
def implement_update_V_diagramJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_V_diagram() in a Javascript code.
    The implemented function can update the V diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_V_diagram().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph (bokeh.models.renderers.GlyphRendere): Shear force diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    return f"""
        function update_V_diagram(data, glyph, discr={discr}) {{
            const L = data['L'][0]
            const q = data['q'][0]
            const x = linspace(0, L, {discr})
            const V_discr = Array.from({{length: discr}}, (_, i) => compute_V(x[i], q, L))
            update_NVM_diagram(glyph, V_discr)
        }}
    """


def implement_update_M_diagramJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_M_diagram() in a Javascript code.
    The implemented function can update the M diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_M_diagram().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph (bokeh.models.renderers.GlyphRendere): Bending moment diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    return f"""
        function update_M_diagram(data, glyph, discr={discr}) {{
            const L = data['L'][0]
            const q = data['q'][0]
            const x = linspace(0, L, {discr})
            const M_discr = Array.from({{length: discr}}, (_, i) => compute_M(x[i], q, L))
            update_NVM_diagram(glyph, M_discr)
        }}
    """


# notebook demo 6
def compute_T(x, Mt, L):
    """
    Function that computes the torsion in the section x.

    @param x (float): Position analyzed in m.
    @param Mt (float): External torsion applied in kNm.
    @param L (float): Length of the beam in m.

    @returns float: Torsion in kNm.
    """
    x_tmp = x*0+1
    x_tmp[x > L/2] = -1
    return Mt*x_tmp/2


def implement_compute_TJS():
    """"
    Function that creates the Javascript code for the implementation of the function compute_T() in a Javascript code.
    The implemented function can compute the torsion in the section x.

    @returns str: Javascript code to implement the function compute_T().
    
    JS function:

    @paramJS x (float): Position analyzed in m.
    @paramJS Mt (float): External torsion applied in kNm.
    @paramJS L (float): Length of the beam in m.

    @returnsJS float: Torsion in kNm.
    """
    code = f"""
    function compute_T(x, Mt, L) {{
        if (x<L/2) {{
            return Mt/2
        }} else {{
            return -Mt/2
        }}
    }}
    """
    return code


def implement_update_T_diagramJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_T_diagram() in a Javascript code.
    The implemented function can update the T diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_T_diagram().
    
    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph (bokeh.models.renderers.GlyphRendere): Torsional moment diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    return f"""
        function update_T_diagram(data, glyph, discr={discr}) {{
            const L = data['L'][0]
            const Mt = data['Mt'][0]
            const x = linspace(0, L, {discr})
            const T_discr = Array.from({{length: discr}}, (_, i) => compute_T(x[i], Mt, L))
            update_NVM_diagram(glyph, T_discr)
        }}
    """


def implement_update_T_sectionJS(pixel2unit=10, scale_T=1):
    """
    Function that creates the Javascript code for the implementation of the function update_T_section() in a Javascript code.
    The implemented function can dynamically update the T (torsion) arrow in a cross section figure.

    @param pixel2unit (float): Constant to convert corectly the size in pixels in the current plot units. Default to 10.
    @param scale_T (float): Constant to convert the intensity of the torsion T to the plot size. Default to 1. 
    
    @returns str: Javascript code to implement the function update_T_section().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS head_T_curved (bokeh.models.renderers.GlyphRendere): M arrow head glyph.
    @paramJS source_T_curved (bokeh.models.sources.ColumnDataSource): Source with the M arrow's coordinates.
    @paramJS line_T (bokeh.models.renderers.GlyphRendere): Glyph of the body of the double arrow of T.
    @paramJS head_T (bokeh.models.renderers.GlyphRendere): Glyph of the head of the double arrow of T.
    @paramJS source_T (bokeh.models.sources.ColumnDataSource): Source that stores the coordinates of the torsion double arrow's body.
    @paramJS div_T (bokeh.models.widgets.markups.Div): Div widget for torsion.
    @paramJS label_T_section (bokeh.models.renderers.GlyphRendere): Label T.
    @paramJS offset_T (float, optional): Horizontal offset of the T arrow from the designated position. Default to 4.
    @paramJS pixel2unit (float): Constant to convert corectly the size in pixels in the current plot units. Default to the argument pixel2unit.
    @paramJS scale_T (float): Constant to convert the intensity of the torsion T to the plot size. Default to the argument scale_T.
    """
    return f"""
    function update_T_section(data, head_T_curved, source_T_curved, line_T, head_T, source_T, div_T, label_T_section, offset_T=4, pixel2unit={pixel2unit}, scale_T={scale_T}) {{
        const Mt = data['Mt'][0]
        const T = data['T'][0]
        
        if (T > 0) {{
            update_doubleArrow(offset_T, offset_T+T/scale_T, 0, 0, source_T, head_T)
        }} else {{
            update_doubleArrow(offset_T-T/scale_T, offset_T, 0, 0, source_T, head_T)
        }}
        
        // update visibility
        if (Mt==0) {{
            div_T.text = "Torsion M<sub>t</sub>=0 kNm (removed)"
            line_T.glyph.line_alpha = 0 // T
            head_T.glyph.line_alpha = 0
            head_T.glyph.fill_alpha = 0
            // T in cross-section
            update_curvedArrow(0, 0, 0, 0, 0, source_T_curved, head_T_curved)
        }} else {{
            div_T.text = "Torsion M<sub>t</sub>="+Mt+" kNm (applied)"
            line_T.glyph.line_alpha = 1 // T
            head_T.glyph.line_alpha = 1
            head_T.glyph.fill_alpha = 1
            // T in cross-section
            update_curvedArrow(0, T*4/scale_T, Math.abs(T*3/scale_T), 0, 0, source_T_curved, head_T_curved)
        }}
        
        if (T==0) {{
            label_T_section.glyph.text=''
        }} else {{
            label_T_section.glyph.text='T'
        }}
    }}
    """


# notebook demo 8
def compute_deflection_uniform_load(x, q, L, Iy, E):
    """
    Function that computes the deflection of the beam with uniform load (only moment deformation) in the section x.

    @param x (float or np.array): Position analyzed in m.
    @param q (float): Uniform load in kN/m.
    @param L (float): Length of the beam in m.
    @param Iy (float): Inertia with respect to the strong axis in mm^4.
    @param E (float): Young modulus in MPa.

    @returns float or np.array: Vertical deflection in mm.
    """
    return -q*x / (24*E*Iy) * (L**3-2*L*x**2+x**3)*1e12


def implement_compute_deflection_uniform_loadJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_deflection_uniform_load() in a Javascript code.
    The implemented function can compute the deflection of the beam with uniform load (only moment deformation) in the section x.

    @returns str: Javascript code to implement the function compute_deflection_uniform_load().
    
    JS function:

    @paramJS x (float): Position analyzed in m.
    @paramJS q (float): Uniform load in kN/m.
    @paramJS L (float): Length of the beam in m.
    @paramJS Iy (float): Inertia with respect to the strong axis in mm^4.
    @paramJS E (float): Young modulus in MPa.

    @returnsJS float: Vertical deflection in mm.
    """
    code = f"""
    function compute_deflection_uniform_load(x, q, L, Iy, E) {{
        return -q*x / (24*E*Iy) * (L**3-2*L*x**2+x**3)*1e12
    }}
    """
    return code
