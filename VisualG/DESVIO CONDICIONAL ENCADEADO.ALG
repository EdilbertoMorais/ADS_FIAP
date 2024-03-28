Algoritmo "Desvio Condicional Encadeado"
//
//
// Descrição   : Verifica se o aluno é maior ou menor de idade, e se esta
// autorizado pelo responsavel caso seja menor:
// Autor(a)    : Edilberto Morais
// Data atual  : 25-03-2024
Var
   // Secao de Declaracoes das variaveis
   idade: inteiro
   autorizado, rm: caractere


Inicio
   // Secao de Comandos, procedimento, funcoes, operadores, etc...
   escreval ("Por favor, digite seu RM")
   leia (rm)
   Escreval ("Por favor, digite sua idade")
   leia (idade)


   Se idade >= 18 entao
      escreval ("Sua participação foi autorizada, aluno de RM" , rm)
      escreval ("Mais instruções serão enviadas para seu e-mail.")
   Senao
      escreval ("Voce possui autorizacao dos responsaveis para participar? ")
      leia (autorizado)
      se autorizado = ("S") entao
         escreval ("Sua participação foi autorizada, aluno de RM" , rm)
         escreval ("Mais instruções serão enviadas para seu e-mail.")
      senao
         escreval ("Sua participação não foi autorizada por causa da sua idade")
      fimse
   fimse

Fimalgoritmo