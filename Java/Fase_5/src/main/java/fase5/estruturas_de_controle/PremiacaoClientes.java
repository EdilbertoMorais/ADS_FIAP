package fase5.estruturas_de_controle;

import java.util.Scanner;

public class PremiacaoClientes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double valorCompras;
        int frequenciaCompras;

        System.out.println("Informe o valor total das compras: ");
        valorCompras = scanner.nextDouble();

        System.out.println("Informe a quantidade de compras: ");
        frequenciaCompras = scanner.nextInt();

        if (valorCompras >= 2000.0 && frequenciaCompras >= 10) {
            System.out.println("Parabéns! Você é VIP e ganhou 10% de desconto");
        } else if (valorCompras >= 1000.0) {
            System.out.println("Parabéns! Você cliente Ouro, e ganhou 5% de desconto");
        } else {
            System.out.println("Você é cliente Bronze, e ganhou 2% de desconto");
        }
        scanner.close();
    }
}