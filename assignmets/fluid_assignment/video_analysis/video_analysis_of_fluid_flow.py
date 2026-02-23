import marimo

__generated_with = "0.19.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import cv2
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    return cv2, np, plt, sns


@app.cell
def _(cv2):
    video_path = "fluid_assignment/video_analysis/fluid_flow_video.mp4"
    cap = cv2.VideoCapture(video_path)
    return (cap,)


@app.cell
def _(cap):
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    return


@app.cell
def _():
    # analysing video frames at different points

    # fixed points in x-axis and y-axis

    # starting from (909, 634)
    # ending at (909, 1034)

    x = 909
    y = [_i for _i in range(634, 1034, 40)]

    pixel_values = {coord: [] for coord in y}
    frames = []
    return frames, pixel_values, x, y


@app.cell
def _(cap, cv2, frames, pixel_values, x, y):
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for coord in y:
            # record the pixel intensity in gray color at x and y coordinate
            pixel_values[coord].append(gray_frame[coord, x])

            # mark the coordinate on the initial frame using circle and text
            cv2.circle(frame, (x, coord), radius=5, color=(255, 0, 0), thickness=2)
            cv2.putText(frame, f'({x}, {coord})', (x + 10, coord - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        frames.append(frame)

    cap.release()
    return


@app.cell
def _(cv2, frames, plt):
    # display the first frame with the marked coordinates
    plt.figure(figsize=(12, 6))
    plt.imshow(cv2.cvtColor(frames[0], cv2.COLOR_BGR2RGB))
    # plt.title("Video Analysis for Fluid Properties at Various Coordinates")
    plt.grid(True, alpha=0.5)
    plt.axis('on')
    plt.savefig('marked_coordinates_in_first_frame.svg', format='svg')
    plt.show()
    return


@app.cell
def _(np, pixel_values, plt, sns, y):
    # Heatmap of pixel intensities over time
    intensity_matrix = np.array([pixel_values[coord] for coord in y])

    plt.figure(figsize=(14, 6))
    sns.heatmap(intensity_matrix, cmap='crest', cbar_kws={'label': 'Pixel Intensity (0-255)'}, yticklabels=y)
    # plt.title('Heatmap of Pixel Intensities at x={} Over Time'.format(x))
    plt.xlabel('Frame Number')
    plt.ylabel('Y-Coordinate')
    plt.savefig('heatmap_of_different_frame_and_coordinates.svg', format='svg')
    plt.show()
    return


@app.cell
def _(pixel_values, plt, y):
    # Plot pixel intensity over time for each y-coordinate
    plt.figure(figsize=(12, 6))
    for _coord in y:
        plt.plot(pixel_values[_coord], label=f'y={_coord}')
    # plt.title('Pixel Intensity at (x={}) Over Time'.format(x))
    plt.xlabel('Frame Number')
    plt.ylabel('Pixel Intensity (0-255)')
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.savefig('pixel_instensity_over_time.svg', format='svg')
    plt.show()
    return


if __name__ == "__main__":
    app.run()
