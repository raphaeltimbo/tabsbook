import numpy as np
import plotly.graph_objects as go

x = np.arange(10)
for i in range(4):
    fig = go.Figure(data=go.Scatter(x=x, y=x**i))
    fig.write_html(f'plot_{i}.html')


if __name__ == '__main__':
    print('saved figs')


