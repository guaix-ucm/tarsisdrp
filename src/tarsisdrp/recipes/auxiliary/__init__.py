#
# Copyright 2025 Universidad Complutense de Madrid
#
# This file is part of TARSIS DRP
#
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSE
#

from astropy.io import fits

from numina.core import Result
from numina.core.recipes import BaseRecipe
from numina.core.requirements import ObservationResultRequirement
from numina.util.context import manage_fits

from tarsisdrp.products import TarsisFrame


class Test1Recipe(BaseRecipe):
    """
    Test recipe: subtracts two images.
    """

    obresult = ObservationResultRequirement()

    reduced_image = Result(TarsisFrame)

    def run(self, rinput):
        frames = rinput.obresult.frames
        nimages = len(frames)
        if nimages != 2:
            raise ValueError(f'Expected 2 images, got {nimages}')
        with manage_fits(frames) as list_of:
            image1 = list_of[0]
            image2 = list_of[1]
            data = image1[0].data - image2[0].data
            header = image1[0].header
            hdu = fits.PrimaryHDU(data, header)
            reduced_image = hdu

        return self.create_result(reduced_image=reduced_image)

