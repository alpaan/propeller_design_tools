import propeller_design_tools as pdt


pdt.start_ui()

# prop = pdt.Propeller(name='MyPropeller')
# prop.plot_mpl3d_geometry()

# af = pdt.Airfoil('e855.dat')
# af.plot_geometry()
# af.plot_polar_data(x_param='CD', y_param='CL')
# af.calculate_xfoil_polars(re=[7e4], ncrit=[9], mach=[0])

# prop = pdt.Propeller('MyPropeller2')
# prop.plot_geometry()
# prop.plot_ideal_eff()

# pdt.create_propeller(
#     name='MyPropeller2',
#     nblades=5,
#     radius=0.1,
#     hub_radius=0.018,
#     hub_wake_disp_br=0.02,
#     design_speed_mps=6,
#     design_adv=None,
#     design_rpm=20000,
#     design_thrust=None,
#     design_power=250,
#     design_cl={'const': 0.2},
#     design_atmo_props={'altitude_km': 1},
#     design_vorform='vrtx',
#     station_params={0.75: 'e855'},
#     geo_params={'tot_skew': 0, 'n_prof_pts': None, 'n_profs': 50},
#     )
