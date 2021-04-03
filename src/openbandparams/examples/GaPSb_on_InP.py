#
#   Copyright (c) 2013-2014, Scott J Maddox
#
#   This file is part of openbandparams.
#
#   openbandparams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   openbandparams is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with openbandparams.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
# Make sure we import the local openbandparams version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from openbandparams import *


print( 'Lattice matching GaPSb to InP (at the growth temperature of 470 C):')
Tg = 273.15 + 470
print( '>>> a_InP = InP.a(T=Tg)\n', end=' ')
a_InP = InP.a(T=Tg)
print( '>>> GaPSb_on_InP = GaPSb(a=a_InP, T=Tg)\n', end=' ')
GaPSb_on_InP = GaInAs(a=a_InP, T=Tg)
print( '>>> InP.a(T=Tg)\n', InP.a(T=Tg))
print( '>>> GaPSb_on_InP.a()\n', GaPSb_on_InP.a(T=Tg))
print( '>>> GaPSb_on_InP.element_fraction("Ga")\n',
GaPSb_on_InP.element_fraction("Ga"))  # fix

print( '\nGet the properties at 70 C:')
T = 273.15 + 70
kT = 25.8e-3 / 300 * T
print( 'Eg_Gamma', GaPSb_on_InP.Eg_Gamma(T=T))
print( 'Eg_X', GaPSb_on_InP.Eg_X(T=T))
print( 'Eg_L', GaPSb_on_InP.Eg_L(T=T))
xg = GaPSb_on_InP.Eg_X(T=T) - GaPSb_on_InP.Eg_Gamma(T=T)
print( 'Eg_X - Eg_Gamma', xg)
print( '(Eg_X - Eg_Gamma)/kT', xg / kT)
lg = GaPSb_on_InP.Eg_L(T=T) - GaPSb_on_InP.Eg_Gamma(T=T)
print( 'Eg_L - Eg_Gamma', lg)
print( '(Eg_L - Eg_Gamma)/kT', lg / kT)
meff_e_Gamma = GaPSb_on_InP.meff_e_Gamma(T=T)
print( 'meff_e_Gamma', meff_e_Gamma)
meff_e_L_long = GaPSb_on_InP.meff_e_L_long(T=T)
print( 'meff_e_L_long', meff_e_L_long)
meff_e_L_trans = GaPSb_on_InP.meff_e_L_trans(T=T)
print( 'meff_e_L_trans', meff_e_L_trans)
meff_e_L_DOS = (GaPSb_on_InP.meff_e_L_long(T=T) ** (1. / 3) *
                GaPSb_on_InP.meff_e_L_trans(T=T) ** (2. / 3))
print( 'meff_e_L_DOS', meff_e_L_DOS)
DOS_ratio = (meff_e_L_DOS) ** (3. / 2) / (meff_e_Gamma) ** (3. / 2)
print( 'meff_DOS_ratio', DOS_ratio)
