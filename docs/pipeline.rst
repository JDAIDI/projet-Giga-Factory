Pipeline Complet du Projet
==========================

Le projet suit un flux de travail structuré en 10 étapes clés, de la collecte des données brutes à la formulation de recommandations stratégiques.

.. list-table:: Pipeline du projet
   :widths: 5 30 15 50
   :header-rows: 1

   * - #
     - Étape
     - Statut
     - Outputs
   * - 01
     - Collecte Raw Data
     - Fait
     - ``vehicles.csv``, ``japan_car_sales``, ``raw_material_prices``
   * - 02
     - Nettoyage Data
     - Fait
     - ``dataCleaning.py`` → fichiers clean
   * - 03
     - Calcul Battery Demand
     - Fait
     - ``battery_demand.csv``
   * - 04
     - Facteurs Externes
     - Fait
     - ``battery_demand_enriched.csv``
   * - 05
     - Analyse Marché Japonais
     - Fait
     - EDA, saisonnalité, saturation, exports
   * - 06
     - Stationnarité & SARIMA
     - Fait
     - Forecast 2025--2030
   * - 07
     - ARIMAX Enrichi
     - Fait
     - Impact facteurs externes
   * - 08
     - ML/DL XGBoost & Prophet
     - Fait
     - ``TimeSeries_Forecasting_Analysis.ipynb``
   * - 09
     - Scénarios & Décision
     - Fait
     - Base / Optimiste / Pessimiste → :math:`N_{\text{usines}}`/année
   * - 10
     - Rapport Final
     - Fait
     - Stratégie, Timing, Budget risque
