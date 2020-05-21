import re

from django.shortcuts import render
from django.views import generic
from .models import Campionati, Calendario, Squadre


class IndexView(generic.TemplateView):
    template_name = 'app/index.html'


class CampionatoView(generic.ListView):
    template_name = 'app/campionato.html'
    context_object_name = 'campionati_list'

    def get_queryset(self):
        """Ritorna tutti i campionati in ordine di id."""
        return Campionati.objects.order_by('id')[:Campionati.objects.count()]


class CalendarioView(generic.ListView):
    template_name = 'app/calendario.html'
    model = Calendario
    context_object_name = 'calendario_list'

    def post(self, request, *args, **kwargs):
        """La funzione post gestisce l'interazione dell'utente con il selettore \
           di giornata"""
        """Argomenti passati al template: \
                single_giornata_list: ritorna le partite della giornata scelta dall'utente
                giornata_list: ritorna le partite per giornata_list
                campionato_id: ritorna l'id del campionato"""
        """request.POST['giornata'])[1],ar= re.split('(\d+|\D+)',request.POST['giornata'])[3] \
            viene utilizzata la funzione split per dividere la stringa esempio "1A" per ricavare \
            la giornata scelta dall'utente """
        """Calendario.objects.filter(campionato = kwargs['pk']) \
           parametro passato sempre kwargs['pk'] per dividere le squadre di due \
           campionati differenti"""

        context = {
            'single_giornata_list':
                Calendario.objects.select_related().filter(campionato=kwargs['pk']).filter(
                    giornata=re.split('(\d+|\D+)', request.POST['giornata'])[1],
                    ar=re.split('(\d+|\D+)', request.POST['giornata'])[3]),
            'giornata_list': Calendario.objects.filter(campionato=kwargs['pk']).order_by('id')[::10],
            'campionato_id': Calendario.objects.select_related().filter(giornata=1, ar='A')[0].campionato.id}

        return render(request, 'app/calendario.html', context)

    def get(self, request, *args, **kwargs):
        """La funzione get gestisce la GET request"""
        """Argomenti passati al template: \
                single_giornata_list: ritorna le partite della prima giornata
                giornata_list: ritorna le partite per giornata_list
                campionato_id: ritorna l'id del campionato"""

        context = {
            'single_giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).filter(giornata=1, ar='A'),
             'giornata_list': Calendario.objects.filter(campionato=kwargs['pk']).order_by('id')[::10],
             'campionato_id': kwargs['pk']
        }
        return render(request, 'app/calendario.html', context)


###########CalendarioAllView#######################################################

class CalendarioAllView(generic.ListView):
    template_name = 'app/calendarioall.html'
    model = Calendario
    context_object_name = 'calendario_list'

    def get(self, request, *args, **kwargs):
        """La funzione get gestisce la GET request"""
        """Argomenti passati al template: \
                single_giornata_list: ritorna le partite della prima giornata
                giornata_list: ritorna tutte le partite
                campionato_id: ritorna l'id del campionato"""

        context = {'single_giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).filter(
            giornata=1, ar='A'),
                   'giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).order_by('id'),
                   'campionato_id': kwargs['pk']
                   }
        return render(request, 'app/calendarioall.html', context)


#################################################################################


def team_list(campionato_id):
    """funzione che ritorna la lista delle squadre presenti nel campionato"""
    squadre = []
    id_team = Squadre.objects.order_by('id')
    for s in Calendario.objects.filter(campionato=campionato_id).filter(giornata=1, ar='A'):
        for i in id_team:
            if s.locali.nome == i.nome:
                squadre.append((i.id, s.locali.nome))
            if s.ospiti.nome == i.nome:
                squadre.append((i.id, s.ospiti.nome))

    return squadre


def calc_classifica(campionato_id, squadre):
    """funzione che calcola la classifica e ritorna una lista ordinata di tuple con il
    calcolo per ogni squadra del campionato_id"""
    classifica = []
    vinte = 0
    perse = 0
    golfatti = 0
    golsubiti = 0
    partite = Calendario.objects.select_related().filter(campionato=campionato_id).order_by('id')

    for s in squadre:
        for p in partite:
            if p.locali.nome == s[1]:
                for i in p.risultati_set.all():
                    golfatti += i.retilocali
                    golsubiti += i.retiospiti

                    if i.retilocali > i.retiospiti:
                        vinte += 1
                    elif i.retilocali < i.retiospiti:
                        perse += 1
            elif p.ospiti.nome == s[1]:
                for i in p.risultati_set.all():
                    golfatti += i.retiospiti
                    golsubiti += i.retilocali

                    if i.retilocali < i.retiospiti:
                        vinte += 1
                    elif i.retilocali > i.retiospiti:
                        perse += 1
        ### 0.squadrenome,1.vinte,2.pareggiate,3.perse,4.golfatti, 5.golsubiti,6.diffReti,7. Punti
        classifica.append((s[1], vinte, 38 - vinte - perse, perse, golfatti, golsubiti, golfatti - golsubiti,
                           vinte * 3 + 38 - vinte - perse))
        vinte = 0
        perse = 0
        golfatti = 0
        golsubiti = 0
    return sorted(classifica, key=lambda tup: -tup[7])


