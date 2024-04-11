//package com.fiap.introducao.funcoes_procedimentos;
//
//import java.util.Scanner;
//
///**
// * Criar uma função do tipo boolean que retorne True caso uma nota seja valída ou False se não for.
// * No programa principal aplicar a função calculando a média de duas notas.
// */
//public class FuncaoComParametro {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.println("Digite as notas do aluno:");
//
//        System.out.println("Digite a primeira nota: ");
//        double nota1 = scanner.nextDouble();
//        if (notaValida(nota1)){
//            System.out.println("Digite a segunda nota: ");
//            double nota2 = scanner.nextDouble();
//                if (notaValida(nota2)){
//                    System.out.println("Digite a terceira nota: ");
//                    double nota3 = scanner.nextDouble();
//                        if (notaValida(nota3)){
////                            double media = (nota1 + nota2 + nota3) / 3;
//                            double media = calcularMedia(nota1, nota2, nota3); // usando a função calcularMedia().
//                            System.out.println(STR."Nota 1 = \{nota1}, nota 2 = \{nota2}, nota 3 = \{nota3} - Média final= \{media}");
//                        }else {
//                            System.out.println("A nota 3 deve ser > 0 e < 10");
//                        }
//                }else {
//                    System.out.println("A nota 2 deve ser > 0 e < 10");
//                }
//        }else{
//            System.out.println("A nota 1 deve ser > 0 e < 10");
//        }
//
//    }
//
//    public static boolean notaValida(double nota){
//        if (nota >= 0 && nota <= 10)
//            return true;
//        else
//            return false;
//    }
//
//    public static double calcularMedia(double nota1, double nota2, double nota3){
//        return (nota1 + nota2 + nota3) / 3;
//    }
//}
