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
            # Initialize a matrix to represent the grid
            grid = [[0 for _ in range(self.ncol)] for _ in range(self.nrow)]

            # Mark obstacles, start, and goal on the grid
            for obs in self.obstacles:
                grid[obs[1]][obs[0]] = -1  # For obstacles
            grid[self.start[1]][self.start[0]] = 1  # For start
            grid[self.goal[1]][self.goal[0]] = 2  # For goal

            # Create a Plotly figure with a heatmap
            self.fig = go.Figure(data=go.Heatmap(
                z=grid,
                x=list(range(self.ncol)),
                y=list(range(self.nrow)),
                colorscale=[
                    [0.00, "white"],      # Default
                    [0.33, "black"],      # Obstacles
                    [0.66, "green"],      # Start
                    [0.83, "orange"],     # Goal
                    [1.00, "red"]         # Path (example)
                ],
                showscale=False
            ))

            # Set layout
            self.fig.update_layout(
                xaxis=dict(showgrid=False, range=[0, self.ncol]),
                yaxis=dict(showgrid=False, range=[0, self.nrow]),
                width=800, height=800
            )
            return self.fig

    def set_node(self, x, y, state, g=None, h=None, f=None, stop=False):
        # Update the grid based on the state
        state_val = {'red': 3, 'green': 4, 'blue': 5}[state]
        self.fig.data[0].z[y][x] = state_val

        # Optional: Add text for g, h, and f values (if needed)
        if g is not None or h is not None or f is not None:
            annotation_text = f'G: {g:.1f}\nH: {h:.1f}\nF: {f:.1f}' if g is not None and h is not None and f is not None else ''
            self.fig.add_annotation(x=x, y=y, text=annotation_text, showarrow=False, font=dict(size=10))

        # Update the figure to reflect the changes
        self.fig.update_traces()
