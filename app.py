"""
app.py run the streamlit interface.

Author: Damien Jacob
Creation Date: 17/02/2024

"""

import streamlit as st


#init variables
study_fields = [
    "Computer Science",
    "Engineering",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "Psychology",
    "Economics",
    "Business Administration",
    "Political Science",
    "Sociology",
    "History",
    "Literature",
    "Philosophy",
    "Art History",
    "Music",
    "Foreign Languages",
    "Education",
    "Environmental Science",
    "Health Sciences"
]

if "candidate" not in st.session_state:
    #store the candidate object
    candidate = {
        "roles": [],
        "educations": [],
        "work experiences": []
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
candidate_fields = [ "educations", "work experiences", "roles"]
field_selection = st.selectbox(
    "talk more about your ",
    candidate_fields)

#roles
if field_selection == "roles":
    get_roles()

#education
if field_selection == "educations":
    education = {}
    education["grade"] = st.text_input("grade : ")
    #education["title"] = st.text_input("name of the formation : ")
    #education["website"] = st.text_input("website of the formation : ")
    #education["description"] = st.text_area("short description of the purpose of this formation :")

    #education["institute"] = st.text_input("name of the institution : ")
    #education["country"] = st.text_input("country : ")
    #education["city"] = st.text_input("city : ")

    #education["date_start"] = st.date_input("start")
    #education["date_end"] = st.date_input("end")

    #education["field_of_study"] = st.multiselect("select your study field :", study_fields)
    #tasks_str = st.text_input("list task that you accomplish :")
    #education["tasks"] = _str_to_list(tasks_str)
    add = st.button("add :")
    if add:
        st.session_state.candidate["educations"].append(education)
        #delete field


st.write(st.session_state.candidate)