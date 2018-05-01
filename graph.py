import pandas
from math import pi, sqrt
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, NumeralTickFormatter, LabelSet, Label, Range1d
from bokeh.palettes import Blues, GnBu, Viridis
from bokeh.transform import factor_cmap

#palette = Blues[3]
palette = Viridis[8]

#Read data
df = pandas.read_csv("data.csv")


df['radius'] = (df['Per Source'])/pi
print(df)
print(df['radius'])
for i in range(0,6):
    df.loc[i, 'radius'] = sqrt(df.loc[i, 'radius'])*50000000
df['Circle Bottom'] = df['radius'] + df['Total Killed']
df['width'] = df['Total Killed']/df['Per Source']
#print([row.iloc['Circle Bottom'] for row in df])
#print(df['Circle Bottom'])
print(df['radius'])

df['label'] = "Total Killed "
for i in range(0,6):
    df.loc[i, 'label'] = "Total Killed: " + str(df.loc[i, 'Total Killed'])
print(df)

# Format data
src = ColumnDataSource(df)

# Setup plot
plot = figure(
    plot_width=900, plot_height=600, title="Number of Birds Killed by each Human Activity",
    x_axis_label="Type of Activity", y_axis_label="Number of Birds Killed",
    x_range=[row[0] for row in df.values], y_range=Range1d(0, 2800000000)
)
plot.yaxis[0].formatter = NumeralTickFormatter(format="0.0 a")
#plot.xaxis.major_label_orientation = pi/4
plot.xgrid.grid_line_color = None

# Plot circles
plot.circle(x='Source', y='Circle Bottom', radius='radius', radius_dimension='y', color=factor_cmap('Group', palette=Viridis[4], factors=df['Group'].unique()), alpha=.5, source=src) # TODO make bottom of circle the total killed (instead of center). Needs to be by hand
#plot.circle(x='Source', y='Total Killed', radius='radius', radius_dimension='y', color=palette[1], alpha=.20, source=src)
# plot lines
plot.vbar(x='Source', bottom=0, top='Total Killed', width=.01, source=src, color=factor_cmap('Group', palette=Viridis[4], factors=df['Group'].unique()))

# add labels
#labels = LabelSet(x='Source', y='Total Killed', text='Total Killed', x_offset=5, y_offset=0, source=src)
#catStr = "Total Killed: " + str(df.loc[0, 'Total Killed'])
#cats = Label(x=, y=df['Total Killed'], text=catStr)
#cats = LabelSet(x='Source', y='Total Killed', text='label', source=src)
#plot.add_layout(cats)
#plot.add_layout(labels)

#data_table = DataTable(source=src, columns=)

show(plot)