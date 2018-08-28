# ***** Aqui esta localizado a funcao de retorno
import numpy as np
import skfuzzy as fuzz

def fuzzifier(exercicio, glicemia_jejum, glicemia_pos):

	# Generate universe variables
	#   * Quality and service on subjective ranges [0, 10]
	#   * Tip has a range of [0, 25] in units of percentage points
	exercicio = int(exercicio)
	glicemia_jejum = int(glicemia_jejum)
	glicemia_pos = int(glicemia_jejum)

	exercicio = int((exercicio*300)/7)
	
	x_exercicios = np.arange(0, 301, 1) # Dias de exercicio por semana [0,7]
	x_glicemia_jejum = np.arange(0, 301, 1) # Glicemia em jejum [0,300]
	x_glicemia_pos  = np.arange(0, 301, 1) # Glicemia pos refeicao [0,300]
	x_saida = np.arange(0,101,1) # saida em porcento 

	
	# Generate fuzzy membership functions
	exercicio_baixo = fuzz.trimf(x_exercicios, [0, 64, 128])
	exercicio_normal = fuzz.trimf(x_exercicios, [85, 150, 214])
	exercicio_alto = fuzz.trimf(x_exercicios, [171, 235, 300])
	glicemia_jejum_baixo = fuzz.trimf(x_glicemia_jejum, [0, 45, 90])
	glicemia_jejum_normal = fuzz.trimf(x_glicemia_jejum, [70, 105, 140])
	glicemia_jejum_alto = fuzz.trimf(x_glicemia_jejum, [120, 210, 300])
	glicemia_pos_baixo = fuzz.trimf(x_glicemia_pos, [0, 50, 100])
	glicemia_pos_normal = fuzz.trimf(x_glicemia_pos, [80, 100, 120])
	glicemia_pos_alto = fuzz.trimf(x_glicemia_pos, [100, 150, 300])
	saida_pouco_provavel = fuzz.trimf(x_saida, [0, 25, 50])
	saida_provavel = fuzz.trimf(x_saida, [30, 50, 70])
	saida_muito_provavel = fuzz.trimf(x_saida, [60, 85, 100])

	# We need the activation of our fuzzy membership functions at these values.
	# The exact values 6.5 and 9.8 do not exist on our universes...
	# This is what fuzz.interp_membership exists for!
	exercicio_level_baixo = fuzz.interp_membership(x_exercicios, exercicio_baixo, exercicio)
	exercicio_level_normal = fuzz.interp_membership(x_exercicios, exercicio_normal, exercicio)
	exercicio_level_alto = fuzz.interp_membership(x_exercicios, exercicio_alto, exercicio)

	glicemia_jejum_level_baixo = fuzz.interp_membership(x_glicemia_jejum, glicemia_jejum_baixo, glicemia_jejum)
	glicemia_jejum_level_medio = fuzz.interp_membership(x_glicemia_jejum, glicemia_jejum_normal, glicemia_jejum)
	glicemia_jejum_level_alto = fuzz.interp_membership(x_glicemia_jejum, glicemia_jejum_alto, glicemia_jejum)

	glicemia_pos_level_baixo = fuzz.interp_membership(x_glicemia_pos, glicemia_pos_baixo, glicemia_pos)
	glicemia_pos_level_medio = fuzz.interp_membership(x_glicemia_pos, glicemia_pos_normal, glicemia_pos)
	glicemia_pos_level_alto = fuzz.interp_membership(x_glicemia_pos, glicemia_pos_alto, glicemia_pos)


	# ---------------------- REGRAS DE DECISAO -------------------------------------------- 
	# Se glicemia em jejum for alto OR glicemia pos refeicao alto, entao e muito provavel
	saida_mp = np.fmin(np.fmin(glicemia_jejum_level_alto, glicemia_pos_level_alto), saida_muito_provavel)

	# Se glicemia em jejum for alta OR glicemia pos refeicao for alto AND exercicio for baixo => p
	saida_p = np.fmin(
		np.fmin(np.fmax(glicemia_jejum_level_alto, glicemia_pos_level_alto),
			exercicio_level_baixo), saida_provavel)

	# Se glicemia em jejum for medio OR glicemia baixo AND pos for medio => pp
	saida_pp = np.fmin(
		np.fmin(np.fmax(glicemia_jejum_level_medio,glicemia_jejum_level_baixo), 
			glicemia_pos_level_medio), saida_pouco_provavel)
	

	# ---------------- FIM DAS REGRAS DE DECISAO ---------------------------------------------

	# Aggregate all three output membership functions together
	aggregated = np.fmax(saida_pp, np.fmax(saida_p, saida_mp))

	

	# som ou centroid sao as melhores opcoes
	#result = fuzz.defuzz(x_saida, aggregated, 'som') 
	result = fuzz.defuzzify.dcentroid(x_saida, aggregated, 61.4)

	return result