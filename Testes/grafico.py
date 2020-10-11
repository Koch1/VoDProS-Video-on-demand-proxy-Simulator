import plotly.graph_objects as go
import numpy as np

x = np.arange(20)


fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=x**4,
                    mode='lines+markers',
                    name='azul'))
fig.add_trace(go.Scatter(x=x, y=x**3,
                    mode='lines+markers',
                    name='vermelho'))
fig.add_trace(go.Scatter(x=x, y=x**2,
                    mode='lines+markers',
                    name='preto',line=dict(color='rgb()', width=1)))


# Edit the layout
fig.update_layout(title='Average High and Low Temperatures in New York',
                   xaxis_title='Month',
                   yaxis_title='Temperature (degrees F)')


fig.show()