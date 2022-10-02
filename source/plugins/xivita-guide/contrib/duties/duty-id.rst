:og:title: Lista ID

:og:description: Pagina contentente tutti gli ID usati dal plugin XIVGuide.


.. highlight:: c#

Lista degli ID
==============

.. code-block:: csharp
    
    enum DutyType
    {
        Dungeon = 0,
        Trial = 1,
        AllianceRaid = 2
    }

    enum DutyDifficulty 
    {
        Normal = 0,
        Hard = 1,
        Extreme = 2,
        Savage = 3,
        Ultimate = 4,
        Unreal = 5
    }

    enum DutyExpansion
    {
        ARealmReborn = 0,
        Heavensward = 1,
        Stormblood = 2,
        Shadowbringers = 3,
        Endwalker = 4
    }

    enum DutySectionType
    {
        Boss = 0,
        Trashpack = 1,
        Other = 2
    }

    enum DutyDisplayType
    {
        Display = 0,
        Hide = 1,
        Unavailable = 2
    }

    enum DutyMechanics
    {
        Tankbuster = 0,
        Enrage = 1,
        AoE = 2,
        Stackmarker = 3,
        Raidwide = 4,
        Invulnerablity = 5,
        Targetted = 6,
        AddSpawn = 7,
        DPSCheck = 8,
        Cleave = 9,
        Other = 10,
        Gaze = 11,
        Puddle = 12
    }

