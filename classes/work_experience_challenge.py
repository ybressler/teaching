import os
import json
from datetime import datetime

# Load your data
with open('classes/work_experience_challenge.json', 'r') as f:
    data = json.load(f)


class Person:
    """Create a person to represent each person in the dataset"""
    def __init__(self, first_name: str, last_name: str, **kwargs):
        self.first_name = first_name
        self.last_name = last_name

        # If work experiences are provided, initialize them
        if kwargs.get('work_experience'):
            self.work_experience = [WorkExperience(**x) for x in kwargs.get('work_experience')]
        else:
            self.work_experience = []  # always init with no experiences


class WorkExperience:
    """Represents a work experience, regardless of whom"""

    def __init__(self, company: str, title: str, start_date: datetime, end_date: datetime):
        self.company = Company(company)
        self.job_title = JobTitle(title)
        self.start_date = self.validate_dt(start_date)
        self.end_date = self.validate_dt(end_date)

    @staticmethod
    def validate_dt(dt):
        """Convert to date if a string"""
        # If no date is provided, set the dt to now
        if dt is None:
            return datetime.now()

        if isinstance(dt, str):
            return datetime.strptime(dt, '%Y-%m-%d')

        else:
            return dt


class Company:
    """Represent a company"""
    def __init__(self, name: str):
        self.name = name


class JobTitleHelper:
    """Use this class to add functionality to `JobTitle`"""
    def __init__(self):
        # One helper function
        self.is_senior = 'senior' in self.name.lower()
        # Add more helper functions here


class JobTitle(JobTitleHelper):
    """Represents a job title"""

    def __init__(self, name: str):
        # Set your own attributes
        self.name = name

        # Then, initialize `JobTitleHelper`
        super().__init__()





# -----------------------------------------------------------------------------

my_people = []

# Iterate through your records
for record in data:
    my_person = Person(**record)
    my_people.append(my_person)


[x.__dict__ for x in my_people]

my_people[0].work_experience[0].job_title.__dict__
