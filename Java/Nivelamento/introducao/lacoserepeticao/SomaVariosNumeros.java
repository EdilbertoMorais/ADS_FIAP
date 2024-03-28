package com.fiap.introducao.lacoserepeticao;

/**
 * Fazer um algoritmo que leia e some diversos números dados pelo Usuário. Quando o usuário digitar 0 (zero),
 * finaliza o algoritmo. No final, exibira a soma resultante.
 */

import java.util.ArrayList;
import java.util.Scanner;

public class SomaVariosNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numeros = new ArrayList<>();
        int soma = 0;

        while (true){
            System.out.println("Digite um número para ser somado ou 0(zero) para mostrar a soma:");
            int numero = scanner.nextInt();

            if (numero == 0){
                break;
            }
            numeros.add(numero);
        }
        for (int num : numeros){
            soma += num;
        }
        System.out.println("A soma dos números é: " + soma);
        scanner.close();
    }
}
