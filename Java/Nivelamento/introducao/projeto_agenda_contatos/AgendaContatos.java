package com.fiap.introducao.projeto_agenda_contatos;

import java.util.Objects;
import java.util.Scanner;

public class AgendaContatos {
    public static void main(String[] args) {
        int opcao, linha;
        String nome;

        // ao iniciar a aplicação, sempre é bom limparmos a matriz para que a "sujeira"
        // do Buffer não influencie nos resultados
        limparMatriz(agenda);

        do {
            // Exibição do menu
            exibeMenu();

            // Colhe a opção escolhida pelo usuário
            System.out.print("Escolha uma opção:");
            opcao = entrada.nextInt();
            System.out.println();

            // Seleciona a opção escolhida
            switch (opcao) {
                // Caso a escolha seja "adicionar novo contato"
                case 1:
                    novo(agenda, linhaProximoContato(agenda));
                    break;

                // Caso a escolha seja "Editar contato"
                case 2:
                    System.out.println("********* EDITANDO (PESQUISE O CONTATO) *********");
                    System.out.print("Digite o nome.........:");
                    nome = entrada.next();
                    linha = pesquisarContato(agenda, nome);
                    if (linha == -1) {
                        // informa se não encontrou o contato
                        System.out.print("Contato não Cadastrado!");
                    } else {
                        // se encontrou, exibe o contato e o edite
                        exibirContato(agenda, linha);
                        editarContato(agenda, linha);
                    }
                    break;

                // Efetua a pesquisa do contato
                case 3:
                    // pede o nome
                    System.out.println("********* PESQUISE O CONTATO *********");
                    System.out.print("Digite o nome.........:");
                    nome = entrada.next();
                    // Retorna a linha da pesquisa
                    linha = pesquisarContato(agenda, nome);
                    if (linha == -1) {
                        // Se o contato não existe
                        System.out.print("Contato não Cadastrado!");
                    } else {
                        // Se o contato existe, exibí-lo
                        exibirContato(agenda, linha);
                    }
                    break;

                // Lista todos os Contatos da agenda
                case 4:
                    listarAgenda(agenda);
                    break;

                // Exclui um registro digitado pelo usuário
                case 5:

                    System.out.println("********* EXCLUINDO (PESQUISE O CONTATO) *********");
                    System.out.print("Digite o nome.........:");
                    nome = entrada.next();
                    apagarContato(agenda, nome);
                    break;

                case 6:
                    System.out.print("OBRIGADO POR UTILIZAR A NOSSA AGENDA :)");

            }
            System.out.println();
        } while (opcao != 6);
    }

// ####### S U B A L G O R I T M O S #####################
    // variáveis e objetos públicos
    public static Scanner entrada = new Scanner(System.in);
    public static String[][] agenda = new String[10][3];

    /*
     * Descrição....: Este procedimento limpa a matriz
     * Nome.........: limpar_matriz(String matriz)
     * Tipo.........: void (procedimento)
     */
    public static void limparMatriz(String[][] matriz) {
        // Insere vazio em todas as células da matriz
        for (int linha = 0; linha < 10; linha++) {
            for (int coluna = 0; coluna < 3; coluna++) {
                matriz[linha][coluna] = "";
            }
        }
    }

    /*
     * Descrição....: Este procedimento cadastra um novo contato
     * Nome.........: novo(String matriz, int linha)
     * Tipo.........: void (procedimento)
     */
    public static void novo(String[][] matriz, int linha) {
        // Pede ao usuário a edição dos campos da linha passada por parâmetro
        System.out.println("********* PREENCHA O NOVO CONTATO *********");
        System.out.print("Nome.........: ");
        matriz[linha][0] = entrada.next();
        System.out.print("Celular......: ");
        matriz[linha][1] = entrada.next();
        System.out.print("E-mail.......: ");
        matriz[linha][2] = entrada.next();
    }

    /*
     * Descrição....: Este procedimento edita um contato
     * Nome.........: editarContato(String matriz, int linha)
     * Tipo.........: void (procedimento)
     */
    public static void editarContato(String[][] matriz, int linha) {
        // Permite ao usuário editar o contato encontrado
        // Não permite que o nome seja editado por ser a chave de pesquisa
        System.out.println("********* EDITE O CONTATO *********");
//        System.out.print("Nome.........: " + matriz[linha][0] + " ");
        System.out.print(STR."Nome.........: \{matriz[linha][0]} ");
        System.out.print("Celular......: ");
        matriz[linha][1] = entrada.next();
        System.out.print("E-mail.......: ");
        matriz[linha][2] = entrada.next();
    }

