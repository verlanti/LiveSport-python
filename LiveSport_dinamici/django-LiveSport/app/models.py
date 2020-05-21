from django.db import models


class Calendario(models.Model):
    campionato = models.ForeignKey('Campionati', models.CASCADE, db_column='campionato')
    giornata = models.IntegerField()
    ar = models.CharField(db_column='AR', max_length=1)  # Field name made lowercase.
    data = models.CharField(max_length=10)
    locali = models.ForeignKey('Squadre', models.CASCADE, db_column='locali',related_name='locali')
    ospiti = models.ForeignKey('Squadre', models.CASCADE, db_column='ospiti',related_name='ospiti')

    class Meta:
        db_table = 'Calendario'


class Campionati(models.Model):
    nome = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Campionati'


class Risultati(models.Model):
    partita = models.ForeignKey(Calendario, models.CASCADE, db_column='partita')
    retilocali = models.IntegerField(db_column='retiLocali')  # Field name made lowercase.
    retiospiti = models.IntegerField(db_column='retiOspiti')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Risultati'


class Squadre(models.Model):
    nome = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Squadre'
