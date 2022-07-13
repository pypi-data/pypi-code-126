###########################################################################################
# Module with the functions that computes different parameters of a Mohr circle.
# Carmine Schipani, 2022
###########################################################################################


import math


# compute functions
def compute_sigma_average_mohr(sigma_x0, sigma_y0):
    """
    Function that computes the average sigma for the Mohr circle.

    @param sigma_x0 (float): Sigma x of the fixed stress state element in MPa.
    @param sigma_y0 (float): Sigma y of the fixed stress state element in MPa.

    @returns float: Sigma average in MPa.
    """
    return (sigma_x0+sigma_y0)/2


def implement_compute_sigma_average_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_sigma_average_mohr() in a Javascript code.
    The implemented function can compute the average sigma for the Mohr circle.

    @returns str: Javascript code to implement the function compute_sigma_average_mohr().
    
    JS function:
    
    @paramJS sigma_x0 (float): Sigma x of the fixed stress state element in MPa.
    @paramJS sigma_y0 (float): Sigma y of the fixed stress state element in MPa.

    @returnsJS float: Sigma average in MPa.
    """
    code = f"""
    function compute_sigma_average_mohr(sigma_x0, sigma_y0) {{
        return (sigma_x0+sigma_y0)/2
    }}
    """
    return code


def compute_radius_mohr(sigma_x0, sigma_y0, tau_0):
    """
    Function that computes the radius of the Mohr circle.

    @param sigma_x0 (float): Sigma x of the fixed stress state element in MPa.
    @param sigma_y0 (float): Sigma y of the fixed stress state element in MPa.
    @param tau_0 (float): Tau of the fixed stress state element in MPa.

    @returns float: Radius in MPa.
    """
    return math.sqrt(tau_0**2 + (sigma_x0-sigma_y0)**2/4)


def implement_compute_radius_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_radius_mohr() in a Javascript code.
    The implemented function can compute the radius of the Mohr circle.

    @returns str: Javascript code to implement the function compute_radius_mohr().
    
    JS function:
    
    @paramJS sigma_x0 (float): Sigma x of the fixed stress state element in MPa.
    @paramJS sigma_y0 (float): Sigma y of the fixed stress state element in MPa.
    @paramJS tau_0 (float): Tau of the fixed stress state element in MPa.

    @returnsJS float: Radius in MPa.
    """
    code = f"""
    function compute_radius_mohr(sigma_x0, sigma_y0, tau_0) {{
        return Math.sqrt(tau_0**2 + (sigma_x0-sigma_y0)**2/4)
    }}
    """
    return code


def compute_principal_theta_mohr(sigma_x0, sigma_y0, tau_0):
    """
    Function that computes the principal angle theta for the fixed stress state element.

    @param sigma_x0 (flaot): Sigma x of the fixed stress state element in MPa.
    @param sigma_y0 (float): Sigma y of the fixed stress state element in MPa.
    @param tau_0 (float): Tau of the fixed stress state element in MPa.

    @returns float: Angle in rad.
    """
    if (sigma_x0-sigma_y0)==0:
        if tau_0>0:
            return math.pi/2
        else:
            return -math.pi/2
    else:
        return math.atan(2*tau_0/(sigma_y0-sigma_x0))/2


