Ent = []
Exe = []
quantum=50000
def arquivo(arq,q=''):
    with open(arq, 'r') as ent:
        for l in ent:
            Ent.append(str(l).split(';')[1])
            Exe.append(str(l).split(';')[4].rstrip("\n"))
            if q !='':
                quantum=q

arquivo("input.txt")

def fifo(processo):
	for j in range(0,(len(processo)+1)):
		for i in range(0,(len(processo)+1)):
			s=str(processo[j:i+1]).replace("[", "").replace("]", "").replace("'", "").replace(",", " -> ")+"  posisao "+str(i)+" "+str(j)#.replace(" ", ""))
			#if s != "" and i!=j: #and j!=0):
			print(s)
			#c=str(processo[i]).replace("[","").replace("]","").replace("'","").replace(",","->  ").replace(" ","")
			#print(c)
			#print(processo[p]+"       "+c+"       "+str(p2 )+" FOI CRIADO")
			#print(i,str(processo[1:m]).replace("[","").replace("]","").replace("'","").replace(",","->  ").replace(" ",""))

#fifo(processo)
#
def rr ():
	entradas = list(Ent) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(Exe) # MESMA IDEIA DE CIMA
	processados = [0]*(len(Ent)-1)  #CRIAMOS UMA LISTA ONDE A CADA EXECUÇÃO IREMOS INCREMENTAR O TEMPO QUE FOI EXECUTADO
	entraram = [0]*(len(Ent)-1)  #CRIAMOS UMA LISTA DE 0/1 PARA SABER QUAIS PROCESSOS JA ENTRAM
	relogio = 0
	fila = [] #CRIAMOS UMA FILA, QUE IRÁ DETERMINAR QUAIS OS PROXIMOS PROCESSOS IRÃO EXECUTAR
	count = 0
	soma = 0
	#print(relogio,entradas[1])
	def entra():
		for x in range(0,(len(Ent)-1)): #ADICIONA OS TEMPOS QUE NÃO ENTRARAM E MENORES OU IGUAL AO RELOGIO NA FILA
			if entradas[x] <= str(relogio) and entraram[x] == 0:
				print("Entrou ", x)
				entraram[x] = 1  # OS PROCESSOS QUE JÁ ENTRARAM, RECEBEM 1, ASSIM SÓ ENTRAM NOVAMENTE NA FILA EM CASO DE PREEPÇÃO
				fila.append(x)  #O PROCESSO É ADICIONADO AO FIM DA FILA
			pass
	entra()
	for processo in fila:
		#print "=====", processo, "======"
		falta = tempos[processo]-processados[processo]  #VARIÁVEL FALTA RECEBE O TEMPO DO PROCESSO - O QUE JÁ FOI PROCESSADO
		if falta > quantum: #SE FALTA MAIS QUE O QUANTUM ENTRA NO BLOCO
			relogio+=quantum #RELOGIO INCREMENTA O QUANTUM, POIS IRÁ EXECUTAR TODO O TEMPO DO QUANTUM
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=quantum #INCREMENTA EM UM QUANTUM O QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			#print "Executou ", processo, " até ", relogio
			#print "Sobrecarga até ", relogio+1
			#print processo, " foi pro fim da fila"
			fila.append(processo) #COMO O PROCESSO NÃO FOI EXECUTADO TOTALMENTE, ELE VOLTA PARA O FIM DA FILA DE EXECUÇÃO
			relogio+=1 #ADIOCIONA AO RELOGIO O TEMPO DA SOBRECARGA
		elif falta <= quantum and falta > 0: #NESSE CASO VERIFICAMOS SE FALTA ALGUM TEMPO ENTRE 0 E O QUANTUM A SER EXECUTADO
			relogio+=falta #INCREMENTA O RELÓGIO O TEMPO QUE FALTA
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=falta #INCREMENTA O QUE FALTA AO QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			soma+=relogio-entradas[processo] #INCREMENTA A SOMA COM O TURNAROUND DO PROCESSO



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

