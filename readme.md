# 🚀 Organizador Universal de Arquivos

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Interface Gráfica](#️-interface-gráfica)
- [Modo Terminal](#-modo-terminal)
- [Tipos de Arquivo Suportados](#-tipos-de-arquivo-suportados)
- [Exemplos](#-exemplos)
- [Segurança](#️-segurança)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

O **Organizador Universal** é uma ferramenta poderosa que organiza automaticamente qualquer pasta do seu computador, separando arquivos por tipo em subpastas organizadas. Com interface gráfica moderna e modo terminal, funciona com **QUALQUER tipo de arquivo existente**.

### ✨ Por que usar?

- 🗂️ **Pasta Downloads bagunçada** com centenas de arquivos misturados
- 🖥️ **Desktop desorganizado** com arquivos espalhados  
- 📂 **Projetos** com códigos, imagens e documentos misturados
- 💼 **Pastas de trabalho** com diferentes tipos de arquivo

### 🎨 Interface Moderna

- **GUI Responsiva**: Interface gráfica moderna com tema escuro
- **Processamento Assíncrono**: Nunca trava durante organização
- **Logs em Tempo Real**: Acompanhe cada etapa com timestamps
- **Modo Terminal**: Para automação e preferência pessoal

---

## 🌟 Funcionalidades

### 🎯 **Organização Universal**
- ✅ Detecta **QUALQUER** tipo de arquivo (exe, pdf, jpg, json, etc.)
- ✅ Extensões compostas (tar.gz, min.js, backup.old)
- ✅ Arquivos sem extensão organizados em pasta especial
- ✅ Normalização automática de nomes para compatibilidade

### 🖥️ **Interface Dupla**
- ✅ **UI**: Interface gráfica intuitiva
- ✅ **Seleção Rápida**: Botões para Downloads, Desktop, Documentos
- ✅ **Escolha Personalizada**: Organize qualquer pasta do sistema

### 🛡️ **Segurança Total**
- ✅ **Nunca deleta** arquivos - apenas move para subpastas
- ✅ **Anti-sobrescrita**: Adiciona números sequenciais para duplicatas
- ✅ **Confirmação**: Sempre pergunta antes de organizar
- ✅ **Logs detalhados**: Rastreia cada operação realizada

### ⚡ **Performance**
- ✅ **Análise rápida** de milhares de arquivos
- ✅ **Processamento assíncrono** - interface não trava
- ✅ **Uso mínimo de memória**
- ✅ **Multiplataforma**: Windows, macOS, Linux

---

## 🔧 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- tkinter (geralmente incluído com Python)

### Instalação Rápida

```bash
# Clone o repositório
git clone [https://github.com/usuario/organizador-universal.git](https://github.com/Kattiell/python-file-organizator)

# Entre na pasta
cd organizador-universal

# Execute o programa
python organizador_universal.py
```

### Instalação Manual

1. **Baixe o arquivo** `organizador_universal.py`
2. **Salve** em uma pasta de sua escolha
3. **Execute** com Python:

```bash
python organizador_universal.py
```

---

## 🎮 Como Usar

### 🖥️ Interface Gráfica

1. **Execute o programa:**
   ```bash
   python organizador_universal.py
   ```

2. **Escolha a opção 1** (Interface Gráfica)

3. **Selecione uma pasta:**
   - 📥 **Downloads** (botão rápido)
   - 🖥️ **Desktop** (botão rápido)
   - 📄 **Documentos** (botão rápido)
   - 📂 **Escolher Pasta...** (qualquer pasta)

4. **Clique em "🔍 Analisar Pasta"** para ver o que será organizado

5. **Clique em "🚀 Organizar!"** quando estiver pronto

---

## 📁 Tipos de Arquivo Suportados

### 💻 Desenvolvimento
```
py, js, html, css, java, cpp, c, php, sql, rb, go, rust, swift, kt
```

### 📄 Documentos  
```
pdf, doc, docx, txt, rtf, odt, pages, tex, md
```

### 📊 Planilhas
```
xls, xlsx, csv, ods, numbers
```

### 🎥 Mídia
```
mp4, avi, mkv, mov, wmv, mp3, wav, flac, jpg, png, gif, svg
```

### 🗜️ Compactados
```
zip, rar, 7z, tar, gz, bz2, tar.gz, tar.bz2, tar.xz
```

### ⚙️ Executáveis
```
exe, msi, deb, rpm, dmg, pkg, appimage, snap
```

### 💾 Sistemas
```
iso, img, vmdk, vdi, qcow2
```

### 📱 Mobile
```
apk, ipa, xap
```

### 🔧 Configuração
```
json, xml, yaml, yml, ini, cfg, conf, toml
```

### ✨ E MUITO MAIS!
**O programa detecta automaticamente QUALQUER extensão que existe!**

---

## 📊 Exemplos

### 📥 Antes da Organização
```
Downloads/
├── documento.pdf
├── foto.jpg  
├── programa.exe
├── musica.mp3
├── planilha.xlsx
├── video.mp4
├── codigo.py
├── arquivo.zip
└── config.json
```

### 🎯 Depois da Organização
```
Downloads/
├── pdf/
│   └── documento.pdf
├── jpg/
│   └── foto.jpg
├── exe/
│   └── programa.exe  
├── mp3/
│   └── musica.mp3
├── xlsx/
│   └── planilha.xlsx
├── mp4/
│   └── video.mp4
├── py/
│   └── codigo.py
├── zip/
│   └── arquivo.zip
└── json/
    └── config.json
```

### 🔢 Proteção Anti-Sobrescrita
```
Downloads/pdf/
├── documento.pdf      ← Original
├── documento_1.pdf    ← Primeiro duplicata
├── documento_2.pdf    ← Segunda duplicata
└── relatorio.pdf
```

---

## 🛡️ Segurança

### 🔒 Garantias de Segurança

- **✅ NUNCA deleta arquivos** - apenas move para subpastas
- **✅ Proteção anti-sobrescrita** - adiciona números sequenciais
- **✅ Confirmação obrigatória** antes de qualquer organização
- **✅ Logs detalhados** de todas as operações
- **✅ Tratamento de erros** robusto

### ⚠️ O que o programa FAZ:
```python
# MOVE arquivo para subpasta (seguro)
shutil.move("arquivo.pdf", "Downloads/pdf/arquivo.pdf")
```

### ❌ O que o programa NÃO FAZ:
```python
# NUNCA deleta arquivos
os.remove("arquivo.pdf")  # ← NÃO EXISTE NO CÓDIGO!

# NUNCA sobrescreve
shutil.copy2("novo.pdf", "arquivo.pdf")  # ← NÃO EXISTE!
```

### 🛡️ Proteções Implementadas

1. **Validação de Pastas**: Verifica se pasta existe antes de processar
2. **Backup de Nomes**: Mantém nomes originais quando possível  
3. **Numeração Sequencial**: arquivo.pdf → arquivo_1.pdf → arquivo_2.pdf
4. **Tratamento de Erros**: Captura erros sem perder arquivos
5. **Confirmações**: Dialog de confirmação antes de organizar

---

## 🔄 Fluxo de Uso Típico

### 1. 📥 Situação Inicial
```
Downloads/ (47 arquivos misturados)
├── IMG_001.jpg
├── relatorio.pdf  
├── programa.exe
├── musica.mp3
├── (... 43 outros arquivos ...)
```

### 2. 🔍 Análise
```
📊 ANÁLISE COMPLETA:
   Total de arquivos: 47
   Tipos diferentes: 12
   
📁 Pastas que serão criadas:
   📂 jpg/ (15 arquivos)
   📂 pdf/ (8 arquivos)  
   📂 exe/ (3 arquivos)
   📂 mp3/ (12 arquivos)
   📂 ... (8 outros tipos)
```

### 3. 🚀 Organização
```
✅ IMG_001.jpg → jpg/
✅ relatorio.pdf → pdf/
✅ programa.exe → exe/
✅ musica.mp3 → mp3/
🎉 47 arquivos organizados!
```

### 4. 📁 Resultado Final
```
Downloads/
├── jpg/ (15 imagens)
├── pdf/ (8 documentos)
├── exe/ (3 programas)  
├── mp3/ (12 músicas)
└── ... (8 outras pastas)
```

---

## 🚀 Recursos Avançados

### 🧠 Detecção Inteligente

#### Extensões Compostas
```
arquivo.tar.gz    → tar_gz/
script.min.js     → min_js/  
config.backup.old → backup_old/
```

#### Normalização Automática
```
arquivo.PDF       → pdf/          (minúscula)
config.JSON       → json/         (minúscula)
script.min.JS     → min_js/       (normalizado)
```

#### Caracteres Especiais
```
arquivo<test>.pdf → arquivo_test_.pdf (caracteres inválidos removidos)
```

### ⚡ Performance

- **Análise de 1000+ arquivos**: < 2 segundos
- **Organização de 1000+ arquivos**: < 10 segundos  
- **Uso de memória**: Mínimo (< 50MB)
- **Interface responsiva**: Nunca trava

---

## 🎯 Casos de Uso

### 📥 Downloads Bagunçados
```
Situação: 200+ arquivos misturados de anos de downloads
Solução: Organização automática por tipo em minutos
Resultado: Estrutura clara para encontrar qualquer arquivo
```

### 🖥️ Desktop Desorganizado  
```
Situação: Screenshots, documentos, ícones espalhados
Solução: Um clique para organizar tudo
Resultado: Desktop limpo e profissional
```

### 💼 Pasta de Trabalho
```
Situação: PDFs, planilhas, imagens, códigos misturados
Solução: Separação automática por categoria profissional
Resultado: Workflow organizado e produtivo
```

### 🎮 Pasta de Jogos
```
Situação: Saves, mods, screenshots, executáveis misturados  
Solução: Organização por tipo de arquivo de jogo
Resultado: Fácil backup e gerenciamento
```

---

## 🛠️ Personalização

### 🔧 Adicionar Novos Tipos

O programa detecta automaticamente qualquer extensão, mas você pode personalizar o comportamento:

```python
# Exemplo: Adicionar categoria personalizada
def obter_categoria_personalizada(extensao):
    categorias_especiais = {
        'dwg': 'cad_files',
        'step': 'cad_files', 
        'stl': '3d_models',
        'obj': '3d_models'
    }
    return categorias_especiais.get(extensao, extensao)
```

### 🎨 Personalizar Interface

```python
# Cores personalizadas
style.configure('Custom.TButton', 
    background='#your_color',
    foreground='#text_color'
)
```

---

## 🐛 Solução de Problemas

### ❓ Problemas Comuns

#### 🚫 "Pasta não encontrada"
```
Solução: Verifique se o caminho está correto e se você tem permissões
```

#### 🔒 "Erro de permissão"  
```
Solução: Execute como administrador ou escolha pasta com permissões
```

#### 🖥️ "Interface gráfica não abre"
```
Solução: Verifique se tkinter está instalado:
pip install tk
```

#### ⚡ "Programa trava"
```
Solução: Use a versão mais recente - processamento é assíncrono
```

## 🤝 Contribuição

Contribuições são sempre bem-vindas! 

### 📋 Padrões de Código

- Use **type hints** quando possível
- Siga **PEP 8** para formatação
- Adicione **docstrings** para funções
- Inclua **testes** para novas funcionalidades

---

## 📝 Changelog

### v2.0.0 (Atual)
- ✨ Interface gráfica moderna
- ⚡ Processamento assíncrono
- 🧠 Detecção de extensões compostas
- 🛡️ Melhorias na segurança
- 📊 Logs detalhados em tempo real

### v1.0.0  
- 🚀 Versão inicial
- 💻 Modo terminal
- 📁 Organização básica por extensão

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

</div>
