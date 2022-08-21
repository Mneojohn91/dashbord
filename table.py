import pandas as pd
import plotly_express as px #pip install plotly_express
import streamlit as st

# ==================================================================================
#                             Dashboard design
st.set_page_config(
    page_title="Production Dashboard", page_icon=":bar_chart", layout="wide"
)

st.title(":bar_chart:Production Dashboard")
st.markdown("##")

stars = round(75 / 20)
peformence_rating = ":star:" * stars
left_col, right_col = st.columns(2)
with left_col:
    st.subheader("Machine operation %:")
    st.subheader("75%")
with right_col:
    st.subheader("Peformace Rating:")
    st.subheader(f"{peformence_rating}")
st.markdown("...")
# ------------------------------------------------------------------------------------
#                             Creating DataFrames
production_df = pd.read_excel("Production planning for case study.xlsx",  header=2).loc[:15]
planning_hours = pd.read_excel("Production planning for case study.xlsx",  header=29)
summary = pd.read_excel("Production planning for case study.xlsx",  header=22)
# ------------------------------------------------------------------------------------
planning = planning_hours.dropna(how="all", axis=1)
summary_hours = summary[:4].dropna(how="all", axis=1)
downtime_hours = summary_hours.loc[3][1] * planning.loc[3][1]
hours_worked = summary_hours.loc[3][1] - downtime_hours
hours_labels = ["downtime hours", "hours worked"]
# --------------------------------------------------------------------------------------
#                           Plot/design Graphs
pie = px.pie(
    values=[downtime_hours, hours_worked],
    names=hours_labels,
    hover_name=hours_labels,
    title="<b>Hours worked VS machine downtime<b>",
)
bar = px.bar(
    production_df,
    x="Client",
    y=["Est. Profile scrap", "Est. Sellable weight", "Est. But scrap"],
    title="<b>Material Used  from Total Production<b>",
)
scatter = px.scatter(
    production_df,
    x="Client",
    y=["Est. But scrap", "Est. Profile scrap"],
    title="<b>Planned scrap <b>",
)

scatter2 = px.scatter(
    production_df,
    x="Delivery Date",
    y=["Est. Sellable weight", "Est. production mass(Kg)"],
    title="<b>Sellable weight vs Total planned production <b>",
)

# ===========================================================================================
#                           Dashboard Graphs
left_chart, right_chart = st.columns(2)
left_chart.plotly_chart(pie)
right_chart.plotly_chart(bar)

bottom_left, bottom_right = st.columns(2)
bottom_left.plotly_chart(scatter)
bottom_right.plotly_chart(scatter2)
