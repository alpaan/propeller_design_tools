import propeller_design_tools as pdt


# pdt.clear_foil_database(single_foil='clarky.dat', inside_root_db=False, inside_polar_db=True, inside_for_xfoil=True)
pdt.start_ui()

# prop = pdt.Propeller('MyPropeller')
# oper_data = pdt.propeller.PropellerOperData(directory=r"C:\Users\Jake\Desktop\Python Projects\propeller_design_tools\propeller_design_tools\prop_database\MyPropeller\oper_data")
# oper_data.load_oper_sweep_results()
# prop.plot_oper_data(x_param='J', y_param='Efficiency')
# prop.analyze_sweep(velo_vals=[15, 16, 17], sweep_param='power', sweep_vals=[200, 400, 600, 800, 1000], xrotor_verbose=True)



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
