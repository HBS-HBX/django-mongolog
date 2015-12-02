"""
	django-mongolog.  Simple Mongo based logger for Django
    Copyright (C) 2015 - John Furr

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import unittest
from django.test import TestCase
import logging

logger = logging.getLogger(__name__)

class TestLogLevels(TestCase):

    #def setUp(self):
    #    # First we have to setup a test pymongo database...which is trivial
        
        
    def test_info(self):
        self.assertEqual('INFO', logger.info("INFO"))

if __name__ == '__main__':
    unittest.main()

# Create your tests here.
