import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

import seaborn as sns


def barplot_from_list(list_, max_num = 12):
    '''Draws a barplot from a list of objects.
    '''

    f, ax = plt.subplots()
    sns.set_color_codes("muted")
    sns.set(style='whitegrid')

    if type(list_[0]) in (int, float):
        sns.distplot(list_)
    else:
        # Makes a pd.Dataframe for convenience
        items = np.array(Counter(list_).most_common(max_num))
        data = pd.DataFrame(items, columns = ['name', 'num'])
        data['num'] = data['num'].astype('int')
        # Seaborn barplot
        sns.barplot(x='num', y='name', data=data, color="b")
        ax.set(ylabel='', xlabel='counter')
    sns.despine(left=True, bottom=True)
    
if __name__ == '__main__':
    print('This a module for custom drawing functions.')

