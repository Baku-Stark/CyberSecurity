# Wafw00f

[Wafw00f](https://github.com/EnableSecurity/wafw00f)

[Linux Packages - Wafw00f](https://linux-packages.com/ubuntu-24-04/package/wafw00f)

## Install "wafw00f" package 

```bash
sudo apt install wafw00f 
```

**Wafw00f** é uma ferramenta de segurança que faz parte do Kali Linux e é usada para detectar a presença de um Web Application Firewall (WAF) em sites. Um WAF é uma camada de segurança que monitora, filtra ou bloqueia tráfego HTTP entre uma aplicação web e a internet, protegendo contra ataques comuns como SQL injection, cross-site scripting (XSS), e outros.

### Como Funciona o Wafw00f

O Wafw00f funciona enviando uma série de requisições HTTP específicas para o servidor alvo e analisando as respostas. Baseado em padrões conhecidos de como diferentes WAFs respondem a certas requisições, o Wafw00f consegue identificar se um WAF está presente e, em muitos casos, determinar qual é a tecnologia específica do WAF utilizado.

### Funcionalidades do Wafw00f

- **Detecção de WAFs**: Identifica se um WAF está ativo em um site.
- **Identificação do Tipo de WAF**: Tenta determinar o tipo específico de WAF em uso (por exemplo, ModSecurity, Cloudflare, etc.).
- **Bypass Básico**: Enquanto a principal função do Wafw00f é detecção, a identificação do WAF pode ajudar a planejar estratégias para bypass.

### Usando o Wafw00f no Kali Linux

Aqui está um exemplo básico de como usar o Wafw00f:

1. **Verificar a presença de um WAF**:

   ```bash
   wafw00f http://www.example.com
   ```

   Isso vai verificar se um WAF está presente no site `www.example.com` e tentar identificá-lo.

2. **Obter ajuda e ver as opções disponíveis**:

   ```bash
   wafw00f -h
   ```

   Este comando exibe as opções disponíveis no Wafw00f, como a escolha de portas específicas, timeout, e mais.

3. **Especificar uma porta personalizada**:

   Se o site está rodando em uma porta não padrão (por exemplo, porta 8080):

   ```bash
   wafw00f http://www.example.com:8080
   ```

### Limitações

- O Wafw00f não realiza ataques e não tenta contornar o WAF; ele é usado apenas para detecção.
- Alguns WAFs podem ser configurados para mascarar sua presença, tornando a detecção mais difícil.

### Conclusão

O Wafw00f é uma ferramenta útil para quem realiza testes de penetração e deseja saber se um WAF está protegendo um site. Com essa informação, o testador pode ajustar suas abordagens de ataque ou exploração para lidar com a presença de um WAF.
