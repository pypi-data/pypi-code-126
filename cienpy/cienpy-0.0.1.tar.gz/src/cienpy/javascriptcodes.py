###########################################################################################
# Module with codes in Javascript for Jupyter Notebook using Bokeh.
# For Python functions, see models module.
# Carmine Schipani, 2022
###########################################################################################


## string inceptions (change the format to accomodate Javascript and promote flexibility of the code)
def multiline_code_as_stringJS(code):
    """
    Function used when a dynamic multinine string needs to be added in a Javascript code.
    It converts a multiline Javascript code passed as a string into the correct format to be executed correctly.

    @param code (str): The multiline (using triple double quotation marks) Javascript string with the dynamic text.

    @returns str: The same string with the correct format.
    """
    return f" `{code}` "


def var_in_strJS(var):
    """
    Function used on the arguments of f-format string when the string is formatted for Python but needs to be formatted for Javascript.

    @param var (any): Argument of the string in a simple type (str, int, float, char, ...).

    @returns str: The string of the argument, formattted.
    """
    return f"`+{var}+`"


def _implement_compute_(what_to_compute: str, variable: str, formula: str):
    """
    Private function used just for prototyping, debugging or testing simple compute functions.

    @param what_to_compute (str): Name of what to compute.
    @param variable (str): List of variables.
    @param formula (str): Formula in JS format.

    @returns str: Code of the function in JS
    """
    code = f"""
    function compute_{what_to_compute}({variable}) {{
        return {formula}
    }}
    """
    return code


# useful functions in javascript
def implement_linspaceJS():
    """
    Function that creates the Javascript code for the implementation of the function linspace() in a Javascript code.
    The implemented function can generate an array from start to stop with discr number of values.

    @returns str: Javascript code to implement the function linspace().
    
    JS function:
    
    @paramJS start (float): From where the array will begin.
    @paramJS stop (float): The last value of the array.
    @paramJS step (float): The size of the array.
    
    @returnsJS Array: list generated.
    """
    code = """
    function linspace(start, stop, discr = 100) {
        const step = (stop - start) / (discr-1);
        return Array.from({length: discr}, (_, i) => start + step * i);
    }
    """
    return code


def implement_parabolaJS():
    """
    Function that creates the Javascript code for the implementation of the function parabola() in a Javascript code.
    The implemented function can generate an array with the image of a quadratic function.

    @returns str: Javascript code to implement the function parabola().

    JS function:
    
    @paramJS x (array): The array with the set of x-values of the function (inputs).
    @paramJS a1 (float): The first parameter of the function (associated with x^0).
    @paramJS a2 (float): The second parameter of the function (associated with x^1).
    @paramJS a3 (float): The third parameter of the function (associated with x^2).
    
    @returnsJS Array: list generated.
    """
    code = """
    function parabola(x, a1, a2, a3) {
        return Array.from({length: x.length}, (_, i) => a3 * x[i]**2 + a2 * x[i] +  a1);
    }
    """
    return code


def implement_arrow_growthJS():
    """
    Function that creates the Javascript code for the implementation of the function arrow_growth() in a Javascript code.
    The implemented function can dynamically modulates a value.
    The derivative of the function is high with small values and exponentially smaller with high values.

    @returns str: Javascript code to implement the function arrow_growth().

    JS function:
    
    @paramJS variable (float): Variable.

    @returnsJS float: Modulated variable.
    """
    code = """
    function arrow_growth(variable) {
        return Math.log(Math.abs(variable)+1)
    }
    """
    return code


# change bokeh glyph
def implement_arrow_alphaJS():
    """
    Function that creates the Javascript code for the implementation of the function arrow_alpha() in a Javascript code.
    The implemented function changes the transparency of the arrow (body and head).

    @returns str: Javascript code to implement the function arrow_alpha().

    JS function:
    
    @paramJS straight_arrow (bokeh.models.annotations.Arrow): The glyph of the arrow.
    @paramJS alpha (float, optional): The alpha value. Defaults to 1 (solid).
    """
    code = """
    function arrow_alpha(straight_arrow, alpha=1) {
        straight_arrow.end.line_alpha = alpha
        straight_arrow.end.fill_alpha = alpha
        straight_arrow.line_alpha = alpha
    }
    """
    return code


