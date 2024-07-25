import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.affinity import scale, translate

def plot_map(election_results, out_file, title, flipped_states, fig, ax):

    # Dictionary of 2020 election results (Blue for Biden, Red for Trump)

    # Map state abbreviations to election results
    states['color'] = states['STUSPS'].map(election_results)

    # Scale down Alaska and move it to the bottom left corner
    alaska = states[states['STUSPS'] == 'AK'].copy()
    alaska.geometry = alaska.geometry.apply(lambda x: scale(x, xfact=0.35, yfact=0.33, origin='center'))
    alaska.geometry = alaska.geometry.apply(lambda x: translate(x, xoff=-65, yoff=-32))

    # Scale down Hawaii and move it to the bottom left corner
    hawaii = states[states['STUSPS'] == 'HI'].copy()
    hawaii.geometry = hawaii.geometry.apply(lambda x: translate(x, xoff=+50, yoff=7))

    # Exclude Alaska and Hawaii from the main states data frame
    mainland = states[~states['STUSPS'].isin(['AK', 'HI', 'PR', 'DC'])]

    # Plot the map
    mainland.boundary.plot(ax=ax, linewidth=1, color='black')
    mainland.plot(ax=ax, color=mainland['color'])
    alaska.boundary.plot(ax=ax, linewidth=1)
    alaska.plot(ax=ax, color=alaska['color'])
    hawaii.boundary.plot(ax=ax, linewidth=1)
    hawaii.plot(ax=ax, color=hawaii['color'])

    # Plot the map
    #fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    #states.boundary.plot(ax=ax, linewidth=1)
    #states.plot(ax=ax, color=states['color'])

    # Add title
    #plt.title(title, fontsize=20)
    #plt.xlim(-128,-66)
    #plt.axis('off')
    ax.axis('on')
    ax.set_title(title, fontsize=12, color='red' if '(R)' in title else 'blue')
    ax.set_xlim(-128,-66)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.yaxis.set_ticks([])
    ax.xaxis.set_ticks([])
    ax.set_xlabel(flipped_states, color='black', fontsize=8)
    # Save the map to a PNG file
    #plt.savefig('us_election_map_2020.png')

    # Display the map
    # plt.show()

election_results_2020 = {
    "AL": "red", "AK": "red", "AZ": "blue", "AR": "red", "CA": "blue",
    "CO": "blue", "CT": "blue", "DE": "blue", "FL": "red", "GA": "blue",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "blue", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}

election_results_1976 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "blue", "CA": "blue",
    "CO": "red", "CT": "blue", "DE": "blue", "FL": "blue", "GA": "blue",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "blue",
    "KS": "red", "KY": "red", "LA": "blue", "ME": "red", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "blue", "MO": "blue",
    "MT": "red", "NE": "red", "NV": "red", "NH": "red", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "blue", "ND": "red", "OH": "blue",
    "OK": "red", "OR": "red", "PA": "blue", "RI": "blue", "SC": "blue",
    "SD": "red", "TN": "blue", "TX": "red", "UT": "red", "VT": "red",
    "VA": "red", "WA": "blue", "WV": "blue", "WI": "blue", "WY": "red",
}

election_results_1980 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "red",
    "CO": "red", "CT": "red", "DE": "red", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "red", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "red", "MD": "red",
    "MA": "red", "MI": "red", "MN": "red", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "red", "NH": "red", "NJ": "red",
    "NM": "red", "NY": "red", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "red", "PA": "red", "RI": "red", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "red",
    "VA": "red", "WA": "red", "WV": "red", "WI": "red", "WY": "red",
}

election_results_1984 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "red",
    "CO": "red", "CT": "red", "DE": "red", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "red", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "red", "MD": "red",
    "MA": "red", "MI": "red", "MN": "red", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "red", "NH": "red", "NJ": "red",
    "NM": "red", "NY": "red", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "red", "PA": "red", "RI": "red", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "red",
    "VA": "red", "WA": "red", "WV": "red", "WI": "red", "WY": "red",
}

election_results_1988 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "red",
    "CO": "red", "CT": "red", "DE": "blue", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "red", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "red", "MD": "blue",
    "MA": "blue", "MI": "red", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "red", "NH": "red", "NJ": "red",
    "NM": "red", "NY": "red", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "red", "PA": "red", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "red",
    "VA": "red", "WA": "red", "WV": "red", "WI": "red", "WY": "red",
}

