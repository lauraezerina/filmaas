from flask import Flask, render_template
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import sqlite3
from pathlib import Path
def get_db_connection():
    """
    Izveido un atgriež savienojumu ar SQLite datubāzi.
    """
    # Atrod ceļu uz datubāzes failu (tas atrodas tajā pašā mapē, kur šis fails)
    db = Path(__file__).parent / "kopija.smu.db"
    # Izveido savienojumu ar SQLite datubāzi
    conn = sqlite3.connect(db)
    # Nodrošina, ka rezultāti būs pieejami kā vārdnīcas (piemēram: product["name"])
    conn.row_factory = sqlite3.Row
    # Atgriež savienojumu
    return conn
@app.route("/produkti")
def products():
    conn = get_db_connection() # Pieslēdzas datubāzei
    # Izpilda SQL vaicājumu, kas atlasa visus produktus
    products = conn.execute("SELECT * FROM Produkts").fetchall()
    conn.close() # Aizver savienojumu ar datubāzi
    # Atgriežam HTML veidni "products.html", padodot produktus veidnei
    return render_template("products.html", products=products)

@app.route("/produkti/<int:product_id>")
def products_show(product_id):
    conn = get_db_connection() # Pieslēdzas datubāzei
# Izpilda SQL vaicājumu, kurš atgriež tikai vienu produktu pēc ID
    product = conn.execute(
        """
        SELECT "Produkts".*, "ipasibas"."ipasiba" AS "ipasiba", "color"."color" AS "color", "aroma"."aroma" AS "aroma"
        FROM "Produkts"
        LEFT JOIN "ipasibas" ON "Produkts"."ipasibas_id" = "ipasibas"."id"
        LEFT JOIN "color" ON "Produkts"."color_id" = "color"."id"
        LEFT JOIN "aroma" ON "Produkts"."aroma_id" = "aroma"."id"
        WHERE "Produkts"."id" = ?
    """,
        (product_id,),
    ).fetchone()

# ? ir vieta, kur tiks ievietota vērtība – šajā gadījumā product_id
    conn.close() # Aizver savienojumu ar datubāzi
# Atgriežam HTML veidni 'products_show.html', padodot konkrēto produktu veidnei
    return render_template("products_show.html", product=product)

@app.route("/")
def index():
    return render_template("index.html")
# @app.route("/produkti")
# # def products():
# #     return render_template("produkts.html")
@app.route("/par-mums")
def about():
    return render_template("about.html")
