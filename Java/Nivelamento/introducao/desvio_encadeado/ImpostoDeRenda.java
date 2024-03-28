package com.fiap.introducao.desvio_encadeado;

import java.util.Scanner;

/**
 * # Dado o salário do funcionário, calcular o Imposto de renda e o salário líquido de acordo com os seguintes critérios:
 * # Salário até 1900 - Isento         - 0%
 * # Salário entre 1900.01 até 2800    - 15%
 * # Salário acima 2800.01             - 27.5%
 * # Entrada1: Salário de 1500
 * # Saída1 : IR = 0 - Salário líquido: 1500
 * # Entrada2: Salário de 2300
 * # Saída2 : IR = 345 - Salário líquido: 1955
 * # Entrada3: Salário de 5000
 * # Saída3 : IR = 1375 - Salário líquido: 3625
 */
public class ImpostoDeRenda {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double salarioLiquido, impostoRenda, salario;

        System.out.println("Qual o valor do salário do funcionário? ");
        salario = scanner.nextDouble();

        if (salario <= 2500){
            impostoRenda = 0;
        } else if (salario <= 3200 ) {
            impostoRenda = salario * 7.5 / 100 - 187.50; // Ou salario * 0.075 - 187.50
        }else if (salario <= 4250){
            impostoRenda = salario * 15 / 100 - 562.50; // Ou salario * 0.15 - 562.50
        } else if (salario <= 5300) {
            impostoRenda = salario * 22.5 / 100 - 1012.50; // Ou salario * 0.225 - 1012.50
        }else {
            impostoRenda = salario * 27.5 / 100 - 1462.50; // Ou salario * 0.275 - 1462.50
        }

        salarioLiquido = salario - impostoRenda;
//        System.out.println("IR retido na fonte: R$" + impostoRenda + " - Salário líquido: R$" + salarioLiquido);
        System.out.printf("O imposto de renda a ser pago é de R$ %.2f%n", impostoRenda);
        System.out.printf("O salário líquido é de R$ %.2f%n", salarioLiquido);
    }
}