def implement_compute_principal_theta_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_principal_theta_mohr() in a Javascript code.
    The implemented function can compute the principal angle theta for the fixed stress state element.

    @returns str: Javascript code to implement the function compute_principal_theta_mohr().
    
    JS function:
    
    @paramJS sigma_x0 (flaot): Sigma x of the fixed stress state element in MPa.
    @paramJS sigma_y0 (float): Sigma y of the fixed stress state element in MPa.
    @paramJS tau_0 (float): Tau of the fixed stress state element in MPa.

    @returnsJS float: Angle in rad.
    """
    code = f"""
    function compute_principal_theta_mohr(sigma_x0, sigma_y0, tau_0) {{
        if ((sigma_x0-sigma_y0)==0) {{
            if (tau_0>0) {{
                return Math.PI/2
            }} else {{
                return -Math.PI/2
            }}
        }} else {{
            return Math.atan(2*tau_0/(sigma_y0-sigma_x0))/2
        }}
    }}
    """
    return code


def compute_theta_mohr(theta_element, theta_principal):
    """
    Function that computes the Mohr angle of the rotating stress state element.

    @param theta_element (float): Angle of the element in rad.
    @param theta_principal (float): Principal angle of the fixed element in rad.

    @returns float: Angle in rad.
    """
    return theta_element+theta_principal


def implement_compute_theta_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_theta_mohr() in a Javascript code.
    The implemented function can compute the Mohr angle of the rotating stress state element.

    @returns str: Javascript code to implement the function compute_theta_mohr().
    
    JS function:
    
    @paramJS theta_element (float): Angle of the element in rad.
    @paramJS theta_principal (float): Principal angle of the fixed element in rad.

    @returnsJS float: Angle in rad.
    """
    code = f"""
    function compute_theta_mohr(theta_element, theta_principal) {{
        return theta_element+theta_principal
    }}
    """
    return code


def compute_principal_stresses_mohr(sigma_average, r_circle):
    """
    Function that computes the principal stresses.

    @param sigma_average (float): Average sigma of the Mohr circle in MPa.
    @param r_circle (float): Radius of the Mohr circle in MPa.

    @returns tuple: Principal stress 1 and principla stress 2 in MPa.
    """
    tmp1 = sigma_average + r_circle
    tmp2 = sigma_average - r_circle
    
    if tmp1>tmp2:
        sigma1 = tmp1
        sigma2 = tmp2
    else:
        sigma2 = tmp1
        sigma1 = tmp2
    return (sigma1, sigma2)


def implement_compute_principal_stresses_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_principal_stresses_mohr() in a Javascript code.
    The implemented function can compute the principal stresses.

    @returns str: Javascript code to implement the function compute_principal_stresses_mohr().
    
    JS function:
    
    @paramJS sigma_average (float): Average sigma of the Mohr circle in MPa.
    @paramJS r_circle (float): Radius of the Mohr circle in MPa.

    @returnsJS array: Principal stress 1 and principla stress 2 in MPa.
    """
    code = f"""
    function compute_principal_stresses_mohr(sigma_average, r_circle) {{
        const tmp1 = sigma_average + r_circle
        const tmp2 = sigma_average - r_circle
        
        if (tmp1>tmp2) {{
            var sigma1 = tmp1
            var sigma2 = tmp2
        }} else {{
            var sigma2 = tmp1
            var sigma1 = tmp2
        }}
        return [sigma1, sigma2]
    }}
    """
    return code


def compute_stress_state_mohr(sigma_average, r_circle, theta):
    """
    Function that computes the stress state of a rotated element.

    @param sigma_average (flaot): Average sigma of the Mohr circle in MPa.
    @param r_circle (float): Radis of the Mohr circle in MPa.
    @param theta (flaot): Mohr angle of the element in rad.

    @returns tuple: SIgma x, sigma y and tau in MPa.
    """
    sigma_x = sigma_average + r_circle*math.cos(2*theta-math.pi)
    sigma_y = sigma_average + r_circle*math.cos(2*theta)
    tau = r_circle*math.sin(2*theta)
    return (sigma_x, sigma_y, tau)


def implement_compute_stress_state_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function compute_stress_state_mohr() in a Javascript code.
    The implemented function can compute the stress state of a rotated element.

    @returns str: Javascript code to implement the function compute_stress_state_mohr().
    
    JS function:
    
    @paramJS sigma_average (flaot): Average sigma of the Mohr circle in MPa.
    @paramJS r_circle (float): Radis of the Mohr circle in MPa.
    @paramJS theta (flaot): Mohr angle of the element in rad.

    @returnsJS array: SIgma x, sigma y and tau in MPa.
    """
    code = f"""
    function compute_stress_state_mohr(sigma_average, r_circle, theta) {{
        if (sigma_average > 0) {{
            var sigma_x = sigma_average + r_circle*Math.cos(2*theta)
            var sigma_y = sigma_average + r_circle*Math.cos(2*theta-Math.PI)
            var tau = -r_circle*Math.sin(2*theta)
        }} else {{
            var sigma_x = sigma_average + r_circle*Math.cos(2*theta-Math.PI)
            var sigma_y = sigma_average + r_circle*Math.cos(2*theta)
            var tau = r_circle*Math.sin(2*theta)
        }}
        return [sigma_x, sigma_y, tau]
    }}
    """
    return code


