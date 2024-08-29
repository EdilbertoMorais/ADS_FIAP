package fase5.OOP.personagemMagico.model;

public class Item {

    private String nome;
    private String descricao;
    private Boolean ehRaro;
    private int nivelPoder;

    public Item(){}

    public Item(String nome, String descricao, Boolean ehRaro, int nivelPoder) {
        this.nome = nome;
        this.descricao = descricao;
        this.ehRaro = ehRaro;
        this.nivelPoder = nivelPoder;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public Boolean getEhRaro() {
        return ehRaro;
    }

    public void setEhRaro(Boolean ehRaro) {
        this.ehRaro = ehRaro;
    }

    public int getNivelPoder() {
        return nivelPoder;
    }

    public void setNivelPoder(int nivelPoder) {
        this.nivelPoder = nivelPoder;
    }
}
