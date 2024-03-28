package com.fiap.introducao.desvio_encadeado;

import java.util.Scanner;

/**
 * Dada a parte numérica da placa de um automóvel, fazer um algoritmo que exiba o dia do rodízio.
 * Considere a regra de SP. Para veículos com final placa:
 * 1 e 2 = segunda-feira
 * 3 e 4 = terça-feira
 * 5 e 6 = quarta-feira
 * 7 e 8 = quinta-feira
 * 9 e 0 = sexta-feira
 */

public class Rodizio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe a placa do veiculo: ");
        String placa = scanner.next();

        String finalPlaca = String.valueOf(placa.charAt(placa.length() - 1));

        switch (finalPlaca) {
            case "1":
            case "2":
                System.out.println("Rodizio é segunda-feira");
                break;
            case "3":
            case "4":
                System.out.println("Rodizio é terça-feira");
                break;
            case "5":
            case "6":
                System.out.println("Rodizio é quarta-feira");
                break;
            case "7":
            case "8":
                System.out.println("Rodizio é quinta-feira");
                break;
            case "9":
            case "0":
                System.out.println("Rodizio é sexta-feira");
                break;
            default:
                System.out.println("Placa inválida.");
        }

    }
}
