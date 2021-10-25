#
# update_nb_links.py
#
# To provide a better experience from GH Pages, change notebook links in the
# main README and in individual dataset .md files to point to nbviewer.
#

#%% Imports and constants

import os

input_readme_file = r"C:\git\AIforEarthDataSets\README.md"
output_readme_file = r"C:\git\AIforEarthDataSets\README_nb.md"
input_data_dir = r"C:\git\AIforEarthDataSets\data"

assert os.path.isfile(input_readme_file)
assert os.path.isdir(input_data_dir)

base_url = 'https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/'

custom_encodings = {'gbif.md':'utf-8','uk-met-20crds.md':'utf-8','uk-met-covid-19.md':'utf-8','doe-wave.md':'utf-8'}


#%% Replacement function

import re
pat = '\((.*)\.ipynb\)'
p = re.compile(pat)

def write_list(L,f):
    for s in L:
        f.write(s + '\n')

def replace_notebook_links(input_file,output_file=None):
    
    encoding = None
    fn = os.path.basename(input_file)
    if fn in custom_encodings:
        encoding = custom_encodings[fn]

    if output_file is None:
        output_file = input_file

    with open(input_file,'r',encoding=encoding) as f:    
        input_lines = f.readlines()
    input_lines = [s.rstrip() for s in input_lines]
    
    output_lines = []
    replaced_lines = []
    
    # Make replacements
    for s in input_lines:
        out_s = s
        if '.ipynb' in s and 'nbviewer' not in s:
            if 'data/' in s:
                assert fn == 'README.md'
                out_s = s.replace('data/',base_url)
            else:
                assert fn != 'README.md'
                out_s = p.sub('(' + base_url+'\\1' + '.ipynb)',s)
            print('Replacing:\n{}\n{}\n\n'.format(s,out_s))
            replaced_lines.append(out_s)
        output_lines.append(out_s)
    
    # Write output

    if len(replaced_lines) > 0:        
        with open(output_file,'w',encoding=encoding) as f:
            write_list(output_lines,f)    


#%% Update links in README.md

replace_notebook_links(input_readme_file,output_readme_file)


#%% Update links in individual .md files

# List .md files
md_files = os.listdir(input_data_dir)
md_files = [os.path.join(input_data_dir,s) for s in md_files if s.endswith('.md')]

for s in md_files:
    # input_file = s; output_file = None
    replace_notebook_links(s)
    