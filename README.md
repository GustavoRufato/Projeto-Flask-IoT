# Sistema Inteligente de Gerenciamento de Lixo

Este projeto simula uma lixeira inteligente conectada à Internet das Coisas (IoT). Ele foi desenvolvido para monitorar e gerenciar o estado da lixeira em tempo real, utilizando tecnologias como Flask, sensores ultrassônicos, LEDs e integração com a plataforma ThingSpeak.

---

##  Funcionalidades


1. **Raspberry Pi como núcleo do sistema**:
  - Responsável por integrar todos os componentes do projeto, incluindo sensores, LEDs e comunicação com a web.
  - Processa as leituras do sensor HC-SR04.
  - Gerencia a comunicação com o servidor Flask e envia dados para o ThingSpeak.
  - Controla os sinais GPIO para os LEDs, garantindo o feedback visual.

2. **Servidor Web com Flask**
   - Interface para:
     - Monitorar o estado atual da lixeira (aberta, fechada, disponível, cheia), exibindo o percentual de ocupação.
     - Controlar manualmente a abertura da tampa.
     - Visualizar gráficos dos dados enviados ao ThingSpeak diretamente na interface.

3. **Sensor de Distância HC-SR04**
   - Utilizado para monitorar o nível de ocupação da lixeira em tempo real.

4. **Controle de LEDs**
   - **LED verde**:
     - Pisca 3 vezes quando a lixeira está disponível para uso e a tampa é aberta.
     - Fica aceso enquanto a lixeira estiver disponível.
   - **LED vermelho**:
     - Pisca 3 vezes quando a lixeira está cheia e a tampa é aberta.
     - Fica aceso enquanto a lixeira estiver cheia.

5. **Comunicação com ThingSpeak**
   - Registra o número de vezes que a lixeira foi aberta.
   - Envia um alerta à plataforma ThingSpeak quando a lixeira atinge sua capacidade máxima (baseado no sensor de distância).

---

##  Tecnologias Utilizadas

- **Flask** para desenvolvimento do servidor web.
- **Sensor HC-SR04** para medição da distância e ocupação da lixeira.
- **LEDs** para feedback visual sobre o estado da lixeira.
- **ThingSpeak** para registro de dados e alertas em tempo real.
- **HTML/CSS** para criação da interface web.

## Explicação da Página Web

A página web do *Sistema Inteligente de Gerenciamento de Lixo* foi desenvolvida para monitorar e gerenciar lixeiras de forma interativa. Ela é composta por diferentes seções, cada uma com uma funcionalidade específica:

- **Monitoramento**: Exibe o status atual das lixeiras, incluindo o nível de ocupação e a data da última atualização.
  
- **Controle de Ocupação**: Utiliza o elemento input type="range" para simular a variação no nível de lixo das lixeiras, permitindo ajustes visuais no preenchimento.

- **Histórico: Uma ****tabela** mostra o histórico de monitoramento, incluindo dados sobre a ocupação das lixeiras e ações realizadas, como esvaziamento.

A navegação é simples e intuitiva, e a interface é responsiva, garantindo boa usabilidade em diferentes dispositivos.