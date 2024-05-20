def main(lat,lon):
    # Create a new figure with a specified size
    plt.figure(figsize=(10, 10))
    
    # Define the Arctic polar stereographic projection
    ax = plt.axes(projection=ccrs.NorthPolarStereo())

    # Set the extent of the map (Arctic region)
    ax.set_extent([-180, 180, 60, 90], ccrs.PlateCarree())

    # Add coastlines
    ax.coastlines(resolution='110m', linewidth=1)

    # Add gridlines for latitude and longitude
    ax.gridlines(color='gray', linestyle='--')

    # Add a title
    plt.title('Arctic Map Projection with Latitude and Longitude Lines')

    # Example dataset of points with latitudes and longitudes


    # Plot the dataset onto the map
    ax.plot(lon, lat, marker='o', color='red', markersize=5, transform=ccrs.PlateCarree())

    # Show the plot
    plt.show()