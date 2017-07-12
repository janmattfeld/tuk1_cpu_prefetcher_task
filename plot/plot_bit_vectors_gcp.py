import matplotlib.pyplot as plt
import pandas as pds
import numpy as np
import operator as o

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12

# read results
dpoints = pds.read_csv('./results/bit_vector_table_scan.csv', ';', skipinitialspace=True)
dpoints = dpoints.values

fig = plt.figure()
ax = fig.add_subplot(111)


def barplot(ax, dpoints):
    conditions = [(c, np.max(dpoints[dpoints[:, 0] == c][:, 2].astype(float)))
                  for c in np.unique(dpoints[:, 0])]
    categories = [(c, np.max(dpoints[dpoints[:, 1] == c][:, 2].astype(float)))
                  for c in np.unique(dpoints[:, 1])]

    conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
    categories = [c[0] for c in sorted(categories, key=o.itemgetter(1))]

    dpoints = np.array(sorted(dpoints, key=lambda x: categories.index(x[1])))

    space = 0.5
    n = len(conditions)
    width = (1 - space) / (len(conditions))

    for i, cond in enumerate(conditions):
        indeces = range(1, len(categories) + 1)
        vals = dpoints[dpoints[:, 0] == cond][:, 2].astype(np.float)
        pos = [j - (1 - space) / 2. + i * width for j in indeces]
        ax.bar(pos, vals, width=width, label=cond)

    ax.set_xticks(indeces)
    ax.set_xticklabels(categories)
    plt.setp(plt.xticks()[1])

    plt.title('AVX Implementations on Table Scan', y=1.10)

    ax.set_ylabel("Tuples per Second")

    plt.figtext(0, 0, 'Google Cloud Platform Instances: 4 vCPUs, 16 GB Ram', fontsize=8)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])
    plt.legend(frameon=False)

    # Remove the plot frame lines.
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Remove the tick marks and use a grid instead.
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='on', left='off', right='off', labelleft='on')


barplot(ax, dpoints)
plt.ylim([0,700000000])
plt.savefig('./plot/' + '4_bit_vector_table_scan' + '.pdf', bbox_inches='tight', dpi=200)
plt.savefig('./plot/' + '4_bit_vector_table_scan' + '.png', bbox_inches='tight', dpi=200)


dpoints = pds.read_csv('./results/bit_vector_point_lookup.csv', ';', skipinitialspace=True)
dpoints = dpoints.values

fig = plt.figure()
ax = fig.add_subplot(111)

def barplot2(ax, dpoints):
    conditions = [(c, np.max(dpoints[dpoints[:, 0] == c][:, 2].astype(float)))
                  for c in np.unique(dpoints[:, 0])]
    categories = [(c, np.max(dpoints[dpoints[:, 1] == c][:, 2].astype(float)))
                  for c in np.unique(dpoints[:, 1])]

    conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
    categories = [c[0] for c in sorted(categories, key=o.itemgetter(1))]

    dpoints = np.array(sorted(dpoints, key=lambda x: categories.index(x[1])))

    space = 0.5
    n = len(conditions)
    width = (1 - space) / (len(conditions))

    for i, cond in enumerate(conditions):
        indeces = range(1, len(categories) + 1)
        vals = dpoints[dpoints[:, 0] == cond][:, 2].astype(np.float)
        pos = [j - (1 - space) / 2. + i * width for j in indeces]
        ax.bar(pos, vals, width=width, label=cond)

    ax.set_xticks(indeces)
    ax.set_xticklabels(categories)
    plt.setp(plt.xticks()[1])

    plt.title('Point Lookups', y=1.10)

    ax.set_ylabel("Tuples per Second")

    plt.figtext(0, 0, 'Google Cloud Platform Instances: 4 vCPUs, 16 GB Ram', fontsize=8)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])
    plt.legend(frameon=False)

    # Remove the plot frame lines.
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Remove the tick marks and use a grid instead.
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='on', left='off', right='off', labelleft='on')

barplot2(ax, dpoints)
plt.ylim([0,700000000])
plt.savefig('./plot/' + '4_bit_vector_point_lookups' + '.pdf', bbox_inches='tight', dpi=200)
plt.savefig('./plot/' + '4_bit_vector_point_lookups' + '.png', bbox_inches='tight', dpi=200)