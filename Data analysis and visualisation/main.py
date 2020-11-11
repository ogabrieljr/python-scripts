import pandas
from bokeh.plotting import ColumnDataSource, figure, show

data_frame = pandas.read_csv("data.csv")
df1 = pandas.DataFrame(data_frame, columns=["Name", "Wage", "Value"])


def value_to_float(value):
    removed_euro = value.replace("€", "")
    if type(removed_euro) == float or type(removed_euro) == int:
        return removed_euro
    if "K" in removed_euro:
        if len(removed_euro) > 1:
            return float(removed_euro.replace("K", "")) * 1000
        return 1000.0
    if "M" in removed_euro:
        if len(removed_euro) > 1:
            return float(removed_euro.replace("M", "")) * 1000000
        return 1000000.0
    if "B" in removed_euro:
        if len(removed_euro) > 1:
            return float(removed_euro.replace("B", "")) * 1000000000
        return 1000000000.0
    return 0.0


wage = df1["Wage"].apply(value_to_float)
value = df1["Value"].apply(value_to_float)
df1["Difference"] = value - wage
df1["Wage"], df1["Value"] = wage, value

source = ColumnDataSource(data=df1)

tooltips = [
    ("index", "$index"),
    ("(Wage,Value)", "(@Wage,@Value)"),
    ("Name", "@Name")
]

p = figure(title="example", plot_width=700, tooltips=tooltips)

p.circle("Wage", "Value", size=10, source=source)

show(p)
