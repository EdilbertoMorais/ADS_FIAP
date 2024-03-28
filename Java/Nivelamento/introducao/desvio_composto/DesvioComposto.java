package com.fiap.introducao.desvio_composto;

import java.util.Scanner;

/**
 * # Uma empresa dará aumento para os seus funcionários.
 * # Caso ele trabalhe menos de três anos na empresa,
 * # ganhará 5% de aumento, caso contrário 10%
 * # Entrada1:
 * # Tempo de casa: 2
 * # Salario: 5000
 * # Saida1:
 * # O seu salário foi de 5000 para 5250
 * # Entrada2:
 * # Tempo de casa: 5
 * # Salário: 2000
 * # Saida2:
 * # O seu salário foi de 2000 para 2200
 */
public class DesvioComposto {
    public static void main(String[] args) {
        int tempoDeCasa;
        double salario;
        double novoSalario;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Quanto tempo de casa o funcionário tem? ");
        tempoDeCasa = scanner.nextInt();
        System.out.println("Qual o valor do salário do funcionário? ");
        salario = scanner.nextDouble();

        if (tempoDeCasa >= 3) {
            novoSalario = salario + (salario * 10 / 100);
        } else {
            novoSalario = salario + (salario * 5 / 100);
        }
        System.out.println("O seu salario foi de R$ " + salario + " Para R$ " + novoSalario);
    }
}
