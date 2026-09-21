import pandas as pd
import matplotlib.pyplot as plt

# Caminho do CSV extraído do ZIP
caminho = r"/mnt/data/AtividadeIDH_extracted/AtividadeIDH/Tabela4.csv"

# O arquivo usa ; como separador e vírgula como decimal.
# A primeira linha do arquivo é um título; a segunda contém os nomes das colunas.
df = pd.read_csv(caminho, sep=";", decimal=",", encoding="latin1", header=1)

# Remove colunas totalmente vazias e espaços dos nomes
df = df.dropna(axis=1, how="all")
df.columns = [str(c).strip() for c in df.columns]

df.head()

# 1) Limpeza e conversão das colunas de anos
anos = [c for c in df.columns if str(c).isdigit()]
df[anos] = df[anos].apply(pd.to_numeric, errors="coerce")

print("Anos disponíveis:", anos)
print("\nColunas:", df.columns.tolist())

# 2) Estados ordenados pelo maior IDH em 2024
df_ordenado = df.sort_values("2024", ascending=False)

df_ordenado[["Sigla", "Estado", "2024"]]

# 3) Qual estado teve a maior melhora entre 1991 e 2024?
df["Melhora_1991_2024"] = df["2024"] - df["1991"]

maior_melhora = df.loc[df["Melhora_1991_2024"].idxmax()]

print(
    f"Estado com maior melhora: {maior_melhora['Estado']} ({maior_melhora['Sigla']})"
)
print(f"IDH em 1991: {maior_melhora['1991']:.3f}")
print(f"IDH em 2024: {maior_melhora['2024']:.3f}")
print(f"Melhora: {maior_melhora['Melhora_1991_2024']:.3f}")

# 4) Existe algum estado em que o IDH piorou?
pioraram = df[df["Melhora_1991_2024"] < 0][
    ["Sigla", "Estado", "1991", "2024", "Melhora_1991_2024"]
]

if pioraram.empty:
    print("Não. Nenhum estado apresentou piora do IDH entre 1991 e 2024.")
else:
    display(pioraram)

# 5) Transformação do formato largo para o formato longo (melt)
anos = [c for c in df.columns if str(c).isdigit()]
print(anos)

id_vars = [c for c in df.columns if c not in anos]
df_longo = df.melt(
    id_vars=id_vars,
    value_vars=anos,
    var_name="Ano",
    value_name="IDH",
)

df_longo["Ano"] = df_longo["Ano"].astype(int)
df_longo["IDH"] = pd.to_numeric(df_longo["IDH"], errors="coerce")

df_longo.head()

# 6) Plotar apenas Minas Gerais
mg = df_longo[df_longo["Sigla"] == "MG"].sort_values("Ano")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(mg["Ano"], mg["IDH"], marker="o", linewidth=2, label="MG")

ax.set_title("Evolução do IDH — Minas Gerais (1991–2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
plt.show()

# 7) Evolução do IDH de cada estado
fig, ax = plt.subplots(figsize=(12, 7))

for sigla, grupo in df_longo.groupby("Sigla"):
    grupo = grupo.sort_values("Ano")
    ax.plot(
        grupo["Ano"],
        grupo["IDH"],
        marker="o",
        markersize=3,
        linewidth=1.5,
        label=sigla
    )

ax.set_title("Evolução do IDH por estado (1991–2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)
ax.legend(ncol=3, bbox_to_anchor=(1.02, 1), loc="upper left", title="UF")
fig.tight_layout()
plt.show()