package fase5.OOP.SistemaFaculdade;

public class Endereco {
    String logradouro;
    String numero;
    Cidade cidade;
    String cep;

    // Construtor personalizado
    public Endereco(String logradouro, String numero, Cidade cidade, String cep) {
        this.logradouro = logradouro;
        this.numero = numero;
        this.cidade = cidade;
        this.cep = cep;
    }
}
