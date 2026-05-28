Analyse Statistique (EDA) & Modèles Classiques
==============================================

Tests de stationnarité
----------------------

.. list-table:: Tests de stationnarité sur la série Dadj_GWh journalière
   :widths: 30 20 20 30
   :header-rows: 1

   * - Test
     - Statistique
     - p-value
     - Conclusion
   * - ADF (Augmented Dickey-Fuller)
     - 0,3432
     - 0,9792
     - **Non-Stationnaire**
   * - KPSS
     - 6,3782
     - 0,0100
     - **Non-Stationnaire**
   * - Phillips-Perron
     - -17,1892
     - 0,0000
     - **Stationnaire**

.. note::
   ADF et KPSS concordent : la série est **non-stationnaire**. Phillips-Perron donne un résultat contradictoire dû à la rupture structurelle de 2022.
   **Décision :** log-transformation + différenciation :math:`d = 1`.

SARIMA --- Modèle baseline
--------------------------

.. list-table:: Résultats SARIMA
   :widths: 25 25 25 25
   :header-rows: 1

   * - Ordre AR/I/MA
     - Ordre saisonnier (P,D,Q)
     - AIC
     - MAPE test
   * - (0,1,0)
     - (1,1,1)[12]
     - -61,68
     - 59,3 %

ARIMAX --- Modèle enrichi
-------------------------

L'ARIMAX reprend les mêmes ordres SARIMA en ajoutant deux variables exogènes standardisées : ``policy_score`` et ``charger_lag12``.

.. list-table:: Résultats ARIMAX
   :widths: 25 25 25 25
   :header-rows: 1

   * - AIC ARIMAX
     - MAPE test
     - Variables exogènes
     - Seuil 1 usine
   * - -726
     - 72,6 %
     - policy + charger
     - 2026 (SARIMA médian)

Comparaison SARIMA vs ARIMAX
----------------------------

.. list-table:: Comparaison SARIMA vs ARIMAX
   :widths: 30 30 30 10
   :header-rows: 1

   * - Critère
     - SARIMA(0,1,0)(1,1,1)[12]
     - ARIMAX + policy + charger
     - Gagnant
   * - AIC (train)
     - -61,68
     - -72,60
     - **ARIMAX**
   * - MAE test (GWh)
     - 0,721
     - 0,901
     - **SARIMA**
   * - RMSE test (GWh)
     - 0,820
     - 1,040
     - **SARIMA**
   * - MAPE test (%)
     - 59,3%
     - 72,6%
     - **SARIMA**
   * - Interprétabilité
     - Limitée
     - Riche
     - **ARIMAX**
