"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_admin_assets(app):
    """Configure logged-in asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    less_bundle = Bundle('src/less/account.less',
                         filters='less,cssmin',
                         output='dist/css/account.css',
                         extra={'rel': 'stylesheet/less'})
    # Register global_assets
    assets.register('less_all', less_bundle)
    # Build global_assets in development mode
    if app.config['FLASK_ENV'] == 'development':
        less_bundle.build(force=True)