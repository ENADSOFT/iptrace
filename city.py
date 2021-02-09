import geoip2

 # This creates a Reader object. You should use the same object
 # across multiple requests as creation of it is expensive.
reader = geoip2.database.Reader('')
 
# Replace "city" with the method corresponding to the database
# that you are using, e.g., "country".
response = reader.city('128.101.101.101')
 
response.country.iso_code
'US'
response.country.name
'United States'
response.country.names['zh-CN']
u'美国'
 
response.subdivisions.most_specific.name
'Minnesota'
response.subdivisions.most_specific.iso_code
'MN'
 
response.city.name
'Minneapolis'
 
response.postal.code
'55455'
 
response.location.latitude
44.9733
response.location.longitude
-93.2323
 
response.traits.network
IPv4Network('128.101.101.0/24')
 
reader.close()