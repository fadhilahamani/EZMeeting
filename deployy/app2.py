import streamlit as st
import pandas as pd
from PIL import Image
import gensim
from gensim.models import Word2Vec
import numpy as np


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background-image: url("https://wallpapercave.com/wp/wp7959367.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# input user
st.header("Ez Meeting Information")
df = pd.read_csv('baru.csv')
model_2 = Word2Vec.load('model_2fix.model')
data = pd.read_csv('df_new1.csv')
def input_text(text1, text2, text3):
  list_new =[]
  columns_new= []
  count_word_1 = []
  count_word_2 = []
  count_word_3 = []
  count_word_4 = []
  count_word_5 = []
  count_word_6 = []
  count_word_7 = []
  count_word_8 = []
  count_word_9 = []
  count_word_10 = []
  count_word_11 = []
  count_word_12 = []
  count_word_13 = []
  count_word_14 = []
  count_word_15 = []

  try:
    # Jika bisa semuanya
    res_1 = model_2.wv.most_similar(text1)   
    res_2 = model_2.wv.most_similar(text2)
    res_3 = model_2.wv.most_similar(text3)
    df_res_1 = pd.DataFrame(res_1)
    df_res_2 = pd.DataFrame(res_2)
    df_res_3 = pd.DataFrame(res_3)
    df_result_1 = pd.concat([df_res_1, df_res_2, df_res_3], axis=0).reset_index(drop=True)
    for item in df_result_1[0].unique():
      list_new.append(item)
    for i in range(len(data)):
      count_word_1.append(data['clean stopword'][i].count(list_new[0]))
      count_word_2.append(data['clean stopword'][i].count(list_new[1]))
      count_word_3.append(data['clean stopword'][i].count(list_new[2]))
      count_word_4.append(data['clean stopword'][i].count(list_new[3]))
      count_word_5.append(data['clean stopword'][i].count(list_new[4]))
      count_word_6.append(data['clean stopword'][i].count(list_new[5]))
      count_word_7.append(data['clean stopword'][i].count(list_new[6]))
      count_word_8.append(data['clean stopword'][i].count(list_new[7]))
      count_word_9.append(data['clean stopword'][i].count(list_new[8]))
      count_word_10.append(data['clean stopword'][i].count(list_new[9]))
      count_word_11.append(data['clean stopword'][i].count(list_new[10]))
      count_word_12.append(data['clean stopword'][i].count(list_new[11]))
      count_word_13.append(data['clean stopword'][i].count(list_new[12]))
      count_word_14.append(data['clean stopword'][i].count(list_new[13]))
      count_word_15.append(data['clean stopword'][i].count(list_new[14]))
    data['count_word_1'] = count_word_1
    data['count_word_2'] = count_word_2
    data['count_word_3'] = count_word_3
    data['count_word_4'] = count_word_4
    data['count_word_5'] = count_word_5
    data['count_word_6'] = count_word_6
    data['count_word_7'] = count_word_7
    data['count_word_8'] = count_word_8
    data['count_word_9'] = count_word_9
    data['count_word_10'] = count_word_10
    data['count_word_11'] = count_word_11
    data['count_word_12'] = count_word_12
    data['count_word_13'] = count_word_13
    data['count_word_14'] = count_word_14
    data['count_word_15'] = count_word_15
    data['sum_count_word'] = data.iloc[:, 11:20].sum(axis=1)
    data_1 = data[data['sum_count_word'] != 0]
    data_1 = data_1.sort_values("sum_count_word", ascending=False)[['Title', 'Website', 'Phone Number', 'Rating', 'Harga', 'Kapasitas', 'Size Room', 'Address', 'Kabupaten', 'sum_count_word']]
    return data_1

  except:
    try:
      # Hanya 2 dan 3
      res_2 = model_2.wv.most_similar(text2)
      res_3 = model_2.wv.most_similar(text3)
      df_res_2 = pd.DataFrame(res_2)
      df_res_3 = pd.DataFrame(res_3)
      df_result_2 = pd.concat([df_res_2, df_res_3], axis=0).reset_index(drop=True)
      for item in df_result_2[0].unique():
        list_new.append(item)
      for i in range(len(data)):
        count_word_1.append(data['clean stopword'][i].count(list_new[0]))
        count_word_2.append(data['clean stopword'][i].count(list_new[1]))
        count_word_3.append(data['clean stopword'][i].count(list_new[2]))
        count_word_4.append(data['clean stopword'][i].count(list_new[3]))
        count_word_5.append(data['clean stopword'][i].count(list_new[4]))
        count_word_6.append(data['clean stopword'][i].count(list_new[5]))
        count_word_7.append(data['clean stopword'][i].count(list_new[6]))
        count_word_8.append(data['clean stopword'][i].count(list_new[7]))
        count_word_9.append(data['clean stopword'][i].count(list_new[8]))
        count_word_10.append(data['clean stopword'][i].count(list_new[9]))
      data['count_word_1'] = count_word_1
      data['count_word_2'] = count_word_2
      data['count_word_3'] = count_word_3
      data['count_word_4'] = count_word_4
      data['count_word_5'] = count_word_5
      data['count_word_6'] = count_word_6
      data['count_word_7'] = count_word_7
      data['count_word_8'] = count_word_8
      data['count_word_9'] = count_word_9
      data['count_word_10'] = count_word_10
      data['sum_count_word'] = data.iloc[:,11:15].sum(axis=1)
      data_2 = data[data['sum_count_word'] != 0]
      data_2 = data_2.sort_values("sum_count_word", ascending=False)[['Title', 'Website', 'Phone Number', 'Rating', 'Harga', 'Kapasitas', 'Size Room', 'Address', 'Kabupaten', 'sum_count_word']]
      return data_2

    except:
      try:
        # Hanya 3 
        res_3 = model_2.wv.most_similar(text3)
        df_result_3 = pd.DataFrame(res_3).reset_index(drop=True)
        for item in df_result_3[0].unique():
          list_new.append(item)
        for i in range(len(data)):
          count_word_1.append(data['clean stopword'][i].count(list_new[0]))
          count_word_2.append(data['clean stopword'][i].count(list_new[1]))
          count_word_3.append(data['clean stopword'][i].count(list_new[2]))
          count_word_4.append(data['clean stopword'][i].count(list_new[3]))
          count_word_5.append(data['clean stopword'][i].count(list_new[4]))
        data['count_word_1'] = count_word_1
        data['count_word_2'] = count_word_2
        data['count_word_3'] = count_word_3
        data['count_word_4'] = count_word_4
        data['count_word_5'] = count_word_5
        data['sum_count_word'] = data.iloc[:,11:20].sum(axis=1)
        data_3 = data[data['sum_count_word'] != 0]
        data_3 = data_3.sort_values("sum_count_word", ascending=False)[['Title', 'Website', 'Phone Number', 'Rating', 'Harga', 'Kapasitas', 'Size Room', 'Address', 'Kabupaten', 'sum_count_word']]
        return data_3

      except :
        try:
          # Hanya 1 dan 2
          res_1 = model_2.wv.most_similar(text1)
          res_2 = model_2.wv.most_similar(text2)
          df_res_1 = pd.DataFrame(res_1)
          df_res_2 = pd.DataFrame(res_2)
          df_result_4 = pd.concat([df_res_1, df_res_2], axis=0).reset_index(drop=True)
          for item in df_result_4[0].unique():
            list_new.append(item)
          for i in range(len(data)):
            count_word_1.append(data['clean stopword'][i].count(list_new[0]))
            count_word_2.append(data['clean stopword'][i].count(list_new[1]))
            count_word_3.append(data['clean stopword'][i].count(list_new[2]))
            count_word_4.append(data['clean stopword'][i].count(list_new[3]))
            count_word_5.append(data['clean stopword'][i].count(list_new[4]))
            count_word_6.append(data['clean stopword'][i].count(list_new[5]))
            count_word_7.append(data['clean stopword'][i].count(list_new[6]))
            count_word_8.append(data['clean stopword'][i].count(list_new[7]))
            count_word_9.append(data['clean stopword'][i].count(list_new[8]))
            count_word_10.append(data['clean stopword'][i].count(list_new[9]))
          data['count_word_1'] = count_word_1
          data['count_word_2'] = count_word_2
          data['count_word_3'] = count_word_3
          data['count_word_4'] = count_word_4
          data['count_word_5'] = count_word_5
          data['count_word_6'] = count_word_6
          data['count_word_7'] = count_word_7
          data['count_word_8'] = count_word_8
          data['count_word_9'] = count_word_9
          data['count_word_10'] = count_word_10
          data['sum_count_word'] = data.iloc[:,11:15].sum(axis=1)
          data_4 = data[data['sum_count_word'] != 0]
          data_4 = data_4.sort_values("sum_count_word", ascending=False)[['Title', 'Website', 'Phone Number', 'Rating', 'Harga', 'Kapasitas', 'Size Room', 'Address', 'Kabupaten', 'sum_count_word']]
          return data_4

        except:
          try:
            # Hanya res 2 
            res_2 = model_2.wv.most_similar(text2)
            df_res_2 = pd.DataFrame(res_2)
            df_result_5 = df_res_2.reset_index(drop=True)
            for item in df_result_5[0].unique():
              list_new.append(item)
            for i in range(len(data)):
              count_word_1.append(data['clean stopword'][i].count(list_new[0]))
              count_word_2.append(data['clean stopword'][i].count(list_new[1]))
              count_word_3.append(data['clean stopword'][i].count(list_new[2]))
              count_word_4.append(data['clean stopword'][i].count(list_new[3]))
              count_word_5.append(data['clean stopword'][i].count(list_new[4]))
            data['count_word_1'] = count_word_1
            data['count_word_2'] = count_word_2
            data['count_word_3'] = count_word_3
            data['count_word_4'] = count_word_4
            data['count_word_5'] = count_word_5
            data['sum_count_word'] = data.iloc[:,11:20].sum(axis=1)
            data_5 = data[data['sum_count_word'] != 0]
            data_5 = data_5.sort_values("sum_count_word", ascending=False)[['Title', 'Website', 'Phone Number', 'Rating', 'Harga', 'Kapasitas', 'Size Room', 'Address', 'Kabupaten', 'sum_count_word']]
            return data_5

          except:
            try:
              # Hanya res 1
              res_1 = model_2.wv.most_similar(text1)
              df_res_1 = pd.DataFrame(res_1)
              df_result_6 = df_res_1.reset_index(drop=True)
              for item in df_result_6[0].unique():
                list_new.append(item)
              for i in range(len(data)):
                count_word_1.append(data['clean stopword'][i].count(list_new[0]))
                count_word_2.append(data['clean stopword'][i].count(list_new[1]))
                count_word_3.append(data['clean stopword'][i].count(list_new[2]))
                count_word_4.append(data['clean stopword'][i].count(list_new[3]))
                count_word_5.append(data['clean stopword'][i].count(list_new[4]))
              data['count_word_1'] = count_word_1
              data['count_word_2'] = count_word_2
              data['count_word_3'] = count_word_3
              data['count_word_4'] = count_word_4
              data['count_word_5'] = count_word_5
              data['sum_count_word'] = data.iloc[:,11:15].sum(axis=1)
              data_6 = data[data['sum_count_word'] != 0]
              data_6 = data_6.sort_values("sum_count_word", ascending=False)[['Title', 'Website', 'Phone Number', 'Rating', 'Harga', 'Kapasitas', 'Size Room', 'Address', 'Kabupaten', 'sum_count_word']]
              return data_6

            except:
              print("Maaf Keyword Tidak ditemukan")


# st.header('REKOMENDASI BERDASARKAN BUDGET')
st.subheader('Silahkan isi sesuai dengan yang kamu mau!')
text1=''
text2=''
text3=''

with st.form('Cari'):
      col1, col2, col3 = st.columns(3)
      with col1:
          text1 = st.text_input('Kata Kunci 1')
      with col2:
          text2 = st.text_input('Kata Kunci 2')
      with col3:
          text3 = st.text_input('Kata Kunci 3')
      col1, col2, col3 = st.columns(3)
      with col1:
        daerah =  st.selectbox('Pilih Daerah : ', sorted(data['Kabupaten'].unique()))
      with col2:
        size = st.selectbox("Size Room", ('Small', 'Medium','Large'), index=1)
      with col3:
        capacity = st.number_input('capacity : ', 0, 350, value=20, step=5)
      st.subheader("Facilities")
      col1, col2, col3, col4, col5, col6 = st.columns(6)
      with col1:
        wifi = st.checkbox("Free Wifi")
      with col2:
        Projector = st.checkbox("Projector")
      with col3:
        Catering = st.checkbox("Food & Drink")
      with col4:
        WhiteBoard = st.checkbox("WhiteBoard")
      with col5:
        AV = st.checkbox("AV Equipment")
      with col6:
        Stationaries = st.checkbox("Stationaries") 
      
      df1 = input_text(text1, text2, text3)
      if st.form_submit_button('Submit'):
        st.write('Rekomendasi berdasarkan : ', text1,', ', text2,', ', text3)
        st.write('Di daerah : ', daerah,'\n','Harga : ', size,'\n','capacity: ', capacity)
        df1 = df1[df1['Kabupaten'] == daerah]
        df1 = df1[df1['Size Room'] == size]
        df1 = df1[df1['Kapasitas'] == capacity]
        # st.write(df1) 
        # st.write(df1)
        # st.write(df1)
        img = df1['Title'].to_list()
        print('img :', img)
        #st.write(img[0])
        for i in range(len(img)):
          # st.subheader('1.')
          print(i,df[df['Title']==str(img[i])]['Image'])
          res1 = Image.open('Image/'+df.loc[df['Title']==str(img[i])]['Image'].values[0])
          col1, col2 = st.columns(2)
          with col1:
            st.image(res1)
          with col2:
            st.header(str(img[i]))
            st.subheader('Website : ' + str(df.loc[df['Title']==str(img[i])]['Website'].values[0]))
            st.subheader('Rating : ' + str(df.loc[df['Title']==str(img[i])]['Rating'].values[0])+' /5')
            st.subheader('Budget : Rp. ' + str(df.loc[df['Title']==str(img[i])]['Harga'].values[0]))

            st.write('-----')
      
       
        
        
   