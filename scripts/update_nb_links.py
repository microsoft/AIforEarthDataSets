#
# update_nb_links.py
#
# To provide a better experience from GH Pages, change notebook links in the
# main README to point to nbviewer.
#

#%% Imports and constants

input_file = r"C:\git\AIforEarthDataSets\README.md"
output_file = r"C:\git\AIforEarthDataSets\README_nb.md"

base_url = 'https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/'


#%% Read input file

with open(input_file,'r') as f:    
    input_lines = f.readlines()
input_lines = [s.strip() for s in input_lines]


#%% Update NB links

output_lines = []

for s in input_lines:
    if '.ipynb' in s:
        s = s.replace('data/',base_url)
    output_lines.append(s)


#%% Write output

def write_list(L,f):
    for s in L:
        f.write(s + '\n')
        
with open(output_file,'w') as f:
    write_list(output_lines,f)
    