import pytest
import astropy.io.fits as fits
import numina.instrument.generic
import numina.core
from tarsisdrp.loader import load_drp


def create_simple_frame():
    hdr = {'INSTRUME': 'TARSIS', 'INSCONF': '866d074e-bc03-49a6-941a-11ebc1b3f136'}
    hdu = fits.PrimaryHDU(data=[[1]])
    for k, v in hdr.items():
        hdu.header[k] = v
    hdulist = fits.HDUList([hdu])
    frame = numina.core.DataFrame(frame=hdulist)
    return frame


@pytest.mark.parametrize("conf, uuix", [
    ['default', "866d074e-bc03-49a6-941a-11ebc1b3f136"],
    ["866d074e-bc03-49a6-941a-11ebc1b3f136", "866d074e-bc03-49a6-941a-11ebc1b3f136"],
])
def test_loader1(conf, uuix):
    import numina.core
    from numina.instrument.assembly import assembly_instrument

    obs = numina.core.ObservationResult(instrument='TARSIS')
    drpm = load_drp()
    obs.configuration = conf

    key, date_obs, keyname = drpm.select_profile(obs)
    ins = assembly_instrument(drpm.configurations, key, date_obs, by_key=keyname)
    assert isinstance(ins, numina.instrument.generic.InstrumentGeneric)
    assert str(ins.origin.uuid) == uuix
