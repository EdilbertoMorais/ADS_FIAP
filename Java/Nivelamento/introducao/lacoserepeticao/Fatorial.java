package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

public class Fatorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int fat = 1;
        System.out.println("Digite um número: ");
        int numero = scanner.nextInt();

        while (numero > 1){
            fat = fat * numero;
            numero = numero - 1;
        }
        System.out.println("O Fatorial é: " + fat);
    }
}
