import simpy
import random

RANDOM_SEED = 33 #Semilla
PROCESOS = 25 #Número total de procesos a simular
INTERVALO = 10.0 #Tiempo entre llegadas de procesos
CPUTIME = 1 #Tiempo que tarda la CPU en ejecutar la cantidad de instrucciones en CPUINST
CPUINST = 3 #Número de instrucciones ejecutadas por tiempo en CPUTIME
tiempos = []

def source(env, cantidad, intervalo, cpu):
    for i in range(cantidad):
        c = proceso(env, "proceso_" + str(i), cpu,random.randint(1,10) ,random.randint(1,10),CPUTIME,CPUINST)
        env.process(c)
        t = random.expovariate(1.0 / intervalo)
        yield env.timeout(t)

def proceso(env, nombre, cpu, ram, instrucciones, tiempo, instportiempo):
    created = env.now
    yield RAM.get(ram)
    while instrucciones > 0:
        with cpu.request() as req:
            yield req
            yield env.timeout(tiempo)
            instrucciones -= instportiempo
        if instrucciones > 0:
            io = random.randint(1,2)
            if io == 1:
                simulacion = random.randint(1,5)
                yield env.timeout(simulacion)

    RAM.put(ram)
    TiempoTerminar = round((env.now - created), 2)
    tiempos.append(TiempoTerminar)
    print(nombre, "created at: ", round(created, 2) ," Terminated at:", round(env.now, 2) ,"Time to terminate: ",TiempoTerminar)

random.seed(RANDOM_SEED)
env = simpy.Environment()
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env, capacity=1)

env.process(source(env, PROCESOS, INTERVALO, CPU))
env.run()
promedio = sum(tiempos) / len(tiempos)
print("Tiempo promedio en terminar: ", round(promedio, 2))