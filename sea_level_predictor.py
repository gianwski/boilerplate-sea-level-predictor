import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", sep=",")
    print(df)


    # Create scatter plot
    plt.figure(figsize=(6, 6))
    plt.scatter(x=df["Year"],
                y=df["CSIRO Adjusted Sea Level"],
                facecolors="none",
                edgecolors="blue")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Create first line of best fit
    regression = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(df["Year"].min(), 2051)
    plt.plot(years_extended,
             regression.slope * years_extended  + regression.intercept,
             color="red",
             linestyle="--")
    
    # Create second line of best fit
    df_since2000 = df[df["Year"] >= 2000]
    print(df_since2000)
    regression_since2000 = linregress(x=df_since2000["Year"], y=df_since2000["CSIRO Adjusted Sea Level"])
    years_extended_since2000 = np.arange(df_since2000["Year"].min(), 2051)
    plt.plot(years_extended_since2000,
             regression_since2000.slope * years_extended_since2000  + regression_since2000.intercept,
             color="green",
             linestyle="--")


    # Add labels and title
    plt.xlabel("Year", fontsize=16)
    plt.ylabel("Sea Level (inches)", fontsize=16)
    plt.title("Rise in Sea Level", fontsize=16)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.tight_layout()
    plt.savefig('sea_level_plot.png', dpi=300)
    return plt.gca()