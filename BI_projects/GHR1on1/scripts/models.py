from dataclasses import dataclass
from datetime import datetime

@dataclass
class ORGANIZATION_DATA:
    organization_id: int
    organization_name: str
    organization_level: int

@dataclass
class EMPLOYEE_DATA:
    employee_id: int
    organization_id: int
    employee_name: str
    manager_id: int

@dataclass
class SURVEY_MASTER:
    survey_id: int
    survey_name: str
    created_date: datetime

@dataclass
class SURVEY_DATA:
    response_id: int
    question_1: int
    question_2: int

@dataclass
class SURVEY_RESPONSE_META_DATA:
    response_id: int
    survey_id: int
    employee_id: int
    submit_date: datetime

def get_list_of_all_models():
    # [<class '__main__.ORGANIZATION_DATA'>, <class '__main__.EMPLOYEE_DATA'>, <class '__main__.SURVEY_MASTER'>, <class '__main__.SURVEY_DATA'>, <class '__main__.SURVEY_RESPONSE_META_DATA'>]
    return [cls for cls in globals().values() if isinstance(cls, type) and hasattr(cls, '__dataclass_fields__')]
