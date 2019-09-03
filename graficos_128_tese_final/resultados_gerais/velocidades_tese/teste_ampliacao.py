#importar pacotes
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE")
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#ler os dados
#caso1
r_1, v_1 = np.loadtxt("u_mono_128_dt10(-4)_novo_180000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
r_1 = r_1*0.030236987/(0.001/1000)
v_1 = v_1/0.030236987
#caso2
r_2, v_2 = np.loadtxt("u_average_alfa_0.1_d0.1_172000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
r_2 = r_2*0.030236987/(0.001/1000)
v_2 = v_2/0.030236987
#caso5
r_5, v_5 = np.loadtxt("u_average_alfa_0.1_d0.2_172000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso5
r_5 = r_5*0.030236987/(0.001/1000)
v_5 = v_5/0.030236987    
#caso6
r_6, v_6 = np.loadtxt("u_average_bif_alfa0.1_d0.5_172000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso5
r_6 = r_6*0.030236987/(0.001/1000)
v_6 = v_6/0.030236987
#caso3
#r_3, v_3 = np.loadtxt("vel_mono_log.csv",
#                      dtype='float',
#                      skiprows=0,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso3
#r_3 = r_3*(0.001/1000)/0.03
#v_3 = v_3*0.03
#caso4
#r_4, v_4 = np.loadtxt("vel_caso_b_d0.5.csv",
#                      dtype='float',
#                      skiprows=2,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso4
#r_4 = r_4*(0.001/1000)/0.03
#v_4 = v_4*0.03

#criar figura
fig, ax = plt.subplots()
#nome do gráfico
plt.title('', fontsize=16)
# reduzir fonte da legenda
plt.rcParams['legend.fontsize'] = 12
plt.rc('text', usetex=True)
plt.rc('text.latex', unicode= True)
#nomes nos eixos
ax.set_xlabel('$h \, [m]$', fontsize=16)
ax.set_ylabel("$\overline{u} \,\, [m/s]$", fontsize=16)
#dimensao dos eixos
ax.axis([0.1, 150.0, 0.0, 20.0])
#grafico 3
#ax.plot(r_3, v_3,
#        label='Exp. Pang e Wei (2013)',
#        color='white',
#        linewidth=1,
#        linestyle= '',
#        marker = 'o',
#        markersize = 5,
#        markeredgecolor = 'black',
#        markeredgewidth= 1)
#grafico 1
ax.semilogx(r_1, v_1,
        label='Monofásico',
        color='blue',
        linewidth=1,
        linestyle='-',
        marker = '',
        markersize = 2)
#grafico 2
ax.plot(r_2, v_2,
        label='Caso A1',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 1)
#grafico 5
ax.plot(r_5, v_5,
        label='Caso A2 ',
        color='black',
        linewidth=1,
        linestyle= ':',
        marker = '',
        markersize = 1)
#grafico 6
ax.plot(r_6, v_6,
        label='Caso A3',
        color='green',
        linewidth=1,
        linestyle= '-.',
        marker = '',
        markersize = 1)        
#grafico 4
#ax.plot(r_4, v_4,
#        label='cont',
#        color='green',
#        linewidth=1,
#        linestyle= '',
#        marker = 'o',
#        markersize = 5)       


axins = inset_axes(ax,
                   3.0,
                   3.0,
                   loc='center',
                   bbox_to_anchor=(1.25, 0.5),
                   bbox_transform=ax.figure.transFigure)
axins.semilogx(r_1, v_1,
        label='Monofásico',
        color='blue',
        linewidth=1,
        linestyle='-',
        marker = '',
        markersize = 2)
axins.plot(r_2, v_2,
        label='Caso A1',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 1)
axins.plot(r_5, v_5,
        label='Caso A2 ',
        color='black',
        linewidth=1,
        linestyle= ':',
        marker = '',
        markersize = 1)
axins.plot(r_6, v_6,
        label='Caso A3',
        color='green',
        linewidth=1,
        linestyle= '-.',
        marker = '',
        markersize = 1)

axins.set_xlim([1,10])
axins.set_ylim([0,8])

#colocar legenda    
ax.legend(loc='lower right', scatterpoints=1)
#ajustar espacamento
#plt.rcParams["figure.figsize"] = (3,2)
#fig.tight_layout()
#salvar a figura
plt.savefig('teste_ampliacao.pdf',
            format='pdf')
#plt.savefig('vel_comp_128_alfa0.1_var_diametro_tese_final.png',
#            format='png')