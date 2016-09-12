# -*- coding: utf-8 -*-

# Import python libs
from __future__ import absolute_import
from urlparse import urljoin
import logging
import requests

# Set up logging
log = logging.getLogger(__name__)


def ext_pillar(minion_id,  # pylint: disable=W0613
               pillar,  # pylint: disable=W0613
               url):

    url = urljoin(url, '/api/v1/rpms')
    log.info('URL to REST servise is ' + url)
    r = requests.get(url, params='hostname=' + __grains__['fqdn'])

    try:
        return r.json()
    except Exception:
        log.critical(
                'JSON data from {0} failed to parse'.format(r.json())
                )
        return {}
