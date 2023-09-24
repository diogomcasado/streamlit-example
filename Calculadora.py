import streamlit as st

st.header('Calculadora de comissões: ', divider='rainbow')

valor = st.number_input(label='Preço a vender: ')

genre = st.radio(
    "Plataforma de venda:",
    ["Chrono24", "Ebay", "Vinted", "Outro"],
    captions = ["6.5%", "15%", "0%"])

if genre == 'Chrono24':
    comissao = valor * (6.5/100)
    st.write('Valor comissao = ', comissao,'€')
elif genre == 'Ebay':
    comissao = valor * (15/100)
    st.write('Valor comissao = ', comissao,'€')
elif genre == 'Vinted':
    comissao = 0
    st.write('Valor comissao = ', comissao,'€')
elif genre == 'Outro':
    comissao_valor = st.number_input(label='Comissao (%): ')
    comissao = valor * (comissao_valor/100)
    st.write('Valor comissao = ', comissao,'€')


final = valor - comissao

st.write('Preço final = ',final,'€')


# labels = 'Comissão', 'Final'
# sizes = [comissao, final]
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, 
#         autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)
