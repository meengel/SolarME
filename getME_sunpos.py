### Michael Engel (adapted from John Clark Craig https://levelup.gitconnected.com/python-sun-position-for-solar-energy-and-research-7a4ead801777) ### 2022-01-31 ### getME_sunpos.py ###
from .dnppy_solar import solar, datetime
import numpy as np

def getME_sunpos(lons, lats, timestamp=None, timezone=0, timeformat=None, key=None):
    if timestamp==None:
        timestamp = datetime.today()
        
    solarobj = solar(lat=np.array(lats),lon=np.array(lons),date_time_obj=timestamp,time_zone=timezone,fmt=timeformat)
    
    if key==None:
        out = {'azimuth':solarobj.get_azimuth(),
               'elevation':solarobj.get_elevation()}
    elif key=='array':
        out = np.stack((solarobj.get_azimuth(),solarobj.get_elevation()))
    elif key=='azimuth':
        out = solarobj.get_azimuth()
    elif key=='elevation':
        out = solarobj.get_elevation()
    elif key=='obj':
        out = solarobj
    else:
        print('getME_sunpos: wrong key chosen!')
        out = False
    
    return out