    /*
     * Descrição....: Esta função retorna a próxima linha em branco da matriz
     * Nome.........: linhaProximoContato(String matriz, int linha)
     * Tipo.........: void (procedimento)
     */
    public static int linhaProximoContato(String[][] matriz) {
        for (int linha = 0; linha < 10; linha++)
            if (matriz[linha][0].isEmpty()) {
                // caso tenha encontrado, retorne o número da linha
                // próxima linha vazia
                return linha;
            }
        // -1 representa a matriz estar cheia
        return -1;
    }

    /*
     * Descrição....: Este procedimento exibe um contato
     * Nome.........: exibirContato(String matriz, int linha)
     * Tipo.........: void (procedimento)
     */
    public static void exibirContato(String[][] matriz, int linha) {
        // Exibe o registro da linha passada por parâmetro
        System.out.println("Nome........: " + matriz[linha][0]);
        System.out.println("Celular.....: " + matriz[linha][1]);
        System.out.println("E-mail......: " + matriz[linha][2]);
    }

    /*
     * Descrição....: Este procedimento lista todos os contatos cadastrados
     * Nome.........: listarAgenda(String matriz)
     * Tipo.........: void (procedimento)
     */
    public static void listarAgenda(String[][] matriz) {
        System.out.println("**************** CONTATOS DA AGENDA ****************");
        for (int linha = 0; linha < 10; linha++) {
            // Enquanto tiver registro, exibe-o
            if (!Objects.equals(matriz[linha][0], "")) {
                // a linha acima é o mesmo que: if (matriz[linha][0] != "") {
                exibirContato(matriz, linha);
                System.out.println("------------------------------------------");
            }
        }
        System.out.println("**************** FIM DA AGENDA ****************");
    }

    /*
     * Descrição....: Esta função pesquisa o contato pelo nome e retorna a linha
     * Nome.........: pesquisarContato(String matriz, string nome)
     * Tipo.........: int (retorna -1 se não encontrou) (função)
     */
    public static int pesquisarContato(String[][] matriz, String nome) {
        // caso encontre o contato, retorna a linha onde ele está
        for (int linha = 0; linha < 10; linha++)
            if (matriz[linha][0].equals(nome)) {
                return linha;
            }
        // Se não encontrou o contato retorna -1
        return -1;
    }

    /*
     * Descrição....: Este procedimento exclui a linha passada por parâmetro
     * Nome.........: ExcluiLinha(String matriz, int linha)
     * Tipo.........: void (procedimento)
     */
    public static void excluiLinha(String[][] matriz, int linha) {
        // exclui o contato a partir da linha passada por parâmetro
        matriz[linha][0] = "";
        matriz[linha][1] = "";
        matriz[linha][2] = "";
        System.out.println("Contato Excluído");
    }

    /*
     * Descrição....: Este procedimento pesquisa e exclui um contato
     * Nome.........: apagarContato(String matriz, String nome)
     * Tipo.........: void (procedimento)
     */
    public static void apagarContato(String[][] matriz, String nome) {
        // inicia a variável que achou como false
        boolean achou = false;
        // alimenta a linha com o valor da pesquisa (-1 não encontrou)
        int linha = pesquisarContato(matriz, nome);
        String opcao;
        if (linha != -1) {
            // Exibe o contato a partir da linha
            exibirContato(matriz, linha);
            // Confirma com o usuário se ele quer excluir ou nao o contato
            System.out.println("Confirma a exclusão do contato? [S]im ou [N]ão?");
            opcao = entrada.next();
            if (opcao.equals("s") || opcao.equals("S")) {
                // se a escolha for Sim, exclui o contato
                excluiLinha(matriz, linha);
            } else {
                // Cancela a exclusão
                System.out.println("Exclusão cancelada!");
            }
        } else {
            // Contato não encontrado
            System.out.println("Contato não encontrado!");
        }
    }

    /*
     * Descrição....: Este procedimento exibe o menu de opções
     * Nome.........: exibeMenu()
     * Tipo.........: void (procedimento)
     */
    public static void exibeMenu() {
        System.out.println("****************** M E N U *****************");
        System.out.println("1 - Adicionar novo contato");
        System.out.println("2 - Editar contato");
        System.out.println("3 - Pesquisar contato");
        System.out.println("4 - Lista de contatos");
        System.out.println("5 - Apagar um contato");
        System.out.println("6 - Sair");
    }
}
