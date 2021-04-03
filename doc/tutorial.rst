Tutorial
========

Welcome to the `openbandparams` tutorial. This will teach you the basics.
If you have not already installed `openbandparams`, please see
:doc:`installation`. First, start up an interactive python shell::

    $ python

Next, import everything from the `openbandparams` package::

    >>> from openbandparams import *

Now you can access the materials and their properties::

    >>> GaAs
    GaAs
    >>> InAs
    InAs
    >>> InSb
    InSb

The lattice constant, in units of Angstroms (Å), is accessed like this::

    >>> GaAs.a()
    5.65325

The bandgap, in units of electron Volts (eV), is accessed like this::

    >>> GaAs.Eg()
    1.4224821428571428

Some parameters depend on temperature. If the temperature is not provided,
it defaults to 300 Kelvin::

    >>> GaAs.Eg(T=300)
    1.4224821428571428
    >>> GaAs.Eg(T=0)
    1.519

There are many parameters available::

    >>> GaAs.Eg_Gamma()
    1.4224821428571428
    >>> GaAs.Eg_X()
    1.898857142857143
    >>> GaAs.Eg_L()
    1.7069642857142857
    >>> GaAs.meff_e_Gamma()
    0.067

A full list of parameters available for a given material
can be printed using the following one-liner::

    >>> sorted([p.name for p in GaAs.get_unique_parameters()])
    ['CBO', 'CBO_Gamma', 'CBO_L', 'CBO_X', 'Delta_SO', 'Eg', 'Eg_Gamma',
    'Eg_Gamma_0', 'Eg_L', 'Eg_L_0', 'Eg_X', 'Eg_X_0', 'Ep', 'F', 'VBO', 'a',
    'a_300K', 'a_c', 'a_v', 'alpha_Gamma', 'alpha_L', 'alpha_X', 'b',
    'beta_Gamma', 'beta_L', 'beta_X', 'c11', 'c12', 'c44', 'd',
    'electron_affinity', 'luttinger1', 'luttinger2', 'luttinger3',
    'luttinger32', 'meff_SO', 'meff_e_Gamma', 'meff_e_Gamma_0',
    'meff_e_L_DOS', 'meff_e_L_long', 'meff_e_L_trans', 'meff_e_X_DOS',
    'meff_e_X_long', 'meff_e_X_trans', 'meff_hh_100', 'meff_hh_110',
    'meff_hh_111', 'meff_lh_100', 'meff_lh_110', 'meff_lh_111',
    'nonparabolicity', 'thermal_expansion']

A description of any parameter can easily be printed::

    >>> print GaAs.Eg.description
    bandgap energy

For documentation of the parameters, see :doc:`supported_parameters`.

Ternary alloys are also supported::

    >>> AlGaAs(x=.3)
    AlGaAs(Al=0.3)
    >>> AlGaAs(Al=.3)
    AlGaAs(Al=0.3)
    >>> AlGaAs(Ga=0.7)
    AlGaAs(Al=0.3)
    >>> AlGaAs(Al=0.3).Eg()
    1.840788343373494

As of version 0.8, you must follow the alloy naming scheme. Group III
elements come first, with the lowest atomic number elements first,
followed by the Group V elements, also ordered by atomic number::

    >>> GaInAs
    GaInAs
    >>> GaPAs
    GaPAs

If you reverse the element order, an error will be raised to let you know::

    >>> InGaAs
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'InGaAs' is not defined
    >>> GaAsP
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'GaAsP' is not defined

Ternaries can be lattice matched to a desired lattice constant
using the following syntax::

    >>> GaInP(a=GaAs.a())
    GaInP(Ga=0.516340648855)
    >>> GaInP(a=GaAs.a()).Eg()
    1.9259077529765196

In the previous example, a lattice matching temperature of 300 K is assumed.
To lattice match to a different lattice matching temperature use the
following syntax::

    >>> GaInP(a=GaAs.a(), T=300)
    GaInP(Ga=0.516340648855)
    >>> GaInP(a=GaAs.a(), T=400)
    GaInP(Ga=0.523158422221)

Instancing can be used to get multiple parameters from an alloy::

    >>> GaInP_on_GaAs = GaInP(a=GaAs.a(), T=300)
    >>> GaInP_on_GaAs
    GaInP(Ga=0.516340648855)
    >>> GaInP_on_GaAs.Eg(T=300)
    1.9259077529765196
    >>> GaInP_on_GaAs.Eg(T=77)
    2.010415191481605
    >>> GaInP_on_GaAs.a()
    5.653250000000166

The same concepts also apply to quaternaries::

    >>> GaInPAs(P=0.1, a=InP.a(), T=300)
    GaInPAs(Ga=0.4176, P=0.1)
    >>> GaInPAs(P=0.1, a=InP.a(), T=300).Eg()
    0.8237397670939017
    >>> myGaInPAs = GaInPAs(P=0.1, a=InP.a(), T=300)
    >>> myGaInPAs.Eg()
    0.8237397670939017
    >>> myGaInPAs.a()
    5.869700012767527

It's also possible to get a LaTeX representation of the alloy::

    >>> GaInPAs.latex()
    'Ga_{x}In_{1-x}P_{y}As_{1-y}'
    >>> GaInPAs(P=0.1, a=InP.a(), T=300).latex()
    'Ga_{0.4176}In_{0.5824}P_{0.1}As_{0.9}'

Now that you have the basics down, check out the :doc:`examples` to see
what's possible.
