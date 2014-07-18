from clld.web.app import get_configurator

# we must make sure custom models are known at database initialization!
from csd import models


_ = lambda s: s
_('Value')
_('Values')
_('Parameter')
_('Parameters')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = get_configurator('csd', settings=settings)
    config.include('clldmpg')
    config.include('csd.datatables')
    config.include('csd.adapters')
    return config.make_wsgi_app()
