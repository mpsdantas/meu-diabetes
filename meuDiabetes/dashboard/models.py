from django.db import models
from autentication.models import Usuario

class Parametros(models.Model):

	dias_exercicio = models.IntegerField('Dias de exercicio por semana')
	glicemia_em_jejum = models.FloatField('Glicemia em jejum (mg/mL)')
	glicemia_pos_refeicao = models.FloatField('Glicemia pos refeicao (mg/mL)')
	fuzzy_result = models.FloatField('Resultado Fuzzy')
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	created = models.DateTimeField('Criado em', auto_now_add=True)

	def __str__(self):
		return ("Resultado: " + str(self.fuzzy_result))
	
	class meta:
		verbose_name = "Parametro"
		verbose_name_plural = "Parametros"
