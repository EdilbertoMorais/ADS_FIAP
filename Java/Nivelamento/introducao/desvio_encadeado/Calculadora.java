package com.fiap.introducao.desvio_encadeado;

import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double resultado = 0;
        String operacao;

        System.out.println("Digite o primeiro número:");
        double numero1 = scanner.nextDouble();
        System.out.println("Digite o segundo número:");
        double numero2 = scanner.nextDouble();
        System.out.println("Digite a operação desejada (+ - * /):");
        operacao = scanner.next();

        switch (operacao){
            case "+":
                resultado = numero1 + numero2;
                System.out.println("Soma = " + resultado);
                break;
            case "-":
                resultado = numero1 - numero2;
                System.out.println("Subtração = " + resultado);
                break;
            case "*":
                resultado = numero1 * numero2;
                System.out.println("Multiplicação = " + resultado);
                break;
            case "/":
                if (numero2 == 0)
                    System.out.println("Não existe divisão por zero.");
                else {
                    resultado = numero1 / numero2;
                    System.out.println("Divisão = " + resultado);
                }
                break;
            default:
                System.out.println("Operação inválida");
        }
    }
}
