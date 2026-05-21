from crewai import Agent, Task, Crew, LLM
from crewai_tools import ScrapeWebsiteTool

# Configuração do LLM via Ollama
# Na live usamos "ollama/glm-5:cloud" (gratuito no Ollama Cloud)
# Para rodar local, troque para "ollama/qwen3:8b" ou outro modelo disponível
llm = LLM(
    model="ollama/glm-5:cloud",
    base_url="http://localhost:11434"
)

# Ferramenta para acessar a página de carreiras da DIO
ferramenta_dio = ScrapeWebsiteTool(
    website_url="https://www.dio.me/#careers"
)

# TODO: Defina o Agente Mentor de Carreira em Tecnologia
mentor = Agent(
    role="Mentor de Carreira em Tecnologia",
    goal="Analisar o perfil, interesses e momento de carreira do aluno para recomendar as melhores trilhas, cursos e formações disponíveis na DIO, criando um roadmap personalizado e acionável.",
    backstory="Você é um mentor sênior com mais de 10 anos de experiência no mercado de tecnologia. Já atuou como dev, tech lead, coordenador de educação e recrutador técnico, o que te dá uma visão privilegiada sobre as habilidades mais requisitadas do mercado. Conhece profundamente o ecossistema DIO — suas carreiras, cursos, bootcamps e formações — e sabe exatamente qual trilha se encaixa em cada perfil. Seu estilo é direto, motivador e prático: você não só aponta o caminho, como diz os próximos 3 passos concretos.",
    tools=[ferramenta_dio],
    llm=llm,
    verbose=True
)

# Input do aluno
print("=== Mentor de Carreira em Tecnologia ===\n")
nome_aluno = input("Qual seu nome? ")
nivel = input("Qual seu nível atual (iniciante/intermediário/avançado)? ")
area_interesse = input("Qual área te interessa (frontend, backend, mobile, IA, dados, etc)? ")
experiencia = input("Fale brevemente sobre sua experiência e o que busca na tecnologia:\n> ")

necessidade_aluno = f"""
Aluno: {nome_aluno}
Nível: {nivel}
Área de interesse: {area_interesse}
Experiência: {experiencia}
"""

# TODO: Defina a Tarefa do agente
tarefa = Task(
    description=f"""
Analise as carreiras disponíveis na DIO (acesse o site de carreiras para conferir as opções) e forneça orientações completas para o seguinte aluno:

{necessidade_aluno}

Sua resposta deve incluir:
1. **Diagnóstico** — Análise do momento atual do aluno com base no que ele informou.
2. **Recomendação principal** — Qual carreira/trilha da DIO faz mais sentido para ele e por quê.
3. **Roadmap sugerido** — Etapas, cursos recomendados na DIO e prazos estimados (4-6 semanas por fase).
4. **Próximos passos** — Ações concretas que o aluno pode executar imediatamente.
5. **Dicas extras** — Habilidades complementares, portfólio, projetos práticos.
""",
    expected_output="Um texto completo e personalizado em português brasileiro, contendo: diagnóstico do perfil do aluno, recomendação de carreira na DIO com justificativa, roadmap dividido em fases com cursos sugeridos e prazos, ações imediatas e dicas complementares. Tom motivador e direto.",
    agent=mentor
)

# Execução
crew = Crew(agents=[mentor], tasks=[tarefa])
resultado = crew.kickoff()
print("\n=== Resultado ===\n")
print(resultado)
