from eartquakes import get_csv, Converti
import math
from numpy import interp
import pandas as pd 
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource, NumeralTickFormatter, CDSView, GroupFilter
import numpy as np 
from PIL import Image



def elaborate(csv_url):
    zoom = 1
    x=[]
    y=[]
    mag2x = []
    mag2y =  []
    mag2 = []

    mag3x = []
    mag3y = []
    mag3 = []

    mag4x = []
    mag4y = []
    mag4 = []

    mag5x = []
    mag5y = []
    mag5 = []

    mag6x = []
    mag6y = []
    mag6 = []

    mag7x = []
    mag7y = []
    mag7 = []

    mag_8_and_morex = []
    mag_8_and_morey = []
    mag_8_and_more = []


    mags=[]


    daily_eartquakes = pd.read_csv(csv_url, parse_dates=['mag'])
 
    maxmag = math.sqrt(math.pow(10,10))
    csv_content = get_csv(csv_url)
    #call the function get_csv to get the csv file from usgs up to what we chose on the menù

    
    for row in csv_content:
        if row[4] != '':
            temp_mag = math.pow(10,float(row[4]))
            temp_mag =  math.sqrt(temp_mag )
            temp_mag = interp(temp_mag ,[0,maxmag],[0,60])
            #for differentiate magnitude from for example(1.2 and 1.9) we make calculation and then we map these values
            #to 0/60 like that we won't have similar circle because we can't write circle with a float number as diameter
            convertito = Converti(float(row[2]),float(row[1]),zoom)
            a = convertito.mercX()
            b =  convertito.mercY()
            
            if float(row[4]) <= 2 :
                mag2x.append(a)
                mag2y.append(b)
                mag2.append(row[4])
            elif float(row[4]) >2 and float(row[4]) <=3:
                mag3x.append(a)
                mag3y.append(b)
                mag3.append(row[4])
            elif float(row[4]) >3 and float(row[4]) <=4:
                mag4x.append(a)
                mag4y.append(b)
                mag4.append(row[4])
            elif float(row[4]) >4 and float(row[4]) <=5:
                mag5x.append(a)
                mag5y.append(b)
                mag5.append(row[4])
            elif float(row[4]) >5 and float(row[4]) <=6:
                mag6x.append(a)
                mag6y.append(b)
                mag6.append(row[4])
            elif float(row[4]) >6 and float(row[4]) <=7:
                mag7x.append(a)
                mag7y.append(b)
                mag7.append(row[4])
            else:
                mag_8_and_morex.append(a)
                mag_8_and_morey.append(b)
                mag_8_and_more.append(row[4])

               



            

   
    # open the image, converte in rgb , transform it as numpy array , and create a figure of 1024x1024 with the nparrya of the image
    im = Image.open('map_raw_rotated.png')
    im = im.convert("RGBA")
    imarray = np.array(im)
    plotTools = 'box_zoom, wheel_zoom, pan, tap, crosshair, reset, save'
    p = figure(x_range=(0,1024), y_range=(1024,0), width=1024, height=1024,tools = plotTools,active_scroll = 'wheel_zoom')
    p.image_rgba(image=[imarray], x=0, y=1024, dw=1024, dh=1024)

    
    
    

    
    

    mag2_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) <= 2)])
    mag3_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) > 2) & (daily_eartquakes['mag'].astype(float) <= 3)])
    mag4_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) > 3) & (daily_eartquakes['mag'].astype(float) <= 4)])
    mag5_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) > 4) & (daily_eartquakes['mag'].astype(float) <= 5)])
    mag6_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) > 5) & (daily_eartquakes['mag'].astype(float) <= 6)])
    mag7_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) > 6) & (daily_eartquakes['mag'].astype(float) <= 7)])
    mag8_and_more_eartquakes = (daily_eartquakes[(daily_eartquakes['mag'].astype(float) > 7)])
    

    data_mag2 = {
            'x':mag2x,
            'y':mag2y,
            'mags':mag2,
            'latitude':mag2_eartquakes['latitude'],
            'longitude':mag2_eartquakes['longitude'],
            'mag':mag2_eartquakes['mag'],
            'net':mag2_eartquakes['net'],
            'place':mag2_eartquakes['place'],
            'time':mag2_eartquakes['time'],
        }
    data_mag3 = {
            'x':mag3x,
            'y':mag3y,
            'mags':mag3,
            'latitude':mag3_eartquakes['latitude'],
            'longitude':mag3_eartquakes['longitude'],
            'mag':mag3_eartquakes['mag'],
            'net':mag3_eartquakes['net'],
            'place':mag3_eartquakes['place'],
            'time':mag3_eartquakes['time'],
        }  
    data_mag4 = {
            'x':mag4x,
            'y':mag4y,
            'mags':mag4,
            'latitude':mag4_eartquakes['latitude'],
            'longitude':mag4_eartquakes['longitude'],
            'mag':mag4_eartquakes['mag'],
            'net':mag4_eartquakes['net'],
            'place':mag4_eartquakes['place'],
            'time':mag4_eartquakes['time'],
        }  
    data_mag5 = {
            'x':mag5x,
            'y':mag5y,
            'mags':mag5,
            'latitude':mag5_eartquakes['latitude'],
            'longitude':mag5_eartquakes['longitude'],
            'mag':mag5_eartquakes['mag'],
            'net':mag5_eartquakes['net'],
            'place':mag5_eartquakes['place'],
            'time':mag5_eartquakes['time'],
        }  
    data_mag6 = {
            'x':mag6x,
            'y':mag6y,
            'mags':mag6,
            'latitude':mag6_eartquakes['latitude'],
            'longitude':mag6_eartquakes['longitude'],
            'mag':mag6_eartquakes['mag'],
            'net':mag6_eartquakes['net'],
            'place':mag6_eartquakes['place'],
            'time':mag6_eartquakes['time'],
        }  
    data_mag7 = {
            'x':mag7x,
            'y':mag7y,
            'mags':mag7,
            'latitude':mag7_eartquakes['latitude'],
            'longitude':mag7_eartquakes['longitude'],
            'mag':mag7_eartquakes['mag'],
            'net':mag7_eartquakes['net'],
            'place':mag7_eartquakes['place'],
            'time':mag7_eartquakes['time'],
        }  
    data_mag8_and_more = {
            'x':mag_8_and_morex,
            'y':mag_8_and_morey,
            'mags':mag_8_and_more,
            'latitude':mag8_and_more_eartquakes['latitude'],
            'longitude':mag8_and_more_eartquakes['longitude'],
            'mag':mag8_and_more_eartquakes['mag'],
            'net':mag8_and_more_eartquakes['net'],
            'place':mag8_and_more_eartquakes['place'],
            'time':mag8_and_more_eartquakes['time'],
        }  


    mag2_eartquakes_cds = ColumnDataSource(data_mag2)
    mag3_eartquakes_cds = ColumnDataSource(data_mag3) 
    mag4_eartquakes_cds = ColumnDataSource(data_mag4) 
    mag5_eartquakes_cds = ColumnDataSource(data_mag5) 
    mag6_eartquakes_cds = ColumnDataSource(data_mag6) 
    mag7_eartquakes_cds = ColumnDataSource(data_mag7) 
    mag8_and_more_eartquakes_cds = ColumnDataSource(data_mag8_and_more) 

    hover = HoverTool(
        tooltips = [
                ('Place','@place'),
                ('Latitude', '@latitude'),
                ('Longitude', '@longitude'),
                ('Magnitude','@mags'),
                ('Time','@time'),
               ])

 
  

    p.circle(x='x',
           y='y',
           source=mag2_eartquakes_cds,
           color='white',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.3,
           size=0.3,
           legend='Magnitude 0-2',
           alpha=1)
    #
    p.circle(x='x',
           y='y',
           source=mag3_eartquakes_cds,
           color='#7bdece',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.6,
           size=0.6,
           legend='Magnitude 2-3',
           alpha=1)
    p.circle(x='x',
           y='y',
           source=mag4_eartquakes_cds,
           color='#89ef61',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=1,
           size=1,
           legend='Magnitude 3-4',
           alpha=1)
    p.circle(x='x',
           y='y',
           source=mag5_eartquakes_cds,
           color='#2b7f1f',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=2,
           size=2,
           legend='Magnitude 4-5',
           alpha=1)
    p.circle(x='x',
           y='y',
           source=mag6_eartquakes_cds,
           color='yellow',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=4,
           size=4,
           legend='Magnitude 5-6',
           alpha=1)
    p.circle(x='x',
           y='y',
           source=mag7_eartquakes_cds,
           color='orange',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=8,
           size=8,
           legend='Magnitude 6-7',
           alpha=1)
    p.circle(x='x',
           y='y',
           source=mag8_and_more_eartquakes_cds,
           color='red',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=16,
           size=16,
           legend='Magnitude 7- ->',
           alpha=1)

    #add the over tool at the figure
    p.add_tools(hover)
    #hide tool from
    p.legend.click_policy = 'hide'


    #show the figure 
    show(p)


    
    


