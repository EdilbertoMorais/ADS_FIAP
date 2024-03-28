package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

/**
 * # Solicitar ao usuário que digite S para sim e N para não.
 * # Entrada 1 = Digite [S]im ou [N]ão: S
 * # Saída 1: Você digitou S ou N
 * #
 * # Solicitar ao usuário que digite S para sim e N para não obrigatóriamente.
 * # Entrada 2 = Digite [S]im ou [N]ão: H
 * # Saída 2: Você digitou "H", digite S ou N.
 */
public class LacoRepeticaoWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite [S] para [S]im e [N] para [N]ão:");
        String opcao = scanner.next().toUpperCase();

        while (!opcao.equals("S") && !opcao.equals("N")){
            System.out.println("Você digitou, " + opcao);
            System.out.println("Digite [S] para [S]im e [N] para [N]ão:");
            opcao = scanner.next().toUpperCase();
        }
        System.out.println("Você digitou, " + opcao);
    }
}
