# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""
from hack.n.dine.testing import INTEGRATION
from plone import api

import unittest2 as unittest


class TestInstall(unittest.TestCase):
    """Test installation of hack.n.dine into Plone."""

    layer = INTEGRATION

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if hack.n.dine is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('hack.n.dine'))

    def test_uninstall(self):
        """Test if hack.n.dine is cleanly uninstalled."""
        self.installer.uninstallProducts(['hack.n.dine'])
        self.assertFalse(self.installer.isProductInstalled('hack.n.dine'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IHackNDineLayer is registered."""
        from hack.n.dine.interfaces import IHackNDineLayer
        from plone.browserlayer import utils
        self.assertIn(IHackNDineLayer, utils.registered_layers())
