"""
Mixin for Flask-specific functionality. This aides the migration between Pylons and Flask.
"""
import ckan.plugins as p


class MixinPlugin(object):

    # IConfigurer
    def update_config(self, config):
        p.toolkit.add_public_directory(config, '../public')

    # ITemplateHelpers
    def get_helpers(self):
        return {}
