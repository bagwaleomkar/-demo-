
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Student {

    // Structure
    struct StudentData {
        uint rollNo;
        string name;
        uint marks;
    }

    // Array
    StudentData[] public students;

    // Add Student
    function addStudent(
        uint _rollno,
        string memory _name,
        uint _marks
    ) public {
        students.push(StudentData(_rollno, _name, _marks));
    }

    // Display function
    function getstudent(uint index)
        public
        view
        returns (uint, string memory, uint)
    {
        StudentData memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    // Fallback function
    fallback() external {
    }
}
