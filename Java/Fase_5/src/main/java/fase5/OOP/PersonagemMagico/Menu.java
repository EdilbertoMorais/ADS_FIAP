package fase5.OOP.PersonagemMagico;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PersonagemMagico personagem = new PersonagemMagico();

        int opcao;

        do {
            System.out.println("""
                    Escolha uma opção:
                    1- Cadastrar Personagem
                    2- Exibir Personagem
                    0- Sair do Programa
                    """);

            opcao = sc.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("Digite o nome do personagem: ");
                    String nome = sc.next() + sc.nextLine();
                    System.out.println("Digite o nivel de energia do personagem: ");
                    int nivelEnergia = sc.nextInt();
                    System.out.println("Digite o poder do personagem: ");
                    String poderMagico = sc.next() + sc.nextLine();
                    personagem.nome = nome;
                    personagem.nivelEnergia = nivelEnergia;
                    personagem.poderMagico = poderMagico;

                    System.out.println("Digite o nome da habilidade especial: ");
                    String nomeHabilidade = sc.next() + sc.nextLine();
                    System.out.println("digite o custo de energia para usar a habilidade: ");
                    int custoEnergia = sc.nextInt();
                    System.out.println("A habilidade esta ativa?: (true/false)");
                    boolean habilidadeAtiva = sc.nextBoolean();

                    personagem.habilidadeEspecial = new HabilidadeEspecial(nomeHabilidade, custoEnergia, habilidadeAtiva);
                    break;
                case 2:
                    System.out.printf("""
                            Nome: %s
                            Energia: %d
                            Poder: %s
                            Habilidade especial:
                            Nome da Habilidade: %s
                            Custo de energia: %d
                            Habilidade ativa?: %b
                            %n""", personagem.nome,
                            personagem.nivelEnergia,
                            personagem.poderMagico,
                            personagem.habilidadeEspecial.nome,
                            personagem.habilidadeEspecial.custoEnergia,
                            personagem.habilidadeEspecial.habilitada);
                    break;
                case 0:
                    System.out.println("Saindo do programa");
                    break;
                default:
                    System.out.println("Opção inválida");
            }
        } while (opcao != 0);
        sc.close();
    }
}
