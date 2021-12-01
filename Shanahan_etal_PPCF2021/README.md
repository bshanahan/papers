# Shanahan et al., PPCF 2021

This repo contains the input files and figure data for the paper: B Shanahan et al., "Estimating the error in filament propagation measurement using a synthetic probe". Plasma Physics and Controlled Fusion 63 125018 (2021)

This is meant to be run with the hermes-1 model (commit 5aa9c3a1e092a801a76d8f68b507bc8c80fadded): github.com/boutproject/hermes
.. which uses BOUT++ (v. 4.4): github.com/boutproject/bout-dev

The BOUT.inp is an input file which should produce the filament simulation.

The plotting.py file will plot the resulting output, once the variables have been collected.

MPM_mimic.py is the file which contains the synthetic diagnostic and its tools.

simulate_mpm is a script which will randomly choose filament seeding parameters, and plot the resulting scaling.

This is a work in progress, and documentation is slowly being prepared. If you have trouble and/or requests, please raise an issue.