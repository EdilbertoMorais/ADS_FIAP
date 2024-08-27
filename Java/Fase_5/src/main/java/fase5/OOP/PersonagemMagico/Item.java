package fase5.OOP.PersonagemMagico;

public class Item {

    String nome;
    String descricao;
    Boolean ehRaro;
    int nivelPoder;

    public Item(){}

    public Item(String nome, String descricao, Boolean ehRaro, int nivelPoder) {
        this.nome = nome;
        this.descricao = descricao;
        this.ehRaro = ehRaro;
        this.nivelPoder = nivelPoder;
    }

}
