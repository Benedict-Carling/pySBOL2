import os
import unittest

from sbol.partshop import PartShop
from sbol.document import Document
from sbol.sbolerror import SBOLError


if 'username' in os.environ:
    username = os.environ['username']
else:
    username = None
if 'password' in os.environ:
    password = os.environ['password']
else:
    password = None


class TestPartShop(unittest.TestCase):
    def test_pull_00(self):
        # Based on tutorial: https://pysbol2.readthedocs.io/en/latest/repositories.html
        doc = Document()
        igem = PartShop('https://synbiohub.org')
        igem.pull('https://synbiohub.org/public/igem/BBa_R0010/1', doc)
        print(doc)
        for obj in doc:
            print(obj)
        self.assertEqual(3, len(doc))

    def test_pull_01(self):
        # Based on tutorial: https://pysbol2.readthedocs.io/en/latest/repositories.html
        doc = Document()
        igem = PartShop('https://synbiohub.org/public/igem')
        igem.pull('BBa_B0032', doc)
        igem.pull('BBa_E0040', doc)
        igem.pull('BBa_B0012', doc)
        print(doc)
        for obj in doc:
            print(obj)
        self.assertEqual(7, len(doc))

    def test_pull_02(self):
        doc = Document()
        ps = PartShop('https://synbiohub.utah.edu/public/RepressionModel')
        ps.pull('CRPb_characterization_Circuit', doc)
        print(doc)
        for obj in doc:
            print(obj)
        self.assertEqual(31, len(doc))

    def test_login(self):
        # NOTE: Add /login because login pages may be different
        # depending on what site you're accessing
        igem = PartShop('https://synbiohub.org')
        response = igem.login('johndoe@example.org', 'test')
        self.assertEqual(response.status_code, 200)

    def test_login_bad(self):
        with self.assertRaises(SBOLError):
            igem = PartShop('https://synbiohub.org')
            igem.login('johndoe@example.org', 'test1')

    @unittest.skipIf(password is None, "No password supplied")
    def test_submit_00(self):
        doc = Document()
        doc.displayId = 'test_collection'
        doc.name = 'test collection'
        doc.description = 'a test collection automatically generated ' \
                          'by the SBOL client library'
        ps = PartShop('https://hub-staging.sd2e.org')
        ps.login(username, password)
        response = ps.submit(doc, overwrite=1)
        self.assertEqual(response.status_code, 200)

    def test_sparqlQuery_00(self):
        ps = PartShop('https://synbiohub.org')
        response = ps.login('johndoe', 'test')
        self.assertEqual(response.status_code, 200)
        query = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX sbh: <http://wiki.synbiohub.org/wiki/Terms/synbiohub#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX sbol: <http://sbols.org/v2#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX purl: <http://purl.obolibrary.org/obo/>
SELECT ?p ?o
WHERE {
  <https://synbiohub.org/public/igem/BBa_K318030/1> ?p ?o
}
'''
        response = ps.sparqlQuery(query)
        print(response.text)
        self.assertEqual(response.status_code, 200)

    def test_getURL(self):
        expected_url = 'https://example.org'
        partShop = PartShop(expected_url)
        self.assertEqual(partShop.getURL(), expected_url)
