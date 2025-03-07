# On year select, load in that year's data - must cache
import streamlit as st

import utils.scoring as scoring
import components.visualizations as viz
import utils.data_loader as data_loader
import components.selectas as selectas
import components.kpi as kpi





if "player_details" not in st.session_state:
    data_loader.init_state("player_details", default_players=[
        {"name": "Olamide Zaccheaus", "position": "WR"},
    ])

# st.write(st.session_state.player_details)
header_container = st.container(border=True)
player_data = st.session_state.player_details["players"][0]["tables"]["player_data"]

with header_container:
    header_cols = st.columns(3)
    with header_cols[0]:
        st.image(player_data["headshot_url"].iloc[0])
    with header_cols[1]:
        st.write(player_data["player_display_name"].iloc[0])
    with header_cols[2]:
        selectas.format_selector("player_details")
        selectas.year_selector("player_details")
        selectas.player_selector("player_details")
        selectas.week_selector("player_details")


scoring_kpis_container = st.container(border=True)
with scoring_kpis_container:
    kpi.player_kpis("player_details")

viz.stat_radar("player_details")

viz.custom_bar("player_details")