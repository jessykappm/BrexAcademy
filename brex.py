import streamlit as st

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home","Guia Básico", "VS","Temporada 1", "Temporada 2", "Regras"])


with tab0:
    st.title("BREX Academy")
  
    col1, col2= st.columns(2, gap="large")
with col1:
    linha_a = "Bem-vindo ao hub de informações da BREX!"
    linha_b = "Aqui você encontra informaçãoes e tutoriais para melhorar sua performance no jogo."
    linha_c = "Navegue pelas abas, e encontre o que precisa."
    st.subheader(linha_a)
    st.write(linha_b)
    st.write(linha_c)
 
with col2:
    st.image("imagens/logo.png")
    
with tab1:
    tanques = "Tanques: Têm vantagem contra aeronaves. São ideais para a linha de frente, absorvendo dano."
    misseis = "Mísseis: Têm vantagem contra aeronaves, mas recebem mais dano de tanques."
    aeronaves = "Aeronaves: Têm vantagem contra tanques, mas recebem mais dano de mísseis."
    bonus_tipo = "Bônus por tipo: Tente ter cinco heróis do mesmo tipo (tanque, míssil ou aeronave) para o maior bônus possível de ataque e defesa. Se não for possível, use três ou quatro do mesmo tipo para obter bônus menores de +5'%' ou +15%."
    comb_tipo = "Combinação por tipo: Se você não puder ter um esquadrão homogêneo, concentre-se em ter um bom equilíbrio entre ataque, defesa e suporte. Uma combinação de três heróis de um tipo e dois de outro já concede um bônus de +10%."
    est_ataque = "Estratégia de ataque: Em combates contra outros jogadores, considere formar seu esquadrão com base no tipo de tropa que você espera encontrar. Se muitos inimigos usam tanques, por exemplo, uma formação de aeronaves seria vantajosa."
    heroi_ur = "Priorize heróis lendários (UR): Embora sejam difíceis de conseguir, são os mais poderosos. Paticipe de eventos como o 'Mercado Brilhante', para conseguir gratuitamente."
    frag_her = "Use fragmentos: Use fragmentos para aumentar as estrelas dos heróis, melhorando seus atributos."
    arma_excl = "Use armas exclusivas: Desbloquear armas exclusivas para heróis lendários aumenta consideravelmente a força."
    with st.expander("Formação dos esquadrões"):
        st.subheader("Estratégia de formação e evolução de heróis-Hero training and evolution strategy")
        st.write(misseis)
        st.write(aeronaves)
        st.write(bonus_tipo)
        st.write(comb_tipo)
        st.write(est_ataque)
        st.write(heroi_ur)
        st.write(frag_her)
        st.write(arma_excl)
        st.video("https://youtu.be/ccrW8UV1nXk")
   
    texto_geral= "A evolução é feita por meio de aprimoramento em múltiplos de 10 (10, 20, 30, etc.) para desbloquear bônus, utilizando itens como cerâmica, minério e ouro, e alcançando o nível 40 em armas lendárias para desbloquear armas míticas. "
    titulo_1 = "Priorização de equipamentos"
    herois_ataque = "Foque em Canhões para aumentar o dano e a taxa de acerto crítico. O Chip também é uma boa opção para aumentar o ataque e resistência contra todos os tipos de dano."
    herois_defesa = "Priorize Armadura para aumentar a defesa e resistência a danos físicos, e Radar para defesa e resistência a dano de energia"
    titulo_2 = "Como evoluir as armas"
    evol_1 = "Alcance o Nível 40 em Armas Lendárias: Isso desbloqueia a capacidade de construir equipamentos com bônus extras."
    evol_2 = "Construa Equipamentos Míticos: Armas míticas são a evolução das lendárias e são obtidas após o nível 40, quando é possível preencher as 'bolinhas' amarelas."
    evol_3 = "Foque em Múltiplos de 10: Ao aprimorar os equipamentos, concentre-se em aumentar o nível em múltiplos de 10 (10, 20, 30...) para obter bônus de ataque ou dano crítico."
    evol_4 = "Os itens para aprimoramento das armas são preciosos. Participe de eventos como 'Batalha do Deserto' e 'Batalha de Inverno', para conseguir itens na loja de honra."
    
    with st.expander("Como evoluir as armas dos heróis"):
        st.subheader("Estratégia de evolução")
        st.write(texto_geral)
        st.write(titulo_1)
        st.write(herois_ataque)
        st.write(herois_defesa)
        st.write(titulo_2)
        st.write(evol_1)
        st.write(evol_2)
        st.write(evol_3)
        st.write(evol_4)
        st.video("https://www.youtube.com/watch?v=rzH0__US7Pg")
       
    with st.expander("Guia de construçãoes"):
        st.write("Aprimore a Sede: Esta é a prioridade máxima, pois desbloqueia todos os outros edifícios, novas unidades e funcionalidades.")
        st.write("Acompanhe os requisitos: Mantenha outras construções (como o muro e o centro de tecnologia) atualizadas para atender aos requisitos mínimos da Sede em cada nível.")
        st.write("Otimize a pesquisa: Invista em pesquisas que reduzam o custo de recursos e acelerem a construção e treinamento, principalmente as que estão no meio da árvore de pesquisa.")
        st.write("Use a profissão de engenheiro: Se escolher essa profissão, foque em diminuir o custo de recursos para construção e acelerar a pesquisa. O engenheiro também aumenta o suporte para a construção cooperativa e a produção rápida de recursos.")
        st.write("Use buff de aceleração de construção do ministério e itens da profissão de engenheiro, para reduzir o tempo das contruções.")
        st.image("imagens/sede_up.jpg")
   
    with st.expander("Pesquisa de tecnologia"):
        st.video("https://www.youtube.com/watch?v=PE3JzjPH118")
    with st.expander("Treinamento de tropas"):
        st.subheader("Treinamento cascata:")
        st.video("https://youtu.be/oeWlkY_FqhI")

