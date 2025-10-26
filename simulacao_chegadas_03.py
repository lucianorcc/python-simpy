'''
UFS - UNIVERSIDADE FEDERAL DE SERGIPE
PROCC - Pós-Graduação em Ciência da Computação
Disciplina: AVALIAÇÃO DE DESEMPENHO DE SISTEMAS COMPUTACIONAIS
Algoritmo desenvolvido pelo o Professor Dr. RUBENS DE SOUZA MATOS JUNIOR

Algoritmo de Simulação com configuração de tempo entre chegadas

'''

import simpy
import random

global fila

def cliente(env, caixa):
    for i in range(20):
       env.process(servico(env, f'Cliente{i}', caixa))
       tempoChegada = random.expovariate(1.0)
       print(f'Tempo para próxima chegada: {tempoChegada:.2f}')
       yield env.timeout(tempoChegada)


def servico(env, nome, caixa):
    global fila
    chegada = env.now
    print(f'{nome} chegou em {chegada:.2f}')
    fila+=1
    print(f'Tamanho da fila: {fila}')
    with caixa.request() as req:
        yield req
        espera = env.now - chegada
        print(f'{nome} esperou {espera:.2f}')
        fila-=1
        tempoServico = random.expovariate(2.0)
        print(f'Serviço: {tempoServico:.2f}')
        yield env.timeout(tempoServico)

fila = 0
env = simpy.Environment()
caixa = simpy.Resource(env, capacity=2)
env.process(cliente(env,caixa))

env.run()
