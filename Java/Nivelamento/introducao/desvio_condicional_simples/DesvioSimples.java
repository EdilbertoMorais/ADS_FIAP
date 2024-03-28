package com.fiap.introducao.desvio_condicional_simples;

import java.util.Scanner;

/**
 * # Dada uma venda, calcular e exibir o desconto de 10% para compras acima de 500 reais
 * # entrada1 : venda: 500
 * # saída1 : valor final: 450
 * # entrada2: venda: 200
 * # saida2: valor final: 200
 * #
 * # PseudoCodigo
 * # var
 * # venda, desconto: real
 * # Inicio
 * # Escreva "Digite o valor da venda: "
 * # Leia venda
 * # Se venda > 300 então
 * #   desconto = venda * 10/100
 * #   venda = venda - desconto
 * #   fim_se
 * # Escreva "Novo valor = ", venda
 * # Fim
 */
public class DesvioSimples {
    public static void main(String[] args) {
        double desconto = 0;
        int percentual = 0;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o valor da venda: ");
        double venda = scanner.nextDouble();

        if (venda > 300) {
            System.out.println("Digite o percentual de desconto: ");
            percentual = scanner.nextInt();
            desconto = venda * percentual / 100;
            venda = venda - desconto;
        }
        System.out.println("Novo valor: R$ " + venda);
    }
}
