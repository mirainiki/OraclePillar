# test_oraclepillar.py
"""
Tests for OraclePillar module.
"""

import unittest
from oraclepillar import OraclePillar

class TestOraclePillar(unittest.TestCase):
    """Test cases for OraclePillar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OraclePillar()
        self.assertIsInstance(instance, OraclePillar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OraclePillar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
