#importar pacotes
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE")
import numpy as np
import matplotlib.pyplot as plt
#ler os dados
#caso1
r_1, v_1 = np.loadtxt("uv_mono_128_dt10(-4)_novo_180000.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
r_1 = r_1*0.030236987/(0.001/1000)
v_1 = -v_1/(0.030236987*0.030236987)
#caso1
r_5, v_5 = np.loadtxt("uv_bif_alfa0.1_d0.5_172000.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
r_5 = r_5*0.030236987/(0.001/1000)
v_5 = -v_5/(0.030236987*0.030236987)
#caso2
r_2, v_2 = np.loadtxt("uv_alfa_0.1_d0.1_172000.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
r_2 = r_2*0.030236987/(0.001/1000)
v_2 = -v_2/(0.030236987*0.030236987)

#r_7, v_7 = np.loadtxt("uv_mono_experimental_caso_a.csv",
#                      dtype='float',
#                      skiprows=0,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso2
#r_7 = r_7*0.03/(0.001/1000)
#v_7 = v_7/(0.03*0.3)
#caso3
r_3, v_3 = np.loadtxt("uv_alfa_0.1_d0.2_172000.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
r_3 = r_3*0.030236987/(0.001/1000)
v_3 = -v_3/(0.030236987*0.030236987)
#caso3
#r_6, v_6 = np.loadtxt("v_rms_alfa_0.1_d0.1_125000.curve",
#                      dtype='float',
#                      skiprows=2,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso2
#r_6 = r_6*0.033385527/(0.001/1000)
#v_6 = v_6/0.033385527
#r_8, v_8 = np.loadtxt("v_rms_alfa0.1_d0.5_76000.curve",
#                      dtype='float',
#                      skiprows=2,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso2
#r_6 = r_6*0.033385527/(0.001/1000)
#v_6 = v_6/0.033385527                     
#caso4
#r_4, v_4 = np.loadtxt("dns_yu_2014_uv.csv",
#                      dtype='float',
#                      skiprows=0,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso4
#r_4 = r_4*(0.001/1000)/0.03
#v_4 = v_4*0.03

#criar figura
fig, ax = plt.subplots()
#nome do gráfico
plt.title('', fontsize=12)
# reduzir fonte da legenda
plt.rcParams['legend.fontsize'] = 10
plt.rc('text', usetex=True)
plt.rc('text.latex', unicode= True)
#nomes nos eixos
ax.set_xlabel('$y^{+}$', fontsize=16)
ax.set_ylabel("$-\, \\overline{u^{+}v^{+}}$", fontsize=18)
#dimensao dos eixos
ax.axis([0.0, 150.0, 0.0, 0.8])
#grafico1
#ax.plot(r_7, v_7,
#        label='$\\overline{u^{+}v^{+}}$ Exp. Pang e Wei (2013)',
#        color='white',
#        linewidth=2,
#        linestyle= '',
#        marker = '^',
#        markersize = 5,
#        markeredgecolor = 'black')
#grafico 1
ax.plot(r_1, v_1,
        label='Monofasico',
        color='blue',
        linewidth=1,
        linestyle='-')
#grafico 2
ax.plot(r_2, v_2,
        label='Caso A1',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 6)            
#grafico 3
ax.plot(r_3, v_3,
        label='Caso A2',
        color='black',
        linewidth=1,
        linestyle=':')
#grafico 1
ax.plot(r_5, v_5,
        label='Caso A3',
        color='green',
        linewidth=1,
        linestyle='-.')
#grafico 8
#ax.plot(r_8, v_8,
#        label='$v_{rms}$ Bifásico: $\\alpha = 0,1 \% \,\, d_b = 0,5 mm$',
#        color='blue',
#        linewidth=1,
#        linestyle='--')
#grafico 3
#ax.plot(r_6, v_6,
#        label='$v_{rms}$ Bifásico: $\\alpha = 0,1 \% \,\, d_b = 0,1 mm$',
#        color='green',
#        linewidth=2,
#        linestyle='-.')        
#grafico 4
#ax.plot(r_4, v_4,
#        label='$v_{rms}$ Exp. Pang e Wei (2013)',
#        color='white',
#        linewidth=4,
#        linestyle='',
#        marker = 'o',
#        markersize = 5,
#        markeredgecolor = 'black')       
#colocar legenda
ax.legend(loc='best',
          edgecolor='k',
          fancybox=False,
          scatterpoints=1)
#ajustar espacamento
fig.tight_layout()
#salvar a figura
plt.savefig('uv_comp_128_norm_alfa01_var_diam_tese_final.pdf',
            format='pdf')
plt.savefig('uv_comp_128_norm_alfa01_var_diam_tese_final.png',
            format='png')            
