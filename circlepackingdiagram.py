import pandas as pd
from bokeh.charts import Horizon, output_file, show

# read in some stock data from the Yahoo Finance API
# AAPL = pd.read_csv(  "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2016",parse_dates=['Date'])
# MSFT = pd.read_csv("http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2016",parse_dates=['Date'])
# IBM = pd.read_csv("http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2016",parse_dates=['Date'])

bdg=[10.23,2.11,4.53,2.75,4.02,7.97]
prov=[11.11,2.02,6.62,3.1,3.86,9.15]
nas=[11.06,2.78,6.96,3.79,4.3,8.38]
Year=[2008,2009,2010,2011,2012,2013]

 #the data and the labels in a dictionary
data = ({ 'Kota Bandung': bdg,'Year': Year,'Provinsi Jawa Barat': prov,'Nasional': nas})
print(data)
p = Horizon(data, x = Year, title="Horizon plot using stock inputs")

output_file("horizon.html")


show(p)