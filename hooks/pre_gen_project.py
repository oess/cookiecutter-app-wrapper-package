import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, package_name):
    print('ERROR: %s is not a valid Python module name. Please do not use a - and use _ instead' % package_name)
    sys.exit(1)
