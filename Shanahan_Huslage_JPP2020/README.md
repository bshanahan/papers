# Shanahan & Huslage, JPP 2020

This repo houses the models, input files, and figure data for the paper: B Shanahan, P. Huslage, "Filament simulations in regions of highly-varying connection length", JPP Submitted 2020.

The models (blob2d.cxx and hermes-1.cxx) are written using the BOUT++ framework, specifically version 4.2.2.  BOUT++ can be found at github.com/boutproject/BOUTdev.

There is also a plot_commands.py file, which will reproduce the plots from the paper using the data stored in the figure_data directory.

Finally, there are methods to generate GPI grids, GPI.py.  This file only works on the IPP (Max Planck-Institut fur Plasmaphysik) network.  