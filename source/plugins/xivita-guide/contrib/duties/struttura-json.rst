:og:title: Chiavi per i file Json

:og:description: Tutte le chiavi che sono parte integrante di ogni duty contenuto dentro al plugin.

Struttura file JSON
======================

-  ``Version``: Versione del file duty, non cambiare a mano.
-  ``Name``: Nome del Duty
-  ``Difficulty``: ID della difficoltà del duty
-  ``Type``: ID del duty
-  ``Expansion``: ID della espansione
-  ``Level``: Livello del duty
-  ``UnlockQuestID``: `ID della
   quest <https://github.com/xivapi/ffxiv-datamining/blob/master/csv/Quest.csv>`__
   che sblocca il duty
-  ``TerritoryID``: ID del territorio del duty quando si è dentro
-  ``Bosses``: Lista dei Boss

   -  ``Name``: Nome del Boss
   -  ``Strategy`` (si preferisce): Una guida testuale completa su come
      battere il boss
   -  ``TLDR`` (opzionale): Una guida per chi ha fretta su come battere
      il boss
   -  ``KeyMechanics`` (opzionale): Una lista delle meccaniche

      -  ``Name``: Nome della meccanicha
      -  ``Description``: Descrizione della meccanica
      -  ``Type``: ID della meccanica


.. centered:: Un esempio di Duty, può essere trovato :doc:`QUI <duty-esempio>`

|

Quando scrivi una descrizione delle meccaniche del boss, cerca sempre di essere il più conciso possibile.