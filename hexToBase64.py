#!/usr/bin/env python

"""
Converts from hexadecimal to base-64.
"""

import sys
import os.path import basename


def main(hex_string):
    """Handle command line parameters"""
    
    try:
        
    except Exception as e:
        script_name = basename(__file__)
        print 'Usage: ' + script_name + ' <hex-value>'


if __name__ == "__main__":
    main(sys.argv[1])
