public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        int result1 = calculator.add(3, 5);
        System.out.println("3 + 5 = " + result1);

        int result2 = calculator.subtract(10, 6);
        System.out.println("10 - 6 = " + result2);
    }
}
