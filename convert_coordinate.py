from astropy import units as u
from astropy.coordinates import SkyCoord

# Luhman 16A
c = SkyCoord('10 49 19.0 -53 19 10', unit=(u.hourangle, u.deg))
print(c)

# Luhman 16B
c = SkyCoord('10 49 18.9 -53 19 09', unit=(u.hourangle, u.deg))
print(c)

# Gl 229B
c = SkyCoord('06 10 34.80 -21 52 00.0', unit=(u.hourangle, u.deg))
print(c)

# 2MASS J00064325-0732147
c = SkyCoord('00 06 43.1972293497 -07 32 17.024270968', unit=(u.hourangle, u.deg))
print(c)
