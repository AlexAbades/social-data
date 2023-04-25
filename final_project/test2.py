# import necessary libraries
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category10
from bokeh.plotting import figure

# define data for the districts
districts = {
    'BROOKLYN': [-73.9442, 40.6782],
    'BRONX': [-73.8648, 40.8448],
    'MANHATTAN': [-73.9712, 40.7831],
    'QUEENS': [-73.8317, 40.7033],
    'STATEN ISLAND': [-74.1538, 40.5795]
}

# create a column data source
source = ColumnDataSource(data=dict(
    district=list(districts.keys()),
    lon=list(districts.values())[0::2],
    lat=list(districts.values())[1::2]
))

# create the map figure
p = figure(x_range=(-74.3, -73.7), y_range=(40.5, 41.0), tools=['wheel_zoom', 'pan', 'reset', 'save'])
p.title.text = "New York City Districts"
p.xaxis.axis_label = "Longitude"
p.yaxis.axis_label = "Latitude"

# plot the districts as circles
p.circle(x='lon', y='lat', size=10, color=Category10[len(districts)],
         source=source, legend_label='district', line_color='black', fill_color='white', hatch_color='black', hatch_alpha=0.5)

# add hover tooltips
hover = HoverTool()
hover.tooltips = [('district', '@district')]
p.add_tools(hover)

# show the plot
output_file("districts.html")
show(p)
