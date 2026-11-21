import re
import sys
from collections import Counter


def analisar_log(caminho_arquivo: str) -> None:
    padrao = re.compile(
        r"^(?P<data>\S+\s+\S+)\s+\[(?P<nivel>INFO|WARN|ERROR)\]\s+(?P<mensagem>.+)$"
    )
    padrao_codigo = re.compile(r"\((COD-\d+)\)")

    contagem_niveis = Counter()
    contagem_codigos = Counter()
    erros_detalhados = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                correspondencia = padrao.match(linha.strip())
                if not correspondencia:
                    continue

                nivel = correspondencia.group("nivel")
                mensagem = correspondencia.group("mensagem")
                data = correspondencia.group("data")

                contagem_niveis[nivel] += 1

                if nivel in ("ERROR", "WARN"):
                    erros_detalhados.append((numero_linha, data, nivel, mensagem))
                    cod = padrao_codigo.search(mensagem)
                    if cod:
                        contagem_codigos[cod.group(1)] += 1

    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_arquivo}' nao encontrado.")
        sys.exit(1)

    print("=== RESUMO DE OCORRENCIAS ===")
    for nivel in ("ERROR", "WARN", "INFO"):
        print(f"- {nivel}: {contagem_niveis[nivel]}")

    if contagem_codigos:
        print("\n=== CODIGOS MAIS RECORRENTES ===")
        for codigo, total in contagem_codigos.most_common():
            print(f"- {codigo}: {total} ocorrencia(s)")

    if erros_detalhados:
        print("\n=== DETALHAMENTO DE ALERTAS E ERROS ===")
        for linha, data, nivel, msg in erros_detalhados:
            print(f"[Linha {linha}] {data} | {nivel} -> {msg}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analisador.py <caminho_do_arquivo.log>")
        sys.exit(1)

    analisar_log(sys.argv[1])