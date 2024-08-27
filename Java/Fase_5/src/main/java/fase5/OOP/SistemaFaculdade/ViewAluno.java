package fase5.OOP.SistemaFaculdade;

import java.util.Scanner;

public class ViewAluno {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Aluno aluno = null;

        int opcao;

        do {
            System.out.println("""
                    Escolha uma Opção:
                    1- Cadastrar aluno;
                    2- Exibir aluno cadastrado;
                    0- Sair do Programa;
                    """);

            System.out.print("Digite sua opção: ");
            opcao = entrada.nextInt();
            entrada.nextLine();

            switch (opcao) {
                case 1:
                    System.out.println("Informe o nome do aluno: ");
                    String nome = entrada.nextLine();

                    System.out.println("Informe o numero de matricula do aluno: ");
                    String matricula = entrada.nextLine();

                    System.out.println("Informe o logradouro do aluno: ");
                    String logradouro = entrada.nextLine();

                    System.out.println("Informe o número do endereço: ");
                    String numero = entrada.nextLine();

                    System.out.println("Informe o CEP: ");
                    String cep = entrada.nextLine();

                    System.out.println("Informe a cidade do aluno: ");
                    String cidadeNome = entrada.nextLine();

                    System.out.println("Informe o estado do aluno: ");
                    String estado = entrada.nextLine();

                    //Instancia dos objetos Endereço e Cidade
                    Cidade cidade = new Cidade(cidadeNome, estado);
                    Endereco endereco = new Endereco(logradouro, numero, cidade, cep);
                    aluno = new Aluno(nome, matricula, endereco);
                    break;

                case 2:
                    if (aluno != null) {
                        System.out.printf("""
                                    Nome aluno: %s
                                    Matricula: %s
                                    Logradouro: %s
                                    Numero: %s
                                    Cep: %s
                                    Cidade: %s
                                    Estado: %s
                                    %n""", aluno.nome,
                                aluno.matricula,
                                aluno.endereco.logradouro,
                                aluno.endereco.numero,
                                aluno.endereco.cep,
                                aluno.endereco.cidade.nome,
                                aluno.endereco.cidade.estado);
                    }else {
                        System.out.println("Nenhum aluno cadastrado.");
                    }

                    break;
                case 0:
                    System.out.println("Saindo do Programa");
                    break;
                default:
                    System.out.println("Opcao invalida");
            }
        } while (opcao != 0);
        entrada.close();
    }
}
