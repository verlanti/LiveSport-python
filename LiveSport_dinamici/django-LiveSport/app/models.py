# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calendario(models.Model):
    campionato = models.ForeignKey('Campionati', models.CASCADE, db_column='campionato')
    giornata = models.IntegerField()
    ar = models.CharField(db_column='AR', max_length=1)  # Field name made lowercase.
    data = models.CharField(max_length=10)
    locali = models.ForeignKey('Squadre', models.CASCADE, db_column='locali',related_name='locali')
    ospiti = models.ForeignKey('Squadre', models.CASCADE, db_column='ospiti',related_name='ospiti')


    class Meta:
        managed = False
        db_table = 'Calendario'


class Campionati(models.Model):
    nome = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
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
        managed = False
        db_table = 'Squadre'