def implement_update_arrowJS():
    """
    Function that creates the Javascript code for the implementation of the function update_arrow() in a Javascript code.
    The implemented function can dynamically change the parameters that characterizes the straight arrow.

    @returns str: Javascript code to implement the function update_arrow().

    JS function:
    
    @paramJS straight_arrow (bokeh.models.annotations.Arrow): The glyph of the arrow.
    @paramJS intensity (float): Intensity of the force.
    @paramJS x_start (float, optional): Horizontal position of the tail of the arrow. Defaults to 0.
    @paramJS x_end (float, optional): Horizontal position of the head of the arrow. Defaults to 0.
    @paramJS y_start (float, optional): Vertical position of the tail of the arrow. Defaults to 0.
    @paramJS y_end (float, optional): Vertical position of the head of the arrow. Defaults to 0.
    @paramJS AHF (float, optional): Arrow Head Factor. Defaults to 7.
    """
    code = """
    function update_arrow(straight_arrow, intensity, x_start=0, x_end=0, y_start=0, y_end=0, AHF=7) {
        straight_arrow.end.size = arrow_growth(intensity)*AHF
        straight_arrow.x_start = x_start
        straight_arrow.x_end = x_end
        straight_arrow.y_start = y_start
        straight_arrow.y_end = y_end
        straight_arrow.line_width = arrow_growth(intensity)
    }
    """
    return code


def implement_update_curvedArrowJS():
    """
    Function that creates the Javascript code for the implementation of the function update_curvedArrow() in a Javascript code.
    The implemented function can dynamically change the parameters that characterizes the curved arrow.

    @returns str: Javascript code to implement the function update_curvedArrow().

    JS function:
    
    @paramJS a (float): First curve parameter: defines the horizontal position of the head and tail.
    @paramJS b (float): Second curve parameter: defines the horizontal position of the center of the arrow.
    @paramJS c (float): Third curve parameter: defines half of the height if the arrow.
    @paramJS pos_x (float): Horizontal position of the center.
    @paramJS pos_y (float): Vertical position of the center.
    @paramJS source (bokeh.models.sources.ColumnDataSource): Source with the coordinates (x called 'x' and y called 'y').
    @paramJS arr_head (bokeh.models.renderers.GlyphRenderer): Scatter point with triangular shape (head).
    @paramJS discr (int, optional): Number of points for the discretisation of the curved body. Defaults to 10.
    @paramJS AHF (int, optional): Arrow Head Factor. Defaults to 6.
    """
    code = """
    function update_curvedArrow(a, b, c, pos_x, pos_y, source, arr_head, discr=10, AHF=6) {
        const data_M = source.data
        if (c==0) {
            var a1 = 0
            var a3 = 0
        } else {
            var a1 = b
            var a3 = (a-b)/c**2
        }
        const step = 2*c / (discr-1);
        const x = Array.from({length: discr}, (_, i) => -c + step * i);
        const y = Array.from({length: x.length}, (_, i) => a3 * x[i]**2 +  a1)
        var theta = -Math.atan(2/c*(a-b))
        if (c<0) {
            theta = theta+Math.PI
        }
        data_M['x'] = y.map(y => y+pos_x)
        data_M['y'] = x.map(x => x+pos_y)
        
        arr_head.glyph.size = arrow_growth(2*c)*AHF
        arr_head.glyph.angle = theta
        arr_head.glyph.x = y[y.length-1]+pos_x
        arr_head.glyph.y = x[x.length-1]+pos_y
        source.change.emit()
    }
    """
    return code


