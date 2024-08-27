package fase5.estruturas_de_controle;

import java.util.Scanner;

public class DecisaoPasseio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Esta ensolarado? (s/n)");
        String op = scanner.nextLine().toUpperCase();

        boolean ensolarado;

        if (op.equals("S")) {
            ensolarado = true;
        } else {
            ensolarado = false;
        }

        System.out.println("É final de semana? (s/n)");
        String fds_op = scanner.nextLine().toUpperCase();

        scanner.close();

        boolean final_semana;

        if (fds_op.equals("S")) {
            final_semana = true;
        } else {
            final_semana = false;
        }

        if (ensolarado && final_semana) {
            System.out.println("Vamos à praia.");
        } else {
            System.out.println("Vamos ao cinema.");
        }

        scanner.close();
    }

}
