import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("census.csv")
states = list(df["State"].unique())
states.insert(0, "OverAll India")

st.sidebar.title("India Data Visualization")
state = st.sidebar.selectbox("Select a state", states)
primary = st.sidebar.selectbox("Select primary parameter",df.columns[8:])
secondary = st.sidebar.selectbox("Select secondary parameter",df.columns[8:])

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represent Primary Parameter")
    st.text("Colour represent Secondary Parameter")
    if state == "OverAll India":
        fig = px.scatter_mapbox(df,lat="Latitude",hover_name="District",lon="Longitude",zoom=3,size=primary,color=secondary,mapbox_style="carto-positron",width=1400 ,height=700)
        st.plotly_chart(fig,use_container_width=True)
    else:
        temp_df = df[df["State"] == state]
        fig = px.scatter_mapbox(temp_df, lat="Latitude",hover_name="District", lon="Longitude", zoom=3, size=primary, color=secondary,
                                mapbox_style="carto-positron", width=1400, height=700)
        st.plotly_chart(fig, use_container_width=True)