election_results_1992 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "blue", "CA": "blue",
    "CO": "blue", "CT": "blue", "DE": "blue", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "blue",
    "KS": "red", "KY": "red", "LA": "blue", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "blue",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "blue", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "red", "WA": "blue", "WV": "blue", "WI": "blue", "WY": "red",
}
election_results_1996 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "blue", "CA": "blue",
    "CO": "red", "CT": "blue", "DE": "blue", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "blue",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "blue",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "red", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}
election_results_2000 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "blue",
    "CO": "red", "CT": "blue", "DE": "blue", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "blue",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "red", "NH": "red", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "red", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}
election_results_2004 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "blue",
    "CO": "red", "CT": "blue", "DE": "blue", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "red", "NH": "red", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "red", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}
election_results_2008 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "blue",
    "CO": "blue", "CT": "blue", "DE": "blue", "FL": "blue", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "blue", "IA": "blue",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "blue", "ND": "red", "OH": "blue",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "blue", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}
election_results_2012 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "blue",
    "CO": "blue", "CT": "blue", "DE": "blue", "FL": "blue", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "blue",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "blue",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "blue", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}
election_results_2016 = {
    "AL": "red", "AK": "red", "AZ": "red", "AR": "red", "CA": "blue",
    "CO": "blue", "CT": "blue", "DE": "blue", "FL": "red", "GA": "red",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "red", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "red", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "blue", "WA": "blue", "WV": "red", "WI": "red", "WY": "red",
}
election_results_2020 = {
    "AL": "red", "AK": "red", "AZ": "blue", "AR": "red", "CA": "blue",
    "CO": "blue", "CT": "blue", "DE": "blue", "FL": "red", "GA": "blue",
    "HI": "blue", "ID": "red", "IL": "blue", "IN": "red", "IA": "red",
    "KS": "red", "KY": "red", "LA": "red", "ME": "blue", "MD": "blue",
    "MA": "blue", "MI": "blue", "MN": "blue", "MS": "red", "MO": "red",
    "MT": "red", "NE": "red", "NV": "blue", "NH": "blue", "NJ": "blue",
    "NM": "blue", "NY": "blue", "NC": "red", "ND": "red", "OH": "red",
    "OK": "red", "OR": "blue", "PA": "blue", "RI": "blue", "SC": "red",
    "SD": "red", "TN": "red", "TX": "red", "UT": "red", "VT": "blue",
    "VA": "blue", "WA": "blue", "WV": "red", "WI": "blue", "WY": "red",
}

election_summary = {
    1976: {
        "president": "Jimmy Carter",
        "party": "Democrat",
        "republican_electoral_votes": 240,
        "democrat_electoral_votes": 297,
        "electoral_map_colors": election_results_1976
    },
    1980: {
        "president": "Ronald Reagan",
        "party": "Republican",
        "republican_electoral_votes": 489,
        "democrat_electoral_votes": 49,
        "electoral_map_colors": election_results_1980
    },
    1984: {
        "president": "Ronald Reagan",
        "party": "Republican",
        "republican_electoral_votes": 525,
        "democrat_electoral_votes": 13,
        "electoral_map_colors": election_results_1984
    },
    1988: {
        "president": "George H. W. Bush",
        "party": "Republican",
        "republican_electoral_votes": 426,
        "democrat_electoral_votes": 111,
        "electoral_map_colors": election_results_1988
    },
    1992: {
        "president": "Bill Clinton",
        "party": "Democrat",
        "republican_electoral_votes": 168,
        "democrat_electoral_votes": 370,
        "electoral_map_colors": election_results_1992
    },
    1996: {
        "president": "Bill Clinton",
        "party": "Democrat",
        "republican_electoral_votes": 159,
        "democrat_electoral_votes": 379,
        "electoral_map_colors": election_results_1996
    },
    2000: {
        "president": "George W. Bush",
        "party": "Republican",
        "republican_electoral_votes": 271,
        "democrat_electoral_votes": 266,
        "electoral_map_colors": election_results_2000
    },
    2004: {
        "president": "George W. Bush",
        "party": "Republican",
        "republican_electoral_votes": 286,
        "democrat_electoral_votes": 251,
        "electoral_map_colors": election_results_2004
    },
    2008: {
        "president": "Barack Obama",
        "party": "Democrat",
        "republican_electoral_votes": 173,
        "democrat_electoral_votes": 365,
        "electoral_map_colors": election_results_2008
    },
    2012: {
        "president": "Barack Obama",
        "party": "Democrat",
        "republican_electoral_votes": 206,
        "democrat_electoral_votes": 332,
        "electoral_map_colors": election_results_2012
    },
    2016: {
        "president": "Donald Trump",
        "party": "Republican",
        "republican_electoral_votes": 304,
        "democrat_electoral_votes": 227,
        "electoral_map_colors": election_results_2016
    },
    2020: {
        "president": "Joe Biden",
        "party": "Democrat",
        "republican_electoral_votes": 232,
        "democrat_electoral_votes": 306,
        "electoral_map_colors": election_results_2020
    }
}


