import pickle
import streamlit as st
from PIL import Image

rf_model = pickle.load(open('Cancer_model.pkl','rb'))

def prediction(inputs):
    prediction = rf_model.predict([inputs])

    if prediction == 0:
        pred = "Benign"
    else:
        pred = "Malignant"

def main():
    html_temp = """
    <div style = "background color:#5F4B8BFF; padding:10px">
    <h1 style="color:#E69A8DFF; text-align:center;">Breast Cancer Prediction</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    image = Image.open('BreastCancerAwareness.jpg')
    st.image(image)

    activities = ['About Breast Cancer','Symptoms']
    option = st.sidebar.selectbox('Menu', activities)


    if option =='About Breast Cancer':
        html_temp_about = """
        Breast cancer is a type of cancer that starts in the breast. Cancer starts when cells begin to grow out of control. (To learn more about how cancers start and spread, see What Is Cancer?)
        Breast cancer cells usually form a tumor that can often be seen on an x-ray or felt as a lump. Breast cancer occurs almost entirely in women, but men can get breast cancer, too.
        It’s important to understand that most breast lumps are benign and not cancer (malignant). Non-cancerous breast tumors are abnormal growths, but they do not spread outside of the breast. They are not life threatening, but some types of benign breast lumps can increase a woman's risk of getting breast cancer. Any breast lump or change needs to be checked by a health care professional to determine if it is benign or malignant (cancer) and if it might affect your future cancer risk. See Non-cancerous Breast Conditions to learn more.
        Breast cancers can start from different parts of the breast.
        Most breast cancers begin in the ducts that carry milk to the nipple (ductal cancers)
        Some start in the glands that make breast milk (lobular cancers)
        There are also other types of breast cancer that are less common like phyllodes tumor and angiosarcoma
        A small number of cancers start in other tissues in the breast. These cancers are called sarcomas and lymphomas and are not really thought of as breast cancers.
        Although many types of breast cancer can cause a lump in the breast, not all do. See Breast Cancer Signs and Symptoms to learn what you should watch for and report to a health care provider.
        Many breast cancers are also found on screening mammograms, which can detect cancers at an earlier stage, often before they can be felt, and before symptoms develop.
        """
        st.sidebar.markdown(html_temp_about, unsafe_allow_html=True)

    elif option=='Symptoms':
        html_temp_symp = """
                Some major symptoms are:
                1) New lump in the breast or underarm(armpit)
                2) Thickening or swelling of part of the breast.
                3) Irritation or dimpling of breast skin.
                4) Redness or flaky skin in the nipple or pain in the nipple area.
                5) Nipple Discharge other than breast milk, including blood.
                6) Any change in the size or shape of the breast.
                7) Pain in any area of the breast.
                For a detailed explaination on the above symptoms, please visit cdc.gov.in
                """
        st.sidebar.markdown(html_temp_symp, unsafe_allow_html=True)


    mean_radius = st.text_input('Enter mean radius')
    mean_texture = st.text_input('Enter mean texture')
    mean_perimeter = st.text_input('Enter mean perimeter')
    mean_area = st.text_input('Enter mean area')
    mean_smoothness = st.text_input('Enter mean smoothness')
    mean_compactness = st.text_input('Enter mean compactness')
    mean_concavity = st.text_input('Enter mean concativtity')
    mean_concavepoints = st.text_input('Enter mean concave points')
    mean_symmetry = st.text_input('Enter symmetry mean')
    mean_fractal_dimension = st.text_input('Enter mean fractal dimension')



    inputs = [mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concavepoints,mean_symmetry,mean_fractal_dimension]
    result = ""

    st.subheader("Get Report")

    if st.button('CALCULATE'):
        st.write("The following is a **report** based on your inputs")

        result = prediction(inputs)
        st.success('Your tumor is {}'.format(result))

    else:
        pass

if __name__ == '__main__':
    main()
