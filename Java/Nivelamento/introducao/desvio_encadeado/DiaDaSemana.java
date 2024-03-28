package com.fiap.introducao.desvio_encadeado;

import java.util.Scanner;

/**
 * # Solicitar um número ao usuário. A partir do número, exibir o dia da semana correspondente
 */
public class DiaDaSemana {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int diaDaSemana;
        do {
            System.out.println("Digite um número entre 1 e 7: ");
            diaDaSemana = scanner.nextInt();

            switch (diaDaSemana){
                case 1:
                    System.out.println("Domingo");
                    break;
                case 2:
                    System.out.println("Segunda-Feira");
                    break;
                case 3:
                    System.out.println("Terça-Feira");
                    break;
                case 4:
                    System.out.println("Quarta-Feira");
                    break;
                case 5:
                    System.out.println("Quinta-Feira");
                    break;
                case 6:
                    System.out.println("Sexta-Feira");
                    break;
                case 7:
                    System.out.println("Sábado");
                    break;
                default:
                    System.out.println("Número inválido.");
            }
        } while (diaDaSemana < 1 || diaDaSemana > 7);
    }
}

