import cv2
import numpy as np
import matplotlib.pyplot as plt

video_path = "fluid_assignment/video_analysis/fluid_flow_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# analyze video properties at different points

# fixed points in x and y axis

# starting from (909, 635)
# ending at (909, 1033)

x = 909
y = [_i for _i in range(635, 1034, 10)]

pixel_values = {coord: [] for coord in y}  # Store pixel values for each y-coordinate
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    for coord in y:
        # record the pixel intensity at (x and y coordinate)
        pixel_values[coord].append(gray_frame[coord, x])
        
        # mark the coordinate on the frame
        cv2.circle(frame, (x, coord), radius=5, color=(255, 0, 0), thickness=2)
        cv2.putText(frame, f'({x}, {coord})', (x + 10, coord - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    frames.append(frame)
    
cap.release()

# display the first frame with the marked coordinates
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(frames[0], cv2.COLOR_BGR2RGB))
plt.title("Video Analysis for Fluid Properties at Various Coordinates")
plt.grid(True, alpha=0.5)
plt.axis('on')
plt.show()

# heatmap of pixel intensities over time
intensity_matrix = np.array([pixel_values[coord] for coord in y])

plt.figure(figsize=(12, 8))
plt.imshow(intensity_matrix, aspect='auto', cmap='coolwarm', extent=[0, intensity_matrix.shape[1], y[-1], y[0]])
plt.colorbar(label='Pixel Intensity (0-255)')
plt.title('Heatmap of Pixel Intensities at x={} Over Time'.format(x))
plt.xlabel('Frame Number')
plt.ylabel('Y-Coordinate')
plt.show()

# plot pixel intensity over time for each y-coordinate
plt.figure(figsize=(10, 6))
for coord in y:
    plt.plot(pixel_values[coord], label=f'y={coord}')
plt.title('Pixel Intensity at (x={}) Over Time'.format(x))
plt.xlabel('Frame Number')
plt.ylabel('Pixel Intensity (0-255)')
plt.grid()
plt.legend()
plt.show()
