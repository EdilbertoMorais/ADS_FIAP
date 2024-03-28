package com.fiap.introducao.projeto_agenda_contatos;

public class teste {
    public static void main(String[] args) {
        System.out.println(mm(20));

    }

    public static String mm(int nn){
        if (nn > 5){
            if (nn <10){
                return ("Abc");
            }else {
                return ("DEF");
            }
        }else {
            if (nn < 0){
                return ("GHI");
            }else {
                return ("JKL");
            }
        }
    }
}