# update dynamically functions
def implement_update_sigmax_stateJS(width_element):
    """
    Function that creates the Javascript code for the implementation of the function update_sigmax_state() in a Javascript code.
    The implemented function updates the sigma x arrows of the fixed stress state element.

    @param width_element (float): Width of the stress state element.

    @returns str: Javascript code to implement the function update_sigmax_state().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS arrow_sigma_x1 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma x 1.
    @paramJS arrow_sigma_x2 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma x 2.
    @paramJS width_element (float, optional): Width of the stress state element. Default to width_element (args).
    """
    code = f"""
    function update_sigmax_state(data, arrow_sigma_x1, arrow_sigma_x2, width_element={width_element}) {{
        const offset_arrows = width_element/3
        const sigma_x0 = data['sigma_x0'][0]
        const AHF = 4
        
        if (sigma_x0 > 0) {{
            update_arrow(arrow_sigma_x1, sigma_x0, width_element/2+offset_arrows, width_element/2+offset_arrows+sigma_x0, 0, 0, AHF)
            update_arrow(arrow_sigma_x2, sigma_x0, -(width_element/2+offset_arrows), -(width_element/2+offset_arrows+sigma_x0), 0, 0, AHF)
        }} else {{
            update_arrow(arrow_sigma_x1, -sigma_x0, width_element/2+offset_arrows-sigma_x0, width_element/2+offset_arrows, 0, 0, AHF)
            update_arrow(arrow_sigma_x2, -sigma_x0, -(width_element/2+offset_arrows-sigma_x0), -(width_element/2+offset_arrows), 0, 0, AHF)
        }}
    }}
    """
    return code


def implement_update_sigmax_state_thetaJS(width_element, center_x):
    """
    Function that creates the Javascript code for the implementation of the function update_sigmax_state_theta() in a Javascript code.
    The implemented function updates the sigma x arrows of the rotating stress state element.
    
    @param width_element (float): Width of the stress state element.
    @param center_x (float): Center x position of the stress state element.

    @returns str: Javascript code to implement the function update_sigmax_state_theta().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS arrow_sigma_x1 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma x 1.
    @paramJS arrow_sigma_x2 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma x 2.
    @paramJS width_element (float, optional): Width of the stress state element. Default to width_element (args).
    @paramJS center_x (float, optional): Center x position of the stress state element. Default to center_x (args).
    """
    code = f"""
    function update_sigmax_state_theta(data, arrow_sigma_x1, arrow_sigma_x2, width_element={width_element}, center_x={center_x}) {{
        const offset_arrows = width_element/3
        const offset_sigma = width_element/2+offset_arrows
        var sigma_x = data['sigma_x'][0]
        const theta = data['theta_element'][0]
        const AHF = 4
        
        if (sigma_x < 0) {{
            var sigma_x = -sigma_x
            update_arrow(arrow_sigma_x1,
                         sigma_x,
                         (offset_sigma+center_x+sigma_x)*Math.cos(theta),
                         (offset_sigma+center_x)*Math.cos(theta),
                         (offset_sigma+center_x+sigma_x)*Math.sin(theta),
                         (offset_sigma+center_x)*Math.sin(theta),
                         AHF)
            update_arrow(arrow_sigma_x2,
                         sigma_x,
                         (-(offset_sigma+sigma_x)+center_x)*Math.cos(theta),
                         (-offset_sigma+center_x)*Math.cos(theta),
                         (-(offset_sigma+sigma_x)+center_x)*Math.sin(theta),
                         (-offset_sigma+center_x)*Math.sin(theta),
                         AHF)
        }} else {{
            update_arrow(arrow_sigma_x1,
                         sigma_x,
                         (offset_sigma+center_x)*Math.cos(theta),
                         (offset_sigma+center_x+sigma_x)*Math.cos(theta),
                         (offset_sigma+center_x)*Math.sin(theta),
                         (offset_sigma+center_x+sigma_x)*Math.sin(theta),
                         AHF)
            update_arrow(arrow_sigma_x2,
                         sigma_x,
                         (-offset_sigma+center_x)*Math.cos(theta),
                         (-(offset_sigma+sigma_x)+center_x)*Math.cos(theta),
                         (-offset_sigma+center_x)*Math.sin(theta),
                         (-(offset_sigma+sigma_x)+center_x)*Math.sin(theta),
                         AHF)
        }}
    }}
    """
    return code


