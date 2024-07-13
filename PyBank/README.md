<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> PyBank - Sistema Bancário em Python</span>
</h1>

Projeto realizado para o Bootcamp "Python AI Backend Developer"

## Descrição:
Criar um Sistema Bancário em Python

### Primeira parte:
Desenvolver um sistema bancário com funções de saque, depósito e extrato em Python.

#### Requisitos:
- Deve ser possível depositar valores inteiros e positivos para a conta bancária;
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;
- Apenas 1 usuário;
- Deve permitir 3 saques diários com limite máximo de R$ 500 por saque;
- Caso o usuário não tenha saldo em conta,exibir mensagem informando que não será possível sacar o dinheiro por falta de saldo;
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato;
- O extrato deve listar todos os depósitos e saques realizados na conta;
- Ao fim da listagem deve serexibido o saldo atual daconta;
- Os valores devem ser exibidos utilizando o formato R$ XXX.XX;

### Segunda parte:
- Separar as funções existentes de saque, depósito e extrato em funções;
- Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária, vinculando ao usuário;
- Deve-se criar uma função para cada operação do sistema;
- Cada função deve ter uma regra na passagem de argumentos;
- A função saque deve receber os argumentos apenas por nome;
- A funçao depósito deve receber os argumenos apenas por posição;
- A função extrato deve receber os argumentos por posição e nome, o saldo deve receber argumentos posicionais, e o extrato, nomeados;
- O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço;
- O endereço é uma string com o formato: logradouro - Número - Bairro - Cidade/Sigla e Estado;
- Devem ser armazenado apenas os números do CPF;
- Não podemos cadastrar dois usuários no mesmo CPF;
- O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário;
- O Número da conta é sequencial, iniciando em 1;
- O número da agência é fixo: 0001;
- O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário;

### Terceira parte:
- Adicionar funcionalidades no sistema: Decorador de log, gerador de relatórios e iterador personalizado.

### Funcionalidades adicionais implementadas:
- Validação de telefone;