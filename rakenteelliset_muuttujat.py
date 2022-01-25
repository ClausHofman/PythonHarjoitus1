# Luodaan LISTA viikonpäivistä, ei välttämättä tarvitse olla välilyöntejä
viikonpaivat = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']

# Testataan tulostuskomennolla
print('Viikon ensimmäinen päivä on', viikonpaivat[0])

# SANAKIRJA eli dict viikonpäivistä suomi - englanti, {} aaltosulkeet
day_names = {'maanantai':'monday', 'tiistai':'tuesday', 'keskiviikko':'wednesday', 'torstai':'thursday', 'perjantai':'friday', 'lauantai':'saturday', 'sunnuntai':'sunday'}

# Testataan tulostuskomennolla
print('Tiistai on englanniksi',day_names['tiistai'],'ja keskiviikko on',day_names['keskiviikko'] )
print('Wednesday on suomeksi',viikonpaivat[2], 'ja friday on',viikonpaivat[4])