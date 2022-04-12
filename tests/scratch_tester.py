import propeller_design_tools as pdt
import numpy as np


pdt.start_ui()

# prop = pdt.Propeller('first_try_clarky')
# prop.clear_sweep_data()
# prop.analyze_sweep(velo_vals=np.arange(.1, .4, .05),
#                    sweep_param='thrust',
#                    sweep_vals=np.arange(375, 3000, 375),
#                    vorform='pot')
# prop.oper_data.plot(x_param='Rpm', y_param='eff', family_param='speed', iso_param='thrust')
# prop.plot_gl3d_wvel_data()

# prop = pdt.Propeller('first_try_mrc')
# opt = pdt.DutyCycleDesignOptimization(base_prop=prop, verbose=True)
# opt.add_duty_cycle_point(velocity=0.2, thrust=750, duration_percent=100)
# opt.create_prop_grid(vels=[0.18, 0.2, 0.22], cl_consts=[0.4, 0.5, 0.6], advs=[0.04, 0.05, 0.06, 0.07], append=False)
# opt.plot_results()


# prop = pdt.Propeller('first_try_clarky', verbose=False)
# sweep_kwargs = {
#     'velo_vals': np.arange(.1, 1, 0.1),
#     'sweep_param': 'thrust',
#     'sweep_vals': np.arange(600, 2400, 150)
# }

# prop.clear_sweep_data()
# prop.analyze_sweep(**sweep_kwargs)
# prop.oper_data.plot(x_param='J', y_param='thrust(N)', family_param='speed(m/s)', iso_param='power(W)')

# pdt.create_propeller(
#     name='first_try_mrc',
#     nblades=3,
#     radius=1,
#     hub_radius=0.12,
#     hub_wake_disp_br=0.12,
#     design_speed_mps=.2,
#     design_adv=.05,
#     design_rpm=None,
#     design_thrust=750,
#     design_power=None,
#     design_cl={'const': 0.5},
#     design_atmo_props={'altitude_km': -1},
#     design_vorform='vrtx',
#     station_params={0.75: 'mrc'},
#     geo_params={'tot_skew': 45, 'n_prof_pts': None, 'n_profs': 50},
#     )
