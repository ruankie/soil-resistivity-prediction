#-----------------------------------------------------------------------------
# these are hlper functions for the
# project on predicting soil resistivity. These are functions 
# from the get_data_functions.ipynb notebook.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# import necessary packages
#-----------------------------------------------------------------------------
import os
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from mpl_toolkits.axes_grid1 import make_axes_locatable

#-----------------------------------------------------------------------------
# my functions:
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# BIOMES
#-----------------------------------------------------------------------------

def load_biomes_data(sh_dir):
    # read shapefile
    return gpd.read_file(sh_dir)
# C:/Wits/2020/COMS7047 - Machine Learning/term project/maps from open africa/South Africa - Biomes/RSA_biome.shp

def plot_biomes(biomes_data, plot_type='basic_grey', final_out_data=None, save_plot_dir=None):
    if plot_type == 'basic_grey':        
        fig, ax = plt.subplots(figsize = (15,15))
        biomes_data.plot(ax=ax,
                           linewidth = 0.3,
                           edgecolor='black',
                           facecolor='lightgrey',
                           alpha=0.9)
        ax.set_title('Biomes', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4)
        plt.show()
        
    elif plot_type == 'all_colour':
        reduced_set = []
        for col in biomes_data.BIOME.unique():
            if col is not None:
                if col !='*':
                    reduced_set.append(col)
        
        cols = ['b', 'g', 'r', 'c', 'm', 'y', 'pink', 'lightblue', 'pink', 'orange', 'lightgreen', 'darkgreen', 'lightgrey', 'darkblue', 'purple']
        cols = cols*int(np.ceil(biomes_data.BIOME.unique().shape[0]/len(cols)))

        fig, ax = plt.subplots(figsize = (15,15))
        leg_handles = []
        transparency = 0.6

        for i, item in enumerate(reduced_set):
            curr_set = biomes_data[biomes_data.BIOME==item]
            curr_set.plot(ax=ax,
                   linewidth = 0.5,
                   edgecolor='black',
                   facecolor=cols[i],
                   alpha=transparency)
            leg_handles.append(mpatches.Patch(color=cols[i], label=item, alpha=transparency))

        plt.legend(handles=leg_handles, loc='upper left')
        ax.set_title('Biomes', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4)
        if not (save_plot_dir == None):
            plt.savefig(save_plot_dir,dpi=200)
            print('figure saved at:',save_plot_dir)
        plt.show()
    
    elif plot_type == 'from_coords':
        final_out_gpd = gpd.GeoDataFrame(final_out_data)
        reduced_set = []
        for col in biomes_data.BIOME.unique():
            if col is not None:
                if col !='*':
                    reduced_set.append(col)
        
        cols = ['b', 'g', 'r', 'c', 'm', 'y', 'pink', 'lightblue', 'pink', 'orange', 'lightgreen', 'darkgreen', 'lightgrey', 'darkblue', 'purple']
        cols = cols*int(np.ceil(biomes_data.BIOME.unique().shape[0]/len(cols)))
        
        fig, ax = plt.subplots(figsize = (15,15))
        leg_handles = []
        transparency = 0.9

        for i, item in enumerate(reduced_set):
            curr_set = biomes_data[biomes_data.BIOME==item]
            curr_set.plot(ax=ax,
                   linewidth = 0.5,
                   edgecolor='black',
                   facecolor='lightgrey',
                   alpha=transparency)

        for i,geo in enumerate(final_out_gpd.geometry.unique()):
            curr_poly = final_out_gpd[final_out_gpd.geometry == geo]
            curr_poly.plot(ax=ax,
                           linewidth = 0.5,
                           edgecolor='black',
                           alpha=0.3,
                           facecolor=cols[i])#,
                           #hatch='//')
            leg_handles.append(mpatches.Patch(color=cols[i], label=final_out_data.BIOME[i], alpha=0.3))

        for i,coor in enumerate(inp_coords.geometry.unique()):
            curr_coor = inp_coords[inp_coords.geometry == coor]
            curr_coor.plot(ax=ax, color=cols[i], linewidth = 1, edgecolor='black', marker='o', markersize=80)
            leg_handles.append(mlines.Line2D([], [],color=cols[i], linewidth = 1, marker='o',linestyle='None', label=inp_coords.Name[i]+': '+final_out_data.BIOME[i]))

        # other details
        plt.legend(handles=leg_handles, loc='upper left')
        ax.set_title('Coordinates Summary - Biome', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4)
        plt.show()    
        
    
        