###########ClassificaView#######################################################

class ClassificaView(generic.ListView):
    template_name = 'app/classifica.html'
    model = Calendario

    def get(self, request, *args, **kwargs):
        """GET request"""
        """Argomenti passati al template: \
            classifica: ritorna la lista classifica dalla funzione calc_classifica \
            team_list: ritorna tutte le squadre del campionato_id \
            campionato_id: ritorna l'id del campionato"""

        context = {'classifica': calc_classifica(kwargs['pk'], team_list(kwargs['pk'])),
                   'team_list': team_list(kwargs['pk']),
                   'campionato_id': Calendario.objects.select_related().filter(giornata=1, ar='A')[0].campionato.id
                   }
        return render(request, 'app/classifica.html', context)


###########SchedinaView#########################################################

class SchedinaView(generic.ListView):
    template_name = 'app/schedina.html'
    model = Calendario

    def post(self, request, *args, **kwargs):
        """La funzione post gestisce l'interazione dell'utente con il selettore \
                di giornata"""
        """Argomenti passati al template: \
                single_giornata_list: ritorna le partite della giornata scelta dall'utente \
                giornata_list: ritorna le partite per giornata_list \
                campionato_id: ritorna l'id del campionato"""
        context = {'single_giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).filter(
            giornata=re.split('(\d+|\D+)', request.POST['giornata'])[1],
            ar=re.split('(\d+|\D+)', request.POST['giornata'])[3]),
                   'giornata_list': Calendario.objects.filter(campionato=kwargs['pk']).order_by('id')[::10],
                   'campionato_id': Calendario.objects.select_related().filter(giornata=1, ar='A')[0].campionato.id
                   }
        return render(request, 'app/schedina.html', context)

    def get(self, request, *args, **kwargs):
        """La funzione get gestisce la GET request"""
        """Argomenti passati al template: \
                    single_giornata_list: ritorna le partite della prima giornata \
                    giornata_list: ritorna le partite per giornata_list \
                    campionato_id: ritorna l'id del campionato"""
        context = {
            'giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).order_by('id')[::10],
            'single_giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).filter(
                giornata=1, ar='A'),
            'campionato_id': Calendario.objects.select_related().filter(giornata=1, ar='A')[0].campionato.id}
        return render(request, 'app/schedina.html', context)


def match_team(campionato_id):
    """Questa funzione ritorna una lista ordinata di tuple con tutte le partite di \
    tutte le squadre """
    partite = []
    for i in Calendario.objects.select_related().filter(campionato=campionato_id).order_by('id'):
        for p in i.risultati_set.all():
            partite.append(
                (p.partita.id, i.giornata, i.ar, i.data, i.locali.nome, i.ospiti.nome, p.retilocali, p.retiospiti))

    return sorted(partite, key=lambda tup: tup[0])


###########SquadraView##########################################################

class SquadraView(generic.ListView):
    template_name = 'app/squadra.html'

    def get(self, request, *args, **kwargs):
        """La funzione get gestisce la GET request"""
        """Argomenti passati al template: \
                match_team: ritorna la lista di tuple della def match_team() \
                statistica_team: calcola la classifica e ritorna una lista (ved calc_classifica) \
                single_giornata_list: ritorna la prima giornata del campionato_id \
                team_list: ritorna la lista di tutte le squadre del model Squadre  """

        context = {'match_team': match_team(kwargs['pk']),
                   'statistica_team': calc_classifica(kwargs['pk'], team_list(kwargs['pk'])),
                   'single_giornata_list': Calendario.objects.select_related().filter(campionato=kwargs['pk']).filter(
                       giornata=1, ar='A'),
                   'team_list': Squadre.objects.order_by('id')[kwargs['id_squadra'] - 1]
                   }
        return render(request, 'app/squadra.html', context)
