# Proxychains-ng

- Link: https://github.com/rofl0r/proxychains-ng

## 💻️ | Diferenças entre Proxychains e Proxychains4

`Proxychains` e `Proxychains4` são ferramentas semelhantes usadas para redirecionar o tráfego de rede através de um ou mais proxies, mas existem algumas diferenças e evoluções entre elas.

### Proxychains

`Proxychains` é a versão mais antiga e foi amplamente utilizada em sistemas Linux para redirecionar o tráfego de rede através de proxies. Sua configuração e uso básico são bastante conhecidos e geralmente envolvem a edição de um arquivo de configuração (`/etc/proxychains.conf`) e o uso de um comando como `proxychains <comando>`.

### Proxychains4

`Proxychains4` é a versão mais recente e é considerada uma evolução do `Proxychains`. Ela oferece algumas melhorias e novas funcionalidades, tais como:

1. **Suporte Aprimorado para Múltiplos Proxies:**
   - `Proxychains4` oferece melhor suporte para o encadeamento de múltiplos proxies, permitindo que o tráfego passe por uma série de proxies antes de alcançar seu destino final.
   
2. **Melhorias de Desempenho e Estabilidade:**
   - A versão mais recente tende a ser mais estável e eficiente, com melhorias no código que reduzem problemas de desempenho e bugs.
   
3. **Configuração Atualizada:**
   - O arquivo de configuração para `Proxychains4` é geralmente encontrado em `/etc/proxychains4.conf` em vez de `/etc/proxychains.conf`.
   
4. **Modo de Cadeia Dinâmica (Dynamic Chain):**
   - `Proxychains4` introduziu o modo de cadeia dinâmica, que permite que ele pule proxies que estão inativos ou falham durante a conexão, aumentando a robustez da ferramenta.

5. **Resolução de DNS:**
   - `Proxychains4` pode redirecionar consultas DNS através dos proxies, o que pode ser útil para esconder a origem das consultas DNS.

### Exemplos de Configuração

Aqui está um exemplo básico do arquivo de configuração para `Proxychains4` (`/etc/proxychains4.conf`):

```conf
# proxychains.conf  VER 4.x
#
#        HTTP, SOCKS4a, SOCKS5 tunneling proxifier with DNS.
# 

# The option below identifies which mode to use, default is dynamic_chain
# dynamic_chain  - Enables Dynamic mode.
# strict_chain   - Enables Strict mode.
# random_chain   - Enables Random mode.

dynamic_chain

# proxy_dns 
# Makes sure that the DNS request is proxified.

# quiet_mode
# Quiet mode: doesn't print messages like "connecting to ...".

# Uncomment the next line to use it:
# quiet_mode

# TCP read timeout in milliseconds.
tcp_read_time_out 15000

# TCP connect timeout in milliseconds.
tcp_connect_time_out 8000

[ProxyList]
# Add your proxies here:
# protocol  host  port
socks5  127.0.0.1 9050
http    192.168.1.1 8080
```

### Uso

O uso de ambas as ferramentas é bastante similar:

- **Proxychains:**
  ```bash
  proxychains curl http://www.google.com
  ```

- **Proxychains4:**
  ```bash
  proxychains4 curl http://www.google.com
  ```

### Resumo

A principal diferença entre `Proxychains` e `Proxychains4` é que `Proxychains4` é uma versão mais nova e melhorada, com suporte aprimorado para múltiplos proxies, melhor desempenho, e novas funcionalidades como o modo de cadeia dinâmica e resolução de DNS através dos proxies. Se você está enfrentando problemas com `Proxychains`, pode valer a pena tentar `Proxychains4` para ver se as melhorias ajudam a resolver seus problemas.
