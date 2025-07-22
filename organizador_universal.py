#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Organizador Universal de Arquivos
=====================================

Organiza automaticamente qualquer pasta por tipo de arquivo
Interface gráfica moderna e intuitiva
Funciona com QUALQUER tipo de arquivo existente

Autor: Kattiel
Versão: 2.0.0
Licença: MIT
"""

import os
import shutil
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from collections import defaultdict
import threading
from datetime import datetime

class OrganizadorUniversal:
    def __init__(self):
        """Inicializa o Organizador Universal"""
        self.pasta_selecionada = None
        self.estatisticas = {}
        self.total_arquivos = 0
        self.organizando = False
        self.historico_organizacao = []  # Guarda histórico para desfazer
        self.pastas_criadas = []  # Guarda pastas criadas para remoção
        
        self.configurar_interface()
    
    def configurar_interface(self):
        """Configura a interface gráfica moderna"""
        self.root = tk.Tk()
        self.root.title("🚀 Organizador Universal de Arquivos")
        self.root.geometry("900x700")
        self.root.configure(bg='#2b2b2b')
        
        try:
            # Se você tiver um ícone, descomente a linha abaixo
            # self.root.iconbitmap('icone.ico')
            pass
        except:
            pass
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#2b2b2b', foreground='#ffffff')
        style.configure('Subtitle.TLabel', font=('Arial', 10), background='#2b2b2b', foreground='#cccccc')
        style.configure('Modern.TButton', font=('Arial', 10, 'bold'))
        style.configure('Success.TButton', background='#4CAF50', foreground='white')
        style.configure('Warning.TButton', background='#FF9800', foreground='white')
        style.configure('Danger.TButton', background='#f44336', foreground='white')
        
        self.centralizar_janela()
        
        self.criar_widgets()
    
    def centralizar_janela(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (900 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f'900x700+{x}+{y}')
    
    def criar_widgets(self):
        """Cria todos os widgets da interface"""

        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(main_frame, text="🚀 Organizador Universal de Arquivos", style='Title.TLabel')
        title_label.pack(pady=(0, 5))
        
        subtitle_label = ttk.Label(main_frame, text="Organize qualquer pasta automaticamente por tipo de arquivo", style='Subtitle.TLabel')
        subtitle_label.pack(pady=(0, 5))
        
        author_label = ttk.Label(main_frame, text="Desenvolvido por Kattiel", style='Subtitle.TLabel')
        author_label.pack(pady=(0, 15))
        
        pasta_frame = ttk.LabelFrame(main_frame, text="📁 Seleção de Pasta", padding=15)
        pasta_frame.pack(fill='x', pady=(0, 15))
        
        botoes_frame = ttk.Frame(pasta_frame)
        botoes_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Button(botoes_frame, text="📥 Downloads", command=self.selecionar_downloads, style='Modern.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(botoes_frame, text="🖥️ Desktop", command=self.selecionar_desktop, style='Modern.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(botoes_frame, text="📄 Documentos", command=self.selecionar_documentos, style='Modern.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(botoes_frame, text="📂 Escolher Pasta...", command=self.selecionar_pasta_custom, style='Modern.TButton').pack(side='right')

        self.pasta_label = ttk.Label(pasta_frame, text="Nenhuma pasta selecionada", foreground='#888888')
        self.pasta_label.pack(anchor='w', pady=(5, 0))
        
        self.analise_frame = ttk.LabelFrame(main_frame, text="📊 Análise dos Arquivos", padding=15)
        self.analise_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        self.texto_analise = scrolledtext.ScrolledText(self.analise_frame, height=12, wrap='word', font=('Consolas', 9))
        self.texto_analise.pack(fill='both', expand=True)

        acoes_frame = ttk.Frame(main_frame)
        acoes_frame.pack(fill='x')
        self.progresso = ttk.Progressbar(acoes_frame, mode='indeterminate')
        self.progresso.pack(fill='x', pady=(0, 10))
        botoes_acoes = ttk.Frame(acoes_frame)
        botoes_acoes.pack(fill='x')
        
        self.btn_analisar = ttk.Button(botoes_acoes, text="🔍 Analisar Pasta", command=self.analisar_pasta_thread, style='Modern.TButton', state='disabled')
        self.btn_analisar.pack(side='left', padx=(0, 10))
        
        self.btn_organizar = ttk.Button(botoes_acoes, text="🚀 Organizar!", command=self.organizar_arquivos_thread, style='Success.TButton', state='disabled')
        self.btn_organizar.pack(side='left', padx=(0, 10))
        
        self.btn_desfazer = ttk.Button(botoes_acoes, text="🔄 Desfazer", command=self.desfazer_organizacao_thread, style='Warning.TButton', state='disabled')
        self.btn_desfazer.pack(side='left', padx=(0, 10))
        
        self.btn_limpar = ttk.Button(botoes_acoes, text="🗑️ Limpar", command=self.limpar_analise, style='Warning.TButton')
        self.btn_limpar.pack(side='left', padx=(0, 10))
        
        ttk.Button(botoes_acoes, text="❌ Sair", command=self.sair_aplicacao, style='Danger.TButton').pack(side='right')
    
    def selecionar_downloads(self):
        """Seleciona a pasta Downloads padrão"""
        pasta = Path.home() / "Downloads"
        self.definir_pasta_selecionada(pasta)
    
    def selecionar_desktop(self):
        """Seleciona a pasta Desktop/Área de Trabalho"""
        pasta = Path.home() / "Desktop"
        if not pasta.exists():
            pasta = Path.home() / "Área de Trabalho"
        self.definir_pasta_selecionada(pasta)
    
    def selecionar_documentos(self):
        """Seleciona a pasta Documentos"""
        pasta = Path.home() / "Documents"
        if not pasta.exists():
            pasta = Path.home() / "Documentos"
        self.definir_pasta_selecionada(pasta)
    
    def selecionar_pasta_custom(self):
        """Abre dialog para seleção de pasta personalizada"""
        pasta = filedialog.askdirectory(title="Selecione a pasta para organizar")
        if pasta:
            self.definir_pasta_selecionada(Path(pasta))
    
    def definir_pasta_selecionada(self, pasta):
        """Define a pasta selecionada e atualiza a interface"""
        if pasta.exists():
            self.pasta_selecionada = pasta
            self.pasta_label.config(text=f"📁 {pasta}", foreground='#4CAF50')
            self.btn_analisar.config(state='normal')
            self.adicionar_log(f"✅ Pasta selecionada: {pasta}")
        else:
            messagebox.showerror("Erro", f"Pasta não encontrada: {pasta}")
    
    def adicionar_log(self, mensagem):
        """Adiciona mensagem ao log com timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.texto_analise.insert(tk.END, f"[{timestamp}] {mensagem}\n")
        self.texto_analise.see(tk.END)
        self.root.update()
    
    def normalizar_nome_pasta(self, extensao):
        """Normaliza o nome da pasta para ser válido no sistema de arquivos"""
        if not extensao:
            return 'sem_extensao'
            
        nome_limpo = re.sub(r'[<>:"/\\|?*]', '_', extensao.lower())
        nome_limpo = nome_limpo.strip('.')
        extensoes_compostas = {
            'tar.gz': 'tar_gz', 
            'tar.bz2': 'tar_bz2', 
            'tar.xz': 'tar_xz',
            'backup.old': 'backup_old', 
            'min.js': 'min_js', 
            'min.css': 'min_css'
        }
        
        return extensoes_compostas.get(nome_limpo, nome_limpo if nome_limpo else 'sem_extensao')
    
    def obter_extensao_completa(self, arquivo):
        """Obtém a extensão completa do arquivo, incluindo extensões compostas"""
        nome = arquivo.name.lower()
        extensoes_compostas = [
            '.tar.gz', '.tar.bz2', '.tar.xz', '.tar.lz', '.tar.Z',
            '.backup.old', '.min.js', '.min.css', '.test.js', '.spec.js'
        ]
        for ext_comp in extensoes_compostas:
            if nome.endswith(ext_comp):
                return ext_comp[1:]
        
        extensao = arquivo.suffix.lower()
        return extensao[1:] if extensao else ''
    
    def analisar_pasta_thread(self):
        """Executa análise em thread separada"""
        if not self.pasta_selecionada:
            messagebox.showwarning("Atenção", "Selecione uma pasta primeiro!")
            return
        
        self.btn_analisar.config(state='disabled')
        self.progresso.start()
        
        thread = threading.Thread(target=self.analisar_pasta, daemon=True)
        thread.start()
    
    def analisar_pasta(self):
        """Analisa todos os arquivos da pasta selecionada"""
        try:
            self.adicionar_log("🔍 Iniciando análise...")
            
            self.estatisticas = defaultdict(list)
            self.total_arquivos = 0
            
            for item in self.pasta_selecionada.iterdir():
                if item.is_file():
                    extensao = self.obter_extensao_completa(item)
                    extensao_normalizada = self.normalizar_nome_pasta(extensao)
                    self.estatisticas[extensao_normalizada].append(item.name)
                    self.total_arquivos += 1
            
            self.mostrar_analise()
            
        except Exception as e:
            self.adicionar_log(f"❌ Erro na análise: {str(e)}")
        finally:
            self.progresso.stop()
            self.btn_analisar.config(state='normal')
    
    def mostrar_analise(self):
        """Exibe os resultados da análise"""
        if self.total_arquivos == 0:
            self.adicionar_log("ℹ️ Nenhum arquivo encontrado para organizar")
            return
        
        self.adicionar_log(f"\n📊 ANÁLISE COMPLETA:")
        self.adicionar_log(f"   Total de arquivos: {self.total_arquivos}")
        self.adicionar_log(f"   Tipos diferentes: {len(self.estatisticas)}")
        self.adicionar_log(f"\n📁 Pastas que serão criadas:")
        
        for extensao, arquivos in sorted(self.estatisticas.items()):
            quantidade = len(arquivos)
            exemplos = ', '.join(arquivos[:3])
            if quantidade > 3:
                exemplos += f" ... (+{quantidade-3} mais)"
            
            self.adicionar_log(f"   📂 {extensao}/ ({quantidade} arquivo{'s' if quantidade > 1 else ''})")
            self.adicionar_log(f"      Exemplos: {exemplos}")
        
        self.adicionar_log(f"\n⚠️ {self.total_arquivos} arquivos serão organizados em {len(self.estatisticas)} pastas")
        self.btn_organizar.config(state='normal')
    
    def organizar_arquivos_thread(self):
        """Executa organização em thread separada"""
        resposta = messagebox.askyesno(
            "Confirmar Organização", 
            f"Deseja organizar {self.total_arquivos} arquivos em {len(self.estatisticas)} pastas?\n\n"
            f"Esta ação moverá os arquivos para subpastas dentro de:\n{self.pasta_selecionada}\n\n"
            f"⚠️ Os arquivos NÃO serão deletados, apenas movidos para subpastas organizadas."
        )
        
        if not resposta:
            return
        
        self.btn_organizar.config(state='disabled')
        self.btn_analisar.config(state='disabled')
        self.progresso.start()
        self.organizando = True
        
        thread = threading.Thread(target=self.organizar_arquivos, daemon=True)
        thread.start()
    
    def organizar_arquivos(self):
        """Organiza todos os arquivos"""
        try:
            self.adicionar_log(f"\n🚀 Iniciando organização...")
            
            # Limpar histórico anterior
            self.historico_organizacao = []
            self.pastas_criadas = []
            
            # Criar pastas
            for extensao in self.estatisticas.keys():
                pasta = self.pasta_selecionada / extensao
                if not pasta.exists():
                    pasta.mkdir(exist_ok=True)
                    self.pastas_criadas.append(pasta)
                    self.adicionar_log(f"✅ Pasta criada: {extensao}/")
                else:
                    self.adicionar_log(f"📁 Pasta já existia: {extensao}/")

            arquivos_movidos = 0
            arquivos_com_erro = 0
            
            for item in self.pasta_selecionada.iterdir():
                if item.is_file() and self.organizando:
                    extensao = self.obter_extensao_completa(item)
                    extensao_normalizada = self.normalizar_nome_pasta(extensao)
                    pasta_destino = self.pasta_selecionada / extensao_normalizada

                    if item.parent == pasta_destino:
                        continue
                    
                    # Salvar estado original antes de mover
                    arquivo_original = item
                    
                    sucesso, resultado = self.mover_arquivo_seguro(item, pasta_destino)
                    
                    if sucesso:
                        # Salvar no histórico para poder desfazer
                        self.historico_organizacao.append({
                            'origem': arquivo_original,
                            'destino': pasta_destino / resultado,
                            'nome_original': arquivo_original.name
                        })
                        
                        self.adicionar_log(f"📦 {arquivo_original.name} → {extensao_normalizada}/")
                        arquivos_movidos += 1
                    else:
                        self.adicionar_log(f"❌ Erro: {arquivo_original.name} - {resultado}")
                        arquivos_com_erro += 1
                        
            self.adicionar_log(f"\n🎉 ORGANIZAÇÃO CONCLUÍDA!")
            self.adicionar_log(f"✅ Arquivos organizados: {arquivos_movidos}")
            self.adicionar_log(f"❌ Arquivos com erro: {arquivos_com_erro}")
            
            # Habilitar botão desfazer se algo foi movido
            if arquivos_movidos > 0:
                self.btn_desfazer.config(state='normal')
                self.adicionar_log(f"🔄 Use 'Desfazer' para reverter a organização")
                
                messagebox.showinfo(
                    "Sucesso!", 
                    f"Organização concluída com sucesso!\n\n"
                    f"✅ {arquivos_movidos} arquivos organizados\n"
                    f"❌ {arquivos_com_erro} erros\n\n"
                    f"📁 Pasta organizada: {self.pasta_selecionada}\n\n"
                    f"💡 Use o botão 'Desfazer' para reverter se necessário"
                )
            
        except Exception as e:
            self.adicionar_log(f"❌ Erro geral: {str(e)}")
            messagebox.showerror("Erro", f"Erro durante organização: {str(e)}")
        finally:
            self.progresso.stop()
            self.btn_analisar.config(state='normal')
            self.btn_organizar.config(state='disabled')
            self.organizando = False
    
    def desfazer_organizacao_thread(self):
        """Executa desfazer organização em thread separada"""
        if not self.historico_organizacao:
            messagebox.showwarning("Atenção", "Nenhuma organização para desfazer!")
            return
        
        resposta = messagebox.askyesno(
            "Confirmar Desfazer", 
            f"Deseja desfazer a organização?\n\n"
            f"🔄 {len(self.historico_organizacao)} arquivos serão movidos de volta\n"
            f"🗑️ Pastas vazias criadas serão removidas\n\n"
            f"Esta ação deixará tudo como estava antes da organização."
        )
        
        if not resposta:
            return
        
        self.btn_desfazer.config(state='disabled')
        self.btn_analisar.config(state='disabled')
        self.btn_organizar.config(state='disabled')
        self.progresso.start()
        
        thread = threading.Thread(target=self.desfazer_organizacao, daemon=True)
        thread.start()
    
    def desfazer_organizacao(self):
        """Desfaz a organização, movendo arquivos de volta e removendo pastas"""
        try:
            self.adicionar_log(f"\n🔄 Iniciando desfazer organização...")
            
            arquivos_restaurados = 0
            arquivos_com_erro = 0
            
            # Mover arquivos de volta para a posição original
            for operacao in reversed(self.historico_organizacao):  # Reverso para desfazer na ordem inversa
                try:
                    arquivo_atual = operacao['destino']
                    pasta_origem = self.pasta_selecionada
                    nome_original = operacao['nome_original']
                    
                    if arquivo_atual.exists():
                        # Caminho de destino original
                        destino_original = pasta_origem / nome_original
                        
                        # Se arquivo original já existe, adiciona número
                        contador = 1
                        while destino_original.exists():
                            nome_base = Path(nome_original).stem
                            extensao = Path(nome_original).suffix
                            novo_nome = f"{nome_base}_restaurado_{contador}{extensao}"
                            destino_original = pasta_origem / novo_nome
                            contador += 1
                        
                        shutil.move(str(arquivo_atual), str(destino_original))
                        self.adicionar_log(f"📦 {arquivo_atual.name} → pasta principal")
                        arquivos_restaurados += 1
                    else:
                        self.adicionar_log(f"⚠️ Arquivo não encontrado: {arquivo_atual.name}")
                        
                except Exception as e:
                    self.adicionar_log(f"❌ Erro ao restaurar {operacao['nome_original']}: {str(e)}")
                    arquivos_com_erro += 1
            
            # Remover pastas vazias que foram criadas
            pastas_removidas = 0
            for pasta in self.pastas_criadas:
                try:
                    if pasta.exists() and pasta.is_dir():
                        # Verificar se pasta está vazia
                        if not any(pasta.iterdir()):
                            pasta.rmdir()
                            self.adicionar_log(f"🗑️ Pasta removida: {pasta.name}/")
                            pastas_removidas += 1
                        else:
                            self.adicionar_log(f"📂 Pasta não removida (contém arquivos): {pasta.name}/")
                except Exception as e:
                    self.adicionar_log(f"❌ Erro ao remover pasta {pasta.name}: {str(e)}")
            
            # Limpar histórico
            self.historico_organizacao = []
            self.pastas_criadas = []
            
            # Relatório final
            self.adicionar_log(f"\n✅ DESFAZER CONCLUÍDO!")
            self.adicionar_log(f"📦 Arquivos restaurados: {arquivos_restaurados}")
            self.adicionar_log(f"🗑️ Pastas removidas: {pastas_removidas}")
            self.adicionar_log(f"❌ Erros: {arquivos_com_erro}")
            
            messagebox.showinfo(
                "Desfazer Concluído!", 
                f"Organização desfeita com sucesso!\n\n"
                f"✅ {arquivos_restaurados} arquivos restaurados\n"
                f"🗑️ {pastas_removidas} pastas removidas\n"
                f"❌ {arquivos_com_erro} erros\n\n"
                f"📁 Pasta voltou ao estado original!"
            )
            
        except Exception as e:
            self.adicionar_log(f"❌ Erro geral ao desfazer: {str(e)}")
            messagebox.showerror("Erro", f"Erro ao desfazer organização: {str(e)}")
        finally:
            self.progresso.stop()
            self.btn_analisar.config(state='normal')
            self.btn_desfazer.config(state='disabled')
    
    def mover_arquivo_seguro(self, arquivo, pasta_destino):
        """Move arquivo de forma segura, evitando sobrescrever"""
        try:
            novo_caminho = pasta_destino / arquivo.name
            contador = 1
            nome_original = arquivo.stem
            extensao_arquivo = arquivo.suffix
            
            while novo_caminho.exists():
                if extensao_arquivo:
                    novo_nome = f"{nome_original}_{contador}{extensao_arquivo}"
                else:
                    novo_nome = f"{nome_original}_{contador}"
                novo_caminho = pasta_destino / novo_nome
                contador += 1
            
            shutil.move(str(arquivo), str(novo_caminho))
            return True, novo_caminho.name
            
        except Exception as e:
            return False, str(e)
    
    def limpar_analise(self):
        """Limpa a análise atual"""
        self.texto_analise.delete(1.0, tk.END)
        self.estatisticas = {}
        self.total_arquivos = 0
        self.btn_organizar.config(state='disabled')
        
        # Manter histórico para desfazer se existir
        if self.historico_organizacao:
            self.adicionar_log("🔄 Histórico de organização mantido - botão 'Desfazer' ainda disponível")
        
        self.adicionar_log("🗑️ Análise limpa - Selecione uma pasta e analise novamente")
    
    def sair_aplicacao(self):
        """Sai da aplicação com confirmação"""
        if self.organizando:
            resposta = messagebox.askyesno(
                "Organização em Andamento", 
                "Uma organização está em andamento. Deseja realmente sair?"
            )
            if not resposta:
                return
        
        self.root.quit()
        self.root.destroy()
    
    def executar(self):
        """Inicia a aplicação"""
        self.adicionar_log("🚀 Organizador Universal iniciado!")
        self.adicionar_log("📁 Selecione uma pasta para começar a organização")
        self.root.protocol("WM_DELETE_WINDOW", self.sair_aplicacao)
        self.root.mainloop()

def main():
    """Função principal - inicia diretamente a interface gráfica"""
    try:
        app = OrganizadorUniversal()
        app.executar()
    except ImportError as e:
        import sys
        print("❌ Erro: Interface gráfica não disponível!")
        print(f"Detalhes: {str(e)}")
        print("\n💡 Soluções:")
        print("1. Instale tkinter: pip install tk")
        print("2. Use Python com tkinter incluído")
        print("3. Reinstale Python com interface gráfica")
        input("\nPressione Enter para sair...")
        sys.exit(1)
    except Exception as e:
        import sys
        print(f"❌ Erro inesperado: {str(e)}")
        print("Por favor, reporte este erro ao desenvolvedor: Kattiel")
        input("\nPressione Enter para sair...")
        sys.exit(1)

if __name__ == "__main__":
    main()