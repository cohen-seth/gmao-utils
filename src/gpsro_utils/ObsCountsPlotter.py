import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import os

# For querying observations_inventory.db and extracting table(s) to a working dataframe (df)
def obs_inv_query(query): #, data_type):
    # Connect to the database
    #conn = sqlite3.connect('gpsro_m21c_observations_inventory.db')
    conn = sqlite3.connect('gpsro_spnasa_observations_inventory.db')

    # 'query':  query = f"SELECT * FROM obs_inventory WHERE data_type LIKE '%{data_type}%' "
    #query = f"SELECT * FROM obs_meta_nceplibs_bufr WHERE filename LIKE '%gpsro%'"
    
    # Execute a query and read the results into a DataFrame
    df = pd.read_sql_query(query, conn)
    df.head()
    
    # Close the connection
    conn.close()
    return df


def satid_dict_gpsro(df):
    # Loop through each sat_id and plot its time series data
    # attempt 2
    cosmic2 = [750,751,752,753,754,755]
    cosmic = [740,741,742,743,744,745]
    spire = [269]
    metop = [3,4,5]
    geo_optics = [265,266]
    planet_iq = [267,268]
    champ = [41]
    
    # not in cosmic2 + cosmic + spire + metop
    values_to_exclude = cosmic2 + cosmic + spire + metop + geo_optics + planet_iq + champ
    other = pd.unique(df[~df['sat_id'].isin(values_to_exclude)].sat_id).tolist()
    other = sorted(other)
    
    sat_groups  = dict({
        'cosmic2' : cosmic2,
        'cosmic' : cosmic,
        'spire' : spire,
        'metop' : metop,
        'geo_optics' : geo_optics,
        'planet_iq' : planet_iq,
        'champ' : champ,
        'other' : other
    })
    return sat_groups


class ObsCountsPlotter:
    def __init__(self, dataframe):
        """
        Initialize with a pandas DataFrame.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame to plot.

        In order to plot using the Gnssro function below the DataFrame NEEDS TO HAVE the columns: obs_day (dateTime), sat_id (i.e. kx)
        """
        self.dataframe = dataframe


    # Plot Timeseries observation count by day for each satellite
    #def line_plot(self, x_column, y_column, title="Line Plot", xlabel="X-axis", ylabel="Y-axis"):
    def Gnssro(self, title):
        # quering observation_inventory.db
        #df = obs_inv_query(query = f"SELECT * FROM obs_meta_nceplibs_bufr WHERE filename LIKE '%{data_type}%'") 
        
        data_type = 'gpsro'
        
        # Create new 'day' variable which will be used to aggregate all 4 cycles of the day into one
        df['obs_day'] = pd.to_datetime(df['obs_day'])  # Ensure obs_day is in datetime format
        df['day'] = pd.to_datetime(df.obs_day.dt.strftime('%Y%m%d'))
        
        # Group by 'obs_day' and 'sat_id' and sum the 'obs_counts'
        grouped_df = df.groupby(['day', 'sat_id'])['obs_count'].sum().reset_index()
    
        # plot size
        mx_ob_ct = -(grouped_df['obs_count'].max())
        print(f'mx_fl_sz: {mx_ob_ct}')
        
        n_subplots = 1 # placeholder for number of subplots. May add this in the future. 
        fig, ax_sub = plt.subplots(
                        n_subplots, 1, sharex=True, figsize=(18,9), dpi=160)
    
        """     
        Loop through each satellite id and plot its timeseries
 
        """     
        if data_type == 'gpsro':
            sat_groups = satid_dict_gpsro(df)
            # Needed for grouping said's and plotting groups
            for said in sat_groups.keys():  #[cosmic2,cosmic,spire,metop,other]:
                #print(f'said: {said} {sat_groups[said]}')
                sat_id_data = df[df["sat_id"].isin(sat_groups[said])]
                grouped_df = sat_id_data.groupby(['day'])['obs_count'].sum().reset_index()
                ax_sub.plot(grouped_df['day'], grouped_df['obs_count'], linewidth=1,
                         label=said.upper())
                #label=f'{said}: {sat_groups[said]}') #, color=colors[m_idx+2])
        else:
            # Needed for grouping said's and plotting groups
            sat_unique = pd.unique(grouped_df['sat_id']).tolist()
            print(f'sat_unique: {sat_unique}')
            for said in sat_unique:   
                sat_id_data = grouped_df[grouped_df["sat_id"] == said]
                #print(sat_id_data.head())
                
                ax_sub.plot(sat_id_data['day'], sat_id_data['obs_count'], linewidth=1,
                         label=said.upper()) 
    
    
        # Title
        figure_title = title # f'Time Series of Occultation Count for Each sat_id (group) \n MERRA 21c {data_type.upper()} Data ' #'Merra 21c GPSRO Data \nTime Series of File size' #'file_size test' #grouping.get_grouping_name()
        fig.suptitle(figure_title, y=0.97, fontsize=25)
        ax = plt.gca()
        
        # Sub-Title
        subplot_title = f'{data_type}'
        ax_sub.text(0.01, 0.5, subplot_title,
                    transform=ax_sub.transAxes, fontsize=17, backgroundcolor='white')
    
        # LEGEND
        leg = ax_sub.legend(loc='upper left', facecolor="white",fontsize=17)
        leg_lines = leg.get_lines()
        for leg_line in leg_lines:
            leg_line.set_linewidth(4)
            
        # Y AXIS
        plt.ylim((0, -mx_ob_ct*1.1))
        plt.ylabel('Occultation Count [# day$^{-1}$]', fontsize=19)
        y_axis = plt.gca()
        y_axis.ticklabel_format(style='plain', axis='y')
        
    
        
        # X AXIS
        plt.xlabel('Observation Day (Y-m-d)', fontsize=19)
    
        
        # TICKS
        ax_sub.minorticks_on()
    
        # Set the font size of the x and y ticks
        ax.tick_params(axis='both', which='major', labelsize=14, width=1, length=8)
        # Customize the appearance of minor ticks
        ax.tick_params(axis='both', which='minor', width=.75, length=4)
    
        # GRID OPTIONS
        ax_sub.grid(which='minor', color='lightgrey',
                    linestyle='--', linewidth=0.2)
        ax_sub.grid(which='major', color='lightgrey',
                    linestyle='--', linewidth=0.6)
    
        # SAVING OPTIONS
        fn = 'obs_count_' + data_type
        #dest_path_png = export_plot(fn)
        dest_path_png = fn # TEMPORARY
        
        plt.show()
        plt.close()
    
        return dest_path_png

###################### 
# Example & How to use


# Step 1 Reading in data from .db file
df = obs_inv_query(query = f"SELECT * FROM obs_meta_nceplibs_bufr WHERE filename LIKE '%gpsro%'") 
df

# Initialize plotter
plotter = ObsCountsPlotter(df)

# Generate a line plot
plotter.Gnssro(title = f'Time Series of Occultation Count for Each sat_id (group) \n MERRA 21c {data_type.upper()} Data ' ) 
