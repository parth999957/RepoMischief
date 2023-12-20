import plotly.graph_objects as go

class MAP(object):
    def __init__(self, nrow, ncol, start, goal, obstacles):
        self.nrow = nrow
        self.ncol = ncol
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.fig = None  # Initialize the figure

    def plot_map(self):
        # Create a Plotly figure
        self.fig = go.Figure()

        # Add grid lines
        for x in range(self.ncol + 1):
            self.fig.add_shape(type="line", x0=x, y0=0, x1=x, y1=self.nrow,
                               line=dict(color="LightGrey", width=2))
        for y in range(self.nrow + 1):
            self.fig.add_shape(type="line", x0=0, y0=y, x1=self.ncol, y1=y,
                               line=dict(color="LightGrey", width=2))

        # Add obstacles, start, and goal
        for obs in self.obstacles:
            self.fig.add_trace(go.Scatter(x=[obs[0]+0.5], y=[obs[1]+0.5],
                                          mode='markers',
                                          marker=dict(color='black', size=10)))
        self.fig.add_trace(go.Scatter(x=[self.start[0]+0.5], y=[self.start[1]+0.5],
                                      mode='markers',
                                      marker=dict(color='green', size=12)))
        self.fig.add_trace(go.Scatter(x=[self.goal[0]+0.5], y=[self.goal[1]+0.5],
                                      mode='markers',
                                      marker=dict(color='orange', size=12)))

        # Set layout
        self.fig.update_layout(showlegend=False,
                               xaxis=dict(showgrid=False, range=[0, self.ncol]),
                               yaxis=dict(showgrid=False, range=[0, self.nrow]),
                               width=800, height=800)
        return self.fig

    def set_node(self, x, y, state, g=None, h=None, f=None, stop=False):
        # Choose color based on the state
        color = {'red': 'red', 'green': 'lightgreen', 'blue': 'blue'}[state]
        self.fig.add_trace(go.Scatter(x=[x+0.5], y=[y+0.5],
                                      mode='markers',
                                      marker=dict(color=color, size=8)))

        # Add text for g, h, and f values
        if g is not None:
            self.fig.add_annotation(x=x+0.7, y=y+0.7, text='%.1f' % g,
                                    showarrow=False, font=dict(size=12))
        if f is not None:
            self.fig.add_annotation(x=x+0.35, y=y+0.2, text='%.1f' % f,
                                    showarrow=False, font=dict(size=12))
        if h is not None:
            self.fig.add_annotation(x=x+0.1, y=y+0.7, text='%.1f' % h,
                                    showarrow=False, font=dict(size=12))
