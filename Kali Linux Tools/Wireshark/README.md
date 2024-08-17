# Wireshark

Wireshark é uma rede “sniffer” – uma ferramenta que captura e analisa Pacotes fora do fio. Wireshark pode decodificar muitos protocolos para listar - Aqui. aqui.

Tamanho instalado: `10.21 MB`
Como instalar: sudo `apt install wireshark`

```bash
sudo apt remove wireshark 
```

## Configurar

```bash
$ whoami

$ sudo usermod -aG wireshark <user>

$ sudo chmod +x /usr/bin/dumpcap

$ sudo wireshark
```

**Wireshark** é uma ferramenta de análise de pacotes de rede muito poderosa e amplamente utilizada em segurança da informação e administração de redes. No Kali Linux, Wireshark é uma ferramenta essencial para capturar e inspecionar dados que trafegam em uma rede em tempo real.

### Funcionalidades do Wireshark

- **Captura de Pacotes**: Wireshark captura pacotes de dados que estão passando pela interface de rede do seu computador.
- **Análise de Pacotes**: Permite inspecionar cada pacote capturado em detalhes, incluindo cabeçalhos, payloads, protocolos e mais.
- **Filtragem**: Oferece uma linguagem de filtros para isolar pacotes específicos ou tipos de tráfego de interesse.
- **Decodificação de Protocolos**: Suporta a decodificação de centenas de protocolos de rede, ajudando a entender como os dados são estruturados.
- **Análise em Tempo Real e Pós-Captura**: Você pode analisar os pacotes em tempo real enquanto são capturados ou carregar arquivos de captura (PCAP) para análise posterior.
- **Detecção de Anomalias**: Pode ser usado para identificar problemas de rede, tentativas de intrusão, e atividades suspeitas.

### Como Usar Wireshark no Kali Linux

#### Iniciando o Wireshark

Para abrir o Wireshark no Kali Linux, você pode usar o terminal ou o menu de aplicativos.

- **Via terminal**:

  ```bash
  sudo wireshark
  ```

  Isso abrirá o Wireshark com privilégios de root, que são necessários para capturar pacotes.

#### Captura de Pacotes

1. **Selecionar a Interface de Rede**:
   - Ao abrir o Wireshark, você verá uma lista de interfaces de rede disponíveis. Selecione a interface pela qual deseja capturar pacotes (por exemplo, `eth0`, `wlan0`).
   
2. **Iniciar a Captura**:
   - Clique no botão de captura (ícone de "tubarão azul") ou pressione `Ctrl+E` para iniciar a captura de pacotes.

3. **Parar a Captura**:
   - Para parar a captura, clique no botão de parada (ícone de "quadrado vermelho") ou pressione `Ctrl+E` novamente.

#### Analisando Pacotes

1. **Visualização dos Pacotes**:
   - A tela principal mostrará uma lista de pacotes capturados. Você pode clicar em qualquer pacote para ver seus detalhes.

2. **Filtragem de Pacotes**:
   - Use a barra de filtro na parte superior para inserir filtros como `ip.addr == 192.168.1.1` para ver apenas o tráfego relacionado a um IP específico, ou `http` para visualizar apenas pacotes HTTP.

3. **Inspecionando Pacotes**:
   - Quando você clica em um pacote, pode expandir as diferentes camadas do protocolo (Ethernet, IP, TCP, etc.) para ver os detalhes.

#### Salvando e Carregando Capturas

- **Salvar Captura**:
  - Depois de capturar os pacotes, você pode salvar a captura em um arquivo `.pcap` para análise futura: `File -> Save As`.
  
- **Carregar Captura**:
  - Para analisar um arquivo de captura existente, vá em `File -> Open` e selecione o arquivo `.pcap`.

### Exemplos de Uso

- **Monitoramento de Tráfego**: Use o Wireshark para monitorar tráfego suspeito em uma rede, como possíveis tentativas de ataque ou anomalias.
  
- **Análise de Protocolo**: Estude como os diferentes protocolos de rede funcionam, visualizando como os dados são transmitidos e recebidos.
  
- **Solução de Problemas**: Identifique e resolva problemas de conectividade ou desempenho de rede, como pacotes perdidos, latência alta, etc.

### Considerações de Segurança

- **Legalidade e Ética**: A captura de pacotes em redes que você não possui ou não tem permissão explícita para monitorar pode ser ilegal e antiética. Use o Wireshark apenas em ambientes onde você tem permissão para fazer a análise de rede.
  
- **Trabalho com Privilégios**: Capturar pacotes requer privilégios de root ou administrador, por isso, tenha cuidado ao usar o Wireshark para garantir que a segurança do sistema não seja comprometida.

### Conclusão

Wireshark é uma ferramenta essencial para qualquer profissional de segurança da informação ou administrador de rede. No Kali Linux, ela é amplamente utilizada para auditorias de segurança, solução de problemas de rede e análise de tráfego. Se usado corretamente, é uma ferramenta incrivelmente poderosa para entender e garantir a segurança das redes.
