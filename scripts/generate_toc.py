#
# generate_toc.py
#
# Generates a TOC for the "AI for Earth Datasets" main markdown file.
#

#%% Imports and constants

input_file = r"C:\git\AIforEarthDataSets\README.md"
output_file = r"C:\git\AIforEarthDataSets\TOC.md"
target_header_level = '##'
exclude_names = set(['Contributing','Trademarks'])


#%% Read input file

with open(input_file,'r') as f:    
    input_lines = f.readlines()
input_lines = [s.strip() for s in input_lines]


#%% Make TOC

toc = []

toc.append('# Table of contents\n')

for s in input_lines:
    if s.startswith(target_header_level):        
        tokens = s.split(' ',1)
        assert tokens[0].startswith('##')
        link_name = tokens[1]
        if link_name not in exclude_names:
            target_link = '#' + link_name.lower().replace(' ','-').\
                replace('(','').replace(')','').replace('/','').replace(',','').replace(':','')
            toc.append('* [{}]({})'.format(link_name,target_link))

#%% Write output

with open(output_file,'w') as f:
    for s in toc:
        print(s)
        snl = s + '\n'
        f.write(snl)
