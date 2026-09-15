
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    media = None
    notas = {}
    erro = None

    if request.method == "POST":
        try:
            linguagens = float(request.form["linguagens"])
            humanas = float(request.form["humanas"])
            natureza = float(request.form["natureza"])
            matematica = float(request.form["matematica"])
            redacao = float(request.form["redacao"])

            notas = {
                "Linguagens": linguagens,
                "Ciências Humanas": humanas,
                "Ciências da Natureza": natureza,
                "Matemática": matematica,
                "Redação": redacao
            }

            for nome, nota in notas.items():
                if nota < 0 or nota > 1000:
                    raise ValueError(
                        f"A nota de {nome} deve estar entre 0 e 1000."
                    )

            media = sum(notas.values()) / len(notas)

        except ValueError as e:
            erro = str(e)
            media = None
            notas = {}

    return render_template(
        "index.html",
        media=media,
        notas=notas,
        erro=erro
    )


if __name__ == "__main__":
    app.run(debug=True)


