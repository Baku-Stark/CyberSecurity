# 😺 Hashcat

Hashcat é uma das ferramentas de cracking de senhas mais poderosas e versáteis disponíveis, usada para recuperar senhas perdidas através de ataques de força bruta e ataques de dicionário. No Kali Linux, Hashcat vem pré-instalado e está pronto para uso.

### Instalação do Hashcat

Se o Hashcat não estiver instalado no seu sistema Kali Linux, você pode instalá-lo com o seguinte comando:

```bash
sudo apt-get update
sudo apt-get install hashcat
```

### Uso Básico do Hashcat

#### 1. **Identificar o Tipo de Hash**

Antes de usar o Hashcat, você precisa identificar o tipo de hash que está tentando quebrar. Você pode usar ferramentas como `hashid` para identificar o tipo de hash. Instale `hashid` se ainda não estiver instalado:

```bash
sudo apt-get install hashid
```

Use o `hashid` para identificar o hash:

```bash
hashid -m [hash]
```

#### 2. **Cracking de Hash com Hashcat**

Uma vez identificado o tipo de hash, você pode usar o Hashcat para quebrá-lo. Aqui está um exemplo básico de como usar o Hashcat para quebrar um hash MD5 usando um ataque de dicionário.

```bash
hashcat -m 0 -a 0 -o cracked.txt hashes.txt wordlist.txt
```

- **-m:** Especifica o tipo de hash (0 para MD5).
- **-a:** Especifica o modo de ataque (0 para ataque de dicionário).
- **-o:** Especifica o arquivo de saída para as senhas quebradas.
- **hashes.txt:** Arquivo que contém os hashes a serem quebrados.
- **wordlist.txt:** Arquivo de dicionário que contém a lista de palavras.

#### 3. **Modos de Ataque Comuns**

- **Ataque de Dicionário:** Usa uma lista de palavras (dicionário) para tentar quebrar o hash.
  ```bash
  hashcat -m [hash-type] -a 0 -o cracked.txt hashes.txt wordlist.txt
  ```

- **Ataque de Regras:** Aplica regras ao dicionário para tentar mais combinações.
  ```bash
  hashcat -m [hash-type] -a 0 -o cracked.txt hashes.txt wordlist.txt -r rules/best64.rule
  ```

- **Ataque de Máscara:** Usa uma máscara para tentar combinações específicas de caracteres.
  ```bash
  hashcat -m [hash-type] -a 3 -o cracked.txt hashes.txt ?a?a?a?a?a
  ```

  - **?a:** Qualquer caractere alfanumérico.
  - **?d:** Qualquer dígito.
  - **?u:** Qualquer letra maiúscula.
  - **?l:** Qualquer letra minúscula.
  - **?s:** Qualquer caractere especial.

- **Ataque Combinado:** Combina duas listas de palavras.
  ```bash
  hashcat -m [hash-type] -a 1 -o cracked.txt hashes.txt wordlist1.txt wordlist2.txt
  ```

### Exemplo Completo

Suponha que você tenha um hash SHA-256 que você deseja quebrar usando um ataque de dicionário. Primeiro, você identificaria o tipo de hash e, em seguida, usaria o Hashcat para quebrá-lo.

1. **Identificar o Tipo de Hash:**

```bash
hashid -m e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

2. **Quebrar o Hash com Hashcat:**

```bash
hashcat -m 1400 -a 0 -o cracked.txt hashes.txt wordlist.txt
```

### Recursos e Documentação

- [Documentação Oficial do Hashcat](https://hashcat.net/wiki/)
- [Hashcat Forum](https://hashcat.net/forum/)
- [GitHub do Hashcat](https://github.com/hashcat/hashcat)

### Conclusão

O Hashcat é uma ferramenta poderosa e versátil para quebra de senhas. Com os modos de ataque e a flexibilidade que oferece, ele pode ser usado em uma ampla gama de cenários de segurança. Certifique-se de usar essa ferramenta de maneira ética e legal, e somente em sistemas para os quais você tem permissão explícita para testar.