def implement_update_sigmay_stateJS(width_element):
    """
    Function that creates the Javascript code for the implementation of the function update_sigmay_state() in a Javascript code.
    The implemented function updates the sigma y arrows of the fixed stress state element.

    @param width_element (float): Width of the stress state element.

    @returns str: Javascript code to implement the function update_sigmay_state().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS arrow_sigma_y1 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma y 1.
    @paramJS arrow_sigma_y2 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma y 2.
    @paramJS width_element (float, optional): Width of the stress state element. Default to width_element (args).
    """
    code = f"""
    function update_sigmay_state(data, arrow_sigma_y1, arrow_sigma_y2, width_element={width_element}) {{
        const offset_arrows = width_element/3
        const sigma_y0 = data['sigma_y0'][0]
        const AHF = 4
        
        if (sigma_y0 > 0) {{
            update_arrow(arrow_sigma_y1, sigma_y0, 0, 0, width_element/2+offset_arrows, width_element/2+offset_arrows+sigma_y0, AHF)
            update_arrow(arrow_sigma_y2, sigma_y0, 0, 0, -(width_element/2+offset_arrows), -(width_element/2+offset_arrows+sigma_y0), AHF)
        }} else {{
            update_arrow(arrow_sigma_y1, -sigma_y0, 0, 0, width_element/2+offset_arrows-sigma_y0, width_element/2+offset_arrows, AHF)
            update_arrow(arrow_sigma_y2, -sigma_y0, 0, 0, -(width_element/2+offset_arrows-sigma_y0), -(width_element/2+offset_arrows), AHF)
        }}
    }}
    """
    return code


