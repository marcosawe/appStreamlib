import streamlit as st

class EmpresaApp:
    def __init__(self, favicon_path, company_logo_path):
        # Define o favicon
        self.favicon = favicon_path

        # Define o logotipo da empresa
        self.company_logo = company_logo_path

    def run(self):
        # Define o título da página
        st.set_page_config(page_title="Home Page", page_icon=self.favicon)

        # Cabeçalho com opções de login e registro
        self.show_header()

        # Página Inicial
        self.pagina_inicial()

    def show_header(self):
        st.title("Sua Empresa")
        # Adicione opções de login e registro aqui
        st.sidebar.header("Opções")
        if st.sidebar.button("Login"):
            self.pagina_login()
        if st.sidebar.button("Registrar"):
            self.pagina_registro()

    def pagina_inicial(self):
        st.title("A Jornada da DataInvest 2007 - Transformando Dados em Ouro")
        # Exiba o logotipo da empresa
        st.image(self.company_logo, use_column_width=True)

        st.write("""
            No agitado ano de 2007, no coração do Brasil, um grupo de entusiastas da computação e da programação uniu forças para fundar a DataInvest, uma empresa especializada em análise de dados financeiros. Eles eram jovens estudantes universitários com grandes ambições de entrar no mercado de trabalho na área de computação e programação, determinados a alcançar o sucesso acadêmico e profissional.

             Os fundadores da DataInvest eram apaixonados por tecnologia e reconheciam a crescente importância dos dados na tomada de decisões financeiras. Com essa visão, eles começaram a desenvolver um software inovador que simplificaria a análise financeira, tornando-a mais acessível e eficiente para empresas e investidores.

             Nos primeiros anos, a DataInvest enfrentou desafios significativos. Eles tiveram que aprimorar constantemente seu software para atender às demandas em constante evolução do mercado financeiro. No entanto, sua paixão e determinação os mantiveram firmes.

             À medida que a empresa crescia, eles expandiram sua equipe, atraindo talentos jovens e talentosos da área de computação. Eles mantiveram um foco contínuo na pesquisa e desenvolvimento, garantindo que sua tecnologia permanecesse na vanguarda da análise financeira.

             Em 2010, a DataInvest lançou sua primeira versão comercial do software, que rapidamente ganhou reconhecimento por sua precisão e facilidade de uso. Empresas financeiras locais e internacionais começaram a adotar a solução DataInvest para tomar decisões informadas e melhorar seu desempenho financeiro.

             Nos anos seguintes, a empresa continuou a crescer e se adaptar às mudanças do mercado, adicionando recursos avançados de inteligência artificial e aprendizado de máquina ao seu software. Isso permitiu que eles oferecessem análises preditivas ainda mais poderosas, ajudando os clientes a antecipar tendências financeiras.

             Em 2023, a DataInvest é uma empresa líder em análise de dados financeiros, com clientes em todo o mundo. Seu software é usado por bancos, fundos de investimento, empresas de consultoria e muitos outros setores financeiros. Os fundadores realizaram seu sonho de entrar no mercado de trabalho na área de computação e programação e alcançaram sucesso acadêmico e profissional, tudo graças à sua paixão pela tecnologia e ao compromisso com a inovação.

             A história da DataInvest é um testemunho de como a perseverança, a paixão pela tecnologia e o compromisso com a excelência podem transformar uma pequena startup em uma potência global na área de análise de dados financeiros.
             """)

        # Lista de projetos em colunas
        projetos = [
            {"nome": "Projeto A", "descricao": "Descrição do Projeto A"},
            {"nome": "Projeto B", "descricao": "Descrição do Projeto B"},
            {"nome": "Projeto C", "descricao": "Descrição do Projeto C"},
            {"nome": "Projeto D", "descricao": "Descrição do Projeto D"},
            {"nome": "Projeto E", "descricao": "Descrição do Projeto E"},
            {"nome": "Projeto F", "descricao": "Descrição do Projeto F"},
        ]

        col1, col2, col3 = st.columns(3)

        for i, projeto in enumerate(projetos):
            if i % 3 == 0:
                col1.write(f"**{projeto['nome']}**")
                col1.write(projeto['descricao'])
                col1.write("---")
            elif i % 3 == 1:
                col2.write(f"**{projeto['nome']}**")
                col2.write(projeto['descricao'])
                col2.write("---")
            else:
                col3.write(f"**{projeto['nome']}**")
                col3.write(projeto['descricao'])
                col3.write("---")

    def pagina_login(self):
        st.title("Login")
        # Adicione o seu formulário de login aqui

    def pagina_registro(self):
        st.title("Registrar")
        # Adicione o seu formulário de registro aqui

if __name__ == "__main__":
    app = EmpresaApp("static\\img\\Data_Invest-favicon.png", "static\\img\\Data Invest.png")
    app.run()