def get_biomes_data(biomes_data, inp_coords):
    # search for point in all polygons
    return_polys_ind = []
    answer_polys = gpd.GeoDataFrame()


    for j in range(inp_coords.shape[0]):

        coord_geo = inp_coords.iloc[j].geometry

        for i in range(biomes_data.shape[0]):
            if coord_geo.within(biomes_data.iloc[i].geometry):
                return_polys_ind.append(i)

        answer_polys = answer_polys.append(biomes_data.iloc[return_polys_ind[j]])
    
    out_dict = {'Name': inp_coords.Name.values,
            'x': inp_coords.x.values,
            'y': inp_coords.y.values,
            'BIOME': answer_polys.BIOME.values,
            'geometry': answer_polys.geometry.values}

    return pd.DataFrame(out_dict) 
    
    
#-----------------------------------------------------------------------------
# RUNOFF
#-----------------------------------------------------------------------------

def load_runoff_data(sh_dir):
    # read shapefile
    return gpd.read_file(sh_dir)
# C:/Wits/2020/COMS7047 - Machine Learning/term project/maps from open africa/South Africa - Runoff/RSA_runperc.shp


def plot_runoff(runoff_data, plot_type='basic_grey', final_out_data=None):
    if plot_type == 'basic_grey':        
        fig, ax = plt.subplots(figsize = (15,15))
        runoff_data.plot(ax=ax,
                           linewidth = 0.3,
                           edgecolor='black',
                           facecolor='lightgrey',
                           alpha=0.9)
        ax.set_title('Runoff', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4)
        plt.show()
        
    elif plot_type == 'all_colour':
        fig, ax = plt.subplots(figsize = (15,15))
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.1)
        runoff_data.plot(ax=ax,
                   column='RUNOFFPERC',
                   linewidth = 0.3,
                   edgecolor='black',
                   legend=True,
                   cax=cax,
                   cmap='GnBu') # GnBu, YlGn, plasma, cividis
        ax.set_title('Runoff', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4);
    
    elif plot_type == 'from_coords':
        final_out_gpd = gpd.GeoDataFrame(final_out_data)
        reduced_set = []
        for col in runoff_data.RUNOFFPERC.unique():
            if col is not None:
                if col !='*':
                    reduced_set.append(col)
        
        cols = ['b', 'g', 'r', 'c', 'm', 'y', 'pink', 'lightblue', 'pink', 'orange', 'lightgreen', 'darkgreen', 'lightgrey', 'darkblue', 'purple']
        cols = cols*int(np.ceil(runoff_data.RUNOFFPERC.unique().shape[0]/len(cols)))
        
        fig, ax = plt.subplots(figsize = (15,15))
        leg_handles = []
        transparency = 0.9

        for i, item in enumerate(reduced_set):
            curr_set = runoff_data[runoff_data.RUNOFFPERC==item]
            curr_set.plot(ax=ax,
                   linewidth = 0.5,
                   edgecolor='black',
                   facecolor='lightgrey',
                   alpha=transparency)

        for i,geo in enumerate(final_out_gpd.geometry.unique()):
            curr_poly = final_out_gpd[final_out_gpd.geometry == geo]
            curr_poly.plot(ax=ax,
                           linewidth = 0.5,
                           edgecolor='black',
                           alpha=0.3,
                           facecolor=cols[i])#,
                           #hatch='//')
            leg_handles.append(mpatches.Patch(color=cols[i], label=final_out_data.RUNOFFPERC[i], alpha=0.3))

        for i,coor in enumerate(inp_coords.geometry.unique()):
            curr_coor = inp_coords[inp_coords.geometry == coor]
            curr_coor.plot(ax=ax, color=cols[i], linewidth = 1, edgecolor='black', marker='o', markersize=80)
            leg_handles.append(mlines.Line2D([], [],color=cols[i], linewidth = 1, marker='o',linestyle='None', label=inp_coords.Name[i]+': '+str(final_out_data.RUNOFFPERC[i])))

        # other details
        plt.legend(handles=leg_handles, loc='upper left')
        ax.set_title('Coordinates Summary - Runoff', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4)
        plt.show()    
        

