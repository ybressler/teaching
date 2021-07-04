import os
import json
from datetime import datetime

# Load your data
with open('classes/work_experience_challenge.json', 'r') as f:
    data = json.load(f)


class Base:
    """Base functionality"""
    def __repr__(self):
        """Neat representation of an obj"""
        my_formatter = lambda k,v : f'{k}: {v}' if not isinstance(v,(list, dict)) else f'{k}: {v.__class__}'
        return ', '.join([my_formatter(k,v) for k,v in  self.__dict__.items()])

class Person(Base):
    """Create a person to represent each person in the dataset"""
    def __init__(self, first_name: str, last_name: str, **kwargs):
        self.first_name = first_name
        self.last_name = last_name

        # If work experiences are provided, initialize them
        if kwargs.get('work_experience'):
            self.work_experience = [WorkExperience(**x) for x in kwargs.get('work_experience')]
        else:
            self.work_experience = []  # always init with no experiences


class WorkExperience(Base):
    """Represents a work experience, regardless of whom"""

    def __init__(self, company: str, title: str, start_date: datetime, end_date: datetime):
        self.company = Company(company)
        self.job_title = JobTitle(title)
        self.start_date = self.validate_dt(start_date)
        self.end_date = self.validate_dt(end_date)

        # Now determine the length of time this person has held this job
        self.duration_months = (self.end_date - self.start_date).days // 30  # say there are 30 days in a month...

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


class Company(Base):
    """Represent a company"""
    def __init__(self, name: str):
        self.name = name


class JobTitleHelper(Base):
    """Use this class to add functionality to `JobTitle`"""
    def __init__(self):
        # One helper function
        self.is_senior = 'senior' in self.name.lower()
        # Add more helper functions here


class JobTitle(JobTitleHelper, Base):
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

# View each person by printing
my_person = my_people[0]
print(my_person)

# View their attributes by printing __dict__
print(my_person.__dict__)

# View their work experiences
for exp in my_person.work_experience:
    print(exp)
