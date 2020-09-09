from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    CHOICES_ANSWER = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )
    question = models.TextField(verbose_name="Pregunta")
    option_a = models.CharField(max_length=250, verbose_name="Opción A")
    option_b = models.CharField(max_length=250, verbose_name="Opción B")
    option_c = models.CharField(max_length=250, verbose_name="Opción C")
    option_d = models.CharField(max_length=250, verbose_name="Opción D")
    correct_answer = models.CharField(max_length=5, choices=CHOICES_ANSWER, verbose_name="Respuesta correcta")

    class Meta:
        ordering = ['id']
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.question

class Score(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Usuario")
    time = models.TimeField(verbose_name="Tiempo", auto_now=False, auto_now_add=False)
    score = models.IntegerField(verbose_name="Puntuación")
    # Comodines
    call_friend = models.BooleanField(verbose_name="LLamar a un amigo", default=False)
    audience = models.BooleanField(verbose_name="Consultar a la audiencia", default=False)
    fifty_fifty = models.BooleanField(verbose_name="50-50", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def username(self):
        return self.user.username
    username.short_description = 'Usuario'

    class Meta:
        ordering = ['score']
        verbose_name = 'Puntuación'
        verbose_name_plural = 'Puntuaciones'

    def __str__(self):
        return str(self.score)


class Prize(models.Model):
    amount = models.IntegerField(verbose_name="Monto", null=False, blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Premio'
        verbose_name_plural = 'Premios'

    def __str__(self):
        return str(self.amount)
