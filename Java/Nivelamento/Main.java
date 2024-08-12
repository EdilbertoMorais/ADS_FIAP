package com.fiap;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe um numero: ");
        int numero1 = scanner.nextInt();

        System.out.println("Informe outro numero: ");
        int numero2 = scanner.nextInt();

//        System.out.println(" Escolha uma operação:");
//        System.out.println("1 - Soma");
//        System.out.println("2 - Subtração");
//        System.out.println("3 - Multiplicação");
//        System.out.println("4 - Divisão");

        System.out.println("""
                Escolha uma operação:
                ----------------------
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
                ----------------------
                """);


        int op = scanner.nextInt();

        switch (op) {
            case 1:
                System.out.println("Resultado: " + (numero1 + numero2));
                break;
            case 2:
                System.out.println("Resultado: " + (numero1 - numero2));
                break;
            case 3:
                System.out.println("Resultado: " + (numero1 * numero2));
                break;
            case 4:
                if (numero2 == 0) {
                    System.out.println("Não é possível dividir por zero");
                    break;
                }
                System.out.println("Resultado: " + (numero1 / numero2));
                break;
            default:
                System.out.println("Operação inválida");
                break;
        }
        scanner.close();
    }
}