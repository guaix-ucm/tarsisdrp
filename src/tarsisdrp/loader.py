#
# Copyright 2022 Universidad Complutense de Madrid
#
# This file is part of TARSIS DRP
#
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSE
#

"""Load TARSIS DRP"""

from numina.core import drp_load


def load_drp():
    """Entry point to load TARSIS DRP."""
    return drp_load('tarsisdrp', 'drp.yaml')

