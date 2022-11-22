import streamlit as st

from lookup_search import Lookup

header = st.container()
intro = st.container()
notes = st.container()
sku = st.container()
variables = st.container()
results = st.container()
notes2 = st.container()

with header:
    st.title('It Goes Forward')
    st.markdown('This interactive tool demonstrates the possible cost and CO2 savings based on various parameters that match your company. Interested in a tailor-made forecast on your data? Contact us!')

with intro:
    st.image('Picture1.png')

with notes:
    st.header('Variables explained')
    st.markdown('**1. Applied discount:** The discount offered to potential buyers on the to-be-returned item')
    st.markdown('**2. Returner-buyer matching period:** The number of days in which a to-be-returned product is offered for sale. When sold within this period, the matching period ends. When not sold within this period, the return is returned to the warehouse a.k.a. the ordinary way.')
    st.markdown('**3. Returner-buyer hand-in period:** The number of days in which the returner is asked to hand-in the sold return. When not handed in on time, the retailer can choose to send an item from the warehouse.')

with sku:
    sku.header('Select product...')
    MM, HH, HL, LH, LL = st.columns(5)
    MM.image('A.png')
    MM.image('ProdA.png')
    HH.image('B.png')
    HH.image('ProdB.png')
    HL.image('C.png')
    HL.image('ProdC.png')
    LH.image('D.png')
    LH.image('ProdD.png')
    LL.image('E.png')
    LL.image('ProdE.png')
    products = ['A', 'B', 'C', 'D', 'E']
    select = st.radio('Product', products, index=0)

with variables:
    st.header('Variables')
    click = st.checkbox('Optimize for CO2 instead of costs')
    if click:
        inleg = st.number_input(label='The additional Euro amount you are willing to pay, per article, to optimise for CO2 emission',value=0, max_value=5, min_value=0)
        co2_korting = Lookup.demo_lookupco2_discount(inleg, select)
        show_co2_korting = st.number_input(label='Applied discount (percentage) for CO2 optimisation',min_value=(co2_korting * 100), max_value=(co2_korting * 100))
    else:
        fixed = st.number_input(label='Applied discount (percentage)', value=7, max_value=100, min_value=1)
    window_sell = st.slider(label='Returner-buyer matching period', min_value=1, max_value=6, value=3, step=1)
    window_del = st.slider(label='Return hand-in period (days)', min_value=1, max_value=9, value=7, step=1)

with results:
    st.header('Results')
    st.markdown('Results for selected SKU given **2 month** selling period')
    if click:
        [res_ass, res_sav, res_co2, fract_ret, discount, savings, co2_korting] = Lookup.demo_lookupco2(inleg, window_sell, window_del, select)
    else:
        [res_ass, res_sav, res_co2, fract_ret, savings] = Lookup.demo_lookup(fixed, window_sell, window_del, select)
    txt, res, eur, co2 = st.columns(4)
    #txt.markdown('**Total number of returns processed in the IGF-method**')
    #res.markdown('**% of returns sold through IGF**')
    txt.image('logo_ret.png')
    res.image('logo_ret%.png')
    eur.image('logo_sav.png')
    co2.image('logo_co2.png')
    txt, res, eur, co2 = st.columns(4)
    #res.title(str(round(res_ass)))
    #txt.markdown('**% of returns sold through IGF**')
    txt.title(str(round(res_ass)))
    res.title(str(round(fract_ret, 1)) + ' %')
    #eur, co2 = st.columns(2)

    eur.title(str(round(res_sav, 1)) + ' %')
    eur.markdown('% of total return handling and shipment costs')
    #eur.markdown('€'+str(round(savings,2)))
    co2.title(str(round(res_co2)))
    co2.markdown('total CO2 reduction')

with notes2:
    st.header('Notes')
    st.markdown('1. The displayed costs and CO2 savings does not include the depreciation savings potential. Making the cost and CO2 saving potential of the IGF-approach even bigger.')
    st.markdown(
        '2. The database of this demo contains all sales, return and shipment data from May 2017 to May 2019 from a Dutch fashion retailer. As a consequence, the assumption is made that your customers have the same behaviour as their customers. For example, on how long they take to hand-in a return at a drop-off point.')
    st.markdown('3. The database does not contain the real-life reaction of consumers to the IGF way of returning and buying. This is inherent to the fact that IGF’s method is not applied in real-life yet. Still the database is fully useful, allowing us to mimic customer behaviour in our model.')
    st.markdown('4. Price elasticity is assumed to be equal among all customers')
    st.markdown('5. For the sake of simplicity, the discount level applied in this demo stays the same throughout the whole returner-buyer matching period. ')
    st.markdown(
        '6. The results serve as an indication for potential CO2 and cost savings for your company based on simulations. The content of this demo is provided for information purposes only.')