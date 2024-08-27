package fase5.OOP.PersonagemMagico;

import java.util.Scanner;

//Implementação do Professor
public class ItemView2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Item item = null;
        int op;

        do {
            System.out.println("""
                    Escolha uma opção:
                    1- Cadastrar item
                    2- Exibir item
                    0- Sair do Programa
                    """);

            op = sc.nextInt();

            switch (op) {
                case 1:
                    System.out.println("Informe o nome do item: ");
                    String nome = sc.next() + sc.nextLine();
                    System.out.println("Informe  a descrição do item: ");
                    String descricao = sc.next() + sc.nextLine();
                    System.out.println("Informe se o item é raro: (true para Sim ou false para não)");
                    boolean raro = sc.nextBoolean();
                    System.out.println("Informe o nivel de poder do item: ");
                    int nivelPoder = sc.nextInt();
                    item = new Item(nome, descricao, raro, nivelPoder);
                    break;
                case 2:
                    if (item != null) {
                        System.out.printf("""
                                Nome: %s
                                Descrição: %s
                                É raro?: %b
                                Poder: %d
                                %n""", item.nome, item.descricao, item.ehRaro, item.nivelPoder);
                    } else {
                        System.out.println("Nenhum item cadastrado.");
                    }
                    break;
                case 0:
                    System.out.println("Saindo do programa.");
                    break;
                default:
                    System.out.println("Opção Inválida.");
            }
        } while (op != 0);

        sc.close();
    }
}
