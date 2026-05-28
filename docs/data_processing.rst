Phase 1 --- Sources & Nettoyage des Données
===========================================

Sources de données
------------------

.. list-table:: Sources de données utilisées
   :widths: 20 20 10 10 15 25
   :header-rows: 1

   * - Fichier
     - Source
     - Lignes
     - Col
     - Période
     - Rôle
   * - ``vehicles.csv``
     - US EPA FE
     - 49 846
     - 84
     - 2010--2024
     - Capacité batterie par modèle EV
   * - ``japan_car_sales_2010_2024.csv``
     - JAMA
     - 5 073
     - 5
     - 2010--2024
     - Ventes BEV / PHEV / HEV / Total
   * - ``raw_material_prices_2008_2024.csv``
     - Marché mondiaux
     - 816
     - 6
     - 2008--2024
     - Prix Li, Co, Ni, Graphite

Nettoyage des données
---------------------

``car_models_clean.csv``
~~~~~~~~~~~~~~~~~~~~~~~~

* Filtrage types EV (BEV/PHEV/HEV) depuis ``vehicles.csv``.
* Calcul :math:`\text{battery\_capacity\_kwh} = \text{charge240} \times 7,2\ \text{kW}`.
* Extraction ``motor_power_kw`` depuis la colonne texte ``evMotor``.
* Simplification ``vehicle_class`` (SUV / Pickup / Sedan / ...).
* Suppression lignes sans ``battery_capacity`` ni ``electric_range``.

``japan_car_sales_clean.csv``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Parse de la colonne ``Date`` → ``datetime``.
* Tri chronologique + ajout colonnes ``year`` / ``month``.
* Interpolation linéaire des valeurs manquantes ; ``Clip(lower=0)``.
* Cast en entier pour BEV / PHEV / HEV / Total_LDV.

``raw_material_prices_clean.csv``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Standardisation des noms matériaux (Title Case).
* Interpolation par groupe matériau (linéaire).
* Remplissage résiduel par médiane ; Suppression prix :math:`\leq 0` ; Arrondi à 2 décimales.