# Load a shapefile of US states
#states = gpd.read_file("https://www2.census.gov/geo/tiger/GENZ2020/shp/cb_2020_us_state_20m.zip")
states = gpd.read_file("cb_2020_us_state_20m.zip")


fig, axes = plt.subplots(3, 4, figsize=(15, 10))
axes_l = axes.flat
states_leaning = {}
for state, result in election_results_1976.items():
#    print(f"{state}: {result}")
    states_leaning[state] = 0

prev = election_results_1976
for i, a in enumerate(range(1976, 2024,4)):
    print(a)
    res = election_summary[a]
    title = str(a) + ':' + res['president']
    if (res['republican_electoral_votes'] >= 270):
        title = title + " (R)"
        title = title + str(res['republican_electoral_votes']) + ' - ' + str(res['democrat_electoral_votes'])
    else:
        title = title + " (D)"
        title = title + str(res['democrat_electoral_votes']) + ' - ' + str(res['republican_electoral_votes'])
    out_file = 'emap-' + str(a) + '.png'
    print(i)
    ax = axes_l[i]
    ax.axis('off')

    for j,k in res['electoral_map_colors'].items():
        if (k == 'red'):
            states_leaning[j] += 1 
    
    print("Flipped states blue to red compared to previous", end = ' ')
    for state, result in prev.items():
        if result != res['electoral_map_colors'][state] and result == 'red':
#            print(state, result, '->', res['electoral_map_colors'][state], end=' ')
             print(state, end=' ')
    print(" ")
    print("Flipped states red to blue compared to previous", end = ' ')
    for state, result in prev.items():
        if result != res['electoral_map_colors'][state] and result == 'blue':
#            print(state, result, '->', res['electoral_map_colors'][state], end=' ')
             print(state, end=' ')
    print(" ")

    print("Flipped states blue to red compared to 2004", end = ' ')
    flipped_states = '(X) Red->Blue:'
    n = 0
    for state, result in election_results_2004.items():
        if result != res['electoral_map_colors'][state] and result == 'red':
#            print(state, result, '->', res['electoral_map_colors'][state], end=' ')
             print(state, end=' ')
             flipped_states += ' ' + state
             n += 1
    flipped_states = flipped_states.replace('(X)', '(+' + str(n) + ')')
    print(" ")
    print("Flipped states red to blue compared to 2004", end = ' ')
    flipped_states += '\n(Y)Blue->Red:'
    n = 0
    for state, result in election_results_2004.items():
        if result != res['electoral_map_colors'][state] and result == 'blue':
#            print(state, result, '->', res['electoral_map_colors'][state], end=' ')
             print(state, end=' ')
             flipped_states += ' ' + state
             n += 1
    flipped_states = flipped_states.replace('(Y)', '(-' + str(n) + ')')
    print(" ")
    if a in [1980, 1984, 1988]:
        flipped_states = ' '
    plot_map(res['electoral_map_colors'], out_file, title, flipped_states, fig, ax)
    prev = res['electoral_map_colors']
sorted_state_scores = sorted(states_leaning.items(), key=lambda item: item[1], reverse=True)

# Print the sorted dictionary
new_map = {}
for state, score in sorted_state_scores:
    new_map[state] = 'blue'
    if score-6 > -2:
        new_map[state] = 'red'

plt.savefig('emap.png', dpi=600, bbox_inches='tight', pad_inches=0)
plt.tight_layout()
plt.show()


fig, ax = plt.subplots(1, 1, figsize=(15, 10))
plot_map(new_map, 'ave-map.png', 'Averaged map', ' ', fig, ax)
plt.savefig('ave-map.png', dpi=600, bbox_inches='tight', pad_inches=0)
plt.tight_layout()
plt.show()
