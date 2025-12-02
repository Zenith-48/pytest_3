from employee import employee_details
def test_employee_details():
   
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E123\n"
        "Department: Engineering\n"
        "Salary: 90000\n"
    )
    assert employee_details("Alice","E123","Engineering","90000") == expected_output