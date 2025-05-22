from math import pi, sqrt, cos, sin, atan
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

# Nested list containing all categories data
categories = [
    [1.80, 3.00, 3.35, 3.65, 3.80, 3.95, 4.10, 4.20, 4.30, 4.35, 4.40],  # Category 0
    [1.50, 2.80, 3.20, 3.45, 3.65, 3.80, 3.90, 4.05, 4.15, 4.20, 4.30],  # Category I
    [1.40, 2.30, 2.80, 3.10, 3.30, 3.50, 3.60, 3.70, 3.80, 3.90, 4.00],  # Category II
    [1.30, 2.00, 2.20, 2.50, 2.70, 2.90, 3.00, 3.15, 3.25, 3.35, 3.45],  # Category III
    [1.20, 1.20, 1.65, 1.95, 2.15, 2.35, 2.50, 2.60, 2.75, 2.85, 2.95]   # Category IV
]

# Heights corresponding to the values in categories
heights = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def interpolate_value(z, category_index):
    """
    Simple linear interpolation to find the value at a specific height z, 
    within the given category, without using any external libraries.
    
    :param z: Target height (must be between 0 and 100)
    :param category_index: Index of the category (0 to 4)
    :return: Interpolated value at height z, rounded to the nearest ten
    """
    if not (0 <= z <= 100):
        raise ValueError("Height z must be between 0 and 100.")
    if not (0 <= category_index < len(categories)):
        raise ValueError("Invalid category index. Must be between 0 and 4.")

    # Get the category data
    category_values = categories[category_index]

    # Find the position in the heights array where z would fit
    for i in range(len(heights) - 1):
        if heights[i] <= z <= heights[i + 1]:
            # Heights and values at the interval endpoints
            x1, y1 = heights[i], category_values[i]
            x2, y2 = heights[i + 1], category_values[i + 1]
            
            # Linear interpolation formula: y = y1 + ((y2 - y1) / (x2 - x1)) * (z - x1)
            interpolated_value = y1 + ((y2 - y1) / (x2 - x1)) * (z - x1)
            return interpolated_value

    # If z exactly matches the last point
    if z == heights[-1]:
        return round(category_values[-1] / 10) * 10

    # If z is outside the interpolation bounds
    raise ValueError("Height z is out of the interpolation bounds.")


def draw_arrow(fig, xList, yList, direction, scaleX, scaleY):
    # Main line with square markers
    fig.add_trace(go.Scatter(
        x=xList,
        y=yList,
        mode="lines+markers",
        marker=dict(
            size=5,
            symbol="circle",
            color='black'
        ),
        line=dict(width=1, color='black')
    ))

    # Short end lines to mark start and end
    if direction == "X":
        xLine1 = [xList[0], xList[0]]
        yLine1 = [yList[0] - 5*scaleY, yList[0] + 5*scaleY]
        xLine2 = [xList[-1], xList[-1]]
        yLine2 = [yList[-1] - 5*scaleY, yList[-1] + 5*scaleY]
    elif direction == "Y":
        xLine1 = [xList[0] - 5*scaleX, xList[0] + 5*scaleX]
        yLine1 = [yList[0], yList[0]]
        xLine2 = [xList[-1] - 5*scaleX, xList[-1] + 5*scaleX]
        yLine2 = [yList[-1], yList[-1]]

    fig.add_trace(go.Scatter(
        x=xLine1, y=yLine1,
        mode="lines",
        line=dict(color='black', width=1)
    ))
    fig.add_trace(go.Scatter(
        x=xLine2, y=yLine2,
        mode="lines",
        line=dict(color='black', width=1)
    ))


def add_text(fig, text, xPosition, yPosition, textSize):
    fig.add_annotation(dict(font=dict(size=textSize, color = "black"),
                                            x = xPosition,
                                            y = yPosition,
                                            showarrow=False,
                                            text=text,
                                            textangle=0,
                                            xanchor='left',
                                            xref="x",
                                            yref="y"))
    
    
def createMatplotTable(columns, cell_text):
    
    # Data for the table
    # columns = ['Roof area', 'Explanation', 'F', 'G', 'H']
    # rows = ['coefficients', '$w_k$ [kN/m²]', '$w_d$ [kN/m²]']
    # cell_text = [['-', '-2.5', '-2', '-1.2'],
    #             ['char. wind load', '-2.97', '-2.38', '-1.43'],
    #             ['design wind load', '-4.46', '-3.57', '-2.15']]

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(8, 2))

    # Hide axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    # Create the table
    table = ax.table(cellText=cell_text,
                    # rowLabels=rows,
                    colLabels=columns,
                    cellLoc='center',
                    loc='center')

    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.5)

    # Highlight header
    for key, cell in table.get_celld().items():
        if key[0] == 0 or key[1] == -1:
            cell.set_text_props(color="red")
            cell.set_fontsize(10)

    # Save the table as an image
    plt.savefig('designWindLoads.png', bbox_inches='tight')


