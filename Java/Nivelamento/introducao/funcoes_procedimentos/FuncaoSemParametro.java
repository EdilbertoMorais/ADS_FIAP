package com.fiap.introducao.funcoes_procedimentos;

/**
 * Criar uma função do tipo real que retorne o valor de pi (3.1415) para calcular
 * a área de um círculo com raio 5 (a = pi . r2).
 */
public class FuncaoSemParametro {
    public static void main(String[] args) {

        double r = 5;
        double a = pi() * (r * r);
//        System.out.println(STR."A área do círculo com raio \{r} é \{a}");
        System.out.printf("A área do círculo com raio %.2f é %.2f%n", r, a);
    }

    public static double pi(){
        return 3.14159;
    }
}
