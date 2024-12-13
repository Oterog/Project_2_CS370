# -*- coding: utf-8 -*-
"""Setup the turbogearsApp application"""
from __future__ import print_function, unicode_literals
import transaction
from turbogearsapp import model

def bootstrap(command, conf, vars):
    """Place any commands to setup turbogearsapp here"""
    print("Bootstrapping the application...")

    try:
        # Add any initial data setup here (if needed)
        transaction.commit()
    except Exception as e:
        print('Error during bootstrapping:', e)
        transaction.abort()
