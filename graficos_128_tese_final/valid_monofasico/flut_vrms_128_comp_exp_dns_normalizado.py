#importar pacotes
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE")
import numpy as np
import matplotlib.pyplot as plt
#ler os dados
#caso1
r_1, v_1 = np.loadtxt("v_rms_mono_128_dt10(-4)_novo_180000.curve",
                      dtype='float',
                      skiprows=2,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
r_1 = r_1*0.0302353/(0.001/1000)
v_1 = v_1/0.0302353
#caso1
r_5, v_5 = np.loadtxt("giust_dns_vrms.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso1
#r_5 = r_5*0.0302353/(0.001/1000)
#v_5 = v_5/0.0302353
#caso2
r_2, v_2 = np.loadtxt("yu_vrms_64.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
#r_2 = r_2*(0.03023711/(0.001/1000)
#v_2 = v_2*0.03023711

r_7, v_7 = np.loadtxt("v_rms_alfa0.5_d1.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
#r_7 = r_7*(0.001/1000)/0.03
#v_7 = v_7*0.03
#caso3
r_3, v_3 = np.loadtxt("dns_pang_vrms.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
#r_3 = r_3*0.030487242/(0.001/1000)
#v_3 = v_3/0.030487242
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
plt.rcParams['legend.fontsize'] = 11
#nomes nos eixos
ax.set_xlabel('$y^{+}$', fontsize=16)
ax.set_ylabel("$v^{+}_{rms}$", fontsize=18)
#dimensao dos eixos
ax.axis([0.0, 150.0, 0.0, 1.0])
#grafico 2
ax.plot(r_7, v_7,
        label='$v^{+}_{rms}$ Pang e Wei (2013)',
        color='white',
        linewidth=2,
        linestyle= '',
        marker = '^',
        markersize = 5,
        markeredgecolor = 'black')  
#grafico 1
ax.plot(r_1, v_1,
        label='$v^{+}_{rms}$ Monofásico',
        color='Blue',
        linewidth=1,
        linestyle='-')
#grafico 2
ax.plot(r_2, v_2,
        label='$v^{+}_{rms}$ Yu e Kawaguchi (2004)',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 6)        
#grafico 1
ax.plot(r_5, v_5,
        label='$v^{+}_{rms}$ Giusti et al. (2005)',
        color='green',
        linewidth=1,
        linestyle='-.')             
#grafico 3
ax.plot(r_3, v_3,
        label='$v^{+}_{rms}$ Pang et al. (2014)',
        color='Black',
        linewidth=1,
        linestyle=':')
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
ax.legend(loc='lower center', scatterpoints=1)
#ajustar espacamento
fig.tight_layout()
#salvar a figura
plt.savefig('flut_vrms_comp_mono_128_dns_normalizado.pdf',
            format='pdf')
plt.savefig('flut_vrms_comp_mono_128_dns_normalizado.png',
            format='png')