package com.fiap.introducao.funcoes_procedimentos;

import java.util.Scanner;

/**
 * Em uma instituição de ensino, um aluno é submetido a 3 avaliações semestrais. A média semestral é calculada por meio de uma média simples das duas
 * maiores notas obtidas entre 3 avaliações.
 * Caso a média semestral sejá inferior a 4, o aluno foi reprovado.
 * Caso a média semestral seja maior ou igual a 7, o aluno foi aprovado direto.
 * Caso a média semestral esteja entre 4 e 6,9 o aluno tem a oportunidade de fazer o exame por meio de uma nova avaliação.
 * Considerando que o aluno esta em exame, a média final é uma média simples da média semestral com a nota da avaliação obtida no exame. Caso a média seja inferior a 5,
 * o aluno foi Reprovado em exame, senão ele foi aprovado,
 * Requisitos:
 * - O algoritmo efetua o cálculo com apenas um aluno.
 * - Consistir as notas para estarem entre 0 e 10.
 * - As mensagens informativas devem ser claras em relação à situação do aluno.
 * - Quando necessário, exibir as médias calculadas para simples conferência.
 */
public class MediaSemestral {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe as notas do aluno: ");
        System.out.println("Informe a primeira nota: ");
        double nota1 =  validaNota(scanner.nextInt());
        System.out.println("Informe a segunda nota: ");
        double nota2 =  validaNota(scanner.nextInt());
        System.out.println("Informe a terceira nota: ");
        double nota3 =  validaNota(scanner.nextInt());

        mostrarNotas(nota1, nota2, nota3);

        double[] mairesNotas = pegaDuasMaioresNotas(nota1, nota2, nota3);

        double media = calculaMedia(mairesNotas);

        situacaoAluno(media);

    }

    public static double[] pegaDuasMaioresNotas(double nota1, double nota2, double nota3) {
        double[] notas = {nota1, nota2, nota3};

        java.util.Arrays.sort(notas);
        double[] duasMaioresNotas = {notas[1], notas[2]};
        return duasMaioresNotas;
    }

    public static double calculaMedia(double[] notas) {
        double soma = 0;
        for (double nota : notas) {
            soma += nota;
        }
        return soma / notas.length; // ou posso colocar 2, já que sabemos que a média é a soma das 2 notas dividas pela quantidade de notas.
    }

    public static double validaNota(double nota) {
        Scanner scanner = new Scanner(System.in);

        while (nota < 0 || nota > 10) {
            System.out.println("Nota inválida. A nota não pode ser maior que 10 e menor do que 0.");
            nota = scanner.nextDouble();
        }
        return nota;
    }

    public static void situacaoAluno(double media){
        Scanner scanner = new Scanner(System.in);

        if (media < 4){
            System.out.println("Aluno reprovado.".toUpperCase());
            System.out.println("A média é: " + media);
        }else if (media > 7){
            System.out.println("Aluno aprovado.".toUpperCase());
            System.out.println("A média é: " + media);
        }else {
            System.out.println("Aluno em exame.".toUpperCase());
            System.out.println("Informar a nota da avaliação de EXAME");
            double notaExame = validaNota(scanner.nextDouble());
            if (notaExame < 5){
                System.out.println("Aluno reprovado em exame".toUpperCase());
            }else {
                System.out.println("Aluno Aprovado em exame".toUpperCase());
            }
            System.out.println("Nota Final: " + notaExame);
        }
    }

    public static void avaliacaoExame(double notaExame){
        if (notaExame < 5){
            System.out.println("Aluno reprovado em exame.".toUpperCase());
        }else {
            System.out.println("Aluno aprovado em exame.".toUpperCase());
        }
    }

    public static void mostrarNotas(double nota1, double nota2, double nota3){
                System.out.println("1ª nota = " + nota1);
                System.out.println("2ª nota = " + nota2);
                System.out.println("3ª nota = " + nota3);
    }
}