def implement_update_doubleArrowJS():
    """
    Function that creates the Javascript code for the implementation of the function update_doubleArrow() in a Javascript code.
    The implemented function can dynamically change the parameters that characterizes the double arrow.

    @returns str: Javascript code to implement the function update_doubleArrow().

    JS function:
    
    @paramJS x_start (float): X position of the tail.
    @paramJS x_end (float): X position of the head.
    @paramJS y_start (float): Y position of the tail.
    @paramJS y_end (float): Y position of the head.
    @paramJS source (bokeh.models.sources.ColumnDataSource): Source with the coordinates (x called 'x' and y called 'y').
    @paramJS arr_head (bokeh.models.renderers.GlyphRenderer): Scatter points with triangular shape (head).
    @paramJS AHF (int, optional): Arrow Head Factor. Defaults to 6.
    @paramJS pixel2unit (int, optional): Value to change the pixel head size in the units of the plot. Defaults to pixel2unit (argument of the python function).
    """
    code = f"""
    function update_doubleArrow(x_start, x_end, y_start, y_end, source, arr_heads, AHF=6, pixel2unit=10) {{
        // compute the angle of the line
        const delta_x = x_end-x_start
        const delta_y = y_end-y_start
        if (delta_x==0) {{
            if (delta_y > 0) {{
                var theta = Math.PI/2
            }} else {{
                var theta = Math.PI*3/2
            }}
        }} else if (delta_x > 0) {{
            var theta = Math.atan(delta_y/delta_x)
        }} else {{
            var theta = Math.atan(delta_y/delta_x)+Math.PI
        }}
        
        // head adjust
        const length_arr = Math.sqrt(delta_x**2 + delta_y**2)
        const size_head = arrow_growth(length_arr)*AHF
        const head_x = size_head/pixel2unit*Math.cos(theta)
        const head_y = size_head/pixel2unit*Math.sin(theta)
        
        // update line
        const data_line = source.data
        data_line['x'] = [x_start, x_end]
        data_line['y'] = [y_start, y_end]
        source.change.emit()
        
        // heads
        arr_heads.glyph.size = size_head
        arr_heads.glyph.angle = theta+Math.PI/6
        //arr_heads.glyph.x = [x_end-head_x/2, x_end-head_x/2*3]
        //arr_heads.glyph.y = [y_end-head_y/2, y_end-head_y/2*3]
        const source_h = arr_heads.data_source
        source_h.data['x'] = [x_end-head_x/2, x_end-head_x/2*3]
        source_h.data['y'] = [y_end-head_y/2, y_end-head_y/2*3]
        source_h.change.emit()
    }}
    """
    return code
    

# update diagrams
def implement_update_NVM_diagramJS():
    """
    Function that creates the Javascript code for the implementation of the function update_NVM_diagram() in a Javascript code.
    The implemented function can dynamically update an N/V/M diagram.

    @returns str: Javascript code to implement the function update_NVM_diagram().

    JS function:

    @paramJS diagram (bokeh.models.renderers.GlyphRenderer): Glyph of the N/V/M diagram. 
    @paramJS y (list): Array of N/V/M.
    """
    return """
    function update_NVM_diagram(diagram, y) {
        const y_ = [...y]
        const source = diagram.data_source
        y_.unshift(0)
        y_.push(0)
        source.data.y = y_
        source.change.emit()
    }
    """


def implement_update_stress_diagramJS():
    """
    Function that creates the Javascript code for the implementation of the function update_stress_diagram() in a Javascript code.
    The implemented function can dynamically update a stress diagram.

    @returns str: Javascript code to implement the function update_stress_diagram().

    JS function:

    @paramJS diagram (bokeh.models.renderers.GlyphRenderer): Stress diagram glyph.
    @paramJS x (list): Array of the stress to plot.
    @paramJS y (list): Array from 0 to h.
    """
    return """
    function update_stress_diagram(diagram, x, y) {
        const x_ = [...x]
        const y_ = [...y]
        const source = diagram.data_source
        x_.unshift(0)
        x_.push(0)
        y_.unshift(y[0])
        y_.push(y[y.length-1])
        source.data.x = x_
        source.data.y = y_
        source.change.emit()
    }
    """


def implement_update_strain_diagramJS():
    """
    Function that creates the Javascript code for the implementation of the function update_strain_diagram() in a Javascript code.
    The implemented function can dynamically update a strain diagram.

    @returns str: Javascript code to implement the function update_strain_diagram().

    JS function:

    @paramJS diagram (bokeh.models.renderers.GlyphRenderer): Strain diagram glyph.
    @paramJS x (list): Array of the strain to plot.
    @paramJS y (list): Array from 0 to h.
    """
    return """
    function update_strain_diagram(diagram, x, y) {
        const source = diagram.data_source
        source.data.x = x
        source.data.y = y
        source.change.emit()
    }
    """


def implement_update_axial_stress_strainJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_axial_stress_strain() in a Javascript code.
    The implemented function can dynamically update the axial stress and strain diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_axial_stress_strain().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_stress (bokeh.models.renderers.GlyphRendere): Axial stress diagram glyph.
    @paramJS glyph_strain (bokeh.models.renderers.GlyphRendere): Axial strain diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    code = f"""
    function update_axial_stress_strain(data, glyph_stress, glyph_strain, discr={discr}) {{  
        // define parameters
        const h = data['h'][0]
        const A = data['A'][0]
        const E = data['E'][0]
        const N = data['N'][0]
        const y_discr = linspace(0, h, discr)
        let sigma_axial = new Array(discr)
        let strain_axial = new Array(discr)
        
        // compute the arrays
        for (var i = 0; i < discr; i++) {{
            sigma_axial[i] = compute_sigma_axial(N, A)
            strain_axial[i] = compute_epsilon_axial(sigma_axial[i], E)
        }}
        
        // change the diagrams
        update_stress_diagram(glyph_stress, sigma_axial, y_discr)
        update_strain_diagram(glyph_strain, strain_axial, y_discr)
    }}
    """
    return code


