import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
def filter_and_plot(csv_file, x_value, y_value_1, y_value_2):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Filter the rows based on the input values for 'number' and 'party-code'
    filtered_df = df[(df['congress'] == x_value) & (df['party_code'] == y_value_1)]

    # Sort the rows by 'party-code'
    sorted_df = filtered_df.sort_values(by='nominate_dim1')
    x_array = range(0, len(sorted_df['nominate_dim1']))
    # print(sorted_df['nominate_dim1'])

    # Plot the results
    fig = plt.figure(figsize=(10, 6))
    plt.plot(x_array, sorted_df['nominate_dim1'], 'bo-', label='D', color='blue')

    filtered_df = df[(df['congress'] == x_value) & (df['party_code'] == y_value_2)]
    sorted_df = filtered_df.sort_values(by='nominate_dim1',  ascending=False)
    x_array = range(0, len(sorted_df['nominate_dim1']))
    plt.plot(x_array, sorted_df['nominate_dim1'], 'bo-', label='R', color='red')

    plt.xlabel('Number')
    plt.ylabel('Ideology Score')
    plt.title('Ideology Score by Number and Party Code')
    plt.legend()
    plt.grid(True)
    plt.show()

def anim(x_value):
    x_value = x_value + 80 
    print(x_value, y_value_1, y_value_2, d_avg_min, d_avg_max)
    # Filter the rows based on the input values for 'number' and 'party-code'
    filtered_df = df[(df['congress'] == x_value) & (df['party_code'] == y_value_1)]

    # Sort the rows by 'party-code'
    sorted_df = filtered_df.sort_values(by='nominate_dim1').dropna()
    avg = sum(sorted_df['nominate_dim1'])/len(sorted_df['nominate_dim1'])
    
    x_array = range(0, len(sorted_df['nominate_dim1']))
    line1.set_data(x_array, sorted_df['nominate_dim1'])
    line1_avg.set_data([0,300],[avg,avg])

    filtered_df = df[(df['congress'] == x_value) & (df['party_code'] == y_value_2)]
    sorted_df = filtered_df.sort_values(by='nominate_dim1',  ascending=False).dropna()
    avg = sum(sorted_df['nominate_dim1'])/len(sorted_df['nominate_dim1'])
    x_array = range(0, len(sorted_df['nominate_dim1']))
    line2.set_data(x_array, sorted_df['nominate_dim1'])
    line2_avg.set_data([0,300],[avg,avg])
    year = x_value*2 + 2023-118*2
    date_text.set_text('Congress ' + str(x_value) + ", year " + str(year))
    print(avg)


    return line1, line1_avg, line2, line2_avg, line1_min, line1_max, date_text

# Example usage
#csv_file = 'senate-data.csv'

csv_file = sys.argv[1]
global x_value
x_value = int(sys.argv[2])  # Replace with your specific value for 'number'
x_range = int(sys.argv[3])
y_value_1 = 100  # Replace with your specific value for 'party-code'
y_value_2 = 200  # Replace with your specific value for 'party-code'
global d_avg_min
global d_avg_max

d_avg_min = 0
d_avg_max = -1



#filter_and_plot(csv_file, x_value, y_value_1, y_value_2)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(autoscale_on=False, xlim=(0, x_range), ylim=(-1, 1.))
ax.grid()

line1, = ax.plot([], [], '.-', label='D', color='blue')
line1_avg, = ax.plot([], [], '-', label='D', color='blue')
line2, = ax.plot([], [], '.-', label='R', color='red')
line2_avg, = ax.plot([], [], '-', label='R', color='red')
date_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
global df
df = pd.read_csv(csv_file)

for x_value in range(40, 118):
    filtered_df = df[(df['congress'] == x_value) & (df['party_code'] == y_value_1)]
    # Sort the rows by 'party-code'
    sorted_df = filtered_df.sort_values(by='nominate_dim1').dropna()
    avg = sum(sorted_df['nominate_dim1'])/len(sorted_df['nominate_dim1'])
    if (avg > d_avg_max):
        d_avg_max = avg
    if (avg < d_avg_min):
        d_avg_min = avg
print(d_avg_max, d_avg_min)
line1_min, = ax.plot([0,300], [d_avg_min, d_avg_min], ':', label='D', color='blue')
line1_max, = ax.plot([0,300], [d_avg_max, d_avg_max], ':', label='D', color='blue')

r_avg_max = -1
r_avg_min = 1
for x_value in range(40, 118):
    filtered_df = df[(df['congress'] == x_value) & (df['party_code'] == y_value_2)]
    # Sort the rows by 'party-code'
    sorted_df = filtered_df.sort_values(by='nominate_dim1').dropna()
    avg = sum(sorted_df['nominate_dim1'])/len(sorted_df['nominate_dim1'])
    if (avg > r_avg_max):
        r_avg_max = avg
    if (avg < r_avg_min):
        r_avg_min = avg
print(r_avg_max, r_avg_min)
line2_min, = ax.plot([0,300], [r_avg_min, r_avg_min], ':', label='R', color='red')
line2_max, = ax.plot([0,300], [r_avg_max, r_avg_max], ':', label='R', color='red')

ani = animation.FuncAnimation(fig, anim, 118-80, repeat=False, interval=1000, blit=True)
writer = animation.FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=7200)
ani.save("movie.mp4", writer=writer)

#plt.show()
