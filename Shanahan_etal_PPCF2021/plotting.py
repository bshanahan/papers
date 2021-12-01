
def plot_fig_3():
    ## Synthetic diagnostic traces.
    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    linewidth=2.5
    y=0
    plt.plot(t_CA,j, label=r'$j_{sat}^{exp}$', color='black', linewidth=linewidth, alpha=0.5)
    plt.plot(1e6*t[:200]-15.5,Isat_raw[:200,224,0,320], label=r'$j_{sat}^{SD}, N_{CA}=1$', color='C0', linewidth=linewidth)
    plt.plot(1e6*t[:150]-12,I, label=r'$j_{sat}^{SD}, \mathrm{no filter}, N_{CA}=551$', color='C1', linewidth=linewidth)
    plt.plot(1e6*t[:150]-12,I_lowpass, label=r'$j_{sat}^{SD}, \mathrm{100kHz filter}, N_{CA}=354$', color='C2', linewidth=linewidth)
    
    plt.axhline(color='black', linestyle = 'dashed', linewidth = linewidth-0.5)
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'$j_{sat} [\mathrm{mA/mm^2}]$', fontsize=18)
    plt.xlim(-42,42)
    
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('Isat_comp.png',dpi=300)
    plt.show()


    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    linewidth=2.5
    y=0
    plt.plot(t_CA,v_r_meas, label=r'$v_{r}^{exp}$', color='black', linewidth=linewidth, alpha=0.5)
    plt.plot(1e6*t[:200]-15.5,vr[:200,224,320], label=r'$v_{r}^{SD}, N_{CA}=1$', color='C0', linewidth=linewidth)
    plt.plot(1e6*t[:150]-12,vr_CA_fl, label=r'$v_{r}^{SD}, \mathrm{no filter}, N_{CA}=551$', color='C1', linewidth=linewidth)
    plt.plot(1e6*t[:150]-12,vr_CA_fl_lowpass, label=r'$v_{r}^{SD}, \mathrm{100kHz filter}, N_{CA}=354$', color='C2', linewidth=linewidth)
    
    plt.axhline(color='black', linestyle = 'dashed', linewidth = linewidth-0.5)
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'$v_{r} [\mathrm{m/s}]$', fontsize=18)
    plt.xlim(-42,42)
    
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('v_comp.png',dpi=300)
    plt.show()



## Raw traces

def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)


def plot_fig_2():
    plt.rc('font', family='Serif')
    linewidth=2.5
    y=0
    fig, ax1 = plt.subplots(figsize=(8,4.5))
    temp_line = ax1.plot(1e6*t[:200]-15.5,100*((te[:200,224,0,320]/18)-1), label=r'$\tilde{T}_{e}^{SD}$', color='C3', linewidth=linewidth, alpha=0.75)
    jsat_line = ax1.plot(1e6*t[:200]-15.5,Isat_raw[:200,224,0,320], label=r'$j_{sat}^{SD}$', color='C0', linewidth=linewidth)
    ax2 = ax1.twinx()

    phi_line1 = ax2.plot(1e6*t[:200]-15.5,vfl[:200,224,0,320+probe_offset_z]-0.7620526261347251, label=r'$\phi_{fl, upper}^{SD}$', color='C1', linewidth=linewidth, linestyle='dashed')
    
    phi_line2 = ax2.plot(1e6*t[:200]-15.5,vfl[:200,224,0,320-probe_offset_z]-0.7620526261347251, label=r'$\phi_{fl,lower}^{SD}$', color='C2', linewidth=linewidth, linestyle='dashed')
    
    
    ax2.set_ylabel(r'$\phi_{fl}$ [Volts]', fontsize=18)
    ax2.tick_params('both', labelsize=14)
    ax1.grid(alpha=0.5)
    ax1.set_xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    ax1.set_ylabel(r'$j_{sat} [\mathrm{mA/mm^2}], \quad \tilde{T}_e [\%]$', fontsize=18)
    ax1.set_xlim(-42,42)
    ax1.tick_params('both', labelsize=14)
    ax2.set_ylim(-10,-3)
    yticks = np.round(vfl[0,0,0,0]-np.arange(-4,4),1)
    ax2.set_yticklabels(yticks[::-1])
    ax1.set_ylim(-6,8)
    # align_yaxis(ax2, 0, ax1, 0)
    lines = jsat_line + phi_line1 + phi_line2 + temp_line
    labels  = [l.get_label() for l in lines]
    ax1.legend(lines,labels,fancybox=True, loc='best', framealpha=0, fontsize=13)
    fig.tight_layout()
    fig.savefig('raw_data_SD_with_T.png',dpi=300)
    plt.show()







