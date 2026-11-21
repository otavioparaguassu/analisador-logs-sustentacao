# Analisador de Logs para Sustentação

Ferramenta de linha de comando desenvolvida em **Python** (usando apenas a biblioteca padrão) para inspecionar arquivos de log, filtrar eventos críticos e resumir falhas recorrentes durante investigações de incidentes.

## Funcionalidades
- Leitura e filtragem de registros por nível (`ERROR`, `WARN`, `INFO`).
- Agrupamento e contagem dos códigos de erro mais frequentes.
- Geração de resumo objetivo no terminal para diagnóstico rápido.

## Como executar
```bash
python3 analisador.py aplicacao.log
