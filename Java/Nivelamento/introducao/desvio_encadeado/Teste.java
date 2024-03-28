package com.fiap.introducao.desvio_encadeado;

public class Teste {
    public static void main(String[] args) {
        int id = 2, valor = 4;
        valor = valor + 2;

        switch (id) {
            case 1:
                valor = valor + 2;
                break;
            case 2:
                valor++;
                break;
            case 3:
                break;
            case 4:
                valor = valor + id;
                break;
            default:
                valor = 0;
        }
        valor++;
        System.out.print("Valor = " + valor);
    }
}
