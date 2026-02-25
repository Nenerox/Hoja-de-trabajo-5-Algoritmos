import simpy
import random

RANDOM_SEED = 3
PROCESOS = 5  #numero total de procesos
INTERVALO = 10.0  # Genera un nuevo proceso cada 10
CPUTIME = 1  # timpo en completar 3 instrucciones

def source(env, cantidad, intervalo, cpu):
    print_stats(cpu)
    for i in range(cantidad):
        c = proceso(env, 'Proceso%02d' % i, cpu,random.randint(1,10) ,random.randint(1,10), CPUTIME)
        env.process(c)
        t = random.expovariate(1.0 / intervalo)
        yield env.timeout(t)

def proceso(env, nombre, cpu, ram, instrucciones, tiempo):
    arrive = env.now
    print('%7.4f %s: new' % (arrive, nombre))
    yield RAM.get(ram)
    while instrucciones > 3:
        with cpu.request() as req:
            yield req
            print('%7.4f %s: running' % (arrive, nombre))
            if instrucciones < 3:
                yield env.timeout(tiempo)
                RAM.put(ram)
                print('%7.4f %s: Terminated' % (env.now, nombre))
            elif instrucciones >= 3:
                yield env.timeout(tiempo)
                instrucciones -= 3
        


def print_stats(res):
    print(f'{res.count} of {res.capacity} slots are allocated.')
    print(f'  running: {res.users}')
    print(f'  ready: {res.queue}')

random.seed(RANDOM_SEED)
env = simpy.Environment()
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env, capacity=1)

env.process(source(env, PROCESOS, INTERVALO, CPU))
env.run()