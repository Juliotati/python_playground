import random

from screening_demo.student import Student


class StudentsScreening:
    _all_students: list = [Student]
    _closing_time: int = 12
    _min_temperature: int = 35
    _max_temperature: int = 42
    _normal_temperature: int = 38
    _campus_capacity: int = 300
    _total_students = 500
    _last_student_arrival: int = 0

    def __init__(self):
        # nothing here
        pass

    def start_screening(self):
        self._reset(self)
        print('------------------------------------------------------------------------------------')
        print('Starting screening')
        for index in range(self._total_students):
            if self._campus_is_full() and self._should_close_campus():
                student_arrival_time: int = random.randint(1, 12)
                student_temperature: int = self._get_student_temperature()
                if self._is_after_closing_time(student_arrival_time) and self._has_high_temp(student_temperature):
                    self._all_students.append(
                        Student(
                            f'Student {index}',
                            student_temperature,
                            True,
                            student_arrival_time,
                        )
                    )
                    self._admitted(index, student_arrival_time, student_temperature)
                    continue

                self._last_student_arrival = student_arrival_time
                self._all_students.append(
                    Student(
                        f'Student {index}',
                        student_temperature,
                        False,
                        student_arrival_time,
                    ),
                )
                self._not_admitted(index, student_arrival_time, student_temperature)

        self._get_results()

    def _get_results(self):
        print('\n')
        print(f'All students: {len(self._students())}')
        print(f'Admitted students: {len(self._students(True))}')

        print(f'Students not admitted: {len(self._students(False))}')
        print('------------------------------------------------------------------------------------')

    @staticmethod
    def _not_admitted(index: int, student_arrival_time, students_temperature: int):
        print(
            f'Student {index} could not enter at {student_arrival_time}, temp is {students_temperature} and is not '
            f'admitted.')

    @staticmethod
    def _admitted(name: int, student_arrival_time: int, students_temperature: int):
        print(f'Student {name} enter at {student_arrival_time}, temp is {students_temperature} and is admitted.')

    @staticmethod
    def _reset(self):
        self._last_student_arrival = 0
        self._all_students.clear()

    def _get_student_temperature(self) -> int:
        return random.randrange(self._min_temperature, self._max_temperature)

    def _is_after_closing_time(self, random_hour: int) -> bool:
        return random_hour < self._closing_time

    def _has_high_temp(self, random_temp) -> bool:
        return random_temp < self._normal_temperature

    def _campus_is_full(self) -> bool:
        return len(self._students(True)) < self._campus_capacity

    def _should_close_campus(self) -> bool:
        return self._last_student_arrival < self._closing_time

    def _students(self, admitted_status: bool = None) -> [Student]:
        if admitted_status is not None:
            return list(filter(lambda st: st.admission_status == admitted_status, self._all_students))
        return self._all_students
