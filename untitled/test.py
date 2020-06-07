tempo_total = 0
tempo_espera_rr = []
tempo_resposta_rr = []
tempo_retorno_rr = []

#Os processos
global num_processos
num_processos = 0
processos = []
processos.append([])
processos.append([])
processos_sjf =[]
processos_sjf.append([])
processos_sjf.append([])
processos_sjf_aux =[]
processos_sjf_aux.append([])
processos_sjf_aux.append([])
#Chegada e Duração CONSTANTES NÃO ALTERAR
CHEGADA = 0
DURACAO = 1
def rr():
	tempo_med_retorno = 0
	tempo_med_resposta = 0
	tempo_med_espera = 0
	global tempo_total
	global tempo_resposta_rr
	tempo_total = 0
	fim = 0
	fila = []
	quantum = 2
	primeiro = -1

	chegada_inicial = []
	for x in range(num_processos):
		chegada_inicial.append(processos[CHEGADA][x])
		pass
	#print(len(fila))
	while fim < num_processos:
		for x in range(num_processos):
			if processos[CHEGADA][x] <= tempo_total and processos[CHEGADA][x] != -1 and x != primeiro:
				if len(fila) == 0:
					fila.append(x)
					pass
				else:
					num	= 0
					for y in range(len(fila)):
						if fila[y] == x:
							num = 0
							break
							pass
						num = 1
						pass
					if num ==  1:
						fila.append(x)
						pass
				pass	
			pass
		if primeiro != -1:
			if processos[CHEGADA][primeiro] <= tempo_total and processos[CHEGADA][primeiro] != -1:
				fila.append(primeiro)
				pass
			pass
		if len(fila) == 0:
			tempo_total+=1
			continue
			pass
		primeiro = fila[0]

		tempo_espera_rr[primeiro] += tempo_total - processos[CHEGADA][primeiro]
		if tempo_resposta_rr[primeiro] == -1:
			tempo_resposta_rr[primeiro] = tempo_total - processos[CHEGADA][primeiro]
			pass
		cont = 0
		while processos[DURACAO][primeiro] != 0:
			cont+=1
			tempo_total+=1
			processos[DURACAO][primeiro] = processos[DURACAO][primeiro] - 1
			if  cont == 2:
				break
				pass
			pass
		processos[CHEGADA][primeiro] = tempo_total
		if processos[DURACAO][primeiro] == 0:
			tempo_retorno_rr[primeiro] = tempo_total - chegada_inicial[primeiro]
			fim+=1
			processos[CHEGADA][primeiro] = -1
			pass
		del fila[0]
		pass

	for x in range(num_processos):
		tempo_med_resposta += tempo_resposta_rr[x]
		tempo_med_retorno += tempo_retorno_rr[x]
		tempo_med_espera += tempo_espera_rr[x]
		pass	
	tempo_med_espera = tempo_med_espera / num_processos
	tempo_med_retorno = tempo_med_retorno / num_processos
	tempo_med_resposta = tempo_med_resposta / num_processos
	print('RR', round(tempo_med_retorno,1), round(tempo_med_resposta,1), round(tempo_med_espera,1))

	pass