package com.fiap.introducao.funcoes_procedimentos;

import java.util.Scanner;

/**
 * Criar uma função que retorne o maior número passado por parâmetro.
 */
public class FuncaoMaiorNumero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe 2 números: ");
        int numero1 = scanner.nextInt();
        int numero2 = scanner.nextInt();

        System.out.println(STR."O número maio é: \{maiorNumero(numero1, numero2)}");
    }
    public static int maiorNumero(int numero1, int numero2){
        return Math.max(numero1, numero2);
    }
}
