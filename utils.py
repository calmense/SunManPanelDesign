from math import pi, sqrt, cos, sin, atan
import plotly.graph_objects as go


def draw_arrow(fig, xList, yList, direction, scaleX, scaleY):
    fig.add_trace(go.Scatter(x = xList, y = yList, marker= dict(size=8, symbol= "arrow", angleref="previous", color='black'), line=dict(width=1)))
       
    fig.add_trace(go.Scatter(x = list(reversed(xList)), y = list(reversed(yList)), marker= dict(size=8, symbol= "arrow", angleref="previous", color='black')))
    
    if direction == "X":
        xLine1 = [xList[0], xList[0]]
        yLine1 = [yList[0] - 5*scaleY, yList[0] + 5*scaleY]

        xLine2 = [xList[-1], xList[-1]]
        yLine2 = [yList[-1] - 5*scaleY, yList[-1] + 5*scaleY]

    elif direction == "Y":
        xLine1 = [xList[0] - 5*scaleY, xList[0] + 5*scaleY]
        yLine1 = [yList[0], yList[0]]

        xLine2 = [xList[-1] - 5*scaleY, xList[-1] + 5*scaleY]
        yLine2 = [yList[-1], yList[-1]]

    fig.add_trace(go.Scatter(x=xLine1, y = yLine1, mode="lines", marker=dict(color='black')))
    fig.add_trace(go.Scatter(x=xLine2, y = yLine2, mode="lines", marker=dict(color='black', angle = 45)))


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
    
    