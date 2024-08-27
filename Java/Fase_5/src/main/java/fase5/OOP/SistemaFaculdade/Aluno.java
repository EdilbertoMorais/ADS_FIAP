package fase5.OOP.SistemaFaculdade;

public class Aluno {
    String nome;
    String matricula;
    Endereco endereco;

    // Construtor personalizado
    public Aluno(String nome, String matricula, Endereco endereco) {
        this.nome = nome;
        this.matricula = matricula;
        this.endereco = endereco;
    }
}
