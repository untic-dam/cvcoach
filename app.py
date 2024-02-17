"""
app.py run the streamlit interface.

Author: Damien Jacob
Creation Date: 17/02/2024

"""

import streamlit as st
import json
import os


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

sector_field = [
    "Agriculture, Forestry, and Fishing",
    "Mining, Quarrying, and Oil and Gas Extraction",
    "Utilities",
    "Manufacturing",
    "Construction",
    "Wholesale Trade",
    "Retail Trade",
    "Transportation and Warehousing",
    "Information",
    "Finance and Insurance",
    "Real Estate, Rental and Leasing",
    "Professional, Scientific, and Technical Services",
    "Administrative and Support Services, Waste Management and Remediation Services",
    "Educational Services",
    "Healthcare and Social Assistance",
    "Arts, Entertainment, and Recreation",
    "Accommodation and Food Services",
    "Other Services (except Public Administration)",
    "Public Administration",
    "Unclassified"
]

if "candidate" not in st.session_state:
    #store the candidate object
    candidate = {
        "roles": [],
        "educations": [],
        "work_experiences": []
    }
    st.session_state.candidate = candidate

if "projects" not in st.session_state:
    st.session_state.projects = []

if "tasks" not in st.session_state:
    st.session_state.tasks = []

#functions
def _export_candidate_to_json():
    candidate_dict = st.session_state.candidate
    data_folder = "data"

    # Create the data folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    with open("data/candidate.json", "w") as file:
        json.dump(candidate_dict, file, indent=4)

def _str_to_list(_list):
    return _list.split(", ")

def get_roles():
    roles_str = st.text_input("type your different roles (seperate your positions by , )")
    roles = _str_to_list(roles_str)
    st.session_state.candidate["roles"] = roles

def get_education():
    education = {}
    add_1 = st.button("add this education", key="add_1")
    education["grade"] = st.text_input("grade : ")
    education["title"] = st.text_input("name of the formation : ")
    education["website"] = st.text_input("website of the formation : ")
    education["description"] = st.text_area("short description of the purpose of this formation :")

    education["institute"] = st.text_input("name of the institution : ")
    education["country"] = st.text_input("country : ")
    education["city"] = st.text_input("city : ")

    education["date_start"] = st.date_input("start")
    education["date_end"] = st.date_input("end")

    education["field_of_study"] = st.multiselect("select your study field :", study_fields)
    tasks_str = st.text_input("list task that you accomplish :")
    education["tasks"] = _str_to_list(tasks_str)
    add_2 = st.button("add this education", key="add_2")

    if add_1 or add_2:
        st.session_state.candidate["educations"].append(education)

#app
st.title("The coach")

#take the input field 
candidate_fields = ["work experiences", "educations", "roles"]
field_selection = st.selectbox(
    "talk more about your ",
    candidate_fields)

#roles
if field_selection == "roles":
    get_roles()

#education
if field_selection == "educations":
    get_education()

#work experience
if field_selection == "work experiences":
    work_experience = {}
    add_3 = st.button("add this experience", key="add_3")
    
    #work_experience["company_name"] = st.text_input("company name : ")
    #work_experience["company_website"] = st.text_input("website of the company: ")
    #work_experience["company_description"] = st.text_area("short description of company :")
    #work_experience["companay_sectors"] = st.multiselect("sectors : ", sector_field)

    #work_experience["company_country"] = st.text_input("country : ")
    #work_experience["company_city"] = st.text_input("city : ")

    #work_experience["date_start"] = st.date_input("start")
    #work_experience["date_end"] = st.date_input("end")

    work_experience["role_title"] = st.text_input("role title : ")
    work_experience["role_description"] = st.text_input("role description : ")

    st.write("projects")
    project = {}
    project["name"] = st.text_input("name : ")
    project["description"] = st.text_input("description :")

    st.write("tasks")
    task = {}
    task["task"] = st.text_input("taks achieved :")
    task["skills"] = st.text_input("skills involved :")
    task["quantification"] = st.text_input("quantification :")
    add_task = st.button("add this task", key="add_task")
    if add_task:
        st.session_state.tasks.append(task)

    #end of tasks
    project["tasks"] = st.session_state.tasks

    add_project = st.button("add this project", key="add_project")
    if add_project:
        st.session_state.projects.append(project)

    #end of projects
    work_experience["projects"] = st.session_state.projects

    #end experience
    add_4 = st.button("add this experience", key="add_4")

    if add_3 or add_4:
        st.session_state.candidate["work_experiences"].append(work_experience)


#export le json
st.button("save json", key="save_json", on_click=_export_candidate_to_json)

st.write(st.session_state.candidate)