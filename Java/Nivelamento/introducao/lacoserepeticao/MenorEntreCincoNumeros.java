package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

public class MenorEntreCincoNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeroMenor = 0;

        System.out.println("Digite 5 números:");
        System.out.println("Digite o 1º número:");
        numeroMenor = scanner.nextInt();

        for (int i = 1; i <= 4; i++){
            System.out.println("Digite o " + (i+1) + "º número:");
            int numero = scanner.nextInt();
            if (numero < numeroMenor){
                numeroMenor = numero;
            }
        }
        System.out.println("Menor valor = " + numeroMenor);
    }
}
