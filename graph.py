import pandas
from math import pi
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d

#Read data
df = pandas.read_csv("data.csv")

#Format data
src = ColumnDataSource(df)

#Setup plot
plot = figure(
    plot_width=600, plot_height=600,
    x_axis_label="Type of Activity", y_axis_label="Number of Birds Killed",
    x_range=[row[0] for row in df.values]#, y_range=Range1d(0, 2450000000)
)

plot.circle('Source', 'Total Killed', size='Per Source', source=src)


show(plot)