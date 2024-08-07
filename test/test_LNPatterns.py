import logging
import os
from itertools import count
import time
import unittest
from src.DLMS_SPODES.types import cdt, cst, ut
from src.DLMS_SPODES.cosem_interface_classes import collection, overview, ln_pattern
from src.DLMS_SPODES import cosem_interface_classes
from src.DLMS_SPODES.obis import media_id
from src.DLMS_SPODES.version import AppVersion
from src.DLMS_SPODES.exceptions import NeedUpdate, NoObject




class TestType(unittest.TestCase):

    @staticmethod
    def get_pattern():
        return ln_pattern.LNPattern("0.b.0.1.0.255")

    def test_create(self):
        p = self.get_pattern()
        print(p)

    def test_equal(self):
        p = self.get_pattern()
        self.assertEqual(p, cst.LogicalName.from_obis("0.2.0.1.0.255"))
        self.assertNotEqual(p, cst.LogicalName.from_obis("0.0.0.1.0.255"))

