package com.fiap.introducao.vetores_matrizes;

import java.util.Scanner;

/**
 * Em uma matriz de inteiros com 3 linhas e 4 colunas, fazer as seguintes rotinas:
 * - Preencher a matriz
 * - Exibir o conteúdo da matriz
 * - Somar os elementos da matriz
 * - Buscar um elemento dentro da matriz
 */
public class MatrizExercicio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] matriz = new int[3][4];

        System.out.println("Preenchendo a Matriz [3][4]".toUpperCase());
        for (int linha = 0; linha < matriz.length; linha++) {
            for (int coluna = 0; coluna < matriz[linha].length; coluna++) {
                System.out.print("Posição [" + linha + "][" + coluna + "] = ");
                matriz[linha][coluna] = scanner.nextInt();
            }
            System.out.println();
        }

        System.out.println("Exibindo a Matriz [3][4] usando for-each".toUpperCase());
        for (int[] linha : matriz) {
            for (int elemento : linha)
                System.out.print(elemento + "\t");
            System.out.println();
        }

        System.out.println("Somando os elementos da Matriz [3][4] usando for-each".toUpperCase());
        int soma = 0;
        for (int[] linha : matriz) {
            for (int elemento : linha)
                soma += elemento;
        }
        System.out.println("Soma= " + soma);

        System.out.println("Buscando um elementos dentro Matriz [3][4]".toUpperCase());
        boolean elementoEncontrado = false;

        System.out.println("Digite o elemento: ");
        int elemento = scanner.nextInt();

        for (int linha = 0; linha < matriz.length; linha++) {
            for (int coluna = 0; coluna < matriz[linha].length; coluna++) {
                if (matriz[linha][coluna] == elemento) {
                    elementoEncontrado = true;
                    break;
                }
            }
        }
        if (elementoEncontrado)
            System.out.println("Elemento " + elemento + " encontrado na matriz");
        else
            System.out.println("Elemento " + elemento + " NÃO encontrado na matriz");
    }
}
