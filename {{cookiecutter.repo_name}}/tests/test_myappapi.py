from unittest import TestCase
from {{cookiecutter.module_name}} import run_{{cookiecutter.executable_name}}


class ApplicationWrapperTest(TestCase):

    def test_app_wrapper(self):
        # define expected output
        expected_value = _what_you_expect_

        # create test parameters
        _create_your_test_parameters_
        
        # read test molecules
        # mol = oechem.OEMol()
        # ifs = oechem.oemolistream('my_test_data.sdf')
        # oechem.OEReadMolecule(ifs, mol)

        # test application
        for output in run_{{cookiecutter.executable_name}}( _put_your_parameters_here_ ):
            # test calculated output value vs expected value
            self.assertEqual(output.value(), expected_value)


