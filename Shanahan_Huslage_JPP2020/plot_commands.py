import numpy as np
import matplotlib.pyplot as plt

def plot_fig_2():

    f = np.load('figure_data/figure_2.npz')
    delta = f['delta_perp']*1e2
    v_inf = f['v_inl']
    v_5k = f['v_5000']
    v_1k = f['v_1000']
    v_100 = f['v_100']
    v_10 = f['v_10']

    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.plot(delta,v_inf,'k--', label=r'$L_\parallel = \infty$')
    plt.plot(delta,v_10,'s', label=r'$L_\parallel = $10m')
    plt.plot(delta,v_100,'o', label=r'$L_\parallel = $100m')
    plt.plot(delta,v_1k,'^', label=r'$L_\parallel = $1km')
    plt.plot(delta,v_5k,'v', label=r'$L_\parallel = $5km')
        
    
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(alpha=0.5)
    plt.xlabel(r'$\delta_\perp$ [cm]', fontsize=18)
    plt.ylabel(r'$\mathrm{v_{max}}$ [m/s]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.tight_layout()
    plt.legend(fancybox=True, loc='lower left', framealpha=0, fontsize=12)
    plt.savefig('fig2.png', dpi=300)
    plt.show()

    
    
def plot_fig_4():
    
    f = np.load('figure_data/figure_4.npz')
    t = f['t']*1e3
    x_10 = f['x_10']*1e2
    x_10_1000 = f['x_10_1000']*1e2
    x_1000 = f['x_1000']*1e2
    x_1000_10 = f['x_1000_10']*1e2
    y = 1.2488476124376016 #from Paul's input
    linewidth=2.5

    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.plot(t,x_10,linewidth=linewidth, color = 'C0', label=r'$L_{\parallel}$ = 10m')
    plt.plot(t,x_10_1000,linewidth=linewidth, label=r'$L_{\parallel}$ = 10m | 1km', color='C0', linestyle='dashed')
    plt.plot(t,x_1000,linewidth=linewidth, label=r'$L_{\parallel}$ = 1km', color='C1', linestyle='solid')
    plt.plot(t,x_1000_10,linewidth=linewidth, label=r'$L_{\parallel}$ = 1km | 10m', color='C1', linestyle='dashed')
    plt.axhline(y, color='black', linestyle = 'dashdot', linewidth = linewidth-0.5, label = r'$L_{\parallel}$ transition')
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'R [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.xlim(np.min(t), np.max(t))
    plt.tight_layout()
    plt.savefig('fig4.png', dpi=300)
    plt.show()


def plot_fig_5b():
    f = np.load('figure_data/figure_5.npz')
    t = f['t']*1e3
    x_02 = f['x_1000_10_02']*1e2
    x_08 = f['x_1000_10_08']*1e2
    x_02 -= x_02[0]
    x_08 -= x_08[0]
    y1 = f['trans1']*1e2-x_02[0]
    y2 = f['trans2']*1e2-x_08[0]
    linewidth=2.5

    plt.rc('font', family='Serif')
    plt.figure(figsize=(6.5,4.5))
    plt.plot(t,x_02,linewidth=linewidth, color = 'C0', label=r'$\delta_{\perp}$ = 1.7cm')
    plt.plot(t,x_08,linewidth=linewidth, label=r'$\delta_{\perp}$ = 7.1cm', color='C1')
    plt.axhline(y1, color='C0', linestyle = 'dashed', linewidth = linewidth-0.5, label = r'$\delta_{\perp}$ = 1.7cm transition')
    plt.axhline(y2, color='C1', linestyle = 'dashed', linewidth = linewidth-0.5, label = r'$\delta_{\perp}$ = 7.1cm transition')
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'R [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=12)
    plt.xlim(np.min(t), np.max(t))
    plt.tight_layout()
    plt.savefig('fig5b.png', dpi=300)
    plt.show()

def plot_fig_6():
        
    f = np.load('figure_data/figure_6.npz')
    t = np.load('figure_data/figure_6.npz')['t']*1e3
    t_vert = np.load('figure_data/figure_4.npz')['t']*1e3
    nt = t_vert.shape[0]
    t = t[:nt]
    x_1000 = np.load('data/vertical.npz')['x_1000']*1e2
    x_1000_10 = f['x_1000_10'][:nt]*1e2
    x_1000_50 = f['x_1000_50'][:nt]*1e2
    x_1000_100 = f['x_1000_100'][:nt]*1e2
    x_1000_250 = f['x_1000_250'][:nt]*1e2
    x_1000_500 = f['x_1000_500'][:nt]*1e2

    x_1000_10 -= x_1000_10[0] 
    x_1000_50 -= x_1000_50[0] 
    x_1000_100 -= x_1000_100[0] 
    x_1000_250 -= x_1000_250[0] 
    x_1000_500 -= x_1000_500[0] 

    y = 1.2488476124376016 #from Paul's input
    linewidth=2.5

    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.plot(t_vert,x_1000,linewidth=linewidth, color = 'C0', label=r'$L_{\parallel}$ = 1km')
    plt.plot(t,x_1000_500,linewidth=linewidth, color = 'C1', label=r'$L_{\parallel}$ = 1km | 500m')
    plt.plot(t,x_1000_250,linewidth=linewidth, color = 'C2', label=r'$L_{\parallel}$ = 1km | 250m')
    plt.plot(t,x_1000_100,linewidth=linewidth, color = 'C3', label=r'$L_{\parallel}$ = 1km | 100m')
    plt.plot(t,x_1000_50,linewidth=linewidth, color = 'C4', label=r'$L_{\parallel}$ = 1km | 50m')
    plt.plot(t,x_1000_10,linewidth=linewidth, color = 'C5', label=r'$L_{\parallel}$ = 1km | 10m')
    plt.axhline(y, color='blue', linestyle = 'dashed', linewidth = linewidth-0.5, label = r'$L_{\parallel}$ transition')
    plt.grid(alpha=0.5)
    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'R [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.legend(fancybox=True, loc='upper left', framealpha=0, fontsize=12)
    plt.tight_layout()
    plt.xlim(np.min(t),np.max(t))
    plt.ylim(np.min(x_1000), np.max(x_1000)+1.250)
    plt.savefig('fig6.png', dpi=300)
    plt.show()

def plot_fig_7():    
    f = np.load('figure_data/figure_7.npz')
    delta = f['delta']*1e2
    zmax = f['z_max']*1e2

    linewidth=2.5

    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.plot(delta,zmax,'ko')
    plt.grid(alpha=0.5)
    plt.xlabel(r'$\delta_\perp$ [cm]', fontsize=18)
    plt.ylabel(r'$\mathrm{z_{max}}$ [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.tight_layout()
    plt.savefig('fig7.png', dpi=300)
    plt.show()

def plot_fig_8():
    f = np.load('figure_data/figure_8.npz')
    t = np.load('figure_data/figure_8.npz')['t']*1e3
    
    x_normal = f['x_normal']*1e2
    x_4s = f['x_4s']*1e2
    x_025s = f['x_025s']*1e2
    ## From Paul's input files.
    y_0 = 1.2488476124376015
    y_4s = 2.933212657814184
    y_025s = 1.3541204277736377

    linewidth=2.5

    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.grid(alpha=0.5)

    plt.axhspan(y_0,y_4s, color='C0', alpha=0.2)
    plt.axhspan(y_0,y_025s, color='C1', alpha=0.67)
    
    plt.plot(t,x_normal,linewidth=linewidth, label=r'no transition', color='black')
    plt.plot(t,x_025s,linewidth=linewidth, label=r'$\sigma/4$', color='C1')
    plt.plot(t,x_4s,linewidth=linewidth, label=r'4$\sigma$', color='C0')

    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'R [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.xlim(np.min(t), np.max(t))
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('fig8.png', dpi=300)
    plt.show()

def plot_fig_9():
    f = np.load('figure_data/figure_9.npz')
    t = np.load('figure_data/figure_8.npz')['t']*1e3
    
    x_normal = f['x_normal']*1e2
    x_1s = f['x_1s']*1e2
    x_025s = f['x_025s']*1e2
    x_1_16s = f['x_1_16s']*1e2
    ## From Paul's input files.
    y_0 = 4.995390449750406
    y_1s = 6.6797554951269875
    y_025s = 5.4164817110945505
    y_1_16s = 5.100663265086444

    linewidth=2.5

    plt.rc('font', family='Serif')
    plt.figure(figsize=(8,4.5))
    plt.grid(alpha=0.5)
    
    plt.axhspan(y_0,y_1s, color='C0', alpha=0.2)
    plt.axhspan(y_0,y_025s, color='C1', alpha=0.33)
    plt.axhspan(y_0,y_1_16s, color='C2', alpha=0.67)

    plt.plot(t,x_normal,linewidth=linewidth, label=r'no transition', color='black')
    plt.plot(t,x_1s,linewidth=linewidth, label=r'$1\sigma$', color='C0')
    plt.plot(t,x_025s,linewidth=linewidth, label=r'$\sigma/4$', color='C1')
    plt.plot(t,x_1_16s,linewidth=linewidth, label=r'$\sigma/16$', color='C2')


    plt.xlabel(r't [$\mathrm{\mu}$s]', fontsize=18)
    plt.ylabel(r'R [cm]', fontsize=18)
    plt.tick_params('both', labelsize=14)
    plt.xlim(np.min(t), np.max(t))
    plt.legend(fancybox=True, loc='best', framealpha=0, fontsize=13)
    plt.tight_layout()
    plt.savefig('fig9.png', dpi=300)
    plt.show()
