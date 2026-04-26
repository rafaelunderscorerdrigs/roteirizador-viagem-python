# 📖 Roteirizador Interativo de Viagens com Python & Folium

## 📝 Descrição
Este projeto nasceu da necessidade de organizar um roteiro de feriado em **Rio do Sul (SC)**. A aplicação automatiza a criação de um mapa interativo, calculando distâncias reais entre pontos turísticos, estadias (Airbnb) e locais de lazer, gerando um arquivo visual de fácil consulta.

---

## 🚀 Evolução e Desafios (Logs de Desenvolvimento)
Durante o desenvolvimento, enfrentamos e resolvemos desafios técnicos reais:

*   **Conflito de Interpretadores:** Resolvemos o erro `ModuleNotFoundError` garantindo que o `folium` fosse instalado no caminho absoluto do Python 3.14 usado pelo VS Code.
*   **Segurança de Navegador (CORS):** Contornamos o bloqueio de acesso (Erro 403r) ao carregar *tiles* de mapas localmente, alternando para o provedor `CartoDB positron`.
*   **Visualização de Dados:** Implementamos uma legenda dinâmica usando HTML injetado e cálculos geodésicos com a biblioteca `geopy`.

---

## 🛠️ Ferramentas Utilizadas
*   **Python 3.14** (Lógica principal)
*   **Folium** (Renderização do mapa interativo)
*   **Geopy** (Cálculo de distâncias entre coordenadas)
*   **VS Code** (Ambiente de desenvolvimento)

---

## 📍 Funcionalidades
*   **Marcadores Personalizados:** Ícones coloridos por categoria (Início, Airbnb, Lazer).
*   **Traçado de Rota:** Linha pontilhada conectando todos os destinos em sequência.
*   **Legenda Lateral Dinâmica:** Uma caixa flutuante (HUD) que mostra a distância exata em quilômetros de cada trecho do roteiro.

---

## 🔧 Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   ```bash
   pip install folium geopy

3. Execute o script:

Bash
python rio_sul.py
Abra o arquivo meu_roteiro_rio_do_sul.html gerado no seu navegador.

Projeto desenvolvido para fins de estudo e organização pessoal.


---

### Dicas de formatação que usei:
*   **H1 (`#`) e H2 (`##`):** Para criar a hierarquia visual.
*   **Horizontal Rules (`---`):** Para separar as seções e não ficar uma "parede de texto".
*   **Code Blocks (`` ` ``):** Para destacar nomes de erros, arquivos e comandos que devem ser digitados no terminal.
*   **Negrito (`**`):** Para destacar os pontos chave.

Agora seu GitHub vai parecer projeto de desenvolvedor Sênior! Só salvar e subir.