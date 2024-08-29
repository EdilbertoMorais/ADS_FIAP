package fase5.OOP.sistemaFaculdade.model;

public class Aluno {
    private String nome;
    private String matricula;
    private Endereco endereco;

    // Construtor personalizado
    public Aluno(String nome, String matricula, Endereco endereco) {
        this.nome = nome;
        this.matricula = matricula;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public Aluno setNome(String nome) {
        this.nome = nome;
        return this;
    }

    public String getMatricula() {
        return matricula;
    }

    public Aluno setMatricula(String matricula) {
        this.matricula = matricula;
        return this;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public Aluno setEndereco(Endereco endereco) {
        this.endereco = endereco;
        return this;
    }
}
