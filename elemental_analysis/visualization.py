import plotly.graph_objs as go


def make_plotly_splom(data):
    fig = go.Figure(
        go.Splom(
            dimensions=[
                dict(label=colname, values=data[colname])
                for colname in data.columns[1:]
            ],
            text=data["name"],
        )
    )

    fig.update_layout(height=950, width=950, title_text="Elemental analysis methods")

    return fig
