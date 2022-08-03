import random

from screening_demo.student import Student


class StudentsScreening:
    all_students: list = [Student]
    closing_time: int = 12
    min_temperature: int = 35
    max_temperature: int = 42
    normal_temperature: int = 38
    campus_capacity: int = 300
    total_students = range(500)
    last_student_arrival: int = 0

    def __init__(self):
        # nothing here
        pass

    def start_screening(self):
        self.reset(self)
        print('------------------------------------------------------------------------------------')
        print('Starting screening')
        for index in self.total_students:
            if self.campus_is_full() and self.should_close_campus():
                student_arrival_time: int = random.randint(0, 12)
                student_temperature: int = self.get_student_temperature()
                if self.is_after_closing_time(student_arrival_time) and self.has_high_temp(student_temperature):
                    self.all_students.append(
                        Student(
                            f'Student {index}',
                            student_temperature,
                            True,
                            student_arrival_time,
                        )
                    )
                    self.admitted(index, student_arrival_time, student_temperature)
                    continue

                self.last_student_arrival = student_arrival_time
                self.all_students.append(
                    Student(
                        f'Student {index}',
                        student_temperature,
                        False,
                        student_arrival_time,
                    ),
                )
                self.not_admitted(index, student_arrival_time, student_temperature)

        self.get_results()

    def get_results(self):
        print('\n')
        print(f'All students: {len(self.students())}')
        print(f'Admitted students: {len(self.students(True))}')

        print(f'Students not admitted: {len(self.students(False))}')
        print('------------------------------------------------------------------------------------')

    @staticmethod
    def not_admitted(index: int, student_arrival_time, students_temperature: int):
        print(
            f'Student {index} could not enter at {student_arrival_time}, temp is {students_temperature} and is not '
            f'admitted.')

    @staticmethod
    def admitted(name: int, student_arrival_time: int, students_temperature: int):
        print(f'Student {name} enter at {student_arrival_time}, temp is {students_temperature} and is admitted.')

    @staticmethod
    def reset(self):
        self.last_student_arrival = 0
        self.all_students.clear()

    def get_student_temperature(self) -> int:
        return random.randrange(self.min_temperature, self.max_temperature)

    def is_after_closing_time(self, random_hour: int) -> bool:
        return random_hour < self.closing_time

    def has_high_temp(self, random_temp) -> bool:
        return random_temp < self.normal_temperature

    def campus_is_full(self) -> bool:
        return len(self.students(True)) < self.campus_capacity

    def should_close_campus(self) -> bool:
        return self.last_student_arrival < self.closing_time

    def students(self, admitted_status: bool = None) -> [Student]:
        if admitted_status is not None:
            return self.students_with_status(admitted_status)
        return self.all_students

    def students_with_status(self, admitted_status: bool):
        students = []
        for stu in self.all_students:
            if stu.admission_status is admitted_status:
                students.append(stu)
        return students
