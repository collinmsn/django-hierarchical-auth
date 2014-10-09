#!/usr/bin/env python

import os, sys
from django.test.runner import DiscoverRunner
from django.conf import settings
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'hierarchical_auth.tests.test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))

sys.path.insert(0, parent)


def runtests():
    django.setup() 
    discover_runner = DiscoverRunner()
    discover_runner.run_tests(['tests'], verbosity=1, interactive=True)

if __name__ == '__main__':
    runtests()

