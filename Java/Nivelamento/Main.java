package com.fiap;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //ler n1
        System.out.println("Digite um número: ");
        int n1 = entrada.nextInt();
        //ler n2
        System.out.println("Digite outro número: ");
        int n2 = entrada.nextInt();
        //soma = n1 + n2
        int soma = n1 + n2;
        //Escreve soma
        System.out.println("A soma dos 2 números é: " + soma);

    }
}