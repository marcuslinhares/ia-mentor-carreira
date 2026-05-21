# 🏦 Desafio Criativo: Extraindo Insights do Feedback de Clientes Bancários

**Bootcamp:** CI&T - Do Prompt ao Agente | **DIO**

---

## Passo 1 — Defina a intenção

Quero que a IA analise **feedbacks de clientes de um banco digital sobre atendimento, aplicativo, cartão de crédito e operações via Pix** para identificar **reclamações frequentes, elogios, pontos de atrito e oportunidades de melhoria nos canais digitais**.

O resultado será usado por **uma equipe de Experiência do Cliente (CX) e pelo time de Produto Digital** para apoiar **priorização de melhorias no app, redução de reclamações recorrentes e otimização dos canais de atendimento**.

A entrega deve conter **um resumo executivo, uma tabela com temas, sentimento, exemplos de comentários e ações sugeridas, e uma lista das 3 prioridades mais urgentes**.

O resultado será considerado bom se for **claro, organizado, baseado exclusivamente nos comentários fornecidos, com recomendações acionáveis e sem expor dados sensíveis dos clientes**.

---

## Passo 2 — Adicione contexto e restrições

**Contexto:** Estou trabalhando com feedbacks de clientes bancários relacionados ao **aplicativo mobile, atendimento por chat, cartão de crédito, Pix e operações de conta corrente**.

**Dados disponíveis:** A base contém **data do comentário, canal de atendimento (chat, telefone, e-mail), texto do feedback, produto citado, nota de satisfação (1 a 5) e segmento do cliente (PF ou PJ)**.

**Critérios de análise:** A IA deve classificar os feedbacks por **tema (ex: lentidão, erro no Pix, atendimento, fatura, senha), sentimento (positivo, neutro, negativo), urgência (baixa, média, alta) e produto citado**.

**Cuidados e restrições:**

- Use apenas os dados fornecidos.
- Não invente números, causas ou conclusões.
- Não exponha dados pessoais ou sensíveis (CPF, agência, conta, nome completo).
- Se houver informação insuficiente, indique a limitação.
- Use linguagem simples, direta e voltada para tomada de decisão.

---

## Passo 3 — Prompt Final (unificado)

```markdown
Atue como analista de dados e experiência do cliente em um banco digital.

Sua tarefa é analisar feedbacks de clientes sobre aplicativo mobile, atendimento por chat, cartão de crédito, Pix e conta corrente para identificar temas recorrentes, sentimento dos clientes, pontos de atrito e oportunidades de melhoria.

Contexto: A análise será usada por uma equipe de Experiência do Cliente (CX) e pelo time de Produto Digital para priorizar melhorias nos canais digitais, reduzir reclamações recorrentes e otimizar o atendimento. O foco é transformar comentários soltos em insights claros e acionáveis.

Dados disponíveis: Serão fornecidos comentários com data, canal de atendimento (chat, telefone, e-mail), texto do feedback, produto citado (app, cartão, Pix, conta), nota de satisfação (1 a 5) e segmento do cliente (PF ou PJ).

Instruções de análise:
1. Classifique os feedbacks por tema, sentimento (positivo, neutro, negativo), urgência (baixa, média, alta) e produto citado.
2. Identifique os principais padrões, problemas recorrentes, elogios e oportunidades de melhoria.
3. Aponte evidências nos dados fornecidos, usando exemplos curtos e anônimos de comentários.
4. Sugira ações práticas para a equipe de CX e para o time responsável pelos canais digitais.
5. Destaque as 3 prioridades mais urgentes com base no volume de reclamações e no impacto na experiência do cliente.

Formato da resposta:
- Um resumo executivo com até 5 linhas.
- Uma tabela com as colunas: Tema | Sentimento | Urgência | Exemplo de Feedback (anônimo) | Ação Sugerida.
- Uma lista final com as 3 prioridades mais importantes em ordem de urgência.

Restrições:
- Use apenas os dados fornecidos.
- Não invente números, causas ou conclusões.
- Não exponha dados pessoais ou sensíveis (CPF, agência, conta, nome completo).
- Informe limitações quando os dados não forem suficientes para conclusões.
- Use linguagem simples, direta e voltada para tomada de decisão.
```

---

## 📁 Como entregar

Este desafio foi publicado no GitHub:

🔗 **Repositório:** https://github.com/marcuslinhares/ia-mentor-carreira/blob/main/desafio-insights-feedback.md
