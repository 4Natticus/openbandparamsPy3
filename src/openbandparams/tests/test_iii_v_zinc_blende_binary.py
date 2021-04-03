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
# Make sure we import the local package
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from openbandparams import iii_v_zinc_blende_binaries, GaAs, InAs
from openbandparams import *
import unittest


class TestIIIVZincBlendeBinary(unittest.TestCase):

    def test_str(self):
        for binary in iii_v_zinc_blende_binaries:
            self.assertEqual(str(binary), binary.name)

    def test_repr(self):
        for binary in iii_v_zinc_blende_binaries:
            self.assertEqual(eval(repr(binary)), binary)

    def test_eq(self):
        self.assertEqual(GaAs, GaAs)
        self.assertNotEqual(GaAs, InAs)

    def test_a_300K(self):
        self.assertAlmostEqual(GaAs.a_300K(), 5.65325, places=5)

    def test_da_dT(self):
        self.assertAlmostEqual(GaAs.thermal_expansion(), 0.0000388, places=7)

    def test_a(self):
        self.assertAlmostEqual(GaAs.a(), 5.65325, places=5)
        self.assertAlmostEqual(GaAs.a(T=301), 5.65325 + 0.0000388, places=7)

    def test_Eg_Gamma_0(self):
        self.assertAlmostEqual(GaAs.Eg_Gamma_0(), 1.519, places=3)

    def test_alpha_Gamma(self):
        self.assertAlmostEqual(GaAs.alpha_Gamma(), 0.0005405, places=7)

    def test_beta_Gamma(self):
        self.assertAlmostEqual(GaAs.beta_Gamma(), 204, places=0)

    def test_Eg_Gamma(self):
        self.assertAlmostEqual(GaAs.Eg_Gamma(), 1.42248214286, places=11)
        self.assertAlmostEqual(GaAs.Eg_Gamma(T=0), 1.519, places=3)

    def test_Eg_X_0(self):
        self.assertAlmostEqual(GaAs.Eg_X_0(), 1.981, places=3)

    def test_alpha_X(self):
        self.assertAlmostEqual(GaAs.alpha_X(), 0.00046, places=5)

    def test_beta_X(self):
        self.assertAlmostEqual(GaAs.beta_X(), 204, places=0)

    def test_Eg_X(self):
        self.assertAlmostEqual(GaAs.Eg_X(), 1.89885714286, places=11)
        self.assertAlmostEqual(GaAs.Eg_X(T=0), 1.981, places=3)

    def test_Eg_L_0(self):
        self.assertAlmostEqual(GaAs.Eg_L_0(), 1.815, places=3)

    def test_alpha_L(self):
        self.assertAlmostEqual(GaAs.alpha_L(), 0.000605, places=6)

    def test_beta_L(self):
        self.assertAlmostEqual(GaAs.beta_L(), 204, places=0)

    def test_Eg_L(self):
        self.assertAlmostEqual(GaAs.Eg_L(), 1.70696428571, places=11)
        self.assertAlmostEqual(GaAs.Eg_L(T=0), 1.815, places=3)

    def test_element_fraction(self):
        self.assertEqual(GaAs.element_fraction('Ga'), 1.)
        self.assertEqual(GaAs.element_fraction('As'), 1.)
        self.assertEqual(GaAs.element_fraction('In'), 0.)
        self.assertEqual(InAs.element_fraction('Ga'), 0.)
        self.assertEqual(InAs.element_fraction('As'), 1.)
        self.assertEqual(InAs.element_fraction('In'), 1.)

    def test_GaAs_Eg(self):
        self.assertAlmostEqual(GaAs.Eg(), 1.42248214286, places=11)
        self.assertAlmostEqual(GaAs.Eg(T=0), 1.519, places=3)
    
    def test_compressive_biaxial_strained(self):
        strain = 0.01 # compressive
        unstrained = GaAs
        strained = GaAs.strained_001(strain)
        self.assert_(strained.strain_out_of_plane() == strain)
        self.assert_(strained.strain_in_plane() < 0)
        self.assert_(unstrained.a_c() < 0)
        self.assert_(unstrained.a_v() < 0)
        self.assert_(unstrained.b() < 0)
        self.assert_(strained.CBO_strain_shift() > 0)
        self.assert_(strained.VBO_hh_strain_shift() > 0)
        self.assert_(strained.VBO_lh_strain_shift() < 0)
        self.assert_(strained.VBO_strain_shift() > 0)
        self.assert_(strained.Eg_strain_shift() > 0)
        self.assert_(strained.Eg() > unstrained.Eg())
    
    def test_tensile_biaxial_strained(self):
        strain = -0.01 # tensile
        unstrained = GaAs
        strained = GaAs.strained_001(strain)
        self.assert_(strained.strain_out_of_plane() == strain)
        self.assert_(strained.strain_in_plane() > 0)
        self.assert_(unstrained.a_c() < 0)
        self.assert_(unstrained.a_v() < 0)
        self.assert_(unstrained.b() < 0)
        self.assert_(strained.CBO_strain_shift() < 0)
        self.assert_(strained.VBO_hh_strain_shift() < 0)
        self.assert_(strained.VBO_lh_strain_shift() > 0)
        self.assert_(strained.VBO_strain_shift() > 0)
        self.assert_(strained.Eg_strain_shift() < 0)
        self.assert_(strained.Eg() < unstrained.Eg())
        

if __name__ == '__main__':
    unittest.main()
