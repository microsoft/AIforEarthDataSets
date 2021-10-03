#
# Generate links to NOAA Climate Data Record docs from a list of product names
# 

#%% Constants and imports

import requests

input_file = r'c:\git\AIforEarthDataSets\data\cdr-to-containers.csv'
output_file = r'c:\temp\noaa-cdr-list.md'
base_url = 'https://www.ncei.noaa.gov/products/climate-data-records/'

replacement_strings = {'patmosx':'patmos',
                      'ocean-nearsurface-atmospheric-properties':'ocean-near-surface-atmosphere',
                      'amsu-brightness-temperaturenoaa':'amsu-brightness-temperature-noaa',
                      'amsua-brightness-temperature':'amsu-a-brightness-temperature',
                      'amsub-and-mhs-brightness-temperature':'amsu-b-and-mhs-brightness-temperature',
                      'geostationary-ir-channel-brightness-temperature-gridsatb1':'geostationary-IR-channel-brightness-temperature',
                      'mean-layer-temperature-ucar-(lower-stratosphere)':'mean-layer-temperature-ucar-lower-strat',
                      'mean-layer-temperature-ucar-(upper-troposphere-and-lower-stratosphere)':'mean-layer-temperature-ucar',
                      'ssm/i(s)':'ssmis','ssmi/s':'ssmis',
                      '-(northern-hemisphere)':''}


#%% Read input file

with open(input_file,'r') as f:
    product_list = f.readlines()

products = []
for s in product_list:
    if len(s.strip()) == 0:
        continue
    tokens = s.split(',')
    assert len(tokens) == 2
    name = tokens[0].strip()
    container = tokens[1].strip()
    record = {'name':name,'container':container}
    products.append(record)
    

#%% Generate and validate links

from tqdm import tqdm

for p in tqdm(products):
    
    name = p['name']
    
    url = name.lower().replace('cdr','').replace('-','')
    url = ' '.join(url.split())
    url = url.strip().replace(' ','-')
    
    for k in replacement_strings.keys():
        url = url.replace(k,replacement_strings[k])
    
    url = base_url + url

    response = requests.get(url)
    assert response.status_code == 200
    
    p['url'] = url
    

#%% Get container names

from azure.storage.blob import BlobServiceClient

account_name = 'noaacdr'
storage_account_url_blob = 'https://' + account_name + '.blob.core.windows.net'

import os
with open(os.path.expanduser('~/tokens/noaa-cdr-sa_sas.txt'),'r') as f:
    lines = f.readlines()
storage_account_sas_token = lines[0].strip()


blob_service_client = BlobServiceClient(account_url=storage_account_url_blob, 
                                        credential=storage_account_sas_token)

container_iter = blob_service_client.list_containers(include_metadata=False)
container_names = []

for container in container_iter:    
    container_names.append(container['name'])


#%% Map each product ID to a container name

for p in tqdm(products):
    if p['container'] == 'unknown':
        continue
    else:
        assert p['container'] in container_names
        

#%% Generate markdown

output_md = ''

for p in products:
    name = p['name']
    assert ' CDR' in name
    name = name.replace(' CDR','')
    url = p['url']
    container = p['container']
    
    if container == 'unknown':
        s = '* <a href="{}">{}</a>'.format(url,name)
    else:
        s = '* <a href="{}">{}</a> ({})'.format(url,name,container)
    output_md += s + '\n'

with open(output_file,'w') as f:
    f.write(output_md)
