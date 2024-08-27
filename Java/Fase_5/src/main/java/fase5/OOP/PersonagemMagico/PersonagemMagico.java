package fase5.OOP.PersonagemMagico;

public class PersonagemMagico {
    public String nome;
    public int nivelEnergia;
    public String poderMagico;
    HabilidadeEspecial habilidadeEspecial;

    public PersonagemMagico(String nome, int nivelEnergia, String poderMagico) {
        this.nome = nome;
        this.nivelEnergia = nivelEnergia;
        this.poderMagico = poderMagico;
    }

    public PersonagemMagico(String nome, int nivelEnergia) {
        this.nome = nome;
        this.nivelEnergia = nivelEnergia;
    }

    public PersonagemMagico() {}
}