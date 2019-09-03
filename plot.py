import os
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')


### READ ALL DATA ###

### Experiment - Pang and Wei (2013)
#Single-phase flow
yP_Exp0, uP_Exp0 = np.loadtxt("graficos_artigo/vel_mono_log.csv",
                               dtype=float,
                               skiprows=0,
                               delimiter=' ',
                               unpack=True)
yP_Exp0 = -1*(yP_Exp0-300)  #'Right side' of data has better results near the wall
                            # changed '0-300' to '300-0'

### Single-phase flow - DNS
#Pang et al. (2014)
yP_Pa, uP_Pa = np.loadtxt("graficos_artigo/vel_dns_pang_norm.csv",
                          dtype=float,
                          skiprows=0,
                          delimiter=' ',
                          unpack=True)

#Giusti et al. (2005)
yP_Gi, uP_Gi = np.loadtxt("graficos_artigo/giust_dns_vel.csv",
                          dtype=float,
                          skiprows=0,
                          delimiter=' ',
                          unpack=True)

#Yu and Kawaguchi (2004)
yP_YK, uP_YK = np.loadtxt("graficos_artigo/vel_yu_2004_dns_128.csv",
                          dtype=float,
                          skiprows=0,
                          delimiter=' ',
                          unpack=True)

### Present work - Simulations
#Single-phase
yP_0, uP_0 = np.loadtxt("graficos_artigo/u_mono_128_dt10(-4)_novo_180000.curve",
                        dtype=float,
                        skiprows=2,
                        delimiter=' ',
                        unpack=True)
yP_0 = yP_0*0.0302353/(0.001/1000)
uP_0 = uP_0/0.0302353


### Figure single-phase
plt.style.use(os.path.join(os.environ['HOME'],
                           'Templates',
                           'matplotlib',
                           'singleColumn.mplstyle'))
fig, ax = plt.subplots()
# plt.rcParams['legend.fontsize'] = 10
ax.set_xlabel(r'$y^{+}$')
ax.set_ylabel(r'$u^{+}$')
ax.axis([0.0, 150.0, 0.0, 20.0])
ax.xaxis.set_major_locator(plt.MultipleLocator(30))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_major_locator(plt.MultipleLocator(4))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))

ax.scatter(yP_Exp0, uP_Exp0,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1',
           label='Pang and Wei (2013)')

ax.plot(yP_0, uP_0,
        label='Present work',
        color='black',
        linewidth=1,
        linestyle='-')

ax.plot(yP_YK, uP_YK,
        label='Yu e Kawaguchi (2004)',
        color='black',
        linewidth=1,
        linestyle= '--')

ax.plot(yP_Pa, uP_Pa,
        label='DNS Pang et al. (2014)',
        color='black',
        linewidth=1,
        linestyle= ':')

ax.plot(yP_Gi, uP_Gi,
        label='DNS Giusti et al. (2005)',
        color='black',
        linewidth=1,
        linestyle= '-.')

ax.legend(loc='lower right')
fig.tight_layout(pad=0.01)
# plt.savefig('vel_mono_comp_exp_dns.png',
#             dpi=1000,
#             format='png')