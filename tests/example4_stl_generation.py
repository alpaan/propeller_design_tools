import propeller_design_tools as pdt


pdt.set_airfoil_database(r'C:\Users\Jake\Desktop\Python Projects\propeller_design_tools\propeller_design_tools\foil_database')
pdt.set_propeller_database(r'C:\Users\Jake\Desktop\Python Projects\propeller_design_tools\propeller_design_tools\prop_database')

prop = pdt.Propeller('MyPropeller')
prop.plot_design_point_panel()
prop.generate_stl_geometry()
