:og:title: XIVITAGuide Esempio file Duty

:og:description: Esempio di Duty caricato dentro XIVITAGuide


.. highlight:: json

Duty di Esempio
================

Di seguito, troviamo (modificato per adattarsi anche ai dispositivi mobile ) un Duty di esempio.

.. code-block:: json

    {
      "Version": 0,
      "Name": "The Howling Eye",
      "Difficulty": 0,
      "Type": 1,
      "Expansion": 0,
      "Level": 44,
      "UnlockQuestID": 66055,
      "TerritoryID": 1047,
      "Bosses": [{
          "Name": "Garuda",
          "Strategy": "Nella prima fase, il tank dovrà attirare Garuda ad un bordo [...]",
          "KeyMechanics": [{
              "Name": "Slipstream",
              "Description": "AOE a linea non visibile che infligge Stun su chiunque venga colpito.",
              "Type": 2
            },
            {
              "Name": "Downburst",
              "Description": "Fendente frontale istantaneo che provoca danni elevati a tutti i giocatori di fronte a Garuda.",
              "Type": 9
            },
            {
              "Name": "Wicked Wheel",
              "Description": "AOE istantanea che dannegga tutti i giocatori attorno a Garuda.",
              "Type": 2
            },
            {
              "Name": "Razor Plumes",
              "Description": "Genera diversi Razor Plumes che attaccheranno.",
              "Type": 7
            },
            {
              "Name": "Mistral Song",
              "Description": "Garuda volerà in aria e riapparirà su un lato a caso dell'arena provocando [...]",
              "Type": 4
            },
            {
              "Name": "Aerial Blast",
              "Description": "Garuda si sposterà al centro dell'arena per lanciare Aerial Blast  [...]",
              "Type": 4
            }
          ]
        },
        {
          "Name": "Garuda Fase 2",
          "Strategy": "La Fase 2 inizia quando Garuda lancia Aerial Blast, poi casterà Eye of the Storm [...]",
          "KeyMechanics": [{
            "Name": "Eye of the Storm",
            "Description": "Garuda si sposterà al centro dell'arena per castarlo creando un tornado [...]",
            "Type": 4
          }]
        }
      ]
    }

