# -*- coding: utf-8 -*-
# Copyright (c) Polyconseil SAS. All rights reserved.

from __future__ import unicode_literals

import os
from unittest import TestCase

from dokang_pdf import PdfHarvester


class TestPdfHarvester(TestCase):

    def test_basics(self):
        path = os.path.join(os.path.dirname('.'), 'test.pdf')
        harvester = PdfHarvester()
        doc = harvester.harvest_file(path)
        self.assertEqual(doc['title'], "The title")
        self.assertEqual(doc['content'], "This is the content with a diacritic: à.")