@app.route("/komanda")
def komanda():
    return render_template("komanda.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# from flask import Flask, render_template, request, redirect
# import sqlite3
# from pathlib import Path

# app = Flask(__name__)

# def get_db_connection():
#     """
#     Izveido un atgriež savienojumu ar SQLite datubāzi.
#     """
#     db = Path(__file__).parent / "kopija.smu.db"
#     conn = sqlite3.connect(db)
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/par-mums")
# def about():
#     return render_template("about.html")

# @app.route("/produkti")
# def products():
#     conn = get_db_connection()
#     products = conn.execute("SELECT * FROM Produkts").fetchall()
#     conn.close()
#     return render_template("products.html", products=products)

# @app.route("/produkti/<int:product_id>")
# def products_show(product_id):
#     conn = get_db_connection()
#     product = conn.execute(
#         """
#         SELECT "Produkts".*, 
#                "ipasibas"."ipasiba" AS "ipasiba", 
#                "color"."color" AS "color", 
#                "aroma"."aroma" AS "aroma"
#         FROM "Produkts"
#         LEFT JOIN "ipasibas" ON "Produkts"."ipasibas_id" = "ipasibas"."id"
#         LEFT JOIN "color" ON "Produkts"."color_id" = "color"."id"
#         LEFT JOIN "aroma" ON "Produkts"."aroma_id" = "aroma"."id"
#         WHERE "Produkts"."id" = ?
#         """,
#         (product_id,)
#     ).fetchone()
#     conn.close()
#     return render_template("products_show.html", product=product)

# # Palaiž Flask serveri tikai tad, ja skripts tiek izpildīts tieši
# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template
# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)
# import sqlite3
# from pathlib import Path
# def get_db_connection():
#     """
#     Izveido un atgriež savienojumu ar SQLite datubāzi.
#     """
#     # Atrod ceļu uz datubāzes failu (tas atrodas tajā pašā mapē, kur šis fails)
#     db = Path(__file__).parent / "kopija.smu.db"
#     # Izveido savienojumu ar SQLite datubāzi
#     conn = sqlite3.connect(db)
#     # Nodrošina, ka rezultāti būs pieejami kā vārdnīcas (piemēram: product["name"])
#     conn.row_factory = sqlite3.Row
#     # Atgriež savienojumu
#     return conn
# @app.route("/produkti")
# def products():
#     conn = get_db_connection() # Pieslēdzas datubāzei
#     # Izpilda SQL vaicājumu, kas atlasa visus produktus
#     products = conn.execute("SELECT * FROM Produkts").fetchall()
#     conn.close() # Aizver savienojumu ar datubāzi
#     # Atgriežam HTML veidni "products.html", padodot produktus veidnei
#     return render_template("products.html", products=products)

# @app.route("/produkti/<int:product_id>")
# def products_show(product_id):
#     conn = get_db_connection() # Pieslēdzas datubāzei
# # Izpilda SQL vaicājumu, kurš atgriež tikai vienu produktu pēc ID
#     product = conn.execute(
#         """
#         SELECT "Produkts".*, "ipasibas"."ipasiba" AS "ipasiba", "color"."color" AS "color", "aroma"."aroma" AS "aroma"
#         FROM "Produkts"
#         LEFT JOIN "ipasibas" ON "Produkts"."ipasibas_id" = "ipasibas"."id"
#         LEFT JOIN "color" ON "Produkts"."color_id" = "color"."id"
#         LEFT JOIN "aroma" ON "Produkts"."aroma_id" = "aroma"."id"
#         WHERE "Produkts"."id" = ?
#     """,
#         (product_id,),
#     ).fetchone()

# # ? ir vieta, kur tiks ievietota vērtība – šajā gadījumā product_id
#     conn.close() # Aizver savienojumu ar datubāzi
# # Atgriežam HTML veidni 'products_show.html', padodot konkrēto produktu veidnei
#     return render_template("products_show.html", product=product)

# @app.route("/")
# def index():
#     return render_template("index.html")
# # @app.route("/produkti")
# # # def products():
# # #     return render_template("produkts.html")
# @app.route("/par-mums")
# def about():
#     return render_template("about.html")

# from flask import Flask, render_template, request, redirect
# import sqlite3
# from pathlib import Path

# app = Flask(__name__)

# def get_db_connection():
#     db_path = Path(__file__).parent / "kopija.smu.db"
#     conn = sqlite3.connect(db_path)
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/par-mums")
# def about():
#     return render_template("about.html")

# @app.route("/produkti")
# def products():
#     conn = get_db_connection()
#     products = conn.execute("SELECT * FROM Produkts").fetchall()
#     conn.close()
#     return render_template("products.html", products=products)

# @app.route("/produkti/<int:product_id>")
# def products_show(product_id):
#     conn = get_db_connection()
#     product = conn.execute(
#         """
#         SELECT Produkts.*, 
#                Apraksts.saturs AS apraksts,
#                Materiali.dzija, Materiali.pildijums, Materiali.acis
#         FROM Produkts
#         LEFT JOIN Apraksts ON Produkts.apraksts_id = Apraksts.id
#         LEFT JOIN Materiali ON Produkts.materiali_id = Materiali.id
#         WHERE Produkts.id = ?
#         """, (product_id,)
#     ).fetchone()
#     conn.close()
#     return render_template("products_show.html", product=product)

# if __name__ == "__main__":
#     app.run(debug=True)