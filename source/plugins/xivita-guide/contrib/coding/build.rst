:og:title: XIVITAGuide: Compilazione & Formattazione

:og:description: Alcune linee guida sulla compilazione e formattazione del codice di XIVITAGUide

Linee Guida
===========

Per una maggiore compatibilità, si raccomanda l’uso del setup
`DevContainer <https://docker.ffxivita.it>`__ che è stato allegato a
questo progetto. Si occuperà di installare tutte le dipendenze e
configurare per te l’ambiente di sviluppo. Se vuoi invece sviluppare
sulla tua macchina anzichè dentro al container, `puoi trovare una guida
qui <https://plugins.ffxivita.it>`__. Se usi sistemi Unix (Linux etc),
dovrai impostare manualmente la variabile ``DALAMUD_HOME`` dove
effettivamente è la cartella (Questo lo fa il nostro DeVContainer per
te, se scegli di usarlo)

Standard di Compilazione
~~~~~~~~~~~~~~~~~~~~~~~~

É fortemente consigliato di formattare il codice in modo appropriato in
modo che sia leggibile e che possa essere esteso in futuro. La
maggiorparte degli editor di codice dovrebbero fornire supporto di
default senza installare una estensione aggiuntiva o un plugin. Per
quanto riguarda il codice in generale, non ci sono regole ferree da
seguire ma seguire le indicazioni standard di CSharp è altamente
raccomandato.

Funzionalità
~~~~~~~~~~~~

Assicurati che il codice sia propriamente separato in base alle sua
funzionalità. Ad esempio gli elementi di UI non dovrebbero contenenere
logiche che non vengono usate per il disegno della stessa o visualizzare
informazioni. Il recupero delle informazioni dovrebbe essere chiamato da
una classe differente e da un file differente.

Documentazione & Commenti
~~~~~~~~~~~~~~~~~~~~~~~~~

Si prega di inserire ``<summary>`` per ogni funzione, metodo e classe;
in modo da capire le intenzioni dietro al codice e aiutare gli altri a
capire come usarlo quando lavorano al plugin.

UpdateManager
~~~~~~~~~~~~~

Cerca di non fare cambiamenti alla classe UpdateManager in quanto è una
classe critica per pubblicare aggiornamenti e visto che li “pesca” da
una fonte esterna, è meglio non toccare questa classe. Comunque, se
ritieni di poter migliorarla, sei il/la benvenuto/a.