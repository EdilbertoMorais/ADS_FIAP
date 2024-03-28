package com.fiap.introducao.vetores_matrizes;

import java.util.Scanner;

public class Matriz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matriz = new int[4][2];

        System.out.println("Preenchendo a Matriz [4][2]".toUpperCase());
        for (int linha = 0; linha < 4; linha++) {
            for (int coluna = 0; coluna < 2; coluna++) {
                System.out.print("Posição [" + linha + "][" + coluna + "] = ");
                matriz[linha][coluna] = scanner.nextInt();
            }
        }
        System.out.println("Exibindo a Matriz [4][2]".toUpperCase());
        for (int linha = 0; linha < 4; linha++) {
            for (int coluna = 0; coluna < 2; coluna++) {
                System.out.print(matriz[linha][coluna] + "\t");// "\t" significa tabulação, Isso é útil ao exibir matrizes ou tabelas, deixa a apresentação mais legível
            }
            System.out.println();
        }

        System.out.println("Exibindo a Matriz [4][2] com for-each".toUpperCase());
        for (int[] linha : matriz) {
            for (int elemento : linha) {
                System.out.print(elemento + "\t"); // "\t" significa tabulação, Isso é útil ao exibir matrizes ou tabelas, deixa a apresentação mais legível
            }
            System.out.println();
        }

        System.out.println("Somando os elementos da Matriz [4][2] com for-each".toUpperCase());
        //Neste caso não foi preciso o uso das {} para delimitar o bloco, pois, cada bloco tem apenas 1 instrução
        int soma = 0;
        for (int[] linha : matriz)
            for (int elemento : linha)
                soma += elemento;

        System.out.println("Soma = " + soma);

        System.out.println("Somando os elementos da Matriz [4][2] com for".toUpperCase());
        int soma2 = 0;
        for (int linha = 0; linha < matriz.length; linha++){
            for (int coluna = 0; coluna < matriz[linha].length; coluna++){
               soma2 += matriz[linha][coluna];
            }
        }
        System.out.println("Soma2 = " + soma2);
    }
}
