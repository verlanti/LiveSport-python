=========
LiveSport
=========

LiveSport e' un'app Django per la visualizzazione dei campionati di calcio.
E' possibile selezionare il campionato preferito, accedere alla classifica,
al calendario e alle partite di una singola squadra etc..

Documentazione dettagliata nella cartella "doc"

Installazione
-------------
 
pip3 install --user /Livesport_dinamici/django-LiveSport/dist/django-LiveSport-1.0.tar.gz

Disinstallazione
-----------------

pip3 uninstall django-LiveSport


Dipendenze
----------

Questo software ha bisogno dei seguenti pacchetti per funzionare che possono essere installati con le seguenti istruzioni in Linux:

python3 

django > 2.1 : pip3 install django
 
pymysql : pip3 install pymyslq

mysql : sudo apt install mysql-server
	
	Creare un database come descritto nel punto 0


Quick start
-----------


0. Creare il Database in mysql con le credenziali del punto 2.1. E' possibile utilizzare lo script testdb.sql

1. LiveSport usa un database mysql gia creato.
        
   2.1 Ricordarsi di creare questo utente in mysql per utilizzare l'app come segue:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'testdb',
                'USER': 'testuser',
                'PASSWORD': 'testpasswd',
                'HOST': 'localhost',
                'PORT': '',
            }
        }
    2.2 Eseguire 'python3 campionato.py *.json' per popolare il database con i dati

    2.3 Esegui `python3 manage.py migrate` per creare le app models. 

3. Far partire il server python3 manage.py runserver
    
4. Visitare http://127.0.0.1:8000/ per utilizzare l'app.
