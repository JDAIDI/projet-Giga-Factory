Machine Learning
================

Approche générale ML
--------------------

.. list-table:: Features utilisées dans les modèles ML
   :widths: 30 30 40
   :header-rows: 1

   * - Feature
     - Optimisé par Optuna ?
     - Description
   * - ``lag_1`` ... ``lag_k``
     - Oui (:math:`k \in [1, 30]`)
     - Valeurs passées de ``Dadj_GWh``
   * - ``rolling_mean_w``
     - Oui (:math:`w \in [2, 30]`)
     - Moyenne des :math:`k` dernières valeurs
   * - ``policy_score``
     - Non
     - Score politique EV (sigmoid)
   * - ``charger_density``
     - Non
     - Densité bornes de recharge
   * - ``byd_pressure``
     - Non
     - Part de marché BYD

Décomposition Tendance-Résidus
------------------------------

1. **Transformation logarithmique :** :math:`\log_y = \log(\text{Dadj\_GWh} + \varepsilon)`
2. **Tendance linéaire** sur :math:`\log_y` (365 derniers jours) : :math:`\text{tendance}(t) = \text{pente} \times t + \text{ordonnée}`
3. **Résidus stationnaires :** :math:`\text{résidus}(t) = \log_y(t) - \text{tendance}(t)`
4. **Entraînement sur les résidus** uniquement (bornés, stationnaires)
5. **Reconstruction :** :math:`\text{GWh} = \exp(\text{tendance\_future} + \text{résidus\_prédits})`

.. note::
   **Pente de tendance :** 0,000259 log-unités/jour (≈ 9,9 %/an)

Résultats des modèles ML
------------------------

.. important::
   **Ridge Regression --- Meilleur modèle :**
   Ridge est le **modèle recommandé** pour la prévision en production.
   :math:`R^2 = 0,8289` ; MAPE = 18,55 %.

Classement complet des modèles
------------------------------

.. list-table:: Classement des 10 modèles sur le test set 2022--2024
   :widths: 10 30 10 10 10 10 20
   :header-rows: 1

   * - Rang
     - Modèle
     - Type
     - :math:`R^2`
     - RMSE
     - MAE
     - MAPE
   * - 1
     - **Ridge**
     - ML
     - 0,8289
     - 0,009317
     - 0,006621
     - **18,55 %**
   * - 2
     - SVR
     - ML
     - 0,7197
     - 0,011925
     - 0,008453
     - 23,33 %
   * - 3
     - Reg. Linéaire
     - ML
     - 0,6085
     - 0,014091
     - 0,009960
     - 26,96 %
   * - 4
     - SimpleRNN
     - DL
     - -0,4451
     - 0,027075
     - 0,021278
     - 90,31 %
   * - 7
     - LSTM
     - DL
     - -1,9692
     - 0,038808
     - 0,031988
     - 77,24 %

.. note::
   **Conclusion clé :** Les modèles ML (Ridge, SVR, Régression Linéaire) surpassent significativement les modèles DL. La raison principale : la période d'entraînement (2010--2021) présente une demande très faible et stable, tandis que la période de test (2022--2024) montre une croissance explosive --- une **rupture structurelle** que les modèles DL ne peuvent pas généraliser.
