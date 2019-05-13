import os

from lisflood.global_modules.globals import outputDir, binding
from lisflood.lisf1 import Lisfloodexe, get_optionxml_path

from tests import listest, reference_files


current_dir = os.path.dirname(os.path.abspath(__file__))


class TestDrina(object):
    domain = 'efas'
    settings_path = os.path.join(current_dir, 'data/Drina/settings/lisfloodSettings_cold_day_base.xml')

    @classmethod
    def setup_class(cls):
        optionxml = get_optionxml_path()
        Lisfloodexe(cls.settings_path, optionxml)

    # @classmethod
    # def teardown_class(cls):
    #     for var in reference_files:
    #         output_nc = os.path.join(outputDir[0], var) + '.nc'
    #         if os.path.exists(output_nc):
    #             os.remove(output_nc)
    # #     cdf_flags['all'] = 0
    # #     cdf_flags['steps'] = 0
    # #     cdf_flags['end'] = 0

    @listest('dis')
    def test_dis(self):
        pass