with tab2:
    st.subheader("Otimizando a pontuação do VS")
    with st.expander("Dia 1"):
        st.video("https://www.youtube.com/watch?v=GtRncMAagUI&list=PL5Ct1GWEEkBQ-IlLsynppZWCiIgFupQ8e&index=2")
    with st.expander("Dia 2"):
        st.video("https://www.youtube.com/watch?v=lGYb1a18cWc&list=PL5Ct1GWEEkBQ-IlLsynppZWCiIgFupQ8e&index=3")
    with st.expander("Dia 3"):
        st.video("https://www.youtube.com/watch?v=vCfTeXXD2LM&list=PL5Ct1GWEEkBQ-IlLsynppZWCiIgFupQ8e&index=4")
    with st.expander("Dia 4"):
        st.video("https://www.youtube.com/watch?v=YBExtxTeY30&list=PL5Ct1GWEEkBQ-IlLsynppZWCiIgFupQ8e&index=5")
    with st.expander("Dia 5"):
        st.video("https://www.youtube.com/watch?v=gL6yxC6yVeY&list=PL5Ct1GWEEkBQ-IlLsynppZWCiIgFupQ8e&index=5&pp=iAQB")
    with st.expander("Dia 6"):
        st.video("https://www.youtube.com/watch?v=u3ChgoXPe_g&list=PL5Ct1GWEEkBQ-IlLsynppZWCiIgFupQ8e&index=6")
    
with tab3:
    with st.expander("Principais mudanças na primeira temorada"):
        st.write("Mapa e conquistas: Um novo mapa foi adicionado, com novas áreas a serem conquistadas.")
        st.write("Novos recursos e vírus: A temporada introduz um vírus, que requer proteínas imunes para curar.")
        st.write("Hospitais de emergência: Adicionados hospitais específicos para tratar tropas infectadas.")
        st.write("Novas profissões: Foram incluídas as profissões de engenheiro e líder de guerra.")
        st.video("https://youtu.be/TGy_DKJukN8?list=PL5Ct1GWEEkBRFpjPIJigLPVyWue4cORSt")

    with st.expander("Tutorial fazenda de soro"):
        st.image("imagens/resistencia.jpeg")
    
    with st.expander("Tutorial construção cooperativa"):
        st.image("imagens/constr_coop.jpg")

    with st.expander("Mapa de ocupação de território"):
        st.image("imagens/mapa_mundo.jpeg")
        st.image("imagens/mapa_brex.jpeg")
        
    with st.expander("Guia de Estratégia para Expedição na Zona de Guerra"):
        st.link_button("Guia de estratégia","https://firstfungroup.zendesk.com/hc/pt-br/articles/44710611930003--Guia-de-Estrat%C3%A9gia-para-Expedi%C3%A7%C3%A3o-na-Zona-de-Guerra")
    

with tab4: #Temporada 2
    with st.expander("Recursos e Construções"):
        st.video("https://www.youtube.com/watch?v=GQ0g0AYMfyw")
    with st.expander("Nevasca e Captura de cidades"):
        st.video("https://www.youtube.com/watch?v=ITvQZeeEo_I")
    with st.expander("Solo raro e Violet UR"):
        st.video("https://www.youtube.com/watch?v=DyCnNgE8Kbw")
    
with tab5:
    with st.expander("Regras gerais"):
        st.write("Motivos de expulsão:")
        st.write("Ficar dois dias offline, sem aviso prévio.")
        st.write("Não seguir o guia de boa conduta da aliança.")
    
    with st.expander("É proibido"):
        st.write("atacar jogadores que fazem parte de qualquer aliança.")
        st.write("Saquear caminhões e tarefas no nosso servidor e no servidor aliado 1593. Veja a imagem e o vídeo abaixo sobre como ir para outro servidor.")
        st.image("imagens/saque.jpg")
        st.video("https://www.youtube.com/watch?v=Zd_-9k5gchU")
    
    
    with st.expander("Guia de boa conduta"):
        st.write("Faltar com respeito com qualquer jogador.")
        st.write("Tópicos proibidos no chat da aliança: política, religião e qualquer assunto sensível.")