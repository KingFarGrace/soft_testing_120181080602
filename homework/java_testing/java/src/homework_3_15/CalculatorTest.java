package homework_3_15;

import static org.junit.Assert.*;

import org.junit.Test;

public class CalculatorTest {

	@Test
	public void testAdd() {
		assertTrue(10 == new Calculator().add(4.5, 5.5));
	}

	@Test
	public void testMinus() {
		assertTrue(10 == new Calculator().minus(15.5, 5.5));
	}

	@Test
	public void testMultiple() {
		assertTrue(6.25 == new Calculator().multiple(2.5, 2.5));
	}
	
	@Test
	public void testDivide() {
		assertTrue(10 == new Calculator().divide(55, 5.5));
	}

}
