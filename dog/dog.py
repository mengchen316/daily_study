import matplotlib.pyplot as plt


def draw_dog():
    print("Setting up the figure and axis...")
    fig, ax = plt.subplots(figsize=(6, 6))

    print("Drawing the head...")
    head = plt.Circle((0.5, 0.7), 0.2, color='tan', ec='black')
    ax.add_patch(head)

    print("Drawing the eyes...")
    left_eye = plt.Circle((0.45, 0.75), 0.02, color='black')
    right_eye = plt.Circle((0.55, 0.75), 0.02, color='black')
    ax.add_patch(left_eye)
    ax.add_patch(right_eye)

    print("Drawing the nose...")
    nose = plt.Circle((0.5, 0.68), 0.02, color='black')
    ax.add_patch(nose)

    print("Drawing the ears...")
    left_ear = plt.Polygon([[0.35, 0.85], [0.4, 0.7], [0.3, 0.7]], color='brown', ec='black')
    right_ear = plt.Polygon([[0.65, 0.85], [0.6, 0.7], [0.7, 0.7]], color='brown', ec='black')
    ax.add_patch(left_ear)
    ax.add_patch(right_ear)

    print("Drawing the body...")
    body = plt.Circle((0.5, 0.3), 0.3, color='tan', ec='black')
    ax.add_patch(body)

    print("Drawing the tail...")
    tail = plt.Polygon([[0.2, 0.35], [0.25, 0.35], [0.2, 0.4]], color='tan', ec='black')
    ax.add_patch(tail)

    print("Drawing the legs...")
    left_leg = plt.Rectangle((0.35, 0.05), 0.08, 0.25, color='tan', ec='black')
    right_leg = plt.Rectangle((0.57, 0.05), 0.08, 0.25, color='tan', ec='black')
    ax.add_patch(left_leg)
    ax.add_patch(right_leg)

    print("Finalizing the plot adjustments...")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    print("Displaying the drawing...")
    plt.show()


print("Calling the draw_dog function...")
draw_dog()
