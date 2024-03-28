package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

public class Tabuada {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int j;

        System.out.print("Digite um numero: ");
        int numero = scanner.nextInt();

        System.out.println("Os 10 primeiros múltiplos de " + numero + " são: ");

        for (int cont = 1; cont <= 10; cont++){
            int resultado = numero * cont;
            System.out.println(numero + " x " + cont + " = " + resultado);
        }

        for (int i=1; i <=2; i++){
            j = 0;
            do {
                j++;
            }while (j <= 2);
            System.out.println("X");
        }
    }
}
