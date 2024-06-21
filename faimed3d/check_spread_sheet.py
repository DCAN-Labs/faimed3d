import pandas as pd
import os.path

df = pd.read_csv('/panfs/jay/groups/4/miran045/reine097/projects2/faimed3d/nbs/../../faimed3d/data/cdni/cases.csv')
for fname in df['file']:
    if not os.path.isfile(fname):
        print(f'nonexistent path:{fname}')
