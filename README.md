# ☕ Radar de Preços — Dolce Gusto Genio S Plus (110V)

Sistema automatizado de monitoramento de preços para a **Cafeteira Arno Nescafé Dolce Gusto Genio S Plus 110V** na Amazon, com coleta diária na nuvem e visualização interativa em dashboard web.

---

## 🛠️ Arquitetura do Projeto

O projeto funciona em uma arquitetura *serverless* e gratuita utilizando o ecossistema do GitHub:

1. **Extração (`scraper.py`):** Script em Python com **Playwright** que acessa a página do produto, extrai o preço atualizado e registra a data da coleta.
2. **Armazenamento (`dados_precos.json`):** Histórico estruturado em JSON que alimenta o painel sem necessidade de banco de dados externo.
3. **Automação (`.github/workflows/atualizar.yml`):** Workflow do **GitHub Actions** agendado para executar o scraper diariamente às 09h (horário de Brasília) e realizar o *commit* automático dos novos dados.
4. **Visualização (`index.html`):** Dashboard responsivo desenvolvido com **HTML5, Tailwind CSS e Chart.js**, hospedado no **GitHub Pages**.

---

## ✨ Funcionalidades do Dashboard

- **Indicadores em tempo real:** Menor preço histórico, média de valores e diferença para a meta configurada.
- **Meta de alerta personalizável:** Banner dinâmico que sinaliza quando o valor atual atinge o preço ideal desejado.
- **Gráfico de evolução:** Comparação visual do histórico de preços ao longo do tempo com linha de referência da meta.
- **Filtros e registros:** Filtro por intervalo de datas, histórico detalhado e opção de inserção manual de cotações.

---

## 🚀 Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/lucasik21/MonitorCafeteira.git
   cd MonitorCafeteira
