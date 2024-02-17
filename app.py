"""
app.py run the streamlit interface.

Author: Damien Jacob
Creation Date: 17/02/2024

"""

import streamlit as st


st.title("The coach")

#take the input field 
candidate_fields = ["roles", "educations", "work experiences"]
option = st.selectbox(
    "talk more about your ",
    candidate_fields)
