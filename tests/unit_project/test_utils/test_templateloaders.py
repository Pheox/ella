from os.path import join, pardir, abspath, dirname

from unittest import TestCase

from nose import tools

from django.template import TemplateDoesNotExist

from ella.utils.template_loaders import _get_template_vars

class TestAppTemplateLoader(TestCase):

    def test_returning_proper_name(self):
        tools.assert_equals("template_name", _get_template_vars("core:template_name")[0])

    def test_returning_proper_dir(self):
        tools.assert_equals(abspath(join(dirname(__file__), pardir, pardir, pardir, 'ella', 'core', 'templates')), _get_template_vars("core:template_name")[1])

    def test_invalid_name_raising_template_exc(self):
        tools.assert_raises(TemplateDoesNotExist, _get_template_vars, \
            "total_invalid_application_do_not_use_or_i_will_kill_you:template_name")
