package fase5.estruturas_de_controle;

import java.util.Scanner;

public class SistemaPedidoCafe {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem-vindo ao sistema de pedidos de café!");
        System.out.println("Escolha o tamanho do café: P - Pequeno (R$2,50), M - Médio (R$3,00), G - Grande (R$3,50)");
        System.out.println("Informe a opção desejada: ");
        char tamanhoCafe = scanner.next().charAt(0);
        tamanhoCafe = Character.toUpperCase(tamanhoCafe);

        System.out.println("Escolha o tipo do café: E - Expresso (R$1,50), C - Cappuccino (R$2,00), L - Latte (R$2,50)");
        System.out.println("Informe a opção desejada: ");
        char tipoCafe = scanner.next().charAt(0);
        tipoCafe = Character.toUpperCase(tipoCafe);

        double precoCafeTamanho = 0;
        double precoCafeTipo = 0;

        System.out.println("Resumo do pedido:");
        switch (tamanhoCafe) {
            case 'P':
                precoCafeTamanho = 2.50;
                System.out.println("Café pequeno selecionado.");
                break;
            case 'M':
                precoCafeTamanho = 3.00;
                System.out.println("Café médio selecionado.");
                break;
            case 'G':
                precoCafeTamanho = 3.50;
                System.out.println("Café grande selecionado.");
                break;
            default:
                System.out.println("Tamanho de café inválido!");
                break;
        }

        switch (tipoCafe) {
            case 'E':
                precoCafeTipo = 1.50;
                System.out.println("Café expresso selecionado.");
                break;
            case 'C':
                precoCafeTipo = 2.00;
                System.out.println("Cappuccino selecionado.");
                break;
            case 'L':
                precoCafeTipo = 2.50;
                System.out.println("Latte selecionado.");
                break;
            default:
                System.out.println("Tipo de café inválido!");
                break;
        }

        System.out.println("Total a pagar: R$" + (precoCafeTamanho + precoCafeTipo));

        scanner.close();
    }
}