def plot_fig_1():
    ### Propagaion windows.
    plt.contourf(RR,ZZ, (n[1,:,0,:] + n[150,:,0,:] + n[300,:,0,:])/3.,100)
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(r'Density [m$^{-3}$]', fontsize=14)
    plt.contour(RR,ZZ, phi[1,:,0,:],10, colors='white', alpha=0.1)
    plt.contour(RR,ZZ, phi[150,:,0,:],10, colors='white', alpha=0.1)
    plt.contour(RR,ZZ, phi[300,:,0,:],10, colors='white', alpha=0.1)
    plt.xlabel(r'R [cm]', fontsize=18)
    plt.ylabel(r'Z [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.tight_layout()
    plt.savefig('n_phi_prop.png',dpi=300)
    plt.show()

def plot_fig_5():
    from MPM_mimic import vary_inclination
    vary_inclination()

def plot_fig_10():
    ## Temp scan
    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    linewidth=2.5
    y=0
    plt.plot(t_CA,v_r_meas, label=r'$v_{r}^{exp}$', color='black', linewidth=linewidth, alpha=0.5)
    
    plt.plot(1e6*t[:150]-9.7,vr_fl_00, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.00T_0$', color='C0', linewidth=linewidth)
    plt.plot(1e6*t[:150]-9.7,vr_fl_05, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.05T_0$', color='C1', linewidth=linewidth)
    plt.plot(1e6*t[:150]-9.7,vr_fl_10, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.10T_0$', color='C2', linewidth=linewidth)
    plt.plot(1e6*t[:150]-9.7,vr_fl_15, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.15T_0$', color='C3', linewidth=linewidth)
    plt.plot(1e6*t[:150]-9.7,vr_fl_20, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.20T_0$', color='C4', linewidth=linewidth)
    plt.plot(1e6*t[:150]-9.7,vr_fl_25, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.25T_0$', color='C5', linewidth=linewidth)
    plt.plot(1e6*t[:150]-9.7,vr_fl_30, label=r'$v_{r}^{SD},\quad \tilde{T} = 1.30T_0$', color='C6', linewidth=linewidth)
    
    plt.axhline(color='black', linestyle = 'dashed', linewidth = linewidth-0.5)
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'$v_{r} [\mathrm{m/s}]$', fontsize=18)
    plt.xlim(-42,42)
    
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='upper left', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('temp_scan_v_fl.png',dpi=300)
    plt.show()

def plot_fig_8():
    ### Pin separation
    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.plot(2e3*pin_sep[:], sigma_v_smaller[:], 'o', color='C0', label = r'$\delta \approx 1.5$cm')
    plt.plot(2e3*pin_sep[:], sigma_G_small[:], 's', color='C0')
    plt.plot(2e3*pin_sep[:], sigma_v[:], 'o', color='C1', label=r'$\delta \approx 2$cm')
    plt.plot(2e3*pin_sep[:], sigma_G[:], 's', color='C1')
    plt.plot(2e3*pin_sep[:], sigma_v_bigger[:], 'o', color='C2', label=r'$\delta \approx 2.5$cm')
    plt.plot(2e3*pin_sep[:], sigma_G_big[:], 's', color='C2')
    if plot_fits:
        plt.plot(2e3*pin_sep, fit, color='C0', label=r'fit: %.2f$\theta^2$ - %.2f$\theta$ + %.2f' %(float(z1[0]),float(np.abs(z1[1])) ,float(z1[2])))
        plt.plot(2e3*pin_sep, fit_small, color='C1', label=r'fit: %.2f$\theta^2$ - %.2f$\theta$ + %.2f' %(float(z1[0]),float(np.abs(z1[1])) ,float(z1[2])))
        plt.plot(2e3*pin_sep, fit_big, color='C2', label=r'fit: %.2f$\theta^2$ - %.2f$\theta$ + %.2f' %(float(z1[0]),float(np.abs(z1[1])) ,float(z1[2])))
    plt.grid(alpha=0.5)
    plt.xlabel(r'Pin separation [mm]', fontsize=18)
    plt.ylabel(r'$v_r, \Gamma_r$ error [%]', fontsize=18)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)

    plt.tick_params('both', labelsize=14)
    plt.tight_layout()
    if save_plot:
        plt.savefig(str(fname), dpi=300)
        plt.show()
    else:
        plt.show()


def plot_fig_9():
    ### Probe area
    plt.figure(figsize=(8,4.5))
    linewidth=2.5
    y=0
    plt.plot(t_CA,v_r_meas, label=r'$v_{r}^{exp}$', color='black', linewidth=linewidth, alpha=0.5)
    plt.plot(4.5e5*t[:150]-13,vr_fl_0, label=r'$v_{r}^{SD}, A_{eff}=0$', color='C0', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,vr_fl_1, label=r'$v_{r}^{SD}, A_{eff}=1 \mathrm{mm} \times 1\mathrm{mm}$', color='C1', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,vr_fl_2, label=r'$v_{r}^{SD}, A_{eff}=2 \mathrm{mm} \times 2\mathrm{mm}$', color='C2', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,vr_fl_3, label=r'$v_{r}^{SD}, A_{eff}=3 \mathrm{mm} \times 3\mathrm{mm}$', color='C3', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,vr_fl_cm, label=r'$v_{r}^{SD}, A_{eff}=1 \mathrm{cm} \times 1\mathrm{cm}$', color='C4', linewidth=linewidth)
    
    plt.axhline(color='black', linestyle = 'dashed', linewidth = linewidth-0.5)
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'$v_{r} [\mathrm{m/s}]$', fontsize=18)
    plt.xlim(-42,42)
    
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('v_finite_area.png',dpi=300)
    plt.show()
    
    plt.figure(figsize=(8,4.5))
    linewidth=2.5
    y=0
    plt.plot(t_CA,j, label=r'$v_{r}^{exp}$', color='black', linewidth=linewidth, alpha=0.5)
    plt.plot(4.5e5*t[:150]-13,I_0, label=r'$j_{sat}^{SD}, A_{eff}=0$', color='C0', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,I_1, label=r'$j_{sat}^{SD}, A_{eff}=1\mathrm{mm} \times 1\mathrm{mm}$', color='C1', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,I_2, label=r'$j_{sat}^{SD}, A_{eff}=2\mathrm{mm} \times 2\mathrm{mm}$', color='C2', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,I_3, label=r'$j_{sat}^{SD}, A_{eff}=3 \mathrm{mm} \times 3\mathrm{mm}$', color='C3', linewidth=linewidth)
    plt.plot(4.5e5*t[:150]-13,I_cm, label=r'$j_{sat}^{SD}, A_{eff}=1 \mathrm{cm} \times 1\mathrm{cm}$', color='C4', linewidth=linewidth)
    
    plt.axhline(color='black', linestyle = 'dashed', linewidth = linewidth-0.5)
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'$j_{sat} [\mathrm{mA/mm}]$', fontsize=18)
    plt.xlim(-42,42)
    
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('jsat_finite_area.png',dpi=300)
    plt.show()