def get_runoff_data(runoff_data, inp_coords):
    # search for point in all polygons
    return_polys_ind = []
    answer_polys = gpd.GeoDataFrame()


    for j in range(inp_coords.shape[0]):

        coord_geo = inp_coords.iloc[j].geometry

        for i in range(runoff_data.shape[0]):
            if coord_geo.within(runoff_data.iloc[i].geometry):
                return_polys_ind.append(i)

        answer_polys = answer_polys.append(runoff_data.iloc[return_polys_ind[j]])
    
    out_dict = {'Name': inp_coords.Name.values,
            'x': inp_coords.x.values,
            'y': inp_coords.y.values,
            'RUNOFFPERC': answer_polys.RUNOFFPERC.values,
            'geometry': answer_polys.geometry.values}

    return pd.DataFrame(out_dict) 
    

#-----------------------------------------------------------------------------
# SOTER Database
#-----------------------------------------------------------------------------

def load_soter_data(sahpefile_dir, mother_query_dir):
    # read shapefile
    geo_poly_data = gpd.read_file(sahpefile_dir)
    # C:/Wits/2020/COMS7047 - Machine Learning/term project/maps from isric.org - soilatlas/SOTER_ZA/GIS/SOTER/ZA_SOTERv1.shp
    
    # read mother query from SOTER database
    query_data = pd.read_excel(mother_query_dir)
    # C:/Wits/2020/COMS7047 - Machine Learning/term project/maps from isric.org - soilatlas/SOTER_ZA/mother_query_SOTER_ZA_18_03_2020_1656_adj_cols.xlsx
    
    # reduce dataframes
    reduced_geo_poly_data = geo_poly_data[['SUID','LITHOLOGY','LANDFORM','SOIL','geometry']]
    reduced_query_data = query_data[['SOTER_ID','RELIEF_I','BEDROCK_DEPTH']]
    
    # drop duplicates from reduced_query_data in SOTER_ID column
    reduced_query_data = reduced_query_data.drop_duplicates(subset=['SOTER_ID'])
    
    # drop duplicates from reduced_geo_poly_data in SUID column
    reduced_geo_poly_data = reduced_geo_poly_data.drop_duplicates(subset=['SUID'])
    
    # rename columns and set index
    reduced_geo_poly_data = reduced_geo_poly_data.rename(columns={'SUID':'SOTER_ID'})
    reduced_geo_poly_data = reduced_geo_poly_data.set_index('SOTER_ID')
    reduced_query_data = reduced_query_data.set_index('SOTER_ID')
    
    # join dataframes
    data = reduced_query_data.join(reduced_geo_poly_data)
    
    # shuffle columns
    final_data = data[['LITHOLOGY','LANDFORM','SOIL','RELIEF_I','BEDROCK_DEPTH','geometry']]
    
    #convert to geopandas dataframe
    geo_dataframe = gpd.GeoDataFrame(final_data)
    
    return geo_dataframe
    
    
