import streamlit as st
import matplotlib.pyplot as plt
from src.analysis import *

st.title("🏏 IPL Data Analysis Dashboard")

matches, deliveries = load_data()

# Top Batsmen
st.subheader("Top 10 Batsmen")
batsmen = top_batsmen(deliveries)
st.bar_chart(batsmen)

# Top Bowlers
st.subheader("Top 10 Bowlers")
bowlers = top_bowlers(deliveries)
st.bar_chart(bowlers)

# Win Percentage
st.subheader("Win Percentage by Team")
win_pct = win_percentage(matches)
st.bar_chart(win_pct)

# Toss Impact
st.subheader("Toss Impact")
impact = toss_impact(matches)
st.write(f"Teams winning toss also win match {impact}% of the time")