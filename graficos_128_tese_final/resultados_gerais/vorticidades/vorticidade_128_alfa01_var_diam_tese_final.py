# -*- coding: latin-1 -*-
 
#importar pacotes
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE")
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#ler os dados
#caso1
r_1, v_1 = np.loadtxt("mag_vort_mono.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
r_1 = r_1*0.030236987/(0.001/1000)
#v_1 = v_1/0.030236987
#caso2
r_2, v_2 = np.loadtxt("mag_vort_alfa01_d01.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
r_2 = r_2*0.030236987/(0.001/1000)
#v_2 = v_2

#r_7, v_7 = np.loadtxt("v_rms_alfa0.5_d1.csv",
#                      dtype='float',
#                      skiprows=0,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso2
#r_7 = r_7*(0.001/1000)/0.03
#v_7 = v_7*0.03
#caso3
r_3, v_3 = np.loadtxt("mag_vort_alfa01_d02.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
r_3 = r_3*0.030236987/(0.001/1000)
#v_3 = v_3
#caso1
r_5, v_5 = np.loadtxt("mag_vort_alfa01_d05.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
r_5 = r_5*0.030236987/(0.001/1000)
#v_5 = v_5
#caso3
#r_6, v_6 = np.loadtxt("v_rms_mono_128_dt10(-4)_novo_180000.curve",
#                      dtype='float',
#                      skiprows=2,
#                      delimiter=' ',
#                      unpack=True)
##modificar os dados do caso2
#r_6 = r_6*0.0302353/(0.001/1000)
#v_6 = v_6/0.0302353
#r_8, v_8 = np.loadtxt("v_rms_bif_alfa0.1_d0.1_90000.curve",
#                      dtype='float',
#                      skiprows=2,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso2
#r_6 = r_6*0.033385527/(0.001/1000)
#v_6 = v_6/0.033385527                     
#caso4
#r_4, v_4 = np.loadtxt("v_rms_alfa0.5_d1.csv",
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
plt.rcParams['legend.fontsize'] = 12
plt.rc('text', usetex= True)
plt.rc('text.latex', unicode= True)
#nomes nos eixos
ax.set_xlabel('$y^{+}$', fontsize=16)
ax.set_ylabel("$||\\overrightarrow{\\omega}|| \,\,\,\,\, [s^{-1}$]", fontsize=18)
#dimensao dos eixos
ax.axis([50.0, 150.0, 0.0, 60.0])
#linhas verticais no gr�fico
#plt.axvline(x=5,
#            color='Black',
#            linewidth=1,
#            linestyle=':')
#plt.axvline(x=30,
#            color='Black',
#            linewidth=1,
#            linestyle=':')
#plt.axvline(x=50,
#            color='Black',
#            linewidth=1,
#            linestyle=':')
#Escrevendo no gr�fico
#ax.annotate('I', xy=(12.5, 700), xytext=(2.0, 1050), size='16'
##            arrowprops=dict(facecolor='black', shrink=0.05),
#            )
#ax.annotate('II', xy=(12.5, 700), xytext=(12.5, 1050), size='16'
##            arrowprops=dict(facecolor='black', shrink=0.05),
#            )
#ax.annotate('III', xy=(12.5, 700), xytext=(37.0, 1050), size='16'
##            arrowprops=dict(facecolor='black', shrink=0.05),
#            )
#ax.annotate('IV', xy=(12.5, 700), xytext=(80.0, 1050), size='16'
##            arrowprops=dict(facecolor='black', shrink=0.05),
#            )
#grafico 2
#ax.plot(r_7, v_7,
#        label='$v^{+}_{rms}$ Pang e Wei (2013)',
#        color='white',
#        linewidth=2,
#        linestyle= '',
#        marker = '^',
#        markersize = 5,
#        markeredgecolor = 'black')  
#grafico 1
ax.plot(r_1, v_1,
        label='Monof�sico',
        color='Blue',
        linewidth=1,
        linestyle='-')
#grafico 2
ax.semilogx(r_2, v_2,
        label='Caso A1',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 6)                    
#grafico 3
ax.plot(r_3, v_3,
        label='Caso A2',
        color='Black',
        linewidth=1,
        linestyle=':')
#grafico 1
ax.plot(r_5, v_5,
        label='Caso A3',
        color='green',
        linewidth=1,
        linestyle='-.')
#grafico 4
#ax.plot(r_4, v_4,
#        label='$v_{rms}$ Pang e Wei (2013)',
#        color='white',
#        linewidth=2,
#        linestyle='',
#        marker = 'o',
#        markersize = 5,
#        markeredgecolor = 'black')        
#grafico 8
#ax.plot(r_8, v_8,
#        label='$v_{rms}$ Bifásico: $\\alpha = 0.1 \% \,\, d_b = 0.1 mm$',
#        color='blue',
#        linewidth=1,
#        linestyle='--')
#grafico 3
#ax.plot(r_6, v_6,
#        label='$v_{rms} \,\, \\alpha = 0.1$% $d_b = 500 \, \\mu m$',
#        color='blue',
#        linewidth=1,
#        linestyle='--')        
      
#colocar legenda
ax.legend(loc='best',
          edgecolor='k',
          fancybox=False,
          scatterpoints=1)
#ajustar espacamento
fig.tight_layout()
#salvar a figura
plt.savefig('vorticidade_alfa01_var_diam_logx_4.pdf',
            format='pdf')
plt.savefig('vorticidade_alfa01_var_diam_logx_4.png',
            format='png')
