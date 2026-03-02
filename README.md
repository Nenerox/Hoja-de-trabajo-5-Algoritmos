# Hoja-de-trabajo-5-Algoritmos

Este proyecto implementa una simulación de ejecución de procesos utilizando la librería SimPy en Python.
Se modela un sistema con CPU y memoria RAM limitadas, donde múltiples procesos compiten por recursos y ejecutan instrucciones hasta finalizar.

La simulación representa:
- Un conjunto de procesos generados aleatoriamente.
- Posibles interrupciones de I/O en los procesos durante la ejecución.
- Un único CPU que ejecuta instrucciones por intervalos de tiempo definidos.

Cada proceso requiere:
- Una cantidad aleatoria de memoria RAM (1-10).
- Un número aleatorio de instrucciones a ejecutar (1-10).

De la simulacion se obtienen:
- Cálculo del tiempo total que tarda cada proceso en completarse.
- Cálculo del tiempo promedio de finalización.

Parametros de la simulacion base:
RANDOM_SEED = 33     # Semilla para reproducibilidad
PROCESOS = 25        # Número total de procesos a simular
INTERVALO = 10.0     # Tiempo entre llegadas de procesos
CPUTIME = 1          # Tiempo que tarda la CPU en ejecutar la cantidad de instrucciones en CPUINST
CPUINST = 3          # Número de instrucciones ejecutadas por tiempo en CPUTIME

Recursos base del sistema:
RAM total 100
CPU 1 