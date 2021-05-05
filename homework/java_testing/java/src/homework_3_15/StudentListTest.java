package homework_3_15;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * @author ZHANGKAIHENG
 */
public class StudentListTest {

    StudentList studentList;
    private static Student stu1 = new Student(1, "张三");
    private static Student stu2 = new Student(2, "李四");
    private static Student stu3 = new Student(3, "王五");

    @Before
    public void testSetUp() {
        studentList = new StudentList();
        studentList.createStudent(stu1);
        studentList.createStudent(stu2);
        studentList.createStudent(stu3);
    }

    @Test
    public void createStudent() {
        studentList.createStudent(new Student(1, "小明"));
        studentList.createStudent(new Student(4, "赵六"));
    }

    @Test
    public void retrieveStudent() {
        assertEquals(studentList.retrieveStudent(1), stu1);
        assertEquals(studentList.retrieveStudent(5), null);
    }

    @Test
    public void updateStudent() {
        assertEquals(studentList.updateStudent(new Student(1, "小明")), true);
        assertEquals(studentList.updateStudent(new Student(4, "小明")), false);
    }

    @Test
    public void deleteStudent() {
        assertEquals(studentList.deleteStudent(1), true);
        assertEquals(studentList.deleteStudent(4), false);
    }
}