def implement_update_shear_stressJS(discr, hollow_rectangular_section=False):
    """
    Function that creates the Javascript code for the implementation of the function update_shear_stress() in a Javascript code.
    The implemented function can dynamically update the shear stress diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    @param hollow_rectangular_section (bool, optional): Option to change the section. Default to False (solid rectangular section).
    
    @returns str: Javascript code to implement the function update_shear_stress().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_stress (bokeh.models.renderers.GlyphRendere): Shear stress diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    
    if hollow_rectangular_section:
        str_args = """
        if (Math.abs(y_discr[i]-yG) >= (h-2*data['t'][0])/2) {
            tau_shear[i] = compute_tau_shear(V, S, Iy, b)
        } else {
            tau_shear[i] = compute_tau_shear(V, S, Iy, 2*data['t'][0])
        }
        """
    else:
        str_args = "tau_shear[i] = compute_tau_shear(V, S, Iy, b)"
    
    code = f"""
    function update_shear_stress(data, glyph_stress, discr={discr}) {{  
        // define parameters
        const h = data['h'][0]
        const b = data['b'][0]
        const yG = data['yG'][0]
        const Iy = data['Iy'][0]
        const V = data['V'][0]
        const y_discr = linspace(0, h, discr)
        let tau_shear = new Array(discr)
        
        // compute the arrays
        for (var i = 0; i < discr; i++) {{
            var S = compute_first_moment_of_area_implicit(y_discr[i], data)
            {str_args}
        }}
        
        // change the diagrams
        update_stress_diagram(glyph_stress, tau_shear, y_discr)
    }}
    """
    return code


def implement_update_bending_stress_strainJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_bending_stress_strain() in a Javascript code.
    The implemented function can dynamically update the bending stress and strain diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_bending_stress_strain().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_stress (bokeh.models.renderers.GlyphRendere): Bending stress diagram glyph.
    @paramJS glyph_strain (bokeh.models.renderers.GlyphRendere): Bending strain diagram glyph.
    @paramJS glyph_centroid (bokeh.models.renderers.GlyphRendere): Centroid horizontal line glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    code = f"""
    function update_bending_stress_strain(data, glyph_stress, glyph_strain, glyph_centroid, discr={discr}) {{  
        // define parameters
        const h = data['h'][0]
        const E = data['E'][0]
        const Iy = data['Iy'][0]
        const yG = data['yG'][0]
        const M = data['M'][0]
        const y_discr = linspace(0, h, discr)
        let sigma_bending = new Array(discr)
        let strain_bending = new Array(discr)
        const src_centroid = glyph_centroid.data_source
        
        // apply the changes
        src_centroid.data.y = [yG, yG]
        
        // compute the arrays
        for (var i = 0; i < discr; i++) {{
            sigma_bending[i] = compute_sigma_bending(y_discr[i], M, Iy, yG)
            strain_bending[i] = compute_epsilon_bending(sigma_bending[i], E)
        }}
        
        // change the diagrams
        update_stress_diagram(glyph_stress, sigma_bending, y_discr)
        update_strain_diagram(glyph_strain, strain_bending, y_discr)
        src_centroid.change.emit()
    }}
    """
    return code


def implement_update_total_stressJS(discr, T_opt=False, hollow_rectangular_section=False):
    """
    Function that creates the Javascript code for the implementation of the function update_total_stress() in a Javascript code.
    The implemented function can dynamically update the total stress diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    @param T_opt (bool, optional): Option to have the torsion. Default to False.
    @param hollow_rectangular_section (bool, optional): Option to change the section. Default to False (solid rectangular section).
    
    @returns str: Javascript code to implement the function update_total_stress().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_sigma (bokeh.models.renderers.GlyphRendere): Total sigma diagram glyph.
    @paramJS glyph_tau (bokeh.models.renderers.GlyphRendere): Total tau diagram glyph.
    @paramJS glyph_neutral_axis (bokeh.models.renderers.GlyphRendere): Neutral axis horizontal line glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """
    if T_opt:
        str_T_1 = f"""
        const t = data['t'][0]
        const T = data['T'][0]
        let tau_torsion = new Array(discr)
        """
        str_T_2 = f"tau_torsion[i] = compute_tau_torsion(T, b, h, t)"
        total_tau = "total_tau[i] = compute_total_tau(tau_shear[i], tau_torsion[i])"
    else:
        str_T_1 = ""
        str_T_2 = ""
        total_tau = "total_tau[i] = compute_total_tau(tau_shear[i])"
    
    if hollow_rectangular_section:
        str_args = """
        if (Math.abs(y_discr[i]-yG) >= (h-2*data['t'][0])/2) {
            tau_shear[i] = compute_tau_shear(V, S, Iy, b)
        } else {
            tau_shear[i] = compute_tau_shear(V, S, Iy, 2*data['t'][0])
        }
        """
    else:
        str_args = "tau_shear[i] = compute_tau_shear(V, S, Iy, b)"
        
    code = f"""
    function update_total_stress(data, glyph_sigma, glyph_tau, glyph_neutral_axis, discr={discr}) {{  
        // define parameters
        const h = data['h'][0]
        const b = data['b'][0]
        const M = data['M'][0]
        const N = data['N'][0]
        const V = data['V'][0]
        const A = data['A'][0]
        const Iy = data['Iy'][0]
        const yG = data['yG'][0]
        const y_discr = linspace(0, h, discr)
        const y_n_axis = compute_neutral_axis(N, A, Iy, M, yG)
        let sigma_bending = new Array(discr)
        let tau_shear = new Array(discr)
        let sigma_axial = new Array(discr)
        let total_sigma = new Array(discr)
        let total_tau = new Array(discr)
        const src_n_axis = glyph_neutral_axis.data_source
        {str_T_1}
        
        // apply the changes
        db['y_n_axis'][0] = y_n_axis
        src_n_axis.data.y = [y_n_axis, y_n_axis]
        
        // compute the arrays
        for (var i = 0; i < discr; i++) {{
            // sigma
            sigma_axial[i] = compute_sigma_axial(N, A)
            sigma_bending[i] = compute_sigma_bending(y_discr[i], M, Iy, yG)
            total_sigma[i] = compute_total_sigma(sigma_axial[i], sigma_bending[i])
            // tau
            var S = compute_first_moment_of_area_implicit(y_discr[i], data)
            {str_args}
            {str_T_2}
            {total_tau}
        }}
        
        // change the diagrams
        update_stress_diagram(glyph_sigma, total_sigma, y_discr)
        update_stress_diagram(glyph_tau, total_tau, y_discr)
        src_n_axis.change.emit()
    }}
    """
    return code


def implement_update_plastic_stress_strainJS(discr):
    """
    Function that creates the Javascript code for the implementation of the function update_plastic_stress_strain() in a Javascript code.
    The implemented function can dynamically update the total plastic strain and stress diagram.

    @param discr (float): Value of the optional parameter discr in the JS function.
    
    @returns str: Javascript code to implement the function update_plastic_stress_strain().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_strain_el (bokeh.models.renderers.GlyphRendere): Total elastic strain diagram glyph.
    @paramJS glyph_strain_pl (bokeh.models.renderers.GlyphRendere): Total plastic strain diagram glyph.
    @paramJS glyph_sigma_pl (bokeh.models.renderers.GlyphRendere): Total plastic sigma diagram glyph.
    @paramJS discr (float, optional): Discretisation of the diagram curve. Defaults to discr (args).
    """ 
    code = f"""
    function update_plastic_stress_strain(data, glyph_strain_el, glyph_strain_pl, glyph_sigma_pl, discr={discr}) {{  
        // define parameters
        const h = data['h'][0]
        const N = data['N'][0]
        const M = data['M'][0]
        const A = data['A'][0]
        const Iy = data['Iy'][0]
        const yG = data['yG'][0]
        const E = data['E'][0]
        const fy = data['fy'][0]
        const y_discr = linspace(0, h, discr)
        let total_epsilon = new Array(discr)
        
        // compute the arrays
        for (var i = 0; i < discr; i++) {{
            var sigma_axial = compute_sigma_axial(N, A)
            var sigma_bending = compute_sigma_bending(y_discr[i], M, Iy, yG)
            var epsilon_bending = compute_epsilon_bending(sigma_bending, E)
            var epsilon_axial = compute_epsilon_axial(sigma_axial, E)
            total_epsilon[i] = compute_total_epsilon(epsilon_axial, epsilon_bending)
        }}
        let [stress_pl, strain_pl, y_discr_strain_pl, yNA] = compute_total_stress_strain(h, fy, E, N, M, A, Iy, yG, discr)
        
        
        // change the diagrams
        update_strain_diagram(glyph_strain_el, total_epsilon, y_discr)
        update_stress_diagram(glyph_sigma_pl, stress_pl, y_discr)
        update_strain_diagram(glyph_strain_pl, strain_pl, y_discr_strain_pl)
    }}
    """
    return code


def implement_update_NVM_sectionJS():
    """
    Function that creates the Javascript code for the implementation of the function update_NVM_section() in a Javascript code.
    The implemented function can dynamically update the NVM arrows in a cross section figure.

    @returns str: Javascript code to implement the function update_NVM_section().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_N (bokeh.models.renderers.GlyphRendere): N arrow glyph.
    @paramJS glyph_V (bokeh.models.renderers.GlyphRendere): V arrow glyph.
    @paramJS glyph_M_head (bokeh.models.renderers.GlyphRendere): M arrow head glyph.
    @paramJS source_M (bokeh.models.sources.ColumnDataSource): Source with the M arrow's coordinates.
    @paramJS label_N_section (bokeh.models.renderers.GlyphRendere): Label N.
    @paramJS label_V_section (bokeh.models.renderers.GlyphRendere): Label V.
    @paramJS label_M_section (bokeh.models.renderers.GlyphRendere): Label M.
    @paramJS lambda (float, optional): Parameter that defines the curvature of the bending moment's arrow (0 = straight). Defaults to 0.25.
    @paramJS offset_N (float, optional): Horizontal offset of the N arrow from the designated position. Defaults to 1.5.
    @paramJS offset_V (float, optional): Horizontal offset of the V arrow from the designated position. Defaults to 1.
    """
    return f"""
    function update_NVM_section(data, glyph_N, glyph_V, glyph_M_head, source_M, label_N_section, label_V_section, label_M_section, lambda=0.25, offset_N=1.5, offset_V=2) {{
        const x = 0
        const y = 0
        const N = data['N'][0]
        const V = data['V'][0]
        const M = data['M'][0]
        
        update_arrow(glyph_N, -N, x-N+offset_N, x+offset_N, y, y)
        update_arrow(glyph_V, -V, x+offset_V, x+offset_V, y-V/2, y+V/2)
        var b = 6
        var c = -M/2*0.8
        var a = b-lambda*c
        update_curvedArrow(a, b, c, x, y, source_M, glyph_M_head)
        
        if (N==0) {{
            label_N_section.glyph.text=''
        }} else {{
            label_N_section.glyph.text='N'
        }}
        
        if (V==0) {{
            label_V_section.glyph.text=''
        }} else {{
            label_V_section.glyph.text='V'
        }}
        
        if (M==0) {{
            label_M_section.glyph.text=''
        }} else {{
            label_M_section.glyph.text='M'
        }}
    }}
    """


def implement_update_deflection_beamJS(discr=20):
    """
    Function that creates the Javascript code for the implementation of the function update_deflection_beam() in a Javascript code.
    The implemented function can dynamically update the deflection of the beam under uniform load.

    @param discr (float, optional): Value of the optional parameter discr in the JS function. Default to 20.
    
    @returns str: Javascript code to implement the function update_deflection_beam().

    JS function:

    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_beam (bokeh.models.renderers.GlyphRendere): Beam glyph.
    @paramJS discr (float, optional): Discretisation of the beam. Defaults to discr (args).
    """
    code = f"""
    function update_deflection_beam(data, glyph_beam, discr={discr}) {{
        const q = data['q'][0]
        const E = data['E'][0]
        const L = data['L'][0]
        const Iy = data['Iy'][0]
        
        const x = linspace(0, L, discr)
        const defl = new Array(discr)
        for(var i = 0; i < discr; i++) {{
            defl[i] = compute_deflection_uniform_load(x[i], q, L, Iy, E)
        }}
        
        const source = glyph_beam.data_source
        source.data.x = x
        source.data.y = defl
        source.change.emit()
    }}
    """
    return code