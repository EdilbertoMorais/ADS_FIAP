package fase5;

import fase5.OOP.PersonagemMagico.PersonagemMagico;

public class Main {
    public static void main(String[] args) {

        // Criando um objeto do tipo PersonagemMagico
        PersonagemMagico mago = new PersonagemMagico("Gandalf", 100, "Magia");

        // Atribuindo valores aos atributos do objeto
//        mago.nome = "Gandalf";
//        mago.nivelEnergia = 100;
//        mago.poderMagico = "Magia";

        System.out.printf("""
                Nome: %s
                Energia: %d
                Poder: %s
                %n""", mago.nome, mago.nivelEnergia, mago.poderMagico);


        // Criando outro objeto do tipo PersonagemMagico
        PersonagemMagico elfo = new PersonagemMagico("Legolas", 50, "Arqueira");

        // Atribuindo valores aos atributos do objeto
//        elfo.nome = "Legolas";
//        elfo.nivelEnergia = 50;
//        elfo.poderMagico = "Arqueira";

        // o %s indica que a variável é uma String / %d = int ou long / %f.2f = numero casas decimais
        System.out.printf("""
                Nome: %s
                Energia: %d
                Poder: %s
                %n""", mago.nome, mago.nivelEnergia, mago.poderMagico);
    }
}