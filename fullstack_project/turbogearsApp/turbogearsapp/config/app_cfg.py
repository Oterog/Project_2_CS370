# -*- coding: utf-8 -*-
"""
Global configuration file for TG2-specific settings in turbogearsApp.

This file complements development/deployment.ini.
"""
from tg import FullStackApplicationConfigurator
import turbogearsapp
from turbogearsapp import model

base_config = FullStackApplicationConfigurator()

# General configuration
base_config.update_blueprint({
    'disable_request_extensions': False,
    'dispatch_path_translator': True,
    'package': turbogearsapp,
})

# ToscaWidgets configuration
base_config.update_blueprint({
    'tw2.enabled': True,
})

# Rendering Engines Configuration
rendering_config = {
    'renderers': ['kajiki'],  # Use Kajiki for XHTML templates
    'default_renderer': 'kajiki',
    'templating.kajiki.strip_text': False,  # Avoid whitespace stripping
}
base_config.update_blueprint(rendering_config)

# Configure Sessions, store data as JSON to avoid pickle security issues
base_config.update_blueprint({
    'session.enabled': True,
    'session.data_serializer': 'json',
})

# Configure the base SQLAlchemy Setup
base_config.update_blueprint({
    'use_sqlalchemy': True,
    'model': turbogearsapp.model,
    'DBSession': turbogearsapp.model.DBSession,
})

# Authentication setup (optional, can be customized further)
from tg.configuration.auth import TGAuthMetadata

class ApplicationAuthMetadata(TGAuthMetadata):
    def __init__(self, dbsession, user_class):
        self.dbsession = dbsession
        self.user_class = user_class

    def authenticate(self, environ, identity):
        login = identity.get('login')
        user = self.dbsession.query(self.user_class).filter_by(user_name=login).first()

        if not user or not user.validate_password(identity['password']):
            from tg.exceptions import HTTPFound
            from urllib.parse import urlencode
            params = {'failure': 'invalid-login'}
            environ['repoze.who.application'] = HTTPFound(
                location=environ['SCRIPT_NAME'] + '/login?' + urlencode(params)
            )
            return None
        return user.user_name

    def get_user(self, identity, userid):
        return self.dbsession.query(self.user_class).filter_by(user_name=userid).first()

    def get_groups(self, identity, userid):
        return [g.group_name for g in identity['user'].groups]

    def get_permissions(self, identity, userid):
        return [p.permission_name for p in identity['user'].permissions]

# Configure authentication backend
# base_config.update_blueprint({
#     'auth_backend': 'sqlalchemy',
#     'sa_auth.cookie_secret': "b7934eb5-b2c1-4aff-a69c-264c9be0a335",  # Replace in production
#     'sa_auth.authmetadata': ApplicationAuthMetadata(model.DBSession, model.User),
#     'sa_auth.post_login_url': '/post_login',
#     'sa_auth.post_logout_url': '/post_logout',
#     'identity.allow_missing_user': False,
# })

# Enable DebugBar if available
try:
    from tgext.debugbar import enable_debugbar
    enable_debugbar(base_config)
except ImportError:
    pass
