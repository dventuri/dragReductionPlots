import os
import numpy as np
import matplotlib.pyplot as plt
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
UP_A3 = np.loadtxt("graficos_artigo/u_average_bif_alfa0.1_d0.5_172000.curve",
                   dtype=float,
                   skiprows=2,
                   delimiter=' ')
UP_A3[:,0] = UP_A3[:,0]*0.0302353/(0.001/1000)
UP_A3[:,1] = UP_A3[:,1]/0.0302353

### ###


### FIGURE SINGLE-PHASE - MEAN VELOCITY
plt.style.use(os.path.join(os.environ['HOME'],
                           'Templates',
                           'matplotlib',
                           'singleColumn.mplstyle'))
fig, ax = plt.subplots()
ax.set_xlabel(r'$y^{+}$')
ax.set_ylabel(r'$u^{+}$')
ax.axis([0.0, 150.0, 0.0, 20.0])
ax.xaxis.set_major_locator(plt.MultipleLocator(30))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_major_locator(plt.MultipleLocator(4))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.scatter(UP_Exp0[:,0], UP_Exp0[:,1],
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1',
           label='Pang and Wei (2013)')
ax.plot(UP_0[:,0], UP_0[:,1],
        label='Present work',
        color='black',
        linewidth=1,
        linestyle='-')
ax.plot(UP_Gi[:,0], UP_Gi[:,1],
        label='Giusti et al. (2005)',
        color='black',
        linewidth=1,
        linestyle= '-.')
ax.plot(UP_YK[:,0], UP_YK[:,1],
        label='Yu e Kawaguchi (2004)',
        color='black',
        linewidth=1,
        linestyle= '--')
ax.plot(UP_Pa[:,0], UP_Pa[:,1],
        label='Pang et al. (2014)',
        color='black',
        linewidth=1,
        linestyle= ':')
ax.legend(loc='lower right')
fig.tight_layout(pad=0.01)
# plt.savefig('vel_mono_comp_exp_dns.png',
#             dpi=1000,
#             format='png')
###


### FIGURE SINGLE-PHASE - RMS VELOCITIES
plt.style.use(os.path.join(os.environ['HOME'],
                           'Templates',
                           'matplotlib',
                           'tiny.mplstyle'))
fig, ax = plt.subplots(1, 3,
                       figsize=(7.5,1.7),
                       sharex=True)
ax[0].set_ylabel(r'$u^{+}$')
ax[0].axis([0.0, 150.0, 0.0, 3.0])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(30))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(10))
#
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
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
ax[2].set_ylim([0.0, 1.2])
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
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
# plt.savefig('velRMS_mono_comp_exp_dns.png',
#             dpi=1000,
#             format='png')
###

### FIGURE TWO-PHASE - MEAN VELOCITY
plt.style.use(os.path.join(os.environ['HOME'],
                           'Templates',
                           'matplotlib',
                           'singleColumn.mplstyle'))
fig, ax = plt.subplots()
ax.set_xlabel(r'$y^{+}$')
ax.set_ylabel(r'$u^{+}$')
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
# plt.savefig('vel_mono_comp_exp_dns.png',
#             dpi=1000,
#             format='png')
###
