:og:title: Plugin d'esempio

:og:description: Un semplice ma efficace plugin di esempio da poter scaricare e modificare a piacimento.





Test Plugin
===========

Un semplice plugin d’esempio per Dalamud.

Non è stato pensato per essere per essere il più semplice possibile ma è
stato pensato per cercare di coprire tutto quello che potresti fare con
Dalamud.

Punti focali
------------

-  Plugin semplice ma funzionale

   -  Comandi testuali “/nomecomando”
   -  UI
   -  Ui delle Impostazioni
   -  Visualizzazione Immagini
   -  File Json
   -  Ambiente WindowsFree® (grazie ai nostri
      `DevContainer <https://docker.ffxivita.it/esempi/devcontainer>`__)

La nostra intenzione è mostrare come sono sviluppati i nostri plugin.
Niente di più, niente di meno.

Prossimi Passi
--------------

Compilazione
~~~~~~~~~~~~

1. Apri il file TestPlugin.sln nel tuo editor C# preferito (`Visual
   Studio Code <https://code.visualstudio.com>`__ (se vuoi usare i
   devcontainer) o `JetBrains
   Rider <https://www.jetbrains.com/rider/>`__)
2. Compila il progetto. Di default verrà selezionata la modalità di
   Debug ma potrai cambiare nella modalità Release in qualsiasi momento.
3. Il plugin compilato potrà essere trovato in questa posizione:
   ``TestPlugin/bin/x64/Debug/TestPlugin.dll`` (o Release, se usata
   quella modalità)

Usalo in Game
~~~~~~~~~~~~~

**Qui hai sostanzialmente due strade**:

1. Cartella Dev

    - Apri il gioco e usa il comando ``/xlsettings`` nella finestra di chat o ``xlsettings``
       se sei nella console Dalamud, in modo da aprire le impostazioni.
    - Vai alla voce ``Experimental`` o ``Sperimentale`` (dipende dalla lingua in
      cui hai configurato Dalamud) e alla voce Dev Plugin Locations inserisci
      il percorso completo al file TestPlugin.dll .
    - Ora usa il comando ``/xlplugins`` se sei nella finestra di chat o il comando ``xlplugins``
      se sei dentro la console di Dalamud per aprire l’installatore di Plugin.
    - Vai alla voce ``Dev Tools`` e infine alla voce
      ``Installed Dev Plugins`` . Il TestPlugin dovrebbe essere visbile. **Attivalo**.
    - Dovresti ora essere in grado di usare il comando ``/testcommand`` (chat) o ``testcommand`` se sei da console di Dalamud.

2. Repo di FFXIVITA

    -  Apri il gioco e usa il comando ``/xlsettings`` nella finestra di
       chat o ``xlsettings`` se sei nella console Dalamud, in modo da
       aprire le impostazioni.
    -  Vai alla voce ``Experimental`` o ``Sperimentale`` (dipende dalla
       lingua in cui hai configurato Dalamud)
    -  Inserisci l’url al nostro repository, `come mostrato in questa guida <https://plugins.ffxivita.it>`__
    -  Una volta aggiunto, Dalamud ricaricherà la lista dei plugin.
    -  Cerca la parola XIVITA nella finesta di ricerca per trovare non solo questo plugin, ma anche tutti gli altri.

Rinconfiguralo in base alle tue esigenze
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ti basterà rinominare tutte le refenze a ``TestPlugin`` in tutti i file
con il nome che vorrai. Non avrai problemi 😁


Scarica i files sorgente del Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. centered::
    Il download dei files è disponibile a `questo
    indirizzo <https://github.com/ffxivita/testplugin/releases/tag/1.0.2>`__
