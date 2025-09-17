package com.example;

public class Main {
    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Usage: add|sub <int> <int>");
            System.exit(1);
        }

        String op = args[0];
        int a = Integer.parseInt(args[1]);
        int b = Integer.parseInt(args[2]);
        int result;

        switch (op) {
            case "add": result = Calculator.add(a, b); break;
            case "sub": result = Calculator.sub(a, b); break;
            default:
                System.out.println("Unknown op: " + op);
                System.exit(2);
                return;
        }

        System.out.println(result);
    }
}
