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
r_1 = r_1*0.0302353/(0.001/1000)
v_1 = v_1/0.0302353
#caso5
r_5, v_5 = np.loadtxt("vel_dns_pang_norm.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
#r_5 = r_5*0.030549203/(0.001/1000)
#v_5 = v_5/0.030549203
#caso2
r_2, v_2 = np.loadtxt("giust_dns_vel.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
##modificar os dados do caso2
#r_2 = r_2*0.030476095/(0.001/1000)
#v_2 = v_2/0.030476095
#caso3
r_3, v_3 = np.loadtxt("vel_mono_log.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso2
#r_3 = r_3*(0.001/1000)/0.03
#v_3 = v_3*0.03
#caso4
r_4, v_4 = np.loadtxt("vel_yu_2004_dns_128.csv",
                      dtype='float',
                      skiprows=0,
                      delimiter=' ',
                      unpack=True)
#modificar os dados do caso4
#r_4 = r_4*(0.001/1000)/0.03
#v_4 = v_4*0.03

#criar figura
fig, ax = plt.subplots()
#nome do gráfico
plt.title('', fontsize=16)
# reduzir fonte da legenda
plt.rcParams['legend.fontsize'] = 10
#nomes nos eixos
ax.set_xlabel('$y^{+}$', fontsize=16)
ax.set_ylabel("$u^{+}$", fontsize=18)
#dimensao dos eixos
ax.axis([0.5,150.0, 0.0, 20.0])
#grafico 3
ax.semilogx(r_3, v_3,
        label='Pang e Wei (2013)',
        color='white',
        linewidth=1,
        linestyle= '',
        marker = 'o',
        markersize = 5,
        markeredgecolor = 'black',
        markeredgewidth= 1) 
#grafico 4
#grafico 1
ax.plot(r_1, v_1,
        label='Monofásico',
        color='blue',
        linewidth=1,
        linestyle='-',
        marker = '',
        markersize = 2)
ax.plot(r_4, v_4,
        label='DNS Yu e Kawaguchi (2004)',
        color='red',
        linewidth=1,
        linestyle= '--',
        marker = '',
        markersize = 5)         
#grafico 5
ax.plot(r_5, v_5,
        label='DNS Pang et al. (2014)',
        color='black',
        linewidth=1,
        linestyle= ':',
        marker = '',
        markersize = 1)        
#grafico 2
ax.plot(r_2, v_2,
        label='DNS Giusti et al. (2005)',
        color='green',
        linewidth=1,
        linestyle= '-.',
        marker = '',
        markersize = 2)
      
#colocar legenda
ax.legend(loc='upper left', scatterpoints=1)
#ajustar espacamento
fig.tight_layout()
#salvar a figura
plt.savefig('vel_mono_comp_exp_dns_semilog.pdf',
            format='pdf')
plt.savefig('vel_mono_comp_exp_dns_semilog.png',
            format='png')