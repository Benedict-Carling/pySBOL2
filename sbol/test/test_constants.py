import os
import unittest

import sbol

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
TEST_LOCATION = os.path.join(MODULE_LOCATION, 'resources', 'crispr_example.xml')


class TestConstants(unittest.TestCase):

    @unittest.expectedFailure
    def test_igem_standard_assembly(self):
        # IGEM_STANDARD_ASSEMBLY is a function in pySBOL.
        self.assertTrue(callable(sbol.IGEM_STANDARD_ASSEMBLY),
                        'IGEM_STANDARD_ASSEMBLY is not callable')

    @unittest.expectedFailure
    def test_in_roles(self):
        doc = sbol.Document()
        doc.read(TEST_LOCATION)
        md_uri = 'http://sbols.org/CRISPR_Example/CRISPR_Template/1.0.0'
        md = doc.moduleDefinitions[md_uri]
        i_uri = ('http://sbols.org/CRISPR_Example/CRISPR_Template' +
                 '/cas9_complex_formation/1.0.0')
        i = md.interactions[i_uri]
        p_uri = ('http://sbols.org/CRISPR_Example/CRISPR_Template' +
                 '/cas9_complex_formation/cas9_gRNA_complex/1.0.0')
        p = i.participations[p_uri]
        # p.roles is a list of strings
        # The constant converted to a string should be in the list of roles
        self.assertIn(str(sbol.SBO_PRODUCT), p.roles)
        # The constant should be in the list of roles for backward compatibility
        self.assertIn(sbol.SBO_PRODUCT, p.roles)

    @unittest.expectedFailure
    def test_string_constants(self):
        # All of these constants have type str (string) in pySBOL. The
        # must be strings in this library as well in order to maintain
        # backward compatibility. One use case is to test for
        # membership in a list like Participant.roles (see above). A
        # use like that will fail if these constants are not strings
        # and roles is a list of strings.
        self.assertEqual(type(sbol.BIOPAX_COMPLEX), str)
        self.assertEqual(type(sbol.BIOPAX_DNA), str)
        self.assertEqual(type(sbol.BIOPAX_PROTEIN), str)
        self.assertEqual(type(sbol.BIOPAX_RNA), str)
        self.assertEqual(type(sbol.BIOPAX_SMALL_MOLECULE), str)
        self.assertEqual(type(sbol.DEFAULT_NS), str)
        self.assertEqual(type(sbol.EDAM_BIOPAX), str)
        self.assertEqual(type(sbol.EDAM_CELLML), str)
        self.assertEqual(type(sbol.EDAM_SBML), str)
        self.assertEqual(type(sbol.IGEM_URI), str)
        self.assertEqual(type(sbol.NODENAME_ABOUT), str)
        self.assertEqual(type(sbol.NODENAME_RESOURCE), str)
        self.assertEqual(type(sbol.PROVO), str)
        self.assertEqual(type(sbol.PROVO_ACTIVITY), str)
        self.assertEqual(type(sbol.PROVO_AGENT), str)
        self.assertEqual(type(sbol.PROVO_AGENT_PROPERTY), str)
        self.assertEqual(type(sbol.PROVO_ASSOCIATION), str)
        self.assertEqual(type(sbol.PROVO_ENDED_AT_TIME), str)
        self.assertEqual(type(sbol.PROVO_ENTITY), str)
        self.assertEqual(type(sbol.PROVO_HAD_PLAN), str)
        self.assertEqual(type(sbol.PROVO_HAD_ROLE), str)
        self.assertEqual(type(sbol.PROVO_PLAN), str)
        self.assertEqual(type(sbol.PROVO_QUALIFIED_ASSOCIATION), str)
        self.assertEqual(type(sbol.PROVO_QUALIFIED_USAGE), str)
        self.assertEqual(type(sbol.PROVO_STARTED_AT_TIME), str)
        self.assertEqual(type(sbol.PROVO_USAGE), str)
        self.assertEqual(type(sbol.PROVO_WAS_GENERATED_BY), str)
        self.assertEqual(type(sbol.PROVO_WAS_INFORMED_BY), str)
        self.assertEqual(type(sbol.PROV_URI), str)
        self.assertEqual(type(sbol.PURL_URI), str)
        self.assertEqual(type(sbol.RDF_URI), str)
        self.assertEqual(type(sbol.SBO), str)
        self.assertEqual(type(sbol.SBOL_ACCESS), str)
        self.assertEqual(type(sbol.SBOL_ACCESS_PRIVATE), str)
        self.assertEqual(type(sbol.SBOL_ACCESS_PUBLIC), str)
        self.assertEqual(type(sbol.SBOL_AT), str)
        self.assertEqual(type(sbol.SBOL_ATTACHMENT), str)
        self.assertEqual(type(sbol.SBOL_ATTACHMENTS), str)
        self.assertEqual(type(sbol.SBOL_BUILD), str)
        self.assertEqual(type(sbol.SBOL_COLLECTION), str)
        self.assertEqual(type(sbol.SBOL_COMBINATORIAL_DERIVATION), str)
        self.assertEqual(type(sbol.SBOL_COMPONENT), str)
        self.assertEqual(type(sbol.SBOL_COMPONENTS), str)
        self.assertEqual(type(sbol.SBOL_COMPONENT_DEFINITION), str)
        self.assertEqual(type(sbol.SBOL_COMPONENT_PROPERTY), str)
        self.assertEqual(type(sbol.SBOL_CUT), str)
        self.assertEqual(type(sbol.SBOL_DEFINITION), str)
        self.assertEqual(type(sbol.SBOL_DESCRIPTION), str)
        self.assertEqual(type(sbol.SBOL_DESIGN), str)
        self.assertEqual(type(sbol.SBOL_DIRECTION), str)
        self.assertEqual(type(sbol.SBOL_DIRECTION_IN), str)
        self.assertEqual(type(sbol.SBOL_DIRECTION_IN_OUT), str)
        self.assertEqual(type(sbol.SBOL_DIRECTION_NONE), str)
        self.assertEqual(type(sbol.SBOL_DIRECTION_OUT), str)
        self.assertEqual(type(sbol.SBOL_DISPLAY_ID), str)
        self.assertEqual(type(sbol.SBOL_DOCUMENT), str)
        self.assertEqual(type(sbol.SBOL_DOCUMENTED), str)
        self.assertEqual(type(sbol.SBOL_ELEMENTS), str)
        self.assertEqual(type(sbol.SBOL_ENCODING), str)
        self.assertEqual(type(sbol.SBOL_ENCODING_IUPAC), str)
        self.assertEqual(type(sbol.SBOL_ENCODING_IUPAC_PROTEIN), str)
        self.assertEqual(type(sbol.SBOL_ENCODING_SMILES), str)
        self.assertEqual(type(sbol.SBOL_END), str)
        self.assertEqual(type(sbol.SBOL_EXPERIMENT), str)
        self.assertEqual(type(sbol.SBOL_EXPERIMENTAL_DATA), str)
        self.assertEqual(type(sbol.SBOL_FRAMEWORK), str)
        self.assertEqual(type(sbol.SBOL_FUNCTIONAL_COMPONENT), str)
        self.assertEqual(type(sbol.SBOL_FUNCTIONAL_COMPONENTS), str)
        self.assertEqual(type(sbol.SBOL_GENERIC_LOCATION), str)
        self.assertEqual(type(sbol.SBOL_GENERIC_TOP_LEVEL), str)
        self.assertEqual(type(sbol.SBOL_IDENTIFIED), str)
        self.assertEqual(type(sbol.SBOL_IDENTITY), str)
        self.assertEqual(type(sbol.SBOL_IMPLEMENTATION), str)
        self.assertEqual(type(sbol.SBOL_INTERACTION), str)
        self.assertEqual(type(sbol.SBOL_INTERACTIONS), str)
        self.assertEqual(type(sbol.SBOL_LANGUAGE), str)
        self.assertEqual(type(sbol.SBOL_LEARN), str)
        self.assertEqual(type(sbol.SBOL_LOCAL), str)
        self.assertEqual(type(sbol.SBOL_LOCATION), str)
        self.assertEqual(type(sbol.SBOL_LOCATIONS), str)
        self.assertEqual(type(sbol.SBOL_MAPS_TO), str)
        self.assertEqual(type(sbol.SBOL_MAPS_TOS), str)
        self.assertEqual(type(sbol.SBOL_MEASURE), str)
        self.assertEqual(type(sbol.SBOL_MEASUREMENTS), str)
        self.assertEqual(type(sbol.SBOL_MEMBERS), str)
        self.assertEqual(type(sbol.SBOL_MODEL), str)
        self.assertEqual(type(sbol.SBOL_MODELS), str)
        self.assertEqual(type(sbol.SBOL_MODULE), str)
        self.assertEqual(type(sbol.SBOL_MODULES), str)
        self.assertEqual(type(sbol.SBOL_MODULE_DEFINITION), str)
        self.assertEqual(type(sbol.SBOL_NAME), str)
        self.assertEqual(type(sbol.SBOL_OBJECT), str)
        self.assertEqual(type(sbol.SBOL_OPERATOR), str)
        self.assertEqual(type(sbol.SBOL_ORIENTATION), str)
        self.assertEqual(type(sbol.SBOL_ORIENTATION_INLINE), str)
        self.assertEqual(type(sbol.SBOL_ORIENTATION_REVERSE_COMPLEMENT), str)
        self.assertEqual(type(sbol.SBOL_PARTICIPANT), str)
        self.assertEqual(type(sbol.SBOL_PARTICIPATION), str)
        self.assertEqual(type(sbol.SBOL_PARTICIPATIONS), str)
        self.assertEqual(type(sbol.SBOL_PERSISTENT_IDENTITY), str)
        self.assertEqual(type(sbol.SBOL_RANGE), str)
        self.assertEqual(type(sbol.SBOL_REFINEMENT), str)
        self.assertEqual(type(sbol.SBOL_REFINEMENT_MERGE), str)
        self.assertEqual(type(sbol.SBOL_REFINEMENT_USE_LOCAL), str)
        self.assertEqual(type(sbol.SBOL_REFINEMENT_USE_REMOTE), str)
        self.assertEqual(type(sbol.SBOL_REFINEMENT_VERIFY_IDENTICAL), str)
        self.assertEqual(type(sbol.SBOL_REMOTE), str)
        self.assertEqual(type(sbol.SBOL_RESTRICTION), str)
        self.assertEqual(type(sbol.SBOL_RESTRICTION_OPPOSITE_ORIENTATION_AS), str)
        self.assertEqual(type(sbol.SBOL_RESTRICTION_PRECEDES), str)
        self.assertEqual(type(sbol.SBOL_RESTRICTION_SAME_ORIENTATION_AS), str)
        self.assertEqual(type(sbol.SBOL_ROLES), str)
        self.assertEqual(type(sbol.SBOL_ROLE_INTEGRATION), str)
        self.assertEqual(type(sbol.SBOL_ROLE_INTEGRATION_MERGE), str)
        self.assertEqual(type(sbol.SBOL_ROLE_INTEGRATION_OVERRIDE), str)
        self.assertEqual(type(sbol.SBOL_SEQUENCE), str)
        self.assertEqual(type(sbol.SBOL_SEQUENCE_ANNOTATION), str)
        self.assertEqual(type(sbol.SBOL_SEQUENCE_ANNOTATIONS), str)
        self.assertEqual(type(sbol.SBOL_SEQUENCE_CONSTRAINT), str)
        self.assertEqual(type(sbol.SBOL_SEQUENCE_CONSTRAINTS), str)
        self.assertEqual(type(sbol.SBOL_SEQUENCE_PROPERTY), str)
        self.assertEqual(type(sbol.SBOL_SOURCE), str)
        self.assertEqual(type(sbol.SBOL_START), str)
        self.assertEqual(type(sbol.SBOL_STRATEGY), str)
        self.assertEqual(type(sbol.SBOL_SUBJECT), str)
        self.assertEqual(type(sbol.SBOL_TEMPLATE), str)
        self.assertEqual(type(sbol.SBOL_TEST), str)
        self.assertEqual(type(sbol.SBOL_TOP_LEVEL), str)
        self.assertEqual(type(sbol.SBOL_TYPES), str)
        self.assertEqual(type(sbol.SBOL_UNIT), str)
        self.assertEqual(type(sbol.SBOL_URI), str)
        self.assertEqual(type(sbol.SBOL_VALUE), str)
        self.assertEqual(type(sbol.SBOL_VARIABLE), str)
        self.assertEqual(type(sbol.SBOL_VARIABLE_COMPONENT), str)
        self.assertEqual(type(sbol.SBOL_VARIABLE_COMPONENTS), str)
        self.assertEqual(type(sbol.SBOL_VARIANTS), str)
        self.assertEqual(type(sbol.SBOL_VARIANT_COLLECTIONS), str)
        self.assertEqual(type(sbol.SBOL_VARIANT_DERIVATIONS), str)
        self.assertEqual(type(sbol.SBOL_VERSION), str)
        self.assertEqual(type(sbol.SBOL_WAS_DERIVED_FROM), str)
        self.assertEqual(type(sbol.SBO_BINDING_SITE), str)
        self.assertEqual(type(sbol.SBO_BIOCHEMICAL_REACTION), str)
        self.assertEqual(type(sbol.SBO_COFACTOR), str)
        self.assertEqual(type(sbol.SBO_CONTINUOUS), str)
        self.assertEqual(type(sbol.SBO_CONTROL), str)
        self.assertEqual(type(sbol.SBO_CONVERSION), str)
        self.assertEqual(type(sbol.SBO_DEGRADATION), str)
        self.assertEqual(type(sbol.SBO_DISCRETE), str)
        self.assertEqual(type(sbol.SBO_ENZYME), str)
        self.assertEqual(type(sbol.SBO_GENE), str)
        self.assertEqual(type(sbol.SBO_GENETIC_PRODUCTION), str)
        self.assertEqual(type(sbol.SBO_INHIBITED), str)
        self.assertEqual(type(sbol.SBO_INHIBITION), str)
        self.assertEqual(type(sbol.SBO_INHIBITOR), str)
        self.assertEqual(type(sbol.SBO_INTERACTION), str)
        self.assertEqual(type(sbol.SBO_LIGAND), str)
        self.assertEqual(type(sbol.SBO_NONCOVALENT_BINDING), str)
        self.assertEqual(type(sbol.SBO_NONCOVALENT_COMPLEX), str)
        self.assertEqual(type(sbol.SBO_PRODUCT), str)
        self.assertEqual(type(sbol.SBO_PROMOTER), str)
        self.assertEqual(type(sbol.SBO_REACTANT), str)
        self.assertEqual(type(sbol.SBO_SIDEPRODUCT), str)
        self.assertEqual(type(sbol.SBO_STIMULATED), str)
        self.assertEqual(type(sbol.SBO_STIMULATION), str)
        self.assertEqual(type(sbol.SBO_STIMULATOR), str)
        self.assertEqual(type(sbol.SBO_SUBSTRATE), str)
        self.assertEqual(type(sbol.SO), str)
        self.assertEqual(type(sbol.SO_CDS), str)
        self.assertEqual(type(sbol.SO_CIRCULAR), str)
        self.assertEqual(type(sbol.SO_GENE), str)
        self.assertEqual(type(sbol.SO_LINEAR), str)
        self.assertEqual(type(sbol.SO_MISC), str)
        self.assertEqual(type(sbol.SO_PLASMID), str)
        self.assertEqual(type(sbol.SO_PROMOTER), str)
        self.assertEqual(type(sbol.SO_RBS), str)
        self.assertEqual(type(sbol.SO_SGRNA), str)
        self.assertEqual(type(sbol.SO_TERMINATOR), str)
        self.assertEqual(type(sbol.SYSBIO_ANALYSIS), str)
        self.assertEqual(type(sbol.SYSBIO_BUILD), str)
        self.assertEqual(type(sbol.SYSBIO_DESIGN), str)
        self.assertEqual(type(sbol.SYSBIO_SAMPLE_ROSTER), str)
        self.assertEqual(type(sbol.SYSBIO_TEST), str)
        self.assertEqual(type(sbol.SYSBIO_URI), str)
        self.assertEqual(type(sbol.UNDEFINED), str)
