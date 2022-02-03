import initializing


map_regions = []
map_province_names = ['adr','aeg','alb','ank','apu','arm','bal','bar','bel','ber','bla','boh','bre','bud','bul',
                'bur','cly','con','den','eas','edi','eng','fin','gal','gas','gre','lyo','bot','hel','hol',
                'ion','ire','iri','kie','lvp','lvn','lon','mar','mao','mos','mun','nap','nao','naf','nth',
                'nor','nwg','par','pic','pie','por','pru','rom','ruh','rum','ser','sev','sil','ska','smy',
                'spa','stp','swe','swi','syr','tri','tun','tus','tyr','tyys','ukr','ven','vie','wal','war',
                'wes','yor']

# water, coast, land, home_supply, supply, coast_home_supply, coast_supply, impassable


map_province_types = ['sea','sea','coast','coast_home_supply','coast','coast','sea','sea','coast_home_supply',
                    'coast_home_supply','sea','land','coast_home_supply','home_supply','coast_supply','land',
                    'coast','coast_home_supply','coast_supply','sea','coast','coast','coast','coast_supply',
                    'sea','sea','sea','coast_supply','sea','impassable','sea','coast_home_supply',
                    'coast_home_supply','coast','coast_home_supply','coast_home_supply','sea','home_supply',
                    'home_supply','coast_home_supply','sea','coast','sea','coast_home_supply','home_supply',
                    'coast','coast','coast_supply','coast','coast_home_supply','land','coast_supply','supply',
                    'coast_home_supply','land','sea','coast_home_supply','coast_supply','coast_home_supply',
                    'coast_supply','impassable','coast','coast_home_supply','coast_supply','coast','land',
                    'sea','land','coast_home_supply','home_supply','coast','home_supply','sea','coast']

print(len(map_province_names))
print(len(map_province_types))

























