from typing import List, Optional
from pydantic import BaseModel, HttpUrl
from datetime import date


class Task(BaseModel):
    task: str
    skills: str
    quantification: Optional[str] = None


class Project(BaseModel):
    name: str
    description: str
    tasks: List[Task]


class WorkExperience(BaseModel):
    company_name: str
    company_website: HttpUrl
    company_description: str
    company_sectors: List[str]
    company_country: str
    company_city: str
    date_start: date
    date_end: date
    role_title: str
    role_description: str
    projects: List[Project]


class Education(BaseModel):
    grade: str
    title: str
    website: HttpUrl
    description: str
    institute: str
    country: str
    city: str
    date_start: date
    date_end: date
    field_of_study: List[str]
    tasks: List[str]  # Assuming tasks are simple strings based on _str_to_list usage


class Candidate(BaseModel):
    roles: List[str]
    educations: List[Education]
    work_experiences: List[WorkExperience]


if __name__ == "__main__":
    # Define your Pydantic models (Task, Project, WorkExperience, Education, Candidate) here

    # Example instantiation and conversion to JSON
    candidate = Candidate(
        roles=['Software Engineer', 'Data Scientist'],
        educations=[
            Education(
                grade='Bachelor',
                title='BSc in Computer Science',
                website='https://www.university.edu',
                description='A comprehensive computer science program.',
                institute='University of Example',
                country='Country',
                city='City',
                date_start=date(2016, 9, 1),
                date_end=date(2020, 5, 31),
                field_of_study=['Computer Science'],
                tasks=['Developed a software project', 'Participated in a research project']
            )
        ],
        work_experiences=[
            WorkExperience(
                company_name='Tech Company',
                company_website='https://www.techcompany.com',
                company_description='A leading tech company.',
                company_sectors=['Technology', 'Software'],
                company_country='Country',
                company_city='City',
                date_start=date(2020, 6, 1),
                date_end=date(2024, 1, 31),
                role_title='Software Engineer',
                role_description='Worked on developing and maintaining software products.',
                projects=[
                    Project(
                        name='Project A',
                        description='A project to develop a new product.',
                        tasks=[
                            Task(
                                task='Developed a feature',
                                skills='Programming, Debugging',
                                quantification='Increased performance by 10%'
                            )
                        ]
                    )
                ]
            )
        ]
    )
    # Convert the candidate instance to a JSON string
    print(candidate)
