class Student:
    def __init__(self, student_id, name):
        # Validate inputs
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty")
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty")
        self.id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        self.is_passed = False
        self.honor_roll = False
        self.average = 0.0
        self.letter_grade = "F"

    def add_grade(self, grade):
        """Add a grade with validation"""
        try:
            grade_value = float(grade)
            if grade_value < 0 or grade_value > 100:
                raise ValueError(f"Grade {grade_value} is out of range "
                                 f"(0-100)")
            self.grades.append(grade_value)
            self._update_calculations()
            return True
        except (ValueError, TypeError) as e:
            print(f"Error adding grade '{grade}': {e}")
            return False

    def calculate_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def _update_calculations(self):
        """Update all calculated values"""
        self.average = self.calculate_average()
        self.letter_grade = self._get_letter_grade()
        self.is_passed = self.average >= 60
        self.honor_roll = self.average >= 90

    def _get_letter_grade(self):
        """Convert average to letter grade"""
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

    def remove_grade_by_value(self, value):
        """Remove grade by its value"""
        try:
            grade_value = float(value)
            if grade_value in self.grades:
                self.grades.remove(grade_value)
                self._update_calculations()
                print(f"Removed grade {grade_value}")
                return True
            else:
                print(f"Grade {grade_value} not found")
                return False
        except (ValueError, TypeError) as e:
            print(f"Error removing grade '{value}': {e}")
            return False

    def remove_grade_by_index(self, index):
        """Remove grade by its index"""
        try:
            if 0 <= index < len(self.grades):
                removed_grade = self.grades.pop(index)
                self._update_calculations()
                print(f"Removed grade {removed_grade} at index {index}")
                return True
            else:
                print(f"Index {index} is out of range "
                      f"(0-{len(self.grades)-1})")
                return False
        except (ValueError, TypeError) as e:
            print(f"Error removing grade at index '{index}': {e}")
            return False

    def generate_report(self):
        """Generate comprehensive student summary report"""
        print("\n" + "="*50)
        print("STUDENT SUMMARY REPORT")
        print("="*50)
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average:.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Pass/Fail Status: {'PASSED' if self.is_passed else 'FAILED'}")
        print(f"Honor Roll: {'YES' if self.honor_roll else 'NO'}")
        print("="*50)


def demo_system():
    """Demonstrate the Student Grade Management System"""
    print("Student Grade Management System Demo")
    print("="*40)

    try:
        # Create student
        student1 = Student("S001", "Alice Johnson")
        print(f"Created student: {student1.name} (ID: {student1.id})")

        # Add grades
        print("\nAdding grades...")
        student1.add_grade(95.5)
        student1.add_grade(87.0)
        student1.add_grade(92.0)
        student1.add_grade(88.5)

        # Try invalid grade
        print("\nTrying invalid grade...")
        student1.add_grade("invalid")
        student1.add_grade(150)  # Out of range

        # Generate report
        student1.generate_report()

        # Test grade removal
        print("\nTesting grade removal...")
        student1.remove_grade_by_value(87.0)
        student1.remove_grade_by_index(0)
        student1.remove_grade_by_index(10)  # Invalid index

        # Final report
        print("\nFinal report after removals:")
        student1.generate_report()

        # Create another student
        print("\n" + "="*40)
        student2 = Student("S002", "Bob Smith")
        student2.add_grade(45.0)
        student2.add_grade(55.0)
        student2.add_grade(65.0)
        student2.generate_report()

    except ValueError as e:
        print(f"Error creating student: {e}")


if __name__ == "__main__":
    demo_system()