def implement_update_sigmay_state_thetaJS(width_element, center_x):
    """
    Function that creates the Javascript code for the implementation of the function update_sigmay_state_theta() in a Javascript code.
    The implemented function updates the sigma y arrows of the rotating stress state element.
    
    @param width_element (float): Width of the stress state element.
    @param center_x (float): Center x position of the stress state element.

    @returns str: Javascript code to implement the function update_sigmay_state_theta().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS arrow_sigma_y1 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma y 1.
    @paramJS arrow_sigma_y2 (bokeh.models.annotations.Arrow): The glyph of the arrow for sigma y 2.
    @paramJS width_element (float, optional): Width of the stress state element. Default to width_element (args).
    @paramJS center_x (float, optional): Center x position of the stress state element. Default to center_x (args).
    """
    code = f"""
    function update_sigmay_state_theta(data, arrow_sigma_y1, arrow_sigma_y2, width_element={width_element}, center_x={center_x}) {{
        const offset_arrows = width_element/3
        const offset_sigma = width_element/2+offset_arrows
        const theta = data['theta_element'][0]
        var sigma_y = data['sigma_y'][0]
        const AHF = 4
        
        if (sigma_y<0) {{
            var sigma_y = -sigma_y
            update_arrow(arrow_sigma_y1,
                         sigma_y,
                         (center_x)*Math.cos(theta)-(offset_sigma+sigma_y)*Math.sin(theta),
                         (center_x)*Math.cos(theta)-(offset_sigma)*Math.sin(theta),
                         (center_x)*Math.sin(theta)+(offset_sigma+sigma_y)*Math.cos(theta),
                         (center_x)*Math.sin(theta)+(offset_sigma)*Math.cos(theta),
                         AHF)
            update_arrow(arrow_sigma_y2,
                         sigma_y,
                         (center_x)*Math.cos(theta)+(offset_sigma+sigma_y)*Math.sin(theta),
                         (center_x)*Math.cos(theta)+(offset_sigma)*Math.sin(theta),
                         (center_x)*Math.sin(theta)-(offset_sigma+sigma_y)*Math.cos(theta),
                         (center_x)*Math.sin(theta)-(offset_sigma)*Math.cos(theta),
                         AHF)
        }} else {{
            update_arrow(arrow_sigma_y1,
                         sigma_y,
                         (center_x)*Math.cos(theta)-(offset_sigma)*Math.sin(theta),
                         (center_x)*Math.cos(theta)-(offset_sigma+sigma_y)*Math.sin(theta),
                         (center_x)*Math.sin(theta)+(offset_sigma)*Math.cos(theta),
                         (center_x)*Math.sin(theta)+(offset_sigma+sigma_y)*Math.cos(theta),
                         AHF)
            update_arrow(arrow_sigma_y2,
                         sigma_y,
                         (center_x)*Math.cos(theta)+(offset_sigma)*Math.sin(theta),
                         (center_x)*Math.cos(theta)+(offset_sigma+sigma_y)*Math.sin(theta),
                         (center_x)*Math.sin(theta)-(offset_sigma)*Math.cos(theta),
                         (center_x)*Math.sin(theta)-(offset_sigma+sigma_y)*Math.cos(theta),
                         AHF)
        }}
    }}
    """
    return code


def implement_update_tau_stateJS(width_element, scale_tau=1):
    """
    Function that creates the Javascript code for the implementation of the function update_tau_state() in a Javascript code.
    The implemented function updates the tau arrows of the fixed stress state element.

    @param width_element (float): Width of the stress state element.
    @param scale_tau (float, optional): Optional scale parameter for the size of the tau arrows. Default to 1.

    @returns str: Javascript code to implement the function update_tau_state().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS arrow_tau_x1 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau x 1.
    @paramJS arrow_tau_x2 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau x 2.
    @paramJS arrow_tau_y1 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau y 1.
    @paramJS arrow_tau_y2 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau y 2.
    @paramJS width_element (float, optional): Width of the stress state element. Default to width_element (args).
    @paramJS scale_tau (float, optional): Optional scale parameter for the size of the tau arrows. Default to scale_tau (args).
    """
    code = f"""
    function update_tau_state(data, arrow_tau_x1, arrow_tau_x2, arrow_tau_y1, arrow_tau_y2, width_element={width_element}, scale_tau={scale_tau}) {{
        const offset_arrows = width_element/3
        const tau_0 = data['tau_0'][0]*scale_tau
        const AHF = 4
        
        update_arrow(arrow_tau_x1, tau_0, width_element/2+offset_arrows/2, width_element/2+offset_arrows/2, -tau_0/2, tau_0/2, AHF)
        update_arrow(arrow_tau_x2, tau_0, -(width_element/2+offset_arrows/2), -(width_element/2+offset_arrows/2), tau_0/2, -tau_0/2, AHF)
        update_arrow(arrow_tau_y1, tau_0, -tau_0/2, tau_0/2, width_element/2+offset_arrows/2, width_element/2+offset_arrows/2, AHF)
        update_arrow(arrow_tau_y2, tau_0, tau_0/2, -tau_0/2, -(width_element/2+offset_arrows/2), -(width_element/2+offset_arrows/2), AHF)
    }}
    """
    return code


