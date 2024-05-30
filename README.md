# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python. Ele permite realizar operações básicas como depósito, saque, exibição de extrato, cadastro de novas contas, listagem de contas e cadastro de novos clientes.

## Funcionalidades

- **Depositar:** Permite realizar depósitos na conta.
- **Sacar:** Permite realizar saques da conta, com verificação de saldo, limite de saque e quantidade de saques diários.
- **Exibir Extrato:** Exibe o extrato da conta com todas as movimentações realizadas.
- **Cadastrar Nova Conta:** Permite o cadastro de novas contas para clientes existentes.
- **Listar Contas:** Lista todas as contas cadastradas no sistema.
- **Novo Usuário:** Permite o cadastro de novos clientes no sistema.

## Como usar

### Pré-requisitos

- Python 3.x instalado no seu sistema.

### Execução

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/DIO_Sistema_Bancario_Otimizado.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd DIO_Sistema_Bancario_Otimizado
    ```

3. Execute o script principal:
    ```sh
    python sistema_bancario.py
    ```

### Exemplo de uso

Ao executar o script, o menu principal será exibido, permitindo escolher uma das opções disponíveis:

```
=========== MENU ============
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Cadastrar nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=>
```

Escolha a opção desejada digitando a letra correspondente e siga as instruções fornecidas.

## Estrutura do Código

- **menu:** Função que exibe o menu principal e captura a escolha do usuário.
- **depositar:** Função que realiza depósitos na conta.
- **sacar:** Função que realiza saques da conta com verificações de saldo, limite e quantidade de saques.
- **exibir_extrato:** Função que exibe o extrato da conta.
- **cadastrar_cliente:** Função que cadastra novos clientes no sistema.
- **cadastrar_conta:** Função que cadastra novas contas para clientes existentes.
- **listar_contas:** Função que lista todas as contas cadastradas.
- **filtrar_cliente:** Função que filtra e retorna clientes com base no CPF.
- **main:** Função principal que controla o fluxo do programa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

1. Faça um fork do projeto.
2. Crie uma nova branch com a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Minha nova feature'`.
4. Faça push para a branch: `git push origin minha-feature`.
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.



Isso deve cobrir as principais informações sobre o projeto e fornecer uma boa base para qualquer um que queira entender, usar ou contribuir para o sistema bancário em Python.