def get_soter_data(soter_data, inp_coords):
    # reset index
    geo_dataframe = soter_data.reset_index()
    
    # search for point in all polygons
    return_polys_ind = [-1]*inp_coords.shape[0]
    answer_polys = gpd.GeoDataFrame()


    for j in range(inp_coords.shape[0]):
        print('j=',j,':',inp_coords.Name[j])

        coord_geo = inp_coords.iloc[j].geometry
        print('\t inp coord located')

        for i in range(geo_dataframe.shape[0]):
            if coord_geo.within(geo_dataframe.iloc[i].geometry):
                #return_polys_ind.append(i)
                return_polys_ind[j] = i
                print('\t\t coord found within poly at:',return_polys_ind[j])
                break

        answer_polys = answer_polys.append(geo_dataframe.iloc[return_polys_ind[j]])
    
    print('Check for -1 in this array. There should not be one!')
    print(return_polys_ind)
        
    # drop duplicates from answer_polys
    #answer_polys = answer_polys.drop_duplicates(subset=['geometry'],keep='last')
    
    out_dict = {'Name': inp_coords.Name.values,
                'x': inp_coords.x.values,
                'y': inp_coords.y.values,
                'BEDROCK_DEPTH': answer_polys.BEDROCK_DEPTH.values,
                'LANDFORM': answer_polys.LANDFORM.values,
                'LITHOLOGY': answer_polys.LITHOLOGY.values,
                'SOIL' : answer_polys.SOIL.values,
                'RELIEF_I': answer_polys.RELIEF_I.values,
                'geometry': answer_polys.geometry.values}
                

    return pd.DataFrame(out_dict), return_polys_ind


def plot_coords(biomes_data, plot_type='from_coords', final_out_data=None, inp_coords=None):
    
    if plot_type == 'from_coords':
        final_out_gpd = gpd.GeoDataFrame(final_out_data)
        reduced_set = []
        for col in biomes_data.BIOME.unique():
            if col is not None:
                if col !='*':
                    reduced_set.append(col)
        
        cols = ['b', 'g', 'r', 'c', 'm', 'y', 'pink', 'lightblue', 'pink', 'orange', 'lightgreen', 'darkgreen', 'lightgrey', 'darkblue', 'purple']
        #cols = cols*int(np.ceil(biomes_data.BIOME.unique().shape[0]/len(cols)))
        cols = cols*100
        
        fig, ax = plt.subplots(figsize = (15,15))
        leg_handles = []
        transparency = 0.9

        for i, item in enumerate(reduced_set):
            curr_set = biomes_data[biomes_data.BIOME==item]
            curr_set.plot(ax=ax,
                   linewidth = 0.5,
                   edgecolor='black',
                   facecolor='lightgrey',
                   alpha=transparency)

        for i,geo in enumerate(final_out_gpd.geometry.unique()):
            curr_poly = final_out_gpd[final_out_gpd.geometry == geo]
            curr_poly.plot(ax=ax,
                           linewidth = 0.5,
                           edgecolor='black',
                           alpha=0.3,
                           facecolor='lightgrey')#,
                           #hatch='//')
            #leg_handles.append(mpatches.Patch(color=cols[i], label=final_out_data.BIOME[i], alpha=0.3))

        for i,coor in enumerate(inp_coords.geometry.unique()):
            curr_coor = inp_coords[inp_coords.geometry == coor]
            curr_coor.plot(ax=ax, color=cols[i], linewidth = 1, edgecolor='black', marker='o', markersize=80)
            leg_handles.append(mlines.Line2D([], [],color=cols[i], linewidth = 1, marker='o',linestyle='None', label=inp_coords.Name[i]))

        # other details
        plt.legend(handles=leg_handles, loc='upper left')
        ax.set_title('Coordinates Plot', fontsize=20)
        ax.grid(color='grey',linestyle='-', linewidth=0.5, alpha=0.4)
        plt.show()    
        
        
def plot_inp_coords_location_from_excel(excel_file_dir, biomes_shapefile_dir='./Data/maps from open africa/South Africa - Biomes/RSA_biome.shp'):
    
    # make pd dataframe from excel file with soil resistivity data
    soil_res_data = pd.read_excel(excel_file_dir, index_col=0)
    soil_res_data = soil_res_data.reset_index()
    soil_res_data.rename(columns={'Name (ID)':'Name', 'x (longi - E_W)':'x', 'y (lati - N-S)':'y'}, inplace = True)
    
    # input coordinates from soil resistivity data
    x = list(soil_res_data.x)
    y = list(soil_res_data.y)
    names = list(soil_res_data.Name)
    df_dict = {'Name': names, 'x': x, 'y': y}
    df = pd.DataFrame.from_dict(df_dict)
    inp_coords = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
    #biomes_data = mhf.load_biomes_data(biomes_shapefile_dir)
    biomes_data = load_biomes_data(biomes_shapefile_dir)
    #biomes_data_summary = mhf.get_biomes_data(biomes_data, inp_coords)
    biomes_data_summary = get_biomes_data(biomes_data, inp_coords)
    #mhf.plot_coords(biomes_data, plot_type='from_coords', final_out_data=biomes_data_summary, inp_coords=inp_coords)
    plot_coords(biomes_data, plot_type='from_coords', final_out_data=biomes_data_summary, inp_coords=inp_coords)
    
    
    
