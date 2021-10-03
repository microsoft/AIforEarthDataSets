#
# sort_datasets.py
#
# Sorts data sets alphabetically in the main README.
#

#%% Imports and constants

input_file = r"C:\git\AIforEarthDataSets\README.md"
output_file = r"C:\git\AIforEarthDataSets\README_sorted.md"
data_start_token = '# Data sets'
data_end_token = '# '


#%% Read input file

with open(input_file,'r') as f:    
    input_lines = f.readlines()
input_lines = [s.strip() for s in input_lines]


#%% Parse input file

# Lines before/after the data sets
header = []
footer = []
states = ['header','data','footer']
state = 'header'

# Mapping from data set name to text
datasets = {}
current_dataset = None

for s in input_lines:
    
    if state == 'header':
        if s.startswith(data_start_token):
            header.append(s)
            header.append('')
            state = 'data'
        else:
            header.append(s)
    elif state == 'footer':
        footer.append(s)
    else:
        assert state == 'data'
        if s.startswith(data_end_token):
            state = 'footer'
            footer.append(s)
        else:            
            if s.startswith('##'):
                assert s not in datasets
                datasets[s] = [s]
                current_dataset = s                
            else:                
                assert not s.startswith('#')
                if current_dataset is not None:
                    datasets[current_dataset].append(s)

# ...for each line

data_lines = []

for k in sorted(datasets.keys()):
    dataset_lines = datasets[k]
    for s in dataset_lines:
        data_lines.append(s)
    data_lines += ''

# datasets[list(datasets.keys())[0]]


#%% Write output file

def write_list(L,f):
    for s in L:
        f.write(s + '\n')
        
with open(output_file,'w') as f:
    write_list(header,f)
    write_list(data_lines,f)
    write_list(footer,f)
    