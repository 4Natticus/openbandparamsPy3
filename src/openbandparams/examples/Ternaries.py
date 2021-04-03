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


print 'All three of these are identical:'
print '>>> AlGaAs(x=0.3).Eg()\n', AlGaAs(x=0.3).Eg()
print '>>> AlGaAs(Al=0.3).Eg()\n', AlGaAs(Al=0.3).Eg()
print '>>> AlGaAs(Ga=0.7).Eg()\n', AlGaAs(Ga=0.7).Eg()
print ''

print 'These two are identical:'
print '>>> AlGaAs(x=0.3).Eg_Gamma()\n', AlGaAs(x=0.3).Eg_Gamma()
print ''

print 'Alternate forms:'
print '>>> AlGaAs(x=0.3).Eg()\n', AlGaAs(x=0.3).Eg()
print '>>> AlGaAs(x=0.3).Eg(T=300)\n', AlGaAs(x=0.3).Eg(T=300)
print ''

print ('This is the preferred usage (more efficient),'
       'if you want multiple parameters from one alloy composition:')
print '>>> myAlGaAs = AlGaAs(x=0.3)\n',
myAlGaAs = AlGaAs(x=0.3)
print '>>> myAlGaAs.Eg()\n', myAlGaAs.Eg()
print '>>> myAlGaAs.Eg(T=300)\n', myAlGaAs.Eg(T=300)
print ''

print 'Lattice matching to a substrate (at the growth temperature):'
print '>>> a_InP = InP.a(T=800)\n',
a_InP = InP.a(T=800)
print '>>> GaInAs_on_InP = GaInAs(a=a_InP, T=800)\n',
GaInAs_on_InP = GaInAs(a=a_InP, T=800)
print '>>> InP.a(T=800)\n', InP.a(T=800)
print '>>> GaInAs_on_InP.a()\n', GaInAs_on_InP.a(T=800)
print '>>> GaInAs_on_InP.element_fraction("Ga")\n', \
       GaInAs_on_InP.element_fraction("Ga")
print '>>> GaInAs_on_InP.Eg()\n', GaInAs_on_InP.Eg()
print ''

print 'Other examples:'
print '>>> AlGaAs.meff_hh_100(Al=0.3)\n', AlGaAs(Al=0.3).meff_hh_100()
print '>>> AlGaAs.meff_hh_110(Al=0.3)\n', AlGaAs(Al=0.3).meff_hh_110()
print '>>> AlGaAs.meff_hh_111(Al=0.3)\n', AlGaAs(Al=0.3).meff_hh_111()
print '>>> AlGaAs.meff_lh_100(Al=0.3)\n', AlGaAs(Al=0.3).meff_lh_100()
print '>>> AlGaAs.meff_lh_110(Al=0.3)\n', AlGaAs(Al=0.3).meff_lh_110()
print '>>> AlGaAs.meff_lh_111(Al=0.3)\n', AlGaAs(Al=0.3).meff_lh_111()
print ''
