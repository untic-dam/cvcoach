"""
app.py run the streamlit interface.

Author: Damien Jacob
Creation Date: 17/02/2024

"""

import streamlit as st


#init variables
if "candidate" not in st.session_state:
    #store the candidate object
    candidate = {
        "roles": None,
        "educations": None,
        "work experiences": None
    }
    st.session_state.candidate = candidate


#functions
def _str_to_list(_list):
    return _list.split(", ")

def get_roles():
    roles_str = st.text_input("type your different roles (seperate your positions by , )")
    roles = _str_to_list(roles_str)
    st.session_state.candidate["roles"] = roles


#app
st.title("The coach")

#take the input field 
candidate_fields = ["roles", "educations", "work experiences"]
field_selection = st.selectbox(
    "talk more about your ",
    candidate_fields)

#roles
if field_selection == "roles":
    get_roles()

#education
if field_selection == "educations":
    pass


st.write(st.session_state.candidate)