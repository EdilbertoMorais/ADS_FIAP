package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

/**
 * Em uma eleição, há três candidatos: 1 - Huguinho; 2 - Zezinho e 3 - Luizinho. Fazer um algoritmo
 * que leia votos dados pelos usuários até que ele digite 0 (zero). Ao finalizar a votação,
 * informal quantos votos cada candidato teve.
 */
public class Eleicao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int huguinho = 0, zezinho = 0, luizinho = 0, total_votos = 0, voto;

        do {
            System.out.println("Insira seu voto: ");
            System.out.println("1-HUGUINHO");
            System.out.println("2-ZEZINHO");
            System.out.println("3-LUIZINHO");
            System.out.print("0 (ZERO) para SAIR: ");
            voto = scanner.nextInt();

            if (voto > 3) {
                System.out.println("Número inválido. Voto não computado");
            } else {
                switch (voto) {
                    case 1:
                        huguinho++;
                        break;
                    case 2:
                        zezinho++;
                        break;
                    case 3:
                        luizinho++;
                        break;
                }
                total_votos++;
            }
        } while (voto != 0);
        total_votos--;

        System.out.println("_____________________________________________");
        System.out.println("Total de votos válidos = " + total_votos);
        System.out.println("Huguinho= " + huguinho + " votos");
        System.out.println("Zezinho = " + zezinho + " votos");
        System.out.println("Luizinho = " + luizinho + " votos");

    }
}