def plot_inp_coords_location_from_coord_table(inp_coords, biomes_shapefile_dir='../Data/maps from open africa/South Africa - Biomes/RSA_biome.shp'):
    
    #-----------------------------------------
    # DO THIS BEFORE EXECUTING THIS FUNCTION:
    #-----------------------------------------
    ## make pd dataframe from excel file with soil resistivity data
    #excel_file_dir = 'set location of exel file'
    #soil_res_data = pd.read_excel(excel_file_dir, index_col=0)
    #soil_res_data = soil_res_data.reset_index()
    #soil_res_data.rename(columns={'Name (ID)':'Name', 'x (longi - E_W)':'x', 'y (lati - N-S)':'y'}, inplace = True)
    #
    ## input coordinates from soil resistivity data
    #x = list(soil_res_data.x)
    #y = list(soil_res_data.y)
    #names = list(soil_res_data.Name)
    #df_dict = {'Name': names, 'x': x, 'y': y}
    #df = pd.DataFrame.from_dict(df_dict)
    #inp_coords = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
    #-----------------------------------------
    # OR
    #-----------------------------------------
    #inp_coords = get_coord_table_from_excel(excel_file_dir)
    #-----------------------------------------
    
    #biomes_data = mhf.load_biomes_data(biomes_shapefile_dir)
    biomes_data = load_biomes_data(biomes_shapefile_dir)
    #biomes_data_summary = mhf.get_biomes_data(biomes_data, inp_coords)
    biomes_data_summary = get_biomes_data(biomes_data, inp_coords)
    #mhf.plot_coords(biomes_data, plot_type='from_coords', final_out_data=biomes_data_summary, inp_coords=inp_coords)
    plot_coords(biomes_data, plot_type='from_coords', final_out_data=biomes_data_summary, inp_coords=inp_coords)
    
    
    
def get_coord_table_from_excel(excel_file_dir):
    
    # make pd dataframe from excel file with soil resistivity data
    soil_res_data = pd.read_excel(excel_file_dir, index_col=0)
    soil_res_data = soil_res_data.reset_index()
    soil_res_data.rename(columns={'Name (ID)':'Name', 'x (longi - E_W)':'x', 'y (lati - N-S)':'y'}, inplace = True)

    # input coordinates from soil resistivity data
    x = list(soil_res_data.x)
    y = list(soil_res_data.y)
    names = list(soil_res_data.Name)
    df_dict = {'Name': names, 'x': x, 'y': y}
    df = pd.DataFrame.from_dict(df_dict)
    inp_coords = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
    
    return inp_coords
    
    
    
def get_resistivity_table_from_excel(excel_file_dir):
    
    # make pd dataframe from excel file with soil resistivity data
    soil_res_data = pd.read_excel(excel_file_dir, index_col=0)
    soil_res_data = soil_res_data.reset_index()
    soil_res_data.rename(columns={'Name (ID)':'Name', 'x (longi - E_W)':'x', 'y (lati - N-S)':'y'}, inplace = True)

    # input coordinates from soil resistivity data
    x = list(soil_res_data.x)
    y = list(soil_res_data.y)
    rho_1 = list(soil_res_data.rho_1)
    rho_2 = list(soil_res_data.rho_2)
    rho_3 = list(soil_res_data.rho_3)
    names = list(soil_res_data.Name)
    df_dict = {'Name': names, 'x': x, 'y': y, 'rho_1': rho_1, 'rho_2': rho_2, 'rho_3': rho_3}
    df = pd.DataFrame.from_dict(df_dict)
    inp_coords = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
    
    return inp_coords