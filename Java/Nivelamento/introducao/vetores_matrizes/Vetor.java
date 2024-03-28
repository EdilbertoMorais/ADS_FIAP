package com.fiap.introducao.vetores_matrizes;

import java.util.Scanner;

public class Vetor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] vetor = new int[5];

        //Preencher o vetor
        System.out.println("Preenchendo o vetor".toUpperCase());
        for (int i = 0; i < 5; i++){
            System.out.print("Posição [" + i + "] = ");
            vetor[i] = scanner.nextInt();
        }

        //Exibindo o vetor
        System.out.println("Exibindo o vetor".toUpperCase());
//        for (int i = 0; i < 5; i++){
//            System.out.println(vetor[i]);
//        }
        for (int elemento : vetor){
            System.out.println(elemento); // Ao usar o loop for-each deve se imprimir o elemento diretamente
        }

        //Somando os elementos do vetor
        System.out.println("Somando o vetor".toUpperCase());
        int soma = 0;
        for (int elemento : vetor){
            soma += elemento;
        }
        System.out.println("Soma= " + soma);
    }
}
