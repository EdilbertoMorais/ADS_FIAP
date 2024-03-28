package com.fiap.introducao.entrada_dados;

public class Main {
    //Exemplos em Pseudo-Código:
    //Programa saida_de_dados
    //Início
    // exibe “Meu primeiro programa
    //Escreva “Meu primeiro programa”
    // exibe o número 12
    //Escreva 12
    //Fim

    public static void main(String[] args) {
        // Exibe "Meu primeiro programa"
        System.out.println("Meu primeiro programa");
        // Exibe o número 12
        System.out.println(12);

        System.out.println("_________________________________");
        //
        int i = 2;
        double r = Math.sqrt(i);
        System.out.print("A raiz de ");
        System.out.print(i);
        System.out.print(" é ");
        System.out.print(r);
        System.out.println(".");
        i = 5;
        r = Math.sqrt(i);
        System.out.println("A raiz de " + i + " é " + r + ".");

    }
}

