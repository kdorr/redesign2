import pandas
from math import pi, sqrt
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, NumeralTickFormatter, Range1d
from bokeh.palettes import Viridis
from bokeh.transform import factor_cmap

# Read data
df = pandas.read_csv("data.csv")

# Calculate radii to size circles by area rather than by radius ( A = pi*r^2 => r = sqrt(A/pi) )
df['radius'] = (df['Per Source'])/pi
for i in range(0, 6):
    df.loc[i, 'radius'] = sqrt(df.loc[i, 'radius'])*50000000  # Multiply for aesthetics (area is independent of axes)

# Calculate new y-coordinate of the circles so the bottoms (not centers) of the circles are at their Total Killed values
df['new center'] = df['radius'] + df['Total Killed']

# Format data
src = ColumnDataSource(df)

# Setup plot
plot = figure(
    plot_width=950, plot_height=600, title="Number of Birds Killed by each Human Activity",
    x_axis_label="Type of Activity", y_axis_label="Number of Birds Killed",
    x_range=[row[0] for row in df.values], y_range=Range1d(0, 2800000000)
)
plot.yaxis[0].formatter = NumeralTickFormatter(format="0.0 a")
plot.xgrid.grid_line_color = None

# Plot circles for Number of Birds Killed Per Source
plot.circle(x='Source', y='new center', radius='radius', radius_dimension='y',
            color=factor_cmap('Group', palette=Viridis[4], factors=df['Group'].unique()), alpha=.5, source=src)

# Plot bars for Total Number of Birds Killed
plot.vbar(x='Source', bottom=0, top='Total Killed', width=.01, source=src,
          color=factor_cmap('Group', palette=Viridis[4], factors=df['Group'].unique()))

show(plot)
