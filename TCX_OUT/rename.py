# rename `xxxxxxx户外跑步.tcx..bin` to `xxxx-xx-xx.tcx`

import os
import re

def rename():
    path = '.'
    files = os.listdir(path)
    for file in files:
        if file.endswith('.tcx..bin'):
            date = re.search(r'\d{8}', file).group()
            new_name = date[:4] + '-' + date[4:6] + '-' + date[6:] + '.tcx'
            os.rename(os.path.join(path, file), os.path.join(path, new_name))

if __name__ == '__main__':
    rename()
    print('Done!')