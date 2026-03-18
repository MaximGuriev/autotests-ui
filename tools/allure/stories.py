from enum import Enum


class AllureStory(str, Enum):
    REGISTRATION = "Registration"
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    AUTHORIZATION = "Authorization"