def implement_update_tau_state_thetaJS(width_element, center_x, scale_tau=1):
    """
    Function that creates the Javascript code for the implementation of the function update_tau_state_theta() in a Javascript code.
    The implemented function updates the tau arrows of the rotating stress state element.

    @param width_element (float): Width of the stress state element.
    @param center_x (float): Center x position of the stress state element.
    @param scale_tau (float, optional): Optional scale parameter for the size of the tau arrows. Default to 1.

    @returns str: Javascript code to implement the function update_tau_state_theta().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS arrow_tau_x1 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau x 1.
    @paramJS arrow_tau_x2 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau x 2.
    @paramJS arrow_tau_y1 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau y 1.
    @paramJS arrow_tau_y2 (bokeh.models.annotations.Arrow): The glyph of the arrow for tau y 2.
    @paramJS width_element (float, optional): Width of the stress state element. Default to width_element (args).
    @paramJS center_x (float, optional): Center x position of the stress state element. Default to center_x (args).
    @paramJS scale_tau (float, optional): Optional scale parameter for the size of the tau arrows. Default to scale_tau (args).
    """
    code = f"""
    function update_tau_state_theta(data, arrow_tau_x1, arrow_tau_x2, arrow_tau_y1, arrow_tau_y2, width_element={width_element}, center_x={center_x}, scale_tau={scale_tau}) {{
        const offset_arrows = width_element/3
        const offset_tau = width_element/2+offset_arrows/2
        const theta = data['theta_element'][0]
        const tau = data['tau'][0]*scale_tau
        const AHF = 4
        
        update_arrow(arrow_tau_x1,
                     tau,
                     (center_x+offset_tau)*Math.cos(theta)+(tau/2)*Math.sin(theta),
                     (center_x+offset_tau)*Math.cos(theta)-(tau/2)*Math.sin(theta),
                     (center_x+offset_tau)*Math.sin(theta)-(tau/2)*Math.cos(theta),
                     (center_x+offset_tau)*Math.sin(theta)+(tau/2)*Math.cos(theta),
                     AHF)
        update_arrow(arrow_tau_x2,
                     tau,
                     (center_x-offset_tau)*Math.cos(theta)-(tau/2)*Math.sin(theta),
                     (center_x-offset_tau)*Math.cos(theta)+(tau/2)*Math.sin(theta),
                     (center_x-offset_tau)*Math.sin(theta)+(tau/2)*Math.cos(theta),
                     (center_x-offset_tau)*Math.sin(theta)-(tau/2)*Math.cos(theta),
                     AHF)
        update_arrow(arrow_tau_y1,
                     tau,
                     (center_x-tau/2)*Math.cos(theta)-(offset_tau)*Math.sin(theta),
                     (center_x+tau/2)*Math.cos(theta)-(offset_tau)*Math.sin(theta),
                     (center_x-tau/2)*Math.sin(theta)+(offset_tau)*Math.cos(theta),
                     (center_x+tau/2)*Math.sin(theta)+(offset_tau)*Math.cos(theta),
                     AHF)
        update_arrow(arrow_tau_y2,
                     tau,
                     (center_x+tau/2)*Math.cos(theta)+(offset_tau)*Math.sin(theta),
                     (center_x-tau/2)*Math.cos(theta)+(offset_tau)*Math.sin(theta),
                     (center_x+tau/2)*Math.sin(theta)-(offset_tau)*Math.cos(theta),
                     (center_x-tau/2)*Math.sin(theta)-(offset_tau)*Math.cos(theta),
                     AHF)
    }}
    """
    return code


