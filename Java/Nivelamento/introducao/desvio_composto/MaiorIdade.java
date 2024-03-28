package com.fiap.introducao.desvio_composto;

import java.util.Scanner;

public class MaiorIdade {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int idade;
        System.out.println("Digite sua idade:");
        idade = entrada.nextInt();
        // Desvio composto exibe mensagem “Maior de idade” quando a idade for maior ou igual a 18 anos e “Menor de idade” caso contrário
        if (idade >= 18) {
            System.out.println("Maior de idade");
        } else {
            System.out.println("Menor de idade");
        }
    }
}
