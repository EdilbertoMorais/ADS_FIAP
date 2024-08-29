package fase5.OOP.personagemMagico.model;

public class Item {

    public String nome;
    public String descricao;
    public Boolean ehRaro;
    public int nivelPoder;

    public Item(){}

    public Item(String nome, String descricao, Boolean ehRaro, int nivelPoder) {
        this.nome = nome;
        this.descricao = descricao;
        this.ehRaro = ehRaro;
        this.nivelPoder = nivelPoder;
    }

}
