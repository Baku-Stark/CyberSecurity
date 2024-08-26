# Quebrando hash de senhas com o Hashcat

Sim, é possível usar o **Hashcat** para quebrar hashes de strings. O Hashcat é uma ferramenta poderosa de cracking de hashes que pode aproveitar a GPU para acelerar o processo de quebra de senhas.

### Como Descobrir o Hash de uma Senha Usando o Terminal do Linux

Você pode gerar o hash de uma senha no terminal do Linux usando várias ferramentas disponíveis, como `echo`, `openssl`, ou `hashcat`. Abaixo estão alguns exemplos de como gerar diferentes tipos de hashes:

#### 1. **Gerar um Hash MD5:**

```bash
echo -n 'sua_senha' | md5sum
```

- **Explicação**: 
  - `echo -n 'sua_senha'`: Imprime a senha sem a nova linha no final.
  - `| md5sum`: Calcula o hash MD5.

#### 2. **Gerar um Hash SHA-256:**

```bash
echo -n 'sua_senha' | sha256sum
```

- **Explicação**:
  - `sha256sum`: Calcula o hash SHA-256.

#### 3. **Gerar um Hash SHA-512:**

```bash
echo -n 'sua_senha' | sha512sum
```

- **Explicação**:
  - `sha512sum`: Calcula o hash SHA-512.

#### 4. **Gerar um Hash com OpenSSL (MD5 como exemplo):**

```bash
echo -n 'sua_senha' | openssl dgst -md5
```

- **Explicação**:
  - `openssl dgst -md5`: Usa o OpenSSL para gerar um hash MD5.

#### 1. **Preparar o Hash**

Primeiro, você deve ter o hash que deseja quebrar. Esse hash deve estar em um arquivo de texto. Suponha que o hash seja algo como `5d41402abc4b2a76b9719d911017c592` (que é o hash MD5 da string `"hello"`). Crie um arquivo chamado `hashes.txt` que contenha o hash:

```plaintext
5d41402abc4b2a76b9719d911017c592
```

#### 2. **Executar o Hashcat**

Agora, você pode usar o Hashcat para tentar quebrar o hash. O comando básico para fazer isso é:

```bash
hashcat -m 0 -a 3 5d41402abc4b2a76b9719d911017c592
```

- **`-m 0`**: Especifica o tipo de hash. No caso de MD5, o código é `0`. Você pode verificar outros tipos de hash [aqui](https://hashcat.net/wiki/doku.php?id=example_hashes).
- **`-a 3`**: Especifica o modo de ataque (serão fornecidos alguns exemplos abaixo)


### Verificar os Resultados

Após o comando ser executado, você pode verificar o arquivo `found.txt` para ver se alguma senha foi encontrada:

```bash
hashcat -m 0 -a 3 5d41402abc4b2a76b9719d911017c592 --show
```

O arquivo terá o seguinte formato:

```plaintext
5d41402abc4b2a76b9719d911017c592:hello
```

Aqui, `5d41402abc4b2a76b9719d911017c592` é o hash original, e `hello` é a senha que foi encontrada.

### Considerações Finais

- **Tipos de Hash**: Se você estiver lidando com outro tipo de hash (SHA-1, SHA-256, etc.), será necessário alterar o valor de `-m` para corresponder ao tipo correto.
- **Desempenho**: Hashcat é otimizado para ser executado em GPUs, o que o torna muito mais rápido que outras ferramentas em operações de força bruta ou wordlist.
- **Legalidade e Ética**: Sempre use essas ferramentas de forma ética e legal, apenas em sistemas e com dados nos quais você tem permissão explícita para realizar tais testes.

Esses passos devem ajudá-lo a quebrar hashes de strings usando Hashcat e uma wordlist.
