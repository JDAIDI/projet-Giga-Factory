Idée & Objectif du Projet
=========================

Contexte
--------

La transition énergétique mondiale vers les véhicules électriques crée une demande croissante et structurelle en batteries lithium-ion. Le Japon, berceau des constructeurs automobiles mondiaux (Toyota, Honda, Nissan), représente un marché stratégique : ses OEMs produisent plus de **18 millions de véhicules par an** à l'échelle mondiale, soit un ratio overseas/domestique de 4:1. Une décision de construction de gigafactory au Japon n'alimente donc pas seulement le marché local, mais les chaînes d'assemblage mondiales.

.. important::
   **Objectif final :** Développer une stratégie quantifiée pour la construction de gigafactories de batteries : **combien d'usines construire**, quand les lancer (délai de construction ≈ 3 ans), et dans quel scénario de demande (base / optimiste / pessimiste), en se basant sur des prédictions de la demande batterie jusqu'en 2035.

Formule centrale
----------------

La logique du projet repose sur une équation simple mais puissante :

.. math::

   \frac{\text{Demande GWh}(t)}{40\ \text{GWh/usine}} = N_{\text{usines}}(t)

Problématiques traitées
-----------------------

* **Qui sont les clients du marché japonais ?** Le marché est domestique à 93--95 % (marques japonaises). Mais la vraie question est la demande mondiale des OEMs japonais.
* **Y a-t-il un risque de saturation ?** Les ventes BEV ont chuté de -32,5 % en 2024 --- signal de saturation domestique. Le marché interne seul ne justifie pas plusieurs usines.
* **Quelle est la position du Japon dans le marché global ?** Production overseas 4× la production domestique. Les usines doivent alimenter les lignes mondiales.
* **Quels facteurs externes influencent la demande ?** 7 facteurs : démographie, politique EV, BYD, taux de change, réseau de recharge, solid-state, risque matières premières.

.. note::
   **Limitation importante identifiée :** ``vehicles.csv`` est une base de données EPA américaine utilisée comme proxy pour les capacités de batteries des modèles japonais. Les données de ventes quotidiennes sont des interpolations de données mensuelles JAMA. Ces limitations sont documentées et prises en compte dans l'interprétation des résultats.
