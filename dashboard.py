import streamlit as st
import pandas as pd
import plotly.express as px

import apis
from apis import apod_generator

from apis import apod_generator

# in the terminal run: streamlit run dashboard.py
st.title('Water Quality Dashboard')
st.header('Internship Ready Software Development')
st.subheader("Jonathan Power")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2D Visualization",
     "3D Plots",
     "NASA's APOD"]
)

with tab1:
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    fig1 = px.line(df,
                   x = "Time",
                   y = "Temperature (c)")
    st.plotly_chart(fig1)

    fig2 = px.scatter(df,
                      x = "ODO mg/L",
                      y = "Temperature (c)",
                      color = "pH")
    st.plotly_chart(fig2)

with tab3:
    fig3 = px.scatter_3d(df,
                      x = "Longitude",
                      y = "Latitude",
                      z = "Total Water Column (m)",
                      color = "Temperature (c)")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("NASA Astronomy Picture of the Day")
    response = apod_generator(apis.url, apis.unique_key)

    st.subheader(response.get("title", "No Title Available"))

    st.image(response.get("url"), use_container_width=True)
    st.write("**Explanation:**")
    st.write(response.get("explanation", "No description provided."))
    st.caption(f"Date: {response.get('date')} | Copyright: {response.get('copyright', 'Public Domain')}")

