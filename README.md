🤖 Automação de Cadastro de Produtos

Este projeto consiste em uma automação desenvolvida em Python capaz de acessar um sistema web e realizar automaticamente o cadastro de produtos a partir de uma base de dados em formato CSV.

A aplicação utiliza automação de interface gráfica para preencher os campos do formulário de cadastro no site, eliminando a necessidade de inserção manual de dados e tornando o processo mais rápido e eficiente.

A automação lê cada linha da planilha de produtos e insere as informações correspondentes no sistema, simulando as ações de um usuário como cliques, digitação e navegação entre campos. 

main

⚙️ Tecnologias utilizadas:
-Python
-PyAutoGUI
-Pandas
-Automação de interface gráfica
-CSV como base de dados

▶️ Como o projeto funciona

O script abre automaticamente o navegador.
Acessa a página de login do sistema.
Realiza o login utilizando credenciais configuradas no código.
Lê os dados da planilha de produtos.
Para cada produto:
-preenche os campos do formulário
-envia o cadastro
-passa para o próximo item. 

🛠 Utilitário auxiliar

O arquivo auxiliar.py serve para identificar as coordenadas da tela necessárias para a automação.
Ele exibe a posição atual do mouse após alguns segundos, permitindo configurar corretamente os pontos de clique utilizados no script.

📊 Base de dados

O arquivo produtos.csv contém as informações utilizadas para preencher os cadastros, como:
-código do produto
-marca
-tipo
-categoria
-preço
-custo
-observações
