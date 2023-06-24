import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_path = 'img/M31 plot.jpg'
image = mpimg.imread(image_path)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Display the image as a background using imshow()
ax.imshow(image)

# Plot additional data on top of the image
x = ['dec'] #dec
y = ['ra'] #RA
ax.scatter(x, y, color='red', marker='o', label='prediction position')

# Add labels, legends, and titles
ax.set_xlabel('Right Ascension (deg)')
ax.set_ylabel('Declination (deg)')
ax.set_title('Sky Coordinate-Aware Plotting Example')

# Show the legend
ax.legend()

# Remove the axis ticks and labels if desired
ax.set_xticks([])
ax.set_yticks([])

# Display the plot
plt.show()
