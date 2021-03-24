import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.themes import built_in_themes
from bokeh.io import curdoc
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure

    
df = pd.read_csv('challenge_data_2.csv', encoding = 'ISO-8859-1')

curdoc().theme = 'dark_minimal'


def plot1():
    
    # Variables For PLOT 1
    df_source = df['source'].value_counts()
    source_list = df_source.iloc[:7].index.tolist()
    source_list
    
    # PLOT 1: AVERAGE FOLLOWERS PER SOURCE
    
    # Finding the average followers per source

    # Twitter Web App
    df_webApp = df.loc[(df['source'] == 'Twitter Web App') & (df['followers_count'])]
    df_webApp[['source', 'followers_count']].mean().round()

    # Twitter for Iphone
    df_twIphone = df.loc[(df['source'] == 'Twitter for iPhone') & (df['followers_count'])]
    df_twIphone[['source', 'followers_count']].mean().round()

    # Twitter for Android
    df_twAndroid = df.loc[(df['source'] == 'Twitter for Android') & (df['followers_count'])]
    df_twAndroid[['source', 'followers_count']].mean().round()

    # Twitter for Ipad
    df_twIpad = df.loc[(df['source'] == 'Twitter for iPad') & (df['followers_count'])]
    df_twIpad[['source', 'followers_count']].mean().round()

    # Twitter TweetDeck
    df_twDeck = df.loc[(df['source'] == 'TweetDeck') & (df['followers_count'])]
    df_twDeck[['source', 'followers_count']].mean().round()

    # Dlvr.it
    df_twDlvr = df.loc[(df['source'] == 'dlvr.it') & (df['followers_count'])]
    df_twDlvr[['source', 'followers_count']].mean().round()

    # Twitter Madgex Twitter Tweeter
    df_twMadgx = df.loc[(df['source'] == 'Madgex Twitter Tweeter') & (df['followers_count'])]
    df_twMadgx[['source', 'followers_count']].mean().round()

    # List of average followers per source
    df_followers = [8445.0, 5266.0, 1742.0, 2428.0, 110515.0, 9760.0, 1184.0]

    # Rename the mode of collection
    source_list = ['Web App', 'iPhone', 'Android', 'iPad', 'TweetDeck', 'dlvr.it', 'Madgex']


    # PLOTTING PLOT 1
    p = figure(x_range=source_list, plot_height=250, title="Followers vs Source",
            toolbar_location=None, tools="", x_axis_label = 'Twitter Source by Device', y_axis_label = 'Average Follower Count')
    
    p.sizing_mode = 'scale_both'

    p.vbar(x=source_list, top=df_followers, width=0.5)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
  
    return p



def plot2():
    
        # Group follower count based on anger level

        # Anger level 0
        anger_0 = df.loc[(df['followers_count']) & (df['anger'] == 0)]
        anger0 = anger_0['followers_count'].sum()

        # Anger level 1
        anger_1 = df.loc[(df['followers_count']) & (df['anger'] == 1)]
        anger1 = anger_1['followers_count'].sum()

        # Anger level 2
        anger_2 = df.loc[(df['followers_count']) & (df['anger'] == 2)]
        anger2 = anger_2['followers_count'].sum()

        # Anger level 3
        anger_3 = df.loc[(df['followers_count']) & (df['anger'] == 3)]
        anger3 = anger_3['followers_count'].sum()

        # Anger level 4
        anger_4 = df.loc[(df['followers_count']) & (df['anger'] == 4)]
        anger4 = anger_4['followers_count'].sum()


        anger_range = df['anger'].unique()

        anger_followers = [anger0, anger1, anger2, anger3, anger4]


        # Variables to use
        anger_range
        anger_followers


        p2 = figure(title = "Correlation Between Follower Count & Anger", plot_height=250, sizing_mode='scale_both')

        p2.xaxis.axis_label = "anger range"
        p2.yaxis.axis_label = "follower count"

        # Styling the Title
        # p2.title.text_font = "Calibri"
        # p2.title.text_font_size = "35px"
        # p2.title.align = "center"
        # p2.title.text_color = "#D93D04"

        # Styling the Background color
        p2.background_fill_color = None

        # Customizing the grid
        p2.xgrid.visible = False
        p2.ygrid.visible = False

        # x-axis
        p2.xgrid.grid_line_color = "red"
        p2.xaxis.axis_label_text_font_size = "20px"
        p2.xaxis.axis_label_text_font_style = "bold"
        p2.xaxis.axis_label_text_color = "#D93D04"
        p2.xaxis.axis_line_color = "#D93D04"
        p2.xaxis.axis_line_width = 0
        # y-axis
        p2.yaxis.axis_label_text_font_size = "20px"
        p2.yaxis.axis_label_text_font_style = "bold"
        p2.yaxis.axis_label_text_color = "#D93D04"
        p2.yaxis.axis_line_color = "#D93D04"
        p2.yaxis.axis_line_width = 0

        # Customizing the y-axis
        p2.yaxis.minor_tick_line_color = None
        # p.yaxis.major_label_text_color = "#D93D04"

        p2.circle(anger_range, anger_followers, size= 15, color = "#D93D04")
        
        return p2
