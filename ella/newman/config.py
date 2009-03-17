"""
This module is intended to hold default constants. 
Constants may be modified via project settings.py.
"""

NEWMAN_URL_PREFIX = 'nm'

# AdminSettings
USER_CONFIG = 'newman_user_config'            # session key for AdminSettings JSON data
CATEGORY_FILTER = 'newman_category_filter'    # user defined category filtering on newman HP

# conversion functions mapping - from JSON to python (i.e. changing item datatypes etc.)
JSON_CONVERSIONS = (
    (CATEGORY_FILTER, 'decode_category_filter_json'),
)


# TODO try to load consts from django.conf.settings