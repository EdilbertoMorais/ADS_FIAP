package fase5.OOP.personagemMagico.view;

import fase5.OOP.personagemMagico.model.Item;

import java.util.Scanner;

public class ItemView {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Item itemMagico = new Item();

        int opcao;

        do {
            System.out.println("""
                    Escolha uma opção:
                    1- Cadastrar item
                    2- Exibir item
                    0- Sair do Programa
                    """);

            opcao = sc.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("Informe o nome do item: ");
                    String nome = sc.next() + sc.nextLine();
                    System.out.println("Informe  a descrição do item: ");
                    String descricao = sc.next() + sc.nextLine();
                    System.out.println("Informe se o item é raro: (1 para Sim ou 2 para não)");
                    int itemRaro = sc.nextInt();
                    System.out.println("Informe o nivel de poder do item: ");
                    int nivelPoder = sc.nextInt();

                    itemMagico.nome = nome;
                    itemMagico.descricao = descricao;
                    if (itemRaro == 1) {
                        itemMagico.ehRaro = true;
                    } else if (itemRaro == 2) {
                        itemMagico.ehRaro = false;
                    }
                    itemMagico.nivelPoder = nivelPoder;
                    break;
                case 2:
                    System.out.printf("""
                            Nome: %s
                            Descrição: %s
                            É raro?: %b
                            Poder: %d
                            %n""", itemMagico.nome, itemMagico.descricao, itemMagico.ehRaro, itemMagico.nivelPoder);
                    break;
                case 0:
                    System.out.println("Saindo do Programa");
                    break;
                default:
                    System.out.println("Opção Inválida.");
            }

        } while (opcao != 0);
        sc.close();
    }
}
