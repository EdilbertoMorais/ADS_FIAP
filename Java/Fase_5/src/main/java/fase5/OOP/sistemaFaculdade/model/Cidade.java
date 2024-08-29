package fase5.OOP.sistemaFaculdade.model;

public class Cidade {
    private String nome;
    private String estado;

    // Construtor personalizado
    public Cidade(String nome, String estado) {
        this.nome = nome;
        this.estado = estado;
    }

    public String getNome() {
        return nome;
    }

    public Cidade setNome(String nome) {
        this.nome = nome;
        return this;
    }

    public String getEstado() {
        return estado;
    }

    public Cidade setEstado(String estado) {
        this.estado = estado;
        return this;
    }

}
