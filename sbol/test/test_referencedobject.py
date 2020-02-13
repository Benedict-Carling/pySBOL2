import locale
import logging
import os
import unittest

import rdflib
import sbol
from sbol.property import ReferencedObject

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
TEST_LOCATION = os.path.join(MODULE_LOCATION, 'resources', 'crispr_example.xml')
PARTS_LOCATION = os.path.join(MODULE_LOCATION, 'resources', 'tutorial', 'parts.xml')


class TestReferencedObjects(unittest.TestCase):

    def test_participant_type(self):
        doc = sbol.Document()
        doc.read(TEST_LOCATION)
        md_uri = 'http://sbols.org/CRISPR_Example/CRISPR_Template/1.0.0'
        md = doc.moduleDefinitions[md_uri]
        # Work with the first interaction
        i = md.interactions[0]
        # participant should be a URIRef
        self.assertEqual(type(i.participations[0].participant), rdflib.URIRef)

    def test_fc_definition(self):
        doc = sbol.Document()
        doc.read(TEST_LOCATION)
        md_uri = 'http://sbols.org/CRISPR_Example/CRISPR_Template/1.0.0'
        md = doc.moduleDefinitions[md_uri]
        fc_uri = ('http://sbols.org/CRISPR_Example/CRISPR_Template' +
                  '/cas9_gRNA_complex/1.0.0')
        fc = md.functionalComponents[fc_uri]
        # definition should be a URIRef
        self.assertEqual(type(fc.definition), rdflib.URIRef)

    def test_cd_sequences(self):
        # Test a referenced object storing a list instead of a singleton
        doc = sbol.Document()
        doc.read(PARTS_LOCATION)

        cd_uri = 'http://examples.org/ComponentDefinition/AmeR/1'
        cd = doc.componentDefinitions[cd_uri]

        s1_uri = 'http://examples.org/Sequence/AmeR_sequence/1'
        s2_uri = 'http://examples.org/Sequence/ECK120010818_sequence/1'

        # Ensure the URI is present, and as a string
        self.assertTrue(rdflib.URIRef(s1_uri) in cd.sequences)

        # Cannot append sequences - it has no effect on the cd
        #
        # The CD returns a copy of the list of sequences, not its
        # internal representation.
        cd.sequences.append(s2_uri)
        self.assertTrue(len(cd.sequences) == 1)

        cd.sequences = [s1_uri, s2_uri]
        self.assertTrue(len(cd.sequences) == 2)

        # Verify that none of the elements are instances of rdflib.URIRef
        self.assertTrue(all([isinstance(uri, rdflib.URIRef) for uri in cd.sequences]))

        # Verify that the attribute is still a ReferencedObject and
        # was not overwritten with the list.
        if 'sequences' in cd.__dict__:
            self.assertIsInstance(cd.__dict__['sequences'], ReferencedObject)
