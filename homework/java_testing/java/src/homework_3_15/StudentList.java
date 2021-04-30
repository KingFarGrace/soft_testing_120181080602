package homework_3_15;

import java.util.ArrayList;
import java.util.List;

/**
 * @author ZHANGKAIHENG
 */
public class StudentList {

    private final List<Student> studentList;

    public StudentList() {
        this.studentList = new ArrayList<>();
    }

    public void createStudent(Student student) {
        this.studentList.add(student);
    }

    public Student retrieveStudent(int id) {
        for (Student stu : this.studentList) {
            if (stu.id == id) {
                return stu;
            }
        }
        return null;
    }

    public boolean updateStudent(Student student) {
        // update the element which has the same id with parameter
        for (int i = 0; i < this.studentList.size(); i++) {
            if (this.studentList.get(i).id == student.id) {
                this.studentList.set(i, student);
                return true;
            }
        }
        return false;
    }

    public boolean deleteStudent(int id) {
        for (int i = 0; i < this.studentList.size(); i++) {
            if (this.studentList.get(i).id == id) {
                this.studentList.remove(i);
                return true;
            }
        }
        return false;
    }

}
