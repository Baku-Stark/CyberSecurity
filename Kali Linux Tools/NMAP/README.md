# Nmap

**Nmap Site Official**: https://nmap.org/book/man.html

O Nmap (Network Mapper) é uma ferramenta de código aberto usada para descoberta de redes e auditoria de segurança. Ele foi projetado para varrer grandes redes de forma rápida, mas também funciona bem contra hosts únicos. Nmap é amplamente utilizado por administradores de rede e segurança para realizar inventários de rede, gerenciar cronogramas de atualizações de serviço e monitorar hosts ou tempo de atividade do serviço.

**Size**: 4071 Mb

**Install**:
```bash
sudo apt-get install nmap   # Debian/Ubuntu
sudo yum install nmap       # CentOS/RHEL
sudo dnf install nmap       # Fedora
```

----

# Help

```bash
Nmap 7.94SVN ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports sequentially - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --noninteractive: Disable runtime interactions via keyboard
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```

### Para Que Serve o Nmap?

1. **Descoberta de Rede:** Identifica dispositivos ativos na rede.
2. **Auditoria de Segurança:** Identifica vulnerabilidades e portas abertas que podem ser exploradas.
3. **Inventário de Rede:** Mapeia a estrutura da rede e os dispositivos conectados.
4. **Detecção de Serviços e Sistemas Operacionais:** Descobre quais serviços (e suas versões) estão rodando em hosts e qual sistema operacional está sendo usado.
5. **Monitoramento de Rede:** Verifica a disponibilidade de serviços e hosts.

----

# Aplicação Básica do Nmap

## Comandos Básicos do Nmap

**Varredura Simples de um Host:**
```bash
nmap [endereço_IP]
```
Este comando realiza uma varredura padrão do endereço IP especificado, listando portas abertas e serviços básicos.

**Varredura de Vários Hosts:**
```bash
nmap [endereço_IP1] [endereço_IP2] ... [endereço_IPN]
```
Varre múltiplos endereços IP.

**Varredura de um Range de IPs:**
```bash
nmap [início_range]-[fim_range]
```
Por exemplo:
```bash
nmap 192.168.1.1-254
```
Varre todos os IPs no intervalo especificado.

**Varredura de uma Sub-rede:**
```bash
nmap 192.168.1.0/24
```
Varre todos os 256 endereços IP em uma sub-rede /24.

**Varredura de Portas Específicas:**
```bash
nmap -p [porta] [endereço_IP]
```
Por exemplo:
```bash
nmap -p 80 192.168.1.1
```
Varre a porta 80 do IP especificado.

**Detecção de Sistema Operacional:**
```bash
nmap -O [endereço_IP]
```
Tenta detectar o sistema operacional do host alvo.

**Varredura de Detecção de Serviços e Versões:**
```bash
nmap -sV [endereço_IP]
```
Detecta versões de serviços em execução nas portas abertas.

**Varredura de Todos os Portos:**
```bash
nmap -p- [endereço_IP]
```
Varre todas as 65535 portas do host alvo.

#### 3. **Exemplo Prático**

Imagine que você deseja fazer uma varredura completa em um dispositivo na rede local com IP 192.168.1.100 para identificar todas as portas abertas e os serviços em execução:

```bash
nmap -A 192.168.1.100
```
A opção `-A` habilita a detecção de sistema operacional, versões de serviços, script scanning e traceroute.

----

# Conexões TCP/UDP

Analisar as conexões com um serviço.

### Analisando uma rede com o NMAP

`nmap [SITE URL]`

**Output**:

```bash
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-21 20:19 -03
Nmap scan report for [URL] ([IP ADDRESS])
Host is up (0.014s latency).
Other addresses for [URL] (not scanned): [MAC ADDRESS]
Not shown: 996 filtered tcp ports (no-response)
PORT                    STATE SERVICE
[PORT NUMBER]/[TYPE]     open   http
```

> **Comando**: `host`

