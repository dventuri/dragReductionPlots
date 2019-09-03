#importar pacotes
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE")
import numpy as np
import matplotlib.pyplot as plt
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
r_2, v_2 = np.loadtxt("u_bolha_average_bif_alfa0.5_d0.1_172000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
r_2 = r_2*0.030236987/(0.001/1000)
v_2 = v_2/0.030236987
#caso5
r_5, v_5 = np.loadtxt("u_bolha_average_bif_alfa0.5_d0.2_180000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso 5
r_5 = r_5*0.030236987/(0.001/1000)
v_5 = v_5/0.030236987
#caso5
r_6, v_6 = np.loadtxt("u_bolha_average_bif_alfa0.5_d0.5_172000.curve",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso 5
r_6 = r_6*0.030236987/(0.001/1000)
v_6 = v_6/0.030236987
#caso3
#r_3, v_3 = np.loadtxt("vel_mono_log.csv",
#                      dtype='float',
#                      skiprows=0,
#                      delimiter=' ',
#                      unpack=True)
#modificar os dados do caso2
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
#nomes nos eixos
ax.set_xlabel('$y^{+}$', fontsize=16)
ax.set_ylabel("$u_b^{+}$", fontsize=16)
#dimensao dos eixos
ax.axis([0.9, 150.0, 0.0, 21.0])
#linhas verticais no gráfico
plt.axvline(x=5,
            color='Black',
            linewidth=1,
            linestyle=':')
plt.axvline(x=30,
            color='Black',
            linewidth=1,
            linestyle=':')
plt.axvline(x=50,
            color='Black',
            linewidth=1,
            linestyle=':')
#Escrevendo no gráfico
ax.annotate('I', xy=(12.5, 17.5), xytext=(4.2, 18.0), size='16'
#            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('II', xy=(12.5, 17.5), xytext=(12.5, 18.0), size='16'
#            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('III', xy=(12.5, 17.5), xytext=(37.0, 18.0), size='16'
#            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('IV', xy=(12.5, 17.5), xytext=(120.0, 18.0), size='16'
#            arrowprops=dict(facecolor='black', shrink=0.05),
            )
#grafico 3
#ax.semilogx(r_3, v_3,
#        label='Exp. Pang e Wei (2013)',
#        color='white',
#        linewidth=1,
#        linestyle= '',
#        marker = 'o',
#        markersize = 5,
#        markeredgecolor = 'black',
#        markeredgewidth= 1) 
#grafico 4
#grafico 1
ax.plot(r_1, v_1,
        label='Monofásico',
        color='blue',
        linewidth=1,
        linestyle='-',
        marker = '',
        markersize = 1)
#grafico 2
ax.semilogx(r_2, v_2,
        label='Caso B1',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 1)        
#grafico 5
ax.plot(r_5, v_5,
        label='Caso B2',
        color='black',
        linewidth=1,
        linestyle= ':',
        marker = '',
        markersize = 1)
#grafico 6
ax.plot(r_6, v_6,
        label='Caso B3',
        color='green',
        linewidth=1,
        linestyle= '-.',
        marker = '',
        markersize = 1)        
#ax.plot(r_4, v_4,
#        label='cont',
#        color='green',
#        linewidth=1,
#        linestyle= '',
#        marker = 'o',
#        markersize = 5)       
#colocar legenda
ax.legend(loc='lower right',
          edgecolor='k',
          fancybox=False,
          scatterpoints=1)
#ajustar espacamento
fig.tight_layout()
#salvar a figura
#plt.savefig('vel_bolhas_alfa05_var_diametro_normlizada_tese_final.pdf',
#            format='pdf')
#plt.savefig('vel_bolhas_alfa05_var_diametro_normlizada_tese_final.png',
#            format='png')