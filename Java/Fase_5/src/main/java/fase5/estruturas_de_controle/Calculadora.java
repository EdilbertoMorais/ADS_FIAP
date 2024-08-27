package fase5.estruturas_de_controle;

import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        int opcao;
        double num1, num2, resultado;

        System.out.println("Bem-vindo à calculadora!");
        System.out.println("""
                Escolha a operação desejada:
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
                """);

        System.out.println("Informe a opção desejada:");
        opcao = teclado.nextInt();

        while (opcao < 1 || opcao > 4) {
            System.out.println("Opção inválida. Informe uma opção válida:");
            System.out.println("""
                    Escolha a operação desejada:
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão
                    """);
            opcao = teclado.nextInt();
        }


        System.out.println("Informe dois numeros:");
        System.out.println("Número 1:");
        num1 = teclado.nextDouble();
        System.out.println("Número 2:");
        num2 = teclado.nextDouble();

        teclado.close();

        switch (opcao) {
            case 1:
                resultado = num1 + num2;
                System.out.println("O resultado da soma é: " + resultado);
                break;
            case 2:
                resultado = num1 - num2;
                System.out.println("O resultado da subtração é: " + resultado);
                break;
            case 3:
                resultado = num1 * num2;
                System.out.println("O resultado da multiplicação é: " + resultado);
                break;
            case 4:
                if (num2 == 0) {
                    System.out.println("Não é possível dividir por zero.");
                } else {
                    resultado = num1 / num2;
                    System.out.println("O resultado da divisão é: " + resultado);
                }
        }
    }
}
