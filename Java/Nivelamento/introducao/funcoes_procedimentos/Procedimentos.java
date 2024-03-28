package com.fiap.introducao.funcoes_procedimentos;

// Programa principal
public class Procedimentos {
    public static void saudacao(int hora) {
        if (hora < 12 )
            System.out.println("Bom dia!");
        else if (hora < 18)
            System.out.println("Boa tarde!");
        else
            System.out.println("Boa noite!");

        System.out.println("Seja bem-vindo a FIAP!!!");
    }

    // Criação do procedimento
    public static void main(String[] args) {
        saudacao(13);

    }
}

