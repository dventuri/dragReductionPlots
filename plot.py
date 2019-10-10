"""
TODO:
Insert zoom in fluid velocity (twophase)
Add singlephase comparison in multiphase rms fluid velocity - validation (?)
Add semilog plot together with fluid velocity validation singlephase
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
plt.style.use('default')


### READ ALL DATA ###

### Experiment - Pang and Wei (2013)
#Single-phase flow
UP_Exp0 = np.loadtxt("graficos_artigo/vel_mono_log.csv",
                     dtype=float,
                     skiprows=0,
                     delimiter=' ')
UP_Exp0[:,0] = -1*(UP_Exp0[:,0]-300)  #'Right side' of data has better results near the wall
                                      # changed '0-300' to '300-0'
uP_Exp0 = np.loadtxt("graficos_artigo/u_rms_alfa0.1_d0.5.csv",
                     dtype=float,
                     skiprows=0,
                     delimiter=' ')
vP_Exp0 = np.loadtxt("graficos_artigo/v_rms_alfa0.1_d0.5.csv",
                     dtype=float,
                     skiprows=0,
                     delimiter=' ')
UP_ExpA3 = np.loadtxt("graficos_artigo/vel_pang_alfa0.1_d0.5.csv",
                      dtype=float,
                      skiprows=0,
                      delimiter=' ')
UP_ExpA3[:,0] = -1*(UP_ExpA3[:,0]-300)  #'Right side' of data has better results near the wall
                                        # changed '0-300' to '300-0'
uP_ExpA3 = np.loadtxt("graficos_artigo/u_rms_alfa0.1_d0.5_bif.csv",
                      dtype=float,
                      skiprows=0,
                      delimiter=' ')
uP_ExpA3[:,0] = -1*(uP_ExpA3[:,0]-300)  #'Right side' of data has better results near the wall
                                        # changed '0-300' to '300-0'
vP_ExpA3 = np.loadtxt("graficos_artigo/v_rms_alfa0.1_d0.5_bif.csv",
                      dtype=float,
                      skiprows=0,
                      delimiter=' ')
vP_ExpA3[:,0] = -1*(vP_ExpA3[:,0]-300)  #'Right side' of data has better results near the wall
                                        # changed '0-300' to '300-0'

### Single-phase flow - DNS
#Giusti et al. (2005)
UP_Gi = np.loadtxt("graficos_artigo/giust_dns_vel.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
UP_Gi = UP_Gi[UP_Gi[:,0].argsort()] #sort ascending y+
uP_Gi = np.loadtxt("graficos_artigo/giust_dns_urms.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
uP_Gi = uP_Gi[uP_Gi[:,0].argsort()] #sort ascending y+
vP_Gi = np.loadtxt("graficos_artigo/giust_dns_yrms.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
vP_Gi = vP_Gi[vP_Gi[:,0].argsort()] #sort ascending y+
wP_Gi = np.loadtxt("graficos_artigo/giust_dns_wrms.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
wP_Gi = wP_Gi[wP_Gi[:,0].argsort()] #sort ascending y+

#Yu and Kawaguchi (2004)
UP_YK = np.loadtxt("graficos_artigo/vel_yu_2004_dns_128.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
UP_YK = UP_YK[UP_YK[:,0].argsort()] #sort ascending y+
uP_YK = np.loadtxt("graficos_artigo/yu_rms_64.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
uP_YK = uP_YK[uP_YK[:,0].argsort()] #sort ascending y+
vP_YK = np.loadtxt("graficos_artigo/yu_vrms_64.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
vP_YK = vP_YK[vP_YK[:,0].argsort()] #sort ascending y+
wP_YK = np.loadtxt("graficos_artigo/yu_wrms_64.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
wP_YK = wP_YK[wP_YK[:,0].argsort()] #sort ascending y+

#Pang et al. (2014)
UP_Pa = np.loadtxt("graficos_artigo/vel_dns_pang_norm.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
UP_Pa = UP_Pa[UP_Pa[:,0].argsort()] #sort ascending y+
uP_Pa = np.loadtxt("graficos_artigo/dns_pang_urms.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
uP_Pa = uP_Pa[uP_Pa[:,0].argsort()] #sort ascending y+
vP_Pa = np.loadtxt("graficos_artigo/dns_pang_vrms.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
vP_Pa = vP_Pa[vP_Pa[:,0].argsort()] #sort ascending y+
wP_Pa = np.loadtxt("graficos_artigo/dns_pang_wrms1.csv",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ')
wP_Pa = wP_Pa[wP_Pa[:,0].argsort()] #sort ascending y+

### Present work - Simulations
#Single-phase
UP_0 = np.loadtxt("graficos_artigo/u_mono_128_dt10(-4)_novo_180000.curve",
                  dtype=float,
                  skiprows=2,
                  delimiter=' ')
UP_0[:,0] = UP_0[:,0]*0.0302353/(0.001/1000)
UP_0[:,1] = UP_0[:,1]/0.0302353
uP_0 = np.loadtxt("graficos_artigo/u_rms_mono_128_dt10(-4)_novo_180000.curve",
                  dtype=float,
                  skiprows=2,
                  delimiter=' ')
uP_0[:,0] = uP_0[:,0]*0.0302353/(0.001/1000)
uP_0[:,1] = uP_0[:,1]/0.0302353
vP_0 = np.loadtxt("graficos_artigo/v_rms_mono_128_dt10(-4)_novo_180000.curve",
                  dtype=float,
                  skiprows=2,
                  delimiter=' ')
vP_0[:,0] = vP_0[:,0]*0.0302353/(0.001/1000)
vP_0[:,1] = vP_0[:,1]/0.0302353
wP_0 = np.loadtxt("graficos_artigo/w_rms_mono_128_dt10(-4)_novo_180000.curve",
                  dtype=float,
                  skiprows=2,
                  delimiter=' ')
wP_0[:,0] = wP_0[:,0]*0.0302353/(0.001/1000)
wP_0[:,1] = wP_0[:,1]/0.0302353

#Mean velocity - two-hase
UP_A1 = np.loadtxt("graficos_artigo/u_average_alfa_0.1_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_A1[:,0] = UP_A1[:,0]*0.0302353/(0.001/1000)
UP_A1[:,1] = UP_A1[:,1]/0.0302353
UP_A2 = np.loadtxt("graficos_artigo/u_average_alfa_0.1_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_A2[:,0] = UP_A2[:,0]*0.0302353/(0.001/1000)
UP_A2[:,1] = UP_A2[:,1]/0.0302353
UP_A3 = np.loadtxt("graficos_artigo/u_average_bif_alfa0.1_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_A3[:,0] = UP_A3[:,0]*0.0302353/(0.001/1000)
UP_A3[:,1] = UP_A3[:,1]/0.0302353
UP_B1 = np.loadtxt("graficos_artigo/u_average_bif_alfa0.5_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_B1[:,0] = UP_B1[:,0]*0.0302353/(0.001/1000)
UP_B1[:,1] = UP_B1[:,1]/0.0302353
UP_B2 = np.loadtxt("graficos_artigo/u_average_bif_alfa0.5_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_B2[:,0] = UP_B2[:,0]*0.0302353/(0.001/1000)
UP_B2[:,1] = UP_B2[:,1]/0.0302353
UP_B3 = np.loadtxt("graficos_artigo/u_average_bif_alfa0.5_d0.5_195000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_B3[:,0] = UP_B3[:,0]*0.0302353/(0.001/1000)
UP_B3[:,1] = UP_B3[:,1]/0.0302353

#rms velocity - two-phase
uP_A1 = np.loadtxt("graficos_artigo/u_rms_alfa_0.1_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
uP_A1[:,0] = uP_A1[:,0]*0.0302353/(0.001/1000)
uP_A1[:,1] = uP_A1[:,1]/0.0302353
vP_A1 = np.loadtxt("graficos_artigo/v_rms_alfa_0.1_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
vP_A1[:,0] = vP_A1[:,0]*0.0302353/(0.001/1000)
vP_A1[:,1] = vP_A1[:,1]/0.0302353
wP_A1 = np.loadtxt("graficos_artigo/w_rms_alfa_0.1_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
wP_A1[:,0] = wP_A1[:,0]*0.0302353/(0.001/1000)
wP_A1[:,1] = wP_A1[:,1]/0.0302353

uP_A2 = np.loadtxt("graficos_artigo/u_rms_alfa_0.1_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
uP_A2[:,0] = uP_A2[:,0]*0.0302353/(0.001/1000)
uP_A2[:,1] = uP_A2[:,1]/0.0302353
vP_A2 = np.loadtxt("graficos_artigo/v_rms_alfa_0.1_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
vP_A2[:,0] = vP_A2[:,0]*0.0302353/(0.001/1000)
vP_A2[:,1] = vP_A2[:,1]/0.0302353
wP_A2 = np.loadtxt("graficos_artigo/w_rms_alfa_0.1_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
wP_A2[:,0] = wP_A2[:,0]*0.0302353/(0.001/1000)
wP_A2[:,1] = wP_A2[:,1]/0.0302353

uP_A3 = np.loadtxt("graficos_artigo/u_rms_bif_alfa0.1_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
uP_A3[:,0] = uP_A3[:,0]*0.0302353/(0.001/1000)
uP_A3[:,1] = uP_A3[:,1]/0.0302353
vP_A3 = np.loadtxt("graficos_artigo/v_rms_alfa0.1_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
vP_A3[:,0] = vP_A3[:,0]*0.0302353/(0.001/1000)
vP_A3[:,1] = vP_A3[:,1]/0.0302353
wP_A3 = np.loadtxt("graficos_artigo/w_rms_alfa0.1_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
wP_A3[:,0] = wP_A3[:,0]*0.0302353/(0.001/1000)
wP_A3[:,1] = wP_A3[:,1]/0.0302353

uP_B1 = np.loadtxt("graficos_artigo/u_rms_alfa0.5_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
uP_B1[:,0] = uP_B1[:,0]*0.0302353/(0.001/1000)
uP_B1[:,1] = uP_B1[:,1]/0.0302353
vP_B1 = np.loadtxt("graficos_artigo/v_rms_alfa0.5_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
vP_B1[:,0] = vP_B1[:,0]*0.0302353/(0.001/1000)
vP_B1[:,1] = vP_B1[:,1]/0.0302353
wP_B1 = np.loadtxt("graficos_artigo/w_rms_alfa0.5_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
wP_B1[:,0] = wP_B1[:,0]*0.0302353/(0.001/1000)
wP_B1[:,1] = wP_B1[:,1]/0.0302353

uP_B2 = np.loadtxt("graficos_artigo/u_rms_alfa0.5_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
uP_B2[:,0] = uP_B2[:,0]*0.0302353/(0.001/1000)
uP_B2[:,1] = uP_B2[:,1]/0.0302353
vP_B2 = np.loadtxt("graficos_artigo/v_rms_alfa0.5_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
vP_B2[:,0] = vP_B2[:,0]*0.0302353/(0.001/1000)
vP_B2[:,1] = vP_B2[:,1]/0.0302353
wP_B2 = np.loadtxt("graficos_artigo/w_rms_alfa0.5_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
wP_B2[:,0] = wP_B2[:,0]*0.0302353/(0.001/1000)
wP_B2[:,1] = wP_B2[:,1]/0.0302353

uP_B3 = np.loadtxt("graficos_artigo/u_rms_alfa0.5_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
uP_B3[:,0] = uP_B3[:,0]*0.0302353/(0.001/1000)
uP_B3[:,1] = uP_B3[:,1]/0.0302353
vP_B3 = np.loadtxt("graficos_artigo/v_rms_alfa0.5_d0.5_172000_teste03.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
vP_B3[:,0] = vP_B3[:,0]*0.0302353/(0.001/1000)
vP_B3[:,1] = vP_B3[:,1]/0.0302353
wP_B3 = np.loadtxt("graficos_artigo/w_rms_alfa0.5_d0.5_172000_teste03.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
wP_B3[:,0] = wP_B3[:,0]*0.0302353/(0.001/1000)
wP_B3[:,1] = wP_B3[:,1]/0.0302353

#bubble concentration
cB_A1 = np.loadtxt("graficos_artigo/volfrac_alfa_0.1_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
cB_A1[:,0] = cB_A1[:,0]*0.0302353/(0.001/1000)
cB_A1[:,1] = cB_A1[:,1]*100
cB_A2 = np.loadtxt("graficos_artigo/volfrac_alfa_0.1_d0.2_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
cB_A2[:,0] = cB_A2[:,0]*0.0302353/(0.001/1000)
cB_A2[:,1] = cB_A2[:,1]*100
cB_A3 = np.loadtxt("graficos_artigo/volfrac_alfa0.1_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
cB_A3[:,0] = cB_A3[:,0]*0.0302353/(0.001/1000)
cB_A3[:,1] = cB_A3[:,1]*100
cB_B1 = np.loadtxt("graficos_artigo/volfrac_alfa0.5_d0.1_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
cB_B1[:,0] = cB_B1[:,0]*0.0302353/(0.001/1000)
cB_B1[:,1] = cB_B1[:,1]*100
cB_B2 = np.loadtxt("graficos_artigo/vol_frac_alfa0.5_d0.2_180000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
cB_B2[:,0] = cB_B2[:,0]*0.0302353/(0.001/1000)
cB_B2[:,1] = cB_B2[:,1]*100
cB_B3 = np.loadtxt("graficos_artigo/volfrac_alfa0.5_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
cB_B3[:,0] = cB_B3[:,0]*0.0302353/(0.001/1000)
cB_B3[:,1] = cB_B3[:,1]*100

UP_B_A1 = np.loadtxt("graficos_artigo/u_bolha_average_alfa_0.1_d0.1_172000.curve",
                     dtype=float,
                     skiprows=2,
                     delimiter=' ')
UP_B_A1[:,0] = UP_B_A1[:,0]*0.0302353/(0.001/1000)
UP_B_A1[:,1] = UP_B_A1[:,1]/0.0302353
UP_B_A2 = np.loadtxt("graficos_artigo/u_bolha_average_alfa_0.1_d0.2_172000.curve",
                     dtype=float,
                     skiprows=2,
                     delimiter=' ')
UP_B_A2[:,0] = UP_B_A2[:,0]*0.0302353/(0.001/1000)
UP_B_A2[:,1] = UP_B_A2[:,1]/0.0302353
UP_B_A3 = np.loadtxt("graficos_artigo/u_bolha_average_bif_alfa0.1_d0.5_172000.curve",
                     dtype=float,
                     skiprows=2,
                     delimiter=' ')
UP_B_A3[:,0] = UP_B_A3[:,0]*0.0302353/(0.001/1000)
UP_B_A3[:,1] = UP_B_A3[:,1]/0.0302353
UP_B_B1 = np.loadtxt("graficos_artigo/u_bolha_average_bif_alfa0.5_d0.1_172000.curve",
                     dtype=float,
                     skiprows=2,
                     delimiter=' ')
UP_B_B1[:,0] = UP_B_B1[:,0]*0.0302353/(0.001/1000)
UP_B_B1[:,1] = UP_B_B1[:,1]/0.0302353
UP_B_B2 = np.loadtxt("graficos_artigo/u_bolha_average_bif_alfa0.5_d0.2_180000.curve",
                     dtype=float,
                     skiprows=2,
                     delimiter=' ')
UP_B_B2[:,0] = UP_B_B2[:,0]*0.0302353/(0.001/1000)
UP_B_B2[:,1] = UP_B_B2[:,1]/0.0302353
UP_B_B3 = np.loadtxt("graficos_artigo/u_bolha_average_bif_alfa0.5_d0.5_172000.curve",
                     dtype=float,
                     skiprows=2,
                     delimiter=' ')
UP_B_B3[:,0] = UP_B_B3[:,0]*0.0302353/(0.001/1000)
UP_B_B3[:,1] = UP_B_B3[:,1]/0.0302353

### ###


### FIGURE SINGLE-PHASE - MEAN VELOCITY
plt.style.use('twoSingleColumn.mplstyle')
fig, ax = plt.subplots(1, 2)
#
ax[0].set_xlabel(r'$y^{+}$')
ax[0].set_ylabel(r'$\overline{u}^{+}$')
ax[0].axis([0.0, 150.0, 0.0, 20.0])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(4))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(1))
ax[0].scatter(UP_Exp0[:,0], UP_Exp0[:,1],
              s=25,
              c='white',
              marker='o',
              edgecolors='black',
              linewidths='1',
              label='Pang and Wei (2013)')
ax[0].plot(UP_0[:,0], UP_0[:,1],
           label='Present work',
           color='black',
           linewidth=1,
           linestyle='-')
ax[0].plot(UP_Gi[:,0], UP_Gi[:,1],
           label='Giusti et al. (2005)',
           color='black',
           linewidth=1,
           linestyle= '-.')
ax[0].plot(UP_YK[:,0], UP_YK[:,1],
           label='Yu e Kawaguchi (2004)',
           color='black',
           linewidth=1,
           linestyle= '--')
ax[0].plot(UP_Pa[:,0], UP_Pa[:,1],
           label='Pang et al. (2014)',
           color='black',
           linewidth=1,
           linestyle= ':')
ax[0].legend(loc='lower right')
#
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylabel(r'$\overline{u}^{+}$')
ax[1].axis([1.0, 150.0, 0.0, 20.0])
ax[1].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(10))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(4))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(1))
ax[1].scatter(UP_Exp0[:,0], UP_Exp0[:,1],
              s=25,
              c='white',
              marker='o',
              edgecolors='black',
              linewidths='1',
              label='Pang and Wei (2013)')
ax[1].semilogx(UP_0[:,0], UP_0[:,1],
               label='Present work',
               color='black',
               linewidth=1,
               linestyle='-')
ax[1].semilogx(UP_Gi[:,0], UP_Gi[:,1],
               label='Giusti et al. (2005)',
               color='black',
               linewidth=1,
               linestyle= '-.')
ax[1].semilogx(UP_YK[:,0], UP_YK[:,1],
               label='Yu e Kawaguchi (2004)',
               color='black',
               linewidth=1,
               linestyle= '--')
ax[1].semilogx(UP_Pa[:,0], UP_Pa[:,1],
               label='Pang et al. (2014)',
               color='black',
               linewidth=1,
               linestyle= ':')
ax[1].plot(np.linspace(1,13), np.linspace(1,13),
        #    label='Pang et al. (2014)',
           color='gray',
           linewidth=1,
           linestyle= '-')
ax[1].plot(np.linspace(8,150), 2.5*np.log(np.linspace(8,150))+5.0,
        #    label='Pang et al. (2014)',
           color='gray',
           linewidth=1,
           linestyle= '-')
ax[1].annotate(r'$u^{+} = y^{+}$',(6.98,7),(1.1,7),
               arrowprops=dict(facecolor='black',
               arrowstyle='->'))
ax[1].annotate(r'$u^{+} = 2.5\ln{(y^{+})}+5$',(15,11.8),(8,18),
               arrowprops=dict(facecolor='black',
               arrowstyle='->'))
ax[1].annotate('I', (2.5, 4), size='6')
ax[1].annotate('II', (11, 4), size='6')
ax[1].annotate('III', (34, 4), size='6')
ax[1].annotate('IV', (79, 4), size='6')
ax[1].vlines((5,30,50),0,17,lw=0.5)
#
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_singlePhaseValidation.pdf',
                  format='pdf')
# plt.savefig('velFluid_singlePhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE SINGLE-PHASE - RMS VELOCITIES
plt.style.use('tiny.mplstyle')
fig, ax = plt.subplots(1, 3,
                       figsize=(7.5,1.7),
                       sharex=True)
ax[0].set_ylabel(r'$u^{+}_{rms}$')
ax[0].set_xlabel(r'$y^{+}$')
ax[0].axis([0.0, 150.0, 0.0, 3.0])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
#
ax[0].yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax[0].scatter(uP_Exp0[:,0], uP_Exp0[:,1],
              s=25,
              c='white',
              marker='o',
              edgecolors='black',
              linewidths='1',
              label='Pang and Wei (2013)')
ax[0].plot(uP_0[:,0], uP_0[:,1],
           label='Present work',
           color='black',
           linewidth=1,
           linestyle='-')
ax[0].plot(uP_Gi[:,0], uP_Gi[:,1],
           label='Giusti et al. (2005)',
           color='black',
           linewidth=1,
           linestyle= '-.')
ax[0].plot(uP_YK[:,0], uP_YK[:,1],
           label='Yu e Kawaguchi (2004)',
           color='black',
           linewidth=1,
           linestyle= '--')
ax[0].plot(uP_Pa[:,0], uP_Pa[:,1],
           label='Pang et al. (2014)',
           color='black',
           linewidth=1,
           linestyle= ':')
ax[0].legend(loc='best')
#
ax[1].set_ylabel(r'$v^{+}_{rms}$')
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylim([0.0, 1.0])
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax[1].scatter(vP_Exp0[:,0], vP_Exp0[:,1],
              s=25,
              c='white',
              marker='o',
              edgecolors='black',
              linewidths='1',
              label='Pang and Wei (2013)')
ax[1].plot(vP_0[:,0], vP_0[:,1],
           label='Present work',
           color='black',
           linewidth=1,
           linestyle='-')
ax[1].plot(vP_Gi[:,0], vP_Gi[:,1],
           label='Giusti et al. (2005)',
           color='black',
           linewidth=1,
           linestyle= '-.')
ax[1].plot(vP_YK[:,0], vP_YK[:,1],
           label='Yu e Kawaguchi (2004)',
           color='black',
           linewidth=1,
           linestyle= '--')
ax[1].plot(vP_Pa[:,0], vP_Pa[:,1],
           label='Pang et al. (2014)',
           color='black',
           linewidth=1,
           linestyle= ':')
#
ax[2].set_ylabel(r'$w^{+}_{rms}$')
ax[2].set_xlabel(r'$y^{+}$')
ax[2].set_ylim([0.0, 1.2])
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.6))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.3))
ax[2].plot(wP_0[:,0], wP_0[:,1],
           label='Present work',
           color='black',
           linewidth=1,
           linestyle='-')
ax[2].plot(wP_Gi[:,0], wP_Gi[:,1],
           label='Giusti et al. (2005)',
           color='black',
           linewidth=1,
           linestyle= '-.')
ax[2].plot(wP_YK[:,0], wP_YK[:,1],
           label='Yu e Kawaguchi (2004)',
           color='black',
           linewidth=1,
           linestyle= '--')
ax[2].plot(wP_Pa[:,0], wP_Pa[:,1],
           label='Pang et al. (2014)',
           color='black',
           linewidth=1,
           linestyle= ':')
#
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_RMS_singlePhaseValidation.pdf',
            format='pdf')
# plt.savefig('velFluid_RMS_singlePhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - FLUID MEAN VELOCITY (VALIDATION)
plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$y^{+}$')
ax.set_ylabel(r'$\overline{u}^{+}$')
ax.axis([0.0, 150.0, 0.0, 20.0])
ax.xaxis.set_major_locator(plt.MultipleLocator(30))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_major_locator(plt.MultipleLocator(4))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.scatter(UP_ExpA3[:,0], UP_ExpA3[:,1],
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1',
           label='Pang and Wei (2013)')
ax.plot(UP_A3[:,0], UP_A3[:,1],
        label='Present work',
        color='black',
        linewidth=1,
        linestyle='-')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_twoPhaseValidation.pdf',
            format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - FLUID RMS VELOCITY (VALIDATION)
plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$y^{+}$')
ax.set_ylabel(r'$u^{+}_{rms}, v^{+}_{rms}$')
ax.axis([0.0, 150.0, 0.0, 2.5])
ax.xaxis.set_major_locator(plt.MultipleLocator(30))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.scatter(uP_ExpA3[:,0], uP_ExpA3[:,1],
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1',
           label='$u^{+}_{rms}$ Pang and Wei (2013)')
ax.scatter(vP_ExpA3[:,0], vP_ExpA3[:,1],
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths='1',
           label='$v^{+}_{rms}$ Pang and Wei (2013)')
ax.plot(uP_A3[:,0], uP_A3[:,1],
        label='$u^{+}_{rms}$ Present work',
        color='black',
        linewidth=1,
        linestyle='-')
ax.plot(vP_A3[:,0], vP_A3[:,1],
        label='$v^{+}_{rms}$ Present work',
        color='black',
        linewidth=1,
        linestyle='-.')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_RMS_twoPhaseValidation.pdf',
            format='pdf')
# plt.savefig('velFluid_RMS_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - FLUID MEAN VELOCITY (ALL CASES)
plt.style.use('twoSingleColumn.mplstyle')
fig, ax = plt.subplots(1, 2)
#
ax[0].axis([0, 150.0, 0.0, 20.0])
ax[0].set_xlabel(r'$y^{+}$')
ax[0].set_ylabel(r'$\overline{u}^{+}$')
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(4))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(1))
ax[0].plot(UP_0[:,0], UP_0[:,1],
           label='Single-phase',
           color='black',
           linewidth=1,
           linestyle='-')
ax[0].plot(UP_A1[:,0], UP_A1[:,1],
           label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
           color='black',
           linewidth=1,
           linestyle='-.')
ax[0].plot(UP_A2[:,0], UP_A2[:,1],
           label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
           color='black',
           linewidth=1,
           linestyle='--')
ax[0].plot(UP_A3[:,0], UP_A3[:,1],
           label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
           color='black',
           linewidth=1,
           linestyle=':')
ax[0].plot(UP_B1[:,0], UP_B1[:,1],
           label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='-.')
ax[0].plot(UP_B2[:,0], UP_B2[:,1],
           label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='--')
ax[0].plot(UP_B3[:,0], UP_B3[:,1],
           label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
           color='gray',
           linewidth=1,
           linestyle=':')
#
axins = zoomed_inset_axes(ax[0], 2, loc='center right')
axins.plot(UP_0[:,0], UP_0[:,1],
           label='Single-phase',
           color='black',
           linewidth=1,
           linestyle='-')
axins.plot(UP_A1[:,0], UP_A1[:,1],
           label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
           color='black',
           linewidth=1,
           linestyle='-.')
axins.plot(UP_A2[:,0], UP_A2[:,1],
           label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
           color='black',
           linewidth=1,
           linestyle='--')
axins.plot(UP_A3[:,0], UP_A3[:,1],
           label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
           color='black',
           linewidth=1,
           linestyle=':')
axins.plot(UP_B1[:,0], UP_B1[:,1],
           label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='-.')
axins.plot(UP_B2[:,0], UP_B2[:,1],
           label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='--')
axins.plot(UP_B3[:,0], UP_B3[:,1],
           label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
           color='gray',
           linewidth=1,
           linestyle=':')
axins.set_xlim(120, 150)
axins.set_ylim(16.5, 20)
axins.xaxis.set_visible(False)
axins.yaxis.set_visible(False)
mark_inset(ax[0], axins, loc1=1, loc2=2, fc="none", ec="0.5")
#
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylabel(r'$\overline{u}^{+}$')
ax[1].axis([0.1, 150.0, 0.0, 20.0])
ax[1].yaxis.set_major_locator(plt.MultipleLocator(4))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(1))
ax[1].semilogx(UP_0[:,0], UP_0[:,1],
               label='Single-phase',
               color='black',
               linewidth=1,
               linestyle='-')
ax[1].semilogx(UP_A1[:,0], UP_A1[:,1],
               label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
               color='black',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(UP_A2[:,0], UP_A2[:,1],
               label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
               color='black',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(UP_A3[:,0], UP_A3[:,1],
               label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
               color='black',
               linewidth=1,
               linestyle=':')
ax[1].semilogx(UP_B1[:,0], UP_B1[:,1],
               label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
               color='gray',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(UP_B2[:,0], UP_B2[:,1],
               label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
               color='gray',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(UP_B3[:,0], UP_B3[:,1],
               label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
               color='gray',
               linewidth=1,
               linestyle=':')
ax[1].annotate('I', (0.7, 4), size='6')
ax[1].annotate('II', (11, 4), size='6')
ax[1].annotate('III', (34, 4), size='6')
ax[1].annotate('IV', (79, 4), size='6')
ax[1].vlines((5,30,50),0,20,lw=0.5)
ax[1].legend(loc='best',
             fontsize=6.5)
#
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_comparisons.pdf',
            format='pdf')
# plt.savefig('velFluid_comparisons.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - BUBLE CONCENTRATION
plt.style.use('twoSingleColumn.mplstyle')
fig, ax = plt.subplots(1, 2)
#
ax[0].set_xlabel(r'$y^{+}$')
ax[0].set_ylabel('$\\alpha$ (%)')
ax[0].axis([0, 150.0, 0.0, 1.0])
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
ax[0].plot(cB_A1[:,0], cB_A1[:,1],
           label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
           color='black',
           linewidth=1,
           linestyle='-.')
ax[0].plot(cB_A2[:,0], cB_A2[:,1],
           label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
           color='black',
           linewidth=1,
           linestyle='--')
ax[0].plot(cB_A3[:,0], cB_A3[:,1],
           label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
           color='black',
           linewidth=1,
           linestyle=':')
ax[0].plot(cB_B1[:,0], cB_B1[:,1],
           label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='-.')
ax[0].plot(cB_B2[:,0], cB_B2[:,1],
           label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='--')
ax[0].plot(cB_B3[:,0], cB_B3[:,1],
           label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
           color='gray',
           linewidth=1,
           linestyle=':')
#
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylabel('$\\alpha$ (%)')
ax[1].axis([0.9, 150.0, 0.0, 1.0])
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1].semilogx(cB_A1[:,0], cB_A1[:,1],
               label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
               color='black',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(cB_A2[:,0], cB_A2[:,1],
               label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
               color='black',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(cB_A3[:,0], cB_A3[:,1],
               label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
               color='black',
               linewidth=1,
               linestyle=':')
ax[1].semilogx(cB_B1[:,0], cB_B1[:,1],
               label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
               color='gray',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(cB_B2[:,0], cB_B2[:,1],
               label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
               color='gray',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(cB_B3[:,0], cB_B3[:,1],
               label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
               color='gray',
               linewidth=1,
               linestyle=':')
ax[1].annotate('I', (2.5, 0.75), size='6')
ax[1].annotate('II', (11, 0.75), size='6')
ax[1].annotate('III', (34, 0.75), size='6')
ax[1].annotate('IV', (79, 0.75), size='6')
ax[1].vlines((5,30,50),0,1,lw=0.5)
# ax[1].legend(loc='best',
#              fontsize=6.5)
#
fig.tight_layout(pad=0.01)
plt.savefig('concBubble_comparisons.pdf',
            format='pdf')
# plt.savefig('concBubble_comparisons.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - MEAN BUBBLE VELOCITY (ALL CASES)
plt.style.use('twoSingleColumn.mplstyle')
fig, ax = plt.subplots(1, 2)
#
ax[0].set_xlabel(r'$y^{+}$')
ax[0].set_ylabel(r'$\overline{u}^{+}$')
ax[0].axis([0, 150.0, 0.0, 20.0])
ax[0].yaxis.set_major_locator(plt.MultipleLocator(4))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(1))
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
ax[0].plot(UP_B_A1[:,0], UP_B_A1[:,1],
           label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
           color='black',
           linewidth=1,
           linestyle='-.')
ax[0].plot(UP_B_A2[:,0], UP_B_A2[:,1],
           label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
           color='black',
           linewidth=1,
           linestyle='--')
ax[0].plot(UP_B_A3[:,0], UP_B_A3[:,1],
           label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
           color='black',
           linewidth=1,
           linestyle=':')
ax[0].plot(UP_B_B1[:,0], UP_B_B1[:,1],
           label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='-.')
ax[0].plot(UP_B_B2[:,0], UP_B_B2[:,1],
           label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
           color='gray',
           linewidth=1,
           linestyle='--')
ax[0].plot(UP_B_B3[:,0], UP_B_B3[:,1],
           label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
           color='gray',
           linewidth=1,
           linestyle=':')
#
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylabel(r'$\overline{u}^{+}$')
ax[1].axis([0.9, 150.0, 0.0, 20.0])
ax[1].yaxis.set_major_locator(plt.MultipleLocator(4))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(1))
ax[1].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(10))
ax[1].semilogx(UP_B_A1[:,0], UP_B_A1[:,1],
               label='A1: $\\alpha=0.1\%$, $d_b=100 \mu$m',
               color='black',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(UP_B_A2[:,0], UP_B_A2[:,1],
               label='A2: $\\alpha=0.1\%$, $d_b=200 \mu$m',
               color='black',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(UP_B_A3[:,0], UP_B_A3[:,1],
               label='A3: $\\alpha=0.1\%$, $d_b=500 \mu$m',
               color='black',
               linewidth=1,
               linestyle=':')
ax[1].semilogx(UP_B_B1[:,0], UP_B_B1[:,1],
               label='B1: $\\alpha=0.5\%$, $d_b=100 \mu$m',
               color='gray',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(UP_B_B2[:,0], UP_B_B2[:,1],
               label='B2: $\\alpha=0.5\%$, $d_b=200 \mu$m',
               color='gray',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(UP_B_B3[:,0], UP_B_B3[:,1],
               label='B3: $\\alpha=0.5\%$, $d_b=500 \mu$m',
               color='gray',
               linewidth=1,
               linestyle=':')
ax[1].annotate('I', (2.5, 4), size='6')
ax[1].annotate('II', (11, 4), size='6')
ax[1].annotate('III', (34, 4), size='6')
ax[1].annotate('IV', (79, 4), size='6')
ax[1].vlines((5,30,50),0,20,lw=0.5)
ax[1].legend(loc='best',
             fontsize=6.5)
#
fig.tight_layout(pad=0.01)
plt.savefig('velBubble_comparisons.pdf',
            format='pdf')
# plt.savefig('velBubble_comparisons.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - FLUID MEAN VELOCITY (ALL CASES) - SPACE AVERAGE
Um_CasesA = np.array([0.462, 0.461, 0.459])/0.0302353
Um_CasesB = np.array([0.512, 0.506, 0.498])/0.0302353
db = np.array([100, 200, 500])
A = np.vstack([db, np.ones(len(db))]).T
m_A, c_A = np.linalg.lstsq(A, Um_CasesA, rcond=None)[0]
m_B, c_B = np.linalg.lstsq(A, Um_CasesB, rcond=None)[0]

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$d_{b}$')
ax.set_ylabel(r'$\overline{u}^{+}$')
ax.axis([90.0, 510.0, 14.8, 17])
ax.xaxis.set_major_locator(plt.MultipleLocator(100))
ax.xaxis.set_minor_locator(plt.MultipleLocator(50))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.scatter(db, Um_CasesA,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1',
           label="Cases 'A': $\\alpha=0.1\%$")
ax.scatter(db, Um_CasesB,
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths='1',
           label="Cases 'B': $\\alpha=0.5\%$")
ax.plot(db, m_A*db + c_A,
        color='black',
        linewidth=1)
ax.plot(db, m_B*db + c_B,
        color='black',
        linewidth=1)
ax.annotate('Single-phase', (100, 14.9), size='6')
ax.hlines(0.45/0.0302353,0,550,lw=1.0,ls='-.',color='grey')
ax.legend(loc='center left')
ax.grid(True,'minor','y')
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_avgVelCompareTable.pdf',
            format='pdf')
# plt.savefig('velFluid_avgVelCompareTable.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - RMS VELOCITIES
single = []
bubble = []
plt.style.use('tiny.mplstyle')
fig, ax = plt.subplots(1, 3,
                       figsize=(7.5,1.7),
                       sharex=True)
ax[0].set_ylabel(r'$u^{+}_{rms}$')
ax[0].set_xlabel(r'$y^{+}$')
ax[0].axis([0.0, 150.0, 0.0, 3.0])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
#
ax[0].yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.5))
single += ax[0].plot(uP_0[:,0], uP_0[:,1],
                     label='Single-phase',
                     color='black',
                     linewidth=1,
                     linestyle='-')
leg1 = ax[0].legend(single, ['Single-phase'],
                    loc='best', ncol=1)
bubble += ax[0].plot(uP_A1[:,0], uP_A1[:,1],
                     label='A1',
                     color='black',
                     linewidth=1,
                     linestyle='-.')
bubble += ax[0].plot(uP_A2[:,0], uP_A2[:,1],
                     label='A2',
                     color='black',
                     linewidth=1,
                     linestyle='--')
bubble += ax[0].plot(uP_A3[:,0], uP_A3[:,1],
                     label='A3',
                     color='black',
                     linewidth=1,
                     linestyle=':')
bubble += ax[0].plot(uP_B1[:,0], uP_B1[:,1],
                     label='B1',
                     color='gray',
                     linewidth=1,
                     linestyle='-.')
bubble += ax[0].plot(uP_B2[:,0], uP_B2[:,1],
                     label='B2',
                     color='gray',
                     linewidth=1,
                     linestyle='--')
bubble += ax[0].plot(uP_B3[:,0], uP_B3[:,1],
                     label='B3',
                     color='gray',
                     linewidth=1,
                     linestyle=':')
ax[0].legend(bubble,['A1','A2','A3','B1','B2','B3'],
             loc='center right',
             bbox_to_anchor=(1,0.75),
             ncol=2)
ax[0].add_artist(leg1)
#
ax[1].set_ylabel(r'$v^{+}_{rms}$')
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylim([0.0, 1.0])
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax[1].plot(vP_0[:,0], vP_0[:,1],
           label='Single-phase',
           color='black',
           linewidth=1,
           linestyle='-')
ax[1].plot(vP_A1[:,0], vP_A1[:,1],
           label='A1',
           color='black',
           linewidth=1,
           linestyle='-.')
ax[1].plot(vP_A2[:,0], vP_A2[:,1],
           label='A2',
           color='black',
           linewidth=1,
           linestyle='--')
ax[1].plot(vP_A3[:,0], vP_A3[:,1],
           label='A3',
           color='black',
           linewidth=1,
           linestyle=':')
ax[1].plot(vP_B1[:,0], vP_B1[:,1],
           label='B1',
           color='gray',
           linewidth=1,
           linestyle='-.')
ax[1].plot(vP_B2[:,0], vP_B2[:,1],
           label='B2',
           color='gray',
           linewidth=1,
           linestyle='--')
ax[1].plot(vP_B3[:,0], vP_B3[:,1],
           label='B3',
           color='gray',
           linewidth=1,
           linestyle=':')
#
ax[2].set_ylabel(r'$w^{+}_{rms}$')
ax[2].set_xlabel(r'$y^{+}$')
ax[2].set_ylim([0.0, 1.2])
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.6))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.3))
ax[2].plot(wP_0[:,0], wP_0[:,1],
           label='Single-phase',
           color='black',
           linewidth=1,
           linestyle='-')
ax[2].plot(wP_A1[:,0], wP_A1[:,1],
           label='A1',
           color='black',
           linewidth=1,
           linestyle='-.')
ax[2].plot(wP_A2[:,0], wP_A2[:,1],
           label='A2',
           color='black',
           linewidth=1,
           linestyle='--')
ax[2].plot(wP_A3[:,0], wP_A3[:,1],
           label='A3',
           color='black',
           linewidth=1,
           linestyle=':')
ax[2].plot(wP_B1[:,0], wP_B1[:,1],
           label='B1',
           color='gray',
           linewidth=1,
           linestyle='-.')
ax[2].plot(wP_B2[:,0], wP_B2[:,1],
           label='B2',
           color='gray',
           linewidth=1,
           linestyle='--')
ax[2].plot(wP_B3[:,0], wP_B3[:,1],
           label='B3',
           color='gray',
           linewidth=1,
           linestyle=':')
#
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_RMS_two-phase.pdf',
            format='pdf')
# plt.savefig('velFluid_RMS_singlePhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
###


### FIGURE TWO-PHASE - RMS VELOCITIES - LOG SCALE
single = []
bubble = []
plt.style.use('tiny.mplstyle')
fig, ax = plt.subplots(1, 3,
                       figsize=(7.5,1.7),
                       sharex=True)
ax[0].set_ylabel(r'$u^{+}_{rms}$')
ax[0].set_xlabel(r'$y^{+}$')
ax[0].axis([0.1, 150.0, 0.0, 3.0])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
#
ax[0].yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.5))
single += ax[0].semilogx(uP_0[:,0], uP_0[:,1],
                         label='Single-phase',
                         color='black',
                         linewidth=1,
                         linestyle='-')
leg1 = ax[0].legend(single, ['Single-phase'],
                    loc='upper left', ncol=1)
bubble += ax[0].semilogx(uP_A1[:,0], uP_A1[:,1],
                         label='A1',
                         color='black',
                         linewidth=1,
                         linestyle='-.')
bubble += ax[0].semilogx(uP_A2[:,0], uP_A2[:,1],
                         label='A2',
                         color='black',
                         linewidth=1,
                         linestyle='--')
bubble += ax[0].semilogx(uP_A3[:,0], uP_A3[:,1],
                         label='A3',
                         color='black',
                         linewidth=1,
                         linestyle=':')
bubble += ax[0].semilogx(uP_B1[:,0], uP_B1[:,1],
                         label='B1',
                         color='gray',
                         linewidth=1,
                         linestyle='-.')
bubble += ax[0].semilogx(uP_B2[:,0], uP_B2[:,1],
                         label='B2',
                         color='gray',
                         linewidth=1,
                         linestyle='--')
bubble += ax[0].semilogx(uP_B3[:,0], uP_B3[:,1],
                         label='B3',
                         color='gray',
                         linewidth=1,
                         linestyle=':')
ax[0].legend(bubble,['A1','A2','A3','B1','B2','B3'],
             loc='center left',
             bbox_to_anchor=(0,0.75),
             ncol=2)
ax[0].add_artist(leg1)
#
ax[1].set_ylabel(r'$v^{+}_{rms}$')
ax[1].set_xlabel(r'$y^{+}$')
ax[1].set_ylim([0.0, 1.0])
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax[1].semilogx(vP_0[:,0], vP_0[:,1],
               label='Single-phase',
               color='black',
               linewidth=1,
               linestyle='-')
ax[1].semilogx(vP_A1[:,0], vP_A1[:,1],
               label='A1',
               color='black',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(vP_A2[:,0], vP_A2[:,1],
               label='A2',
               color='black',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(vP_A3[:,0], vP_A3[:,1],
               label='A3',
               color='black',
               linewidth=1,
               linestyle=':')
ax[1].semilogx(vP_B1[:,0], vP_B1[:,1],
               label='B1',
               color='gray',
               linewidth=1,
               linestyle='-.')
ax[1].semilogx(vP_B2[:,0], vP_B2[:,1],
               label='B2',
               color='gray',
               linewidth=1,
               linestyle='--')
ax[1].semilogx(vP_B3[:,0], vP_B3[:,1],
               label='B3',
               color='gray',
               linewidth=1,
               linestyle=':')
#
ax[2].set_ylabel(r'$w^{+}_{rms}$')
ax[2].set_xlabel(r'$y^{+}$')
ax[2].set_ylim([0.0, 1.2])
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.6))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.3))
ax[2].semilogx(wP_0[:,0], wP_0[:,1],
               label='Single-phase',
               color='black',
               linewidth=1,
               linestyle='-')
ax[2].semilogx(wP_A1[:,0], wP_A1[:,1],
               label='A1',
               color='black',
               linewidth=1,
               linestyle='-.')
ax[2].semilogx(wP_A2[:,0], wP_A2[:,1],
               label='A2',
               color='black',
               linewidth=1,
               linestyle='--')
ax[2].semilogx(wP_A3[:,0], wP_A3[:,1],
               label='A3',
               color='black',
               linewidth=1,
               linestyle=':')
ax[2].semilogx(wP_B1[:,0], wP_B1[:,1],
               label='B1',
               color='gray',
               linewidth=1,
               linestyle='-.')
ax[2].semilogx(wP_B2[:,0], wP_B2[:,1],
               label='B2',
               color='gray',
               linewidth=1,
               linestyle='--')
ax[2].semilogx(wP_B3[:,0], wP_B3[:,1],
               label='B3',
               color='gray',
               linewidth=1,
               linestyle=':')
#
fig.tight_layout(pad=0.01)
plt.savefig('velFluid_RMS_two-phase_log.pdf',
            format='pdf')
# plt.savefig('velFluid_RMS_singlePhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
###