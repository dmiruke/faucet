"""Valve Manager base class"""

# pylint: disable=R0201
# pylint: disable=W0613
class ValveManagerBase(object):
    """Base class for ValveManager objects.

    Expected to control the installation of flows into datapath tables.

    Ideally each datapath table should be controlled by 1 manager only."""

    def initialise_tables(self):
        '''initialise tables controlled by this manager'''
        return []
