# 🤖 IA Mentor de Carreira: Descubra Seu Futuro em Tech

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-FF6B00?style=flat-square&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000?style=flat-square&logo=ollama&logoColor=white)
![Licença](https://img.shields.io/badge/Licença-MIT-green?style=flat-square)

**Agente de IA Mentor de Carreira** — Um agente inteligente que analisa o perfil do aluno, consulta as carreiras disponíveis na DIO e recomenda trilhas personalizadas com roadmap de estudos.

> 🚀 **Projeto do Bootcamp [CI&T - Do Prompt ao Agente](https://www.dio.me/bootcamp/ci-t-do-prompt-ao-agente) — DIO**

---

## ✨ Funcionalidades

- ✅ **Análise personalizada** do perfil, nível e interesses do aluno
- ✅ **Consulta às carreiras da DIO** em tempo real via web scraping
- ✅ **Recomendação inteligente** de trilhas e formações
- ✅ **Roadmap de estudos** dividido em fases com prazos
- ✅ **Próximos passos concretos** e dicas de portfólio
- ✅ **100% gratuito** — roda com modelos open source (Ollama)

---

## 🛠️ Stack

| Tecnologia | Função |
|-----------|--------|
| **Python 3.12+** | Linguagem principal |
| **CrewAI** | Framework de orquestração de agentes |
| **Ollama** | Modelos de IA gratuitos (GLM-5 Cloud / Qwen 3) |
| **ScrapeWebsiteTool** | Ferramenta para ler carreiras da DIO |

---

## 🧠 Como funciona

1. O aluno responde a 4 perguntas (nome, nível, área de interesse, experiência)
2. O agente acessa o site de carreiras da DIO via web scraping
3. Analisa o perfil e cruza com as opções disponíveis
4. Devolve um relatório completo com:
   - Diagnóstico do momento atual
   - Carreira/trilha recomendada
   - Roadmap com fases e cursos
   - Ações imediatas
   - Dicas complementares

---

## 🚀 Como usar

### Pré-requisitos

- [Python 3.12+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com) instalado
- Modelo gratuito configurado (padrão: `glm-5:cloud`)

### Executar

```bash
# Clone o repositório
git clone https://github.com/marcuslinhares/ia-mentor-carreira.git
cd ia-mentor-carreira

# Instale as dependências
pip install -r requirements.txt

# Execute o agente
python agent.py
```

---

## 📁 Estrutura

```
ia-mentor-carreira/
├── agent.py           # Código do agente mentor
├── requirements.txt   # Dependências Python
├── README.md          # Este arquivo
└── RESULT.md          # Exemplo de saída
```

---

## 📄 Licença

MIT — baseado no repositório original [digitalinnovationone/live-ai-agent-career-mentor](https://github.com/digitalinnovationone/live-ai-agent-career-mentor)

---

<p align="center">
  Feito com ❤️ para o Bootcamp CI&T - Do Prompt ao Agente — DIO
</p>
