import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "ipl.jpg")

DATA_PATH = os.path.join(dir_of_interest, "data", "ipl_clean.csv")

st.title(":blue[IPL] Dataset Dashboard  🏏")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("DataFrame")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.header("Team Vs Expenditure On Players")
team = st.selectbox("Choose Team :",options=df["Team"].unique())

col1, col2 = st.columns(2)

fig_1 = px.bar(data_frame=df[df['Team'] == team], y="Price Cr", x="Player Name", title=f"Team : {team}")
col1.plotly_chart(fig_1, use_container_width=False)

fig_2 = px.box(data_frame=df[df['Team'] == team], y="Price Cr",title=f"Team : {team}")
col1.plotly_chart(fig_2, use_container_width=False)


fig_3 = px.bar(data_frame=df[df['Team'] == team], x="Player Name",y="Price Cr", color="Type", title=f"Team : {team}")
col1.plotly_chart(fig_3, use_container_width=False)

st.markdown("Created By : S. Vamshi Krishna, Data Science Intern @ Innomatics.")
