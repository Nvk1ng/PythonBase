email_tmpl = """
  Olá, %(nome)s
  tem interesse em comprar %(produto)s?
  este produto éotima para resolver %(texto)s
  clique agora em %(link)s
  apenas %(quantidade)d disponiveis!
  preco promocional %(preco).2f
  """
clientes = ["joao", "bruno", "maria"]

for cliente in clientes:
    print(
        email_tmpl % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escereve muito bem",
            "link": "https://comprarcanetas.com",
            "quantidade": 1,
            "preco": 50.5,

        }
    )
