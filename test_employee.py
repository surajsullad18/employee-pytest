from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E0110\n"
        "Department: IT\n"
        "Salary: 55000"
    )

    assert employee_details("Alice", "E0110", "IT", 55000) == expected_output