Escaneamento do hosting de um serviço.

```bash
host [URL (SEM HTTP)]
```

> **Comando**: `nc`

Comando para testar as portas abertas do serviço.

```bash
nc [IP ADDRESS] [PORT]
[http req]
```

> **Comando**: `nmap [URL SITE || IP ADDRESS] -p [PORTS]`

Exemplos: `nmap google.com -p 80,21` ou `nmap google.com -p 80,21 -sV`

### Identificando rostos

`nmap [IP ADDRES RANGE] -sn -T<0-5>`

A opção `T<0-5>` (**0** para a analise mais aprofundada e lenta; **5** para analise menos aprofundada e rápida)

----

## Sqlmap (-r | Scan ports sequentially - don't randomize)

O comando `-r` no SQLMap permite que você forneça um arquivo contendo uma requisição HTTP completa. Isso é útil quando você precisa passar cookies, cabeçalhos personalizados, dados de formulário ou qualquer outro detalhe específico da requisição HTTP que não pode ser facilmente passado via linha de comando.
Usar a opção `-r` no SQLMap é extremamente útil para cenários complexos onde a requisição HTTP contém múltiplos cabeçalhos, cookies ou dados de formulário. Isso permite uma maior flexibilidade e precisão ao testar vulnerabilidades de injeção SQL em aplicativos web. Certifique-se de sempre usar essas ferramentas de maneira ética e somente em sistemas para os quais você tem permissão explícita para testar.


### Passo a Passo para Utilizar SQLMap com o Arquivo de Requisição HTTP

#### 1. **Capturar a Requisição HTTP**

Use uma ferramenta como Burp Suite, OWASP ZAP, ou as ferramentas de desenvolvedor do seu navegador para capturar a requisição HTTP completa que você deseja testar.

#### 2. **Salvar a Requisição HTTP em um Arquivo**

Salve a requisição HTTP capturada em um arquivo de texto. O arquivo deve conter todos os detalhes da requisição, incluindo o método HTTP, URL, cabeçalhos e corpo, se aplicável.

Exemplo de arquivo de requisição HTTP (`request.txt`):

```
GET /cat.php?id=1 HTTP/1.1
Host: www.bancocn.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: PHPSESSID=1234567890abcdef
Upgrade-Insecure-Requests: 1
```

#### 3. **Executar SQLMap com o Arquivo de Requisição**

Use a opção `-r` para passar o arquivo de requisição para o SQLMap:

```bash
sqlmap -r request.txt
```

#### 4. **Executar SQLMap com Opções Adicionais**

Você pode adicionar outras opções do SQLMap conforme necessário. Por exemplo, para listar bancos de dados:

```bash
sqlmap -r request.txt --dbs
```

### Exemplo Completo

Aqui está um exemplo completo que inclui a identificação de vulnerabilidade, listagem de bancos de dados, tabelas e colunas, e extração de dados, tudo usando um arquivo de requisição HTTP:

1. **Identificar a Vulnerabilidade:**

```bash
sqlmap -r request.txt
```

2. **Listar Bancos de Dados:**

```bash
sqlmap -r request.txt --dbs
```

3. **Listar Tabelas em um Banco de Dados Específico:**

```bash
sqlmap -r request.txt -D testdb --tables
```

4. **Listar Colunas em uma Tabela Específica:**

```bash
sqlmap -r request.txt -D testdb -T users --columns
```

5. **Extrair Dados de Colunas Específicas:**

```bash
sqlmap -r request.txt -D testdb -T users -C username,password --dump
```

----

### Conclusão

O Nmap é uma ferramenta poderosa e flexível para análise de rede e auditoria de segurança. Com seus diversos modos de varredura e opções avançadas, ele pode fornecer informações detalhadas sobre a infraestrutura de rede, ajudando administradores e profissionais de segurança a proteger melhor seus ambientes. Para um uso mais avançado, explorar a documentação oficial e praticar com diferentes cenários é altamente recomendado.
