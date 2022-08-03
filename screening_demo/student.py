class Student:
    name: str
    temperature: int
    admission_status: bool
    campus_arrival: int

    def __init__(self, name: str, temperature: int, admission_status: bool, campus_arrival: int):
        self.name = name
        self.temperature = temperature
        self.admission_status = admission_status
        self.campus_arrival = campus_arrival


def to_string(self):
    return f'''
        $name: {self.name}
        temperature: {self.temperate}
        admission_status: {self.admission_status}
        campus_arrival: {self.campus_arrival}
        '''