def implement_update_stress_state_elementsJS(max_stress: float, max_dim:float):
    """
    Function that creates the Javascript code for the implementation of the function update_stress_state_elements() in a Javascript code.
    The implemented function updates the fixed and rotating stress state element only (not the arrows).

    @param max_stress (float): Approximate maximal stress for scaling in MPa.
    @param max_dim (float): Approximate dimensions for the stress state elements disposition in MPa.

    @returns str: Javascript code to implement the function update_stress_state_elements().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_stress_state_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the rotating stress state.
    @paramJS glyph_axis (bokeh.models.renderers.GlyphRenderer): The glyph of the dashed line that shows the axis.
    @paramJS glyph_label_element_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the label for the rotating stress state element.
    @paramJS glyph_arc_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the dashed arc that shows the span of the angle theta.
    @paramJS glyph_label_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the label for the element angle theta.
    @paramJS max_stress (float): Approximate maximal stress for scaling in MPa. Default to max_stress (args).
    @paramJS max_dim (float): Approximate dimensions for the stress state elements disposition in MPa. Default to max_dim (args).
    """
    code = f"""
    function update_stress_state_elements(data, glyph_stress_state_theta, glyph_axis, glyph_label_element_theta, glyph_arc_theta, glyph_label_theta, max_stress={max_stress}, max_dim={max_dim}) {{
        // set variables
        const theta_element = data['theta_element'][0]
        const x_new = max_stress*Math.cos(theta_element)
        const y_new = max_stress*Math.sin(theta_element)
        
        
        // update rotating axis
        const src_axis = glyph_axis.data_source
        src_axis.data.x = [0, x_new*max_dim/max_stress]
        src_axis.data.y = [0, y_new*max_dim/max_stress]
        src_axis.change.emit()
        
        // update stress state theta
        glyph_stress_state_theta.glyph.angle = theta_element
        glyph_stress_state_theta.glyph.x = x_new*2
        glyph_stress_state_theta.glyph.y = y_new*2
        
        // label element
        const src_label_element = glyph_label_element_theta.data_source
        src_label_element.data.x = [x_new*2]
        src_label_element.data.y = [y_new*2]
        src_label_element.change.emit()
        
        // arc theta (stress state)
        glyph_arc_theta.glyph.end_angle = theta_element
        
        // label theta (stress state)
        if (theta_element==0) {{
            glyph_label_theta.glyph.text = ""
        }} else {{
            glyph_label_theta.glyph.text = "\N{GREEK SMALL LETTER THETA}"
            const src_label_theta = glyph_label_theta.data_source
            src_label_theta.data.x = [max_stress*Math.cos(theta_element/2)]
            src_label_theta.data.y = [max_stress*Math.sin(theta_element/2)]
            src_label_theta.change.emit()
        }}
    }}
    """
    return code


