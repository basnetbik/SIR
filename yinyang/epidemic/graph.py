import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as pp
import json
import re

param = {'HIV':(0.0000003,0,0.01), 'swine_flu':(0.000003,0.2,0), 'cholera':(0.000002,0.1,0.01)}

def eq_system(state, t, beta, gamma, mu):
   '''Defining SIR System of Equations'''
   Eqs = np.zeros((4))
   Eqs[0] = -beta * state[0]*state[1]
   Eqs[1] = beta * state[0]*state[1] - gamma*state[1] - mu*state[1]
   Eqs[2] = gamma*state[1]
   Eqs[3] = mu*state[1]
   return Eqs

def plot(pop, infected, vaccinated, district, epidemic_name):
    S0 = pop-infected-vaccinated
    I0 = infected
    R0 = 0
    D0 = 0
    startPop = (S0, I0, R0, D0)
    days = 40
    t_interval = np.arange(0,days, 0.02)
    beta, gamma, mu = param[epidemic_name]
    SIR = spi.odeint(eq_system, startPop, t_interval, args=(beta, gamma, mu))
    n = SIR.shape[0]
    sh = 20
    for i in range(1,sh):
        index = int(1./sh *i*n)
        pp.figure()
        pp.plot([days],[0])
        pp.plot(t_interval[0:index],SIR[:,0][0:index],'r',label = 'Susceptable')
        pp.plot(t_interval[0:index], SIR[:,1][0:index],'g', label = 'Infected')
        pp.plot(t_interval[0:index], SIR[:,2][0:index],'b', label = 'Recovered')
        pp.plot(t_interval[0:index], SIR[:,3][0:index],'k', label = 'Dead')
        if (epidemic_name != "HIV"):
            pp.xlabel("Number of Days")
        else:
            pp.xlabel("Number of Years")
        pp.ylabel("Population")
        pp.title("Epidemic progression of %s in %s" % (epidemic_name, district))
        pp.legend()
        # pp.show()
        filename = "templates/img/graph%.2d.png"%i
        pp.savefig(filename)


    data = open("templates/backup.js",'r').read()[9:-1]
    data = data.replace(r"'",'"')
    n = json.loads(data.replace(r"\\'","'"))
    n[district] = int(max(SIR[:,1]))
    t = "var data="+json.dumps(n)+";"+"var population=%d;var recovered=%d;var dead=%d;"%(pop,SIR[-1,2],SIR[-1,3])
    open("templates/data.js",'w').write(t.replace('"',"'"))
    return




def gen_graph(district, infected, vaccinated, epidemic_name, districts, population):
    pop = int(population[list(districts).index(district)][1:-1])
    plot(pop, infected,vaccinated, district, epidemic_name)

    pass


