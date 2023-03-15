import pandas as pd

geoip = pd.read_csv('/root/GeoLite2xtables/GeoIP-legacy.csv')
geoip = geoip.iloc[:, [0,1,4]]

geoip.to_csv('GeoIP-legacy.csv', index=None)