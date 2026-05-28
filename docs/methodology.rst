Calcul de la Demande Batterie & Facteurs Externes
==================================================

Calcul de la demande
--------------------

La demande batterie est calculée en deux temps :

.. math::

   \bar{C}(t,\text{type}) = \overline{\text{battery\_capacity\_kwh}} \text{ groupé par [year, type]} \tag{1}

.. math::

   E_{\text{BEV}}(t) = V_{\text{BEV}}(t) \times \bar{C}_{\text{BEV}}(t) \tag{2}

.. math::

   E_{\text{PHEV}}(t) = V_{\text{PHEV}}(t) \times \bar{C}_{\text{PHEV}}(t) \tag{3}

.. math::

   E_{\text{HEV}}(t) = V_{\text{HEV}}(t) \times \bar{C}_{\text{HEV}}(t) \tag{4}

.. math::

   E_{\text{total}}(t) = [E_{\text{BEV}}(t) + E_{\text{PHEV}}(t) + E_{\text{HEV}}(t)] \div 10^6 \tag{5}

Facteurs Externes
-----------------

.. list-table:: Facteurs externes et formules d'application
   :widths: 20 40 10 10 10
   :header-rows: 1

   * - Variable
     - Formule
     - BEV
     - PHEV
     - HEV
   * - ``demo_index``
     - :math:`(1-0,006)^{\max(0, t-2012)}`
     - × 1,0
     - × 1,0
     - × 1,0
   * - ``policy_score``
     - :math:`\sigma(0,6(t-2020))`
     - × 1,0
     - × 0,6
     - × 0,2
   * - ``byd_pressure``
     - :math:`0,25\sigma(1,5(t-2022))`
     - × 1,0
     - × 0,3
     - ---
   * - ``charger_density``
     - :math:`C_0 e^{0,166(t-2010)}/150\,000`
     - × 1,0
     - × 0,5
     - ---
   * - ``solid_state_proba``
     - :math:`\sigma(1,0(t-2027))` [scénario haussier]
     - +40%
     - +20%
     - ---

Formule de demande ajustée
--------------------------

.. math::

   D_{\text{BEV\_adj}}(t) = E_{\text{BEV}}(t) \times \text{demo} \times (1 + 1,0\text{policy}) \times (1 - 1,0\text{byd}) \times (1 + 1,0\text{charger}) \div 10^6 \tag{6}

.. math::

   D_{\text{PHEV\_adj}}(t) = E_{\text{PHEV}}(t) \times \text{demo} \times (1 + 0,6\text{policy}) \times (1 - 0,3\text{byd}) \times (1 + 0,5\text{charger}) \div 10^6 \tag{7}

.. math::

   D_{\text{HEV\_adj}}(t) = E_{\text{HEV}}(t) \times \text{demo} \times (1 + 0,2\text{policy}) \div 10^6 \tag{8}

.. math::

   D_{\text{total\_adj}}(t) = D_{\text{BEV\_adj}} + D_{\text{PHEV\_adj}} + D_{\text{HEV\_adj}} \tag{9}

.. math::

   D_{\text{BEV\_ss}}(t) = D_{\text{BEV\_adj}}(t) \times (1 + 0,40 \times \text{solid\_state\_proba}(t)) \tag{10}
