Ent = [1,3,2,5,4]
Exe = [2,3,1,4,5]
quantum=50000
#Ent.append([1,2])
#Exe.append([1,2])
# def arquivo(arq):
#     with open(arq, 'r') as ent:
#         for l in ent:
#             Ent.append(str(l).split(';')[1])
#             Exe.append(str(l).split(';')[4].rstrip("\n"))
#             # if q !='':
#             #     quantum=q
#
# arquivo("C:\\Users\\andregoro\\PycharmProjects\\pycham\\untitled\\input.txt")

def fifo ():
	entradas = list(Ent)
	tempos = list(Exe)
	for j in range(0,5): #ORDENA COM BASE NAS ENTRADAS (DA MENOR PARA A MAIOR)
		for i in range(0,5):
			if entradas[i]>entradas[i+1]:
				Aux = entradas[i+1] #TROCA A ENTRADA
				entradas[i+1] = entradas[i]
				entradas[i] = Aux
				Aux = tempos[i+1] #TROCA O TEMPO
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
#
def entra(entradas,relogio,fila,entraram):
	for x in range(0,5): #ADICIONA OS TEMPOS QUE NÃO ENTRARAM E MENORES OU IGUAL AO RELOGIO NA FILA
		print(entradas[x])
		if entradas[x] <= relogio and entraram[x] == 0:
			print("Entrou ", x)
			entraram[x] = 1  # OS PROCESSOS QUE JÁ ENTRARAM, RECEBEM 1, ASSIM SÓ ENTRAM NOVAMENTE NA FILA EM CASO DE PREEPÇÃO
			fila.append(x)  #O PROCESSO É ADICIONADO AO FIM DA FILA
		pass
def rr ():
	entradas = list(Ent) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(Exe) # MESMA IDEIA DE CIMA
	relogio = 0
	processados = [0]*5  #CRIAMOS UMA LISTA ONDE A CADA EXECUÇÃO IREMOS INCREMENTAR O TEMPO QUE FOI EXECUTADO
	entraram = [0]*5 #CRIAMOS UMA LISTA DE 0/1 PARA SABER QUAIS PROCESSOS JA ENTRAM
	fila = [] #CRIAMOS UMA FILA, QUE IRÁ DETERMINAR QUAIS OS PROXIMOS PROCESSOS IRÃO EXECUTAR
	count = 0
	soma = 0

	entra(entradas, relogio, fila, entraram)
	for processo in fila:
		print("a")
		print("=====", processo,"======")
		falta = tempos[processo]-processados[processo]  #VARIÁVEL FALTA RECEBE O TEMPO DO PROCESSO - O QUE JÁ FOI PROCESSADO
		if falta > quantum: #SE FALTA MAIS QUE O QUANTUM ENTRA NO BLOCO
			relogio+=quantum  #RELOGIO INCREMENTA O QUANTUM, POIS IRÁ EXECUTAR TODO O TEMPO DO QUANTUM
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=quantum #INCREMENTA EM UM QUANTUM O QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			print("Executou ", processo, " até ", relogio)
			print("Sobrecarga até ", relogio+1)
			print(processo, " foi pro fim da fila")
			fila.append(processo) #COMO O PROCESSO NÃO FOI EXECUTADO TOTALMENTE, ELE VOLTA PARA O FIM DA FILA DE EXECUÇÃO
			relogio+=1 #ADIOCIONA AO RELOGIO O TEMPO DA SOBRECARGA
		elif falta <= quantum and falta > 0: #NESSE CASO VERIFICAMOS SE FALTA ALGUM TEMPO ENTRE 0 E O QUANTUM A SER EXECUTADO
			relogio+=falta #INCREMENTA O RELÓGIO O TEMPO QUE FALTA
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=falta #INCREMENTA O QUE FALTA AO QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			soma+=relogio-entradas[processo] #INCREMENTA A SOMA COM O TURNAROUND DO PROCESSO
	return float(soma/5) #RETORNA A MEDIA DOS TURNAROUND

def sjf():
	processo = list(Ent)
	tempo = list(Exe)
	tam=len(tempo)-1
	i=0
	j=0
	for j in range(0,tam): #ORDENA AS OS TEMPOS COM BASE NO TEMPO DE PROCESSO (DO MENOR PARA O MAIOR)
		for i in range(0,tam):
			if tempo[i] > tempo[i+1]:
				aux_tmp = tempo[i+1] 	#TROCA O TEMPO
				tempo[i+1] = tempo[i]
				tempo[i] = aux_tmp
				aux_tmp = processo[i+1] #TROCA A ENTRADA
				processo[i+1] = processo[i]
				processo[i] = aux_tmp
	print(processo)
	print(tempo)

rr()
