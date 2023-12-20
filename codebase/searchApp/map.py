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
            self.fig.add_shape(type="rect",
                               x0=obs[0], y0=obs[1], x1=obs[0]+1, y1=obs[1]+1,
                               fillcolor="black"
                               )
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

        # Add a rectangle to represent the block
        self.fig.add_shape(type="rect",
                           x0=x, y0=y, x1=x+1, y1=y+1,
                           line=dict(color=color),
                           fillcolor=color)

        # Add text for g, h, and f values
        if g is not None:
            self.fig.add_annotation(x=x+0.5, y=y+0.5, text='G: %.1f' % g,
                                    showarrow=False, font=dict(size=12), align="center")
        if f is not None:
            self.fig.add_annotation(x=x+0.5, y=y+0.3, text='F: %.1f' % f,
                                    showarrow=False, font=dict(size=12), align="center")
        if h is not None:
            self.fig.add_annotation(x=x+0.5, y=y+0.7, text='H: %.1f' % h,
                                    showarrow=False, font=dict(size=12), align="center")
