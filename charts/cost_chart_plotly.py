import plotly.graph_objects as go
import pandas as pd

import streamlit as st


def get_plot(nl_config, df):
    title = "Annual cost of hosting a newsletter"
    labels = {"x": "Number of subscribers", "y": "Annual cost ($)"}

    trace_gp = go.Scatter(
        x=df["user_levels"],
        y=df["costs_gp"],
        mode="lines",
        name="Ghost Pro",
        line=dict(color=nl_config.gp_color),
    )
    trace_bd = go.Scatter(
        x=df["user_levels"],
        y=df["costs_bd"],
        mode="lines",
        name="Buttondown",
        line=dict(color=nl_config.bd_color),
    )
    trace_bh = go.Scatter(
        x=df["user_levels"],
        y=df["costs_bh"],
        mode="lines",
        name="beehiiv",
        line=dict(color=nl_config.bh_color),
    )
    trace_ss = go.Scatter(
        x=df["user_levels"],
        y=df["costs_ss"],
        mode="lines",
        name="Substack",
        line=dict(color=nl_config.ss_color),
    )

    # Create the figure and add the traces
    fig = go.Figure()
    if nl_config.show_gp:
        fig.add_trace(trace_gp)
    if nl_config.show_bd:
        fig.add_trace(trace_bd)
    if nl_config.show_bh:
        fig.add_trace(trace_bh)
    if nl_config.show_ss:
        fig.add_trace(trace_ss)

    # Update layout with title and axis labels
    fig.update_layout(
        title=title,
        xaxis_title=labels["x"],
        yaxis_title=labels["y"],
    )

    return fig