def implement_update_circle_mohrJS():
    """
    Function that creates the Javascript code for the implementation of the function update_circle_mohr() in a Javascript code.
    The implemented function updates the Mohr circle.

    @returns str: Javascript code to implement the function update_circle_mohr().
    
    JS function:
    
    @paramJS data (dict): Data from the source that stores every essential info.
    @paramJS glyph_circle (bokeh.models.renderers.GlyphRenderer): The glyph of the Mohr circle.
    @paramJS glyph_line (bokeh.models.renderers.GlyphRenderer): The glyph of the line that links the two points of the fixed stress state.
    @paramJS glyph_points (bokeh.models.renderers.GlyphRenderer): The glyph of the two points of the fixed stress state.
    @paramJS glyph_label (bokeh.models.renderers.GlyphRenderer): The glyph of the labels for the two points of the fixed stress state.
    @paramJS glyph_line_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the line that links the two points of the rotating stress state.
    @paramJS glyph_points_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the two points of the rotating stress state.
    @paramJS glyph_label_theta (bokeh.models.renderers.GlyphRenderer): The glyph of the labels for the two points of the rotating stress state.
    @paramJS glyph_arc (bokeh.models.renderers.GlyphRenderer): The glyph of the dashed arc that shows the span of the element angle theta.
    @paramJS glyph_theta_text (bokeh.models.renderers.GlyphRenderer): The glyph of label of the element angle theta.
    @paramJS glyph_arc_p (bokeh.models.renderers.GlyphRenderer): The glyph of the dashed arc that shows the span of the principal angle theta.
    @paramJS glyph_theta_p_text (bokeh.models.renderers.GlyphRenderer): The glyph of label of the principal angle theta.
    """
    code = f"""
    function update_circle_mohr(data, glyph_circle, glyph_line, glyph_points, glyph_label, glyph_line_theta, glyph_points_theta, glyph_label_theta, glyph_arc, glyph_theta_text, glyph_arc_p, glyph_theta_p_text) {{
        // set variables
        const sigma_average = data['sigma_average'][0]
        const r_circle = data['r_circle_mohr'][0]
        const sigma_x0 = data['sigma_x0'][0]
        const sigma_y0 = data['sigma_y0'][0]
        const tau_0 = data['tau_0'][0]
        const sigma_x = data['sigma_x'][0]
        const sigma_y = data['sigma_y'][0]
        const tau = data['tau'][0]
        const theta_element = data['theta_element'][0]
        const theta = data['theta'][0]
        
        // update circle
        glyph_circle.glyph.x = sigma_average
        glyph_circle.glyph.radius = r_circle
        
        // update points
        const src_points = glyph_points.data_source
        src_points.data.x = [sigma_x0, sigma_y0]
        src_points.data.y = [tau_0, -tau_0]
        src_points.change.emit()
        
        // update lines
        const src_line = glyph_line.data_source
        src_line.data.x = [sigma_x0, sigma_y0]
        src_line.data.y = [tau_0, -tau_0]
        src_line.change.emit()
        
        // update labels
        const src_labels = glyph_label.data_source
        src_labels.data.x = [sigma_x0, sigma_y0]
        src_labels.data.y = [tau_0, -tau_0]
        src_labels.change.emit()
        
        // update points theta
        const src_points_theta = glyph_points_theta.data_source
        src_points_theta.data.x = [sigma_x, sigma_y]
        src_points_theta.data.y = [tau, -tau]
        src_points_theta.change.emit()
        
        // update lines theta
        const src_line_theta = glyph_line_theta.data_source
        src_line_theta.data.x = [sigma_x, sigma_y]
        src_line_theta.data.y = [tau, -tau]
        src_line_theta.change.emit()
        
        // update labels theta
        const src_labels_theta = glyph_label_theta.data_source
        src_labels_theta.data.x = [sigma_x, sigma_y]
        src_labels_theta.data.y = [tau, -tau]
        src_labels_theta.change.emit()
        
        // arc theta (Mohr)
        const theta_p = theta-theta_element
        glyph_arc.glyph.start_angle = -2*theta
        glyph_arc.glyph.end_angle = -2*theta_p
        glyph_arc.glyph.x = sigma_average
        glyph_arc.glyph.radius = r_circle/2
        
        // label theta (Mohr)
        if (theta_element==0) {{
            glyph_theta_text.glyph.text = ""
        }} else {{
            glyph_theta_text.glyph.text = "2\N{GREEK SMALL LETTER THETA}"
            const src_label_theta = glyph_theta_text.data_source
            src_label_theta.data.x = [sigma_average + r_circle*Math.cos(theta+theta_p)/2]
            src_label_theta.data.y = [r_circle*Math.sin(-theta-theta_p)/2]
            src_label_theta.change.emit()
        }}
        debugger
        // arc principal theta (Mohr)
        if (theta_p < 0) {{
            var theta_p_tmp = Math.PI/2+theta_p
        }} else {{
            var theta_p_tmp = theta_p
        }}
        glyph_arc_p.glyph.x = sigma_average
        glyph_arc_p.glyph.radius = r_circle/5*2
        glyph_arc_p.glyph.start_angle = -2*theta_p_tmp
        
        // label principal theta (Mohr)
        if (theta_p==0) {{
            glyph_theta_p_text.glyph.text = ""
        }} else {{
            glyph_theta_p_text.glyph.text = "2\N{GREEK SMALL LETTER THETA}\N{LATIN SUBSCRIPT SMALL LETTER P}"
            const src_label_theta_p = glyph_theta_p_text.data_source
            src_label_theta_p.data.x = [sigma_average + r_circle*Math.cos(theta_p_tmp)/5*2]
            src_label_theta_p.data.y = [r_circle*Math.sin(-theta_p_tmp)/5*2]
            src_label_theta_p.change.emit()
        }}
    }}
    """
    return code