# from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
# import numpy as np
# import streamlit as st

# def apps():
#     def classify_waste(img, uploaded_image_name):
#         # Disable scientific notation for clarity
#         np.set_printoptions(suppress=True)

#         # Load the model
#         model = load_model("keras_model.h5", compile=False)

#         # Load the labels
#         class_names = open("labels.txt", "r").readlines()

#         # Create the array of the right shape to feed into the keras model
#         data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#         # Replace this with the path to your image
#         image = img.convert("RGB")

#         # resizing the image to be at least 224x224 and then cropping from the center
#         size = (224, 224)
#         image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

#         # turn the image into a numpy array
#         image_array = np.asarray(image)

#         # Normalize the image
#         normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

#         # Load the image into the array
#         data[0] = normalized_image_array

#         # Predicts the model
#         prediction = model.predict(data)
#         index = np.argmax(prediction)
#         waste_label = class_names[index]
#         confidence_score = float(prediction[0][index])

#         return waste_label, confidence_score

#     # st.set_page_config(layout='wide')

#     st.title("Garbage Classification ")

#     input_img = st.file_uploader("Enter your image", type=['jpg', 'png', 'jpeg'])

#     if input_img is not None:
        # uploaded_image_name = input_img.name

        # if st.button("Classify"):
        #     col1, col2, col3 = st.columns([1, 1, 1])

        #     with col1:
        #         st.info("Your uploaded Image")
        #         st.image(input_img, use_column_width=True)

        #     with col2:
        #         st.info("Your Result")
        #         image_file = Image.open(input_img)
        #         waste_label, confidence_score = classify_waste(image_file, uploaded_image_name)
        #         col4, col5 = st.columns([1, 1])
        #         if waste_label == "0 cardboard\n":
        #             st.success(f"The image is classified as CARDBOARD with confidence score {confidence_score:.2f}.")
        #             with col4:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #             with col5:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #         elif waste_label == "1 glass\n":
        #             st.success(f"The image is classified as GLASS with confidence score {confidence_score:.2f}.")
        #             with col4:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #             with col5:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #         elif waste_label == "2 trash\n":
        #             st.success(f"The image is classified as TRASH with confidence score {confidence_score:.2f}.")
        #             with col4:
        #                 st.image("Bins/1.png", use_column_width=True)
        #             with col5:
        #                 st.image("Bins/1.png", use_column_width=True)
        #         elif waste_label == "3 paper\n":
        #             st.success(f"The image is classified as PAPER with confidence score {confidence_score:.2f}.")
        #             with col4:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #             with col5:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #         elif waste_label == "4 plastic\n":
        #             st.success(f"The image is classified as PLASTIC with confidence score {confidence_score:.2f}.")
        #             with col4:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #             with col5:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True) 
        #         elif waste_label == "5 metal\n":
        #             st.success(f"The image is classified as METAL with confidence score {confidence_score:.2f}.")
        #             with col4:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)
        #             with col5:
        #                 st.image("Bins/1.png", use_column_width=True)
        #                 st.image("Bins/1.png", use_column_width=True)       
        #         else:
        #             st.error("The image is not classified as any relevant class.")

        #     with col3:
        #         st.success("No OpenAI information in this version")

# if __name__ == "__main__":
#     apps()
# from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
# import numpy as np
# import streamlit as st
# import openai

# openai.api_key = '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'

# def apps():
#     def classify_waste(img, uploaded_image_name):
#         # Disable scientific notation for clarity
#         np.set_printoptions(suppress=True)

#         # Load the model
#         model = load_model("keras_model.h5", compile=False)

#         # Load the labels
#         class_names = open("labels.txt", "r").readlines()

#         # Create the array of the right shape to feed into the keras model
#         data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#         # Replace this with the path to your image
#         image = img.convert("RGB")

#         # resizing the image to be at least 224x224 and then cropping from the center
#         size = (224, 224)
#         image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

#         # turn the image into a numpy array
#         image_array = np.asarray(image)

#         # Normalize the image
#         normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

#         # Load the image into the array
#         data[0] = normalized_image_array

#         # Predicts the model
#         prediction = model.predict(data)
#         index = np.argmax(prediction)
#         waste_label = class_names[index]
#         confidence_score = float(prediction[0][index])

#         return waste_label, confidence_score

#     def generate_waste_info(waste_label):
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=f"Provide information about recycling {waste_label.strip()}.",
#             temperature=0.7,
#             max_tokens=200,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#         return response['choices'][0]['text']

#     st.title("Garbage Classification ")

#     input_img = st.file_uploader("Enter your image", type=['jpg', 'png', 'jpeg'])

#     if input_img is not None:
#         uploaded_image_name = input_img.name
                

#         if st.button("Classify"):
#             col1, col2, col3 = st.columns([1, 1, 1])

#             with col1:
#                 st.info("Your uploaded Image")
#                 st.image(input_img, use_column_width=True)

#             with col2:
#                 st.info("Your Result")
#                 image_file = Image.open(input_img)
#                 waste_label, confidence_score = classify_waste(image_file, uploaded_image_name)
#                 col4, col5 = st.columns([1, 1])
#                 if waste_label == "0 cardboard\n":
#                     st.success(f"The image is classified as CARDBOARD with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     # with col5:
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "1 glass\n":
#                     st.success(f"The image is classified as GLASS with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     # with col5:
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "2 trash\n":
#                     st.success(f"The image is classified as TRASH with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/4.png", use_column_width=True)
#                     # with col5:
#                     #     st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "3 paper\n":
#                     st.success(f"The image is classified as PAPER with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     # with col5:
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "4 plastic\n":
#                     st.success(f"The image is classified as PLASTIC with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/2.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     # with col5:
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True) 
#                 elif waste_label == "5 metal\n":
#                     st.success(f"The image is classified as METAL with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     # with col5:
#                     #     st.image("Bins/1.png", use_column_width=True)
#                     #     st.image("Bins/1.png", use_column_width=True)       
#                 else:
#                     st.error("The image is not classified as any relevant class.")

#             with col3:
#                 st.success("No OpenAI information in this version")
        

# if __name__ == "__main__":
#     apps()
# 


#latest apppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
# from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
# import numpy as np
# import streamlit as st
# import openai
# from firebase_admin import credentials, initialize_app
# from firebase_admin import firestore

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate("waste-classifier-be072-95e026b8db39.json")
# #initialize_app(cred)
# db = firestore.client()

# openai.api_key = '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'

# def apps():
#     def classify_waste(img, uploaded_image_name):
#         # Disable scientific notation for clarity
#         np.set_printoptions(suppress=True)

#         # Load the model
#         model = load_model("keras_model.h5", compile=False)

#         # Load the labels
#         class_names = open("labels.txt", "r").readlines()

#         # Create the array of the right shape to feed into the keras model
#         data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#         # Replace this with the path to your image
#         image = img.convert("RGB")

#         # resizing the image to be at least 224x224 and then cropping from the center
#         size = (224, 224)
#         image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

#         # turn the image into a numpy array
#         image_array = np.asarray(image)

#         # Normalize the image
#         normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

#         # Load the image into the array
#         data[0] = normalized_image_array

#         # Predicts the model
#         prediction = model.predict(data)
#         index = np.argmax(prediction)
#         waste_label = class_names[index]
#         confidence_score = float(prediction[0][index])

#         return waste_label, confidence_score

#     def generate_waste_info(waste_label):
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=f"Provide information about recycling {waste_label.strip()}.",
#             temperature=0.7,
#             max_tokens=200,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#         return response['choices'][0]['text']

#     st.title("Garbage Classification ")

#     # Check if user is logged in
#     if 'useremail' in st.session_state:
#         st.write(f"Logged in as: {st.session_state.useremail}")
#     else:
#         st.error("Please log in to use the application.")

#     input_img = st.file_uploader("Enter your image", type=['jpg', 'png', 'jpeg', 'gif', 'bmp', 'webp', 'avif'])

#     if input_img is not None:
#         uploaded_image_name = input_img.name

#         if st.button("Classify"):
#             col1, col2, col3 = st.columns([1, 1, 1])

#             with col1:
#                 st.info("Your uploaded Image")
#                 st.image(input_img, use_column_width=True)

#             with col2:
#                 st.info("Your Result")
#                 image_file = Image.open(input_img)
#                 waste_label, confidence_score = classify_waste(image_file, uploaded_image_name)
#                 col4, col5 = st.columns([1, 1])
#                 if waste_label == "0 cardboard\n":
#                     st.success(f"The image is classified as CARDBOARD with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "1 glass\n":
#                     st.success(f"The image is classified as GLASS with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "2 trash\n":
#                     st.success(f"The image is classified as TRASH with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/4.png", use_column_width=True)
#                 elif waste_label == "3 paper\n":
#                     st.success(f"The image is classified as PAPER with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "4 plastic\n":
#                     st.success(f"The image is classified as PLASTIC with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/2.png", use_column_width=True)
#                 elif waste_label == "5 metal\n":
#                     st.success(f"The image is classified as METAL with confidence score {confidence_score:.2f}.")
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 else:
#                     st.error("The image is not classified as any relevant class.")

#             with col3:
#                 st.success("No OpenAI information in this version")

#             # Store the feedback data in Firestore
#             if 'useremail' in st.session_state:
#                 store_feedback_data(st.session_state.useremail, uploaded_image_name, waste_label, confidence_score)

# def store_feedback_data(useremail, uploaded_image_name, waste_label, confidence_score):
#     try:
#         feedback_ref = db.collection('waste_classifier').document()
#         feedback_ref.set({
#             'useremail': useremail,
#             'uploaded_image_name': uploaded_image_name,
#             'waste_label': waste_label,
#             'confidence_score': confidence_score,
#         })
#     except Exception as e:
#         st.error(f"Error submitting feedback: {e}")

# if __name__ == "__main__":
#     apps()




#openaipinki
# from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
# import numpy as np
# import streamlit as st
# import openai
# from firebase_admin import credentials, initialize_app
# from firebase_admin import firestore

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate("waste-classifier-be072-95e026b8db39.json")
# #initialize_app(cred)
# db = firestore.client()

# openai.api_key = "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"


# def apps():
#     def classify_waste(img, uploaded_image_name):
#         # Disable scientific notation for clarity
#         np.set_printoptions(suppress=True)

#         # Load the model
#         model = load_model("keras_model.h5", compile=False)

#         # Load the labels
#         class_names = open("labels.txt", "r").readlines()

#         # Create the array of the right shape to feed into the keras model
#         data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#         # Replace this with the path to your image
#         image = img.convert("RGB")

#         # resizing the image to be at least 224x224 and then cropping from the center
#         size = (224, 224)
#         image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

#         # turn the image into a numpy array
#         image_array = np.asarray(image)

#         # Normalize the image
#         normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

#         # Load the image into the array
#         data[0] = normalized_image_array

#         # Predicts the model
#         prediction = model.predict(data)
#         index = np.argmax(prediction)
#         waste_label = class_names[index]
#         confidence_score = float(prediction[0][index])

#         return waste_label, confidence_score

#     def chat_with_gpt3(prompt):
#         try:
#             response = openai.Completion.create(
#                 engine="davinci-codex",
#                 prompt=prompt,
#                 max_tokens=100,
#                 temperature=0.7,
#                 stop=["\n", "User:"],  # Stop completion at newline or "User:" prompt
#                 echo=True,  # Echo user input in the bot response
#             )
#             return response["choices"][0]["text"]
#         except Exception as e:
#             return f"Error: {e}"

#     st.title("Garbage Classification ")

#     # Check if user is logged in
#     if "useremail" in st.session_state:
#         st.write(f"Logged in as: {st.session_state.useremail}")
#     else:
#         st.error("Please log in to use the application.")

#     input_img = st.file_uploader(
#         "Enter your image", type=["jpg", "png", "jpeg", "gif", "bmp", "webp", "avif"]
#     )

#     if input_img is not None:
#         uploaded_image_name = input_img.name

#         if st.button("Classify"):
#             col1, col2, col3 = st.columns([1, 1, 1])

#             with col1:
#                 st.info("Your uploaded Image")
#                 st.image(input_img, use_column_width=True)

#             with col2:
#                 st.info("Your Result")
#                 image_file = Image.open(input_img)
#                 waste_label, confidence_score = classify_waste(
#                     image_file, uploaded_image_name
#                 )
#                 col4, col5 = st.columns([1, 1])
#                 if waste_label == "0 cardboard\n":
#                     st.success(
#                         f"The image is classified as CARDBOARD with confidence score {confidence_score:.2f}."
#                     )
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "1 glass\n":
#                     st.success(
#                         f"The image is classified as GLASS with confidence score {confidence_score:.2f}."
#                     )
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "2 trash\n":
#                     st.success(
#                         f"The image is classified as TRASH with confidence score {confidence_score:.2f}."
#                     )
#                     with col4:
#                         st.image("Bins/4.png", use_column_width=True)
#                 elif waste_label == "3 paper\n":
#                     st.success(
#                         f"The image is classified as PAPER with confidence score {confidence_score:.2f}."
#                     )
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 elif waste_label == "4 plastic\n":
#                     st.success(
#                         f"The image is classified as PLASTIC with confidence score {confidence_score:.2f}."
#                     )
#                     with col4:
#                         st.image("Bins/2.png", use_column_width=True)
#                 elif waste_label == "5 metal\n":
#                     st.success(
#                         f"The image is classified as METAL with confidence score {confidence_score:.2f}."
#                     )
#                     with col4:
#                         st.image("Bins/1.png", use_column_width=True)
#                 else:
#                     st.error("The image is not classified as any relevant class.")

#             with col3:
#                 st.success("Bot ne kya bola")
#                 bot_response = get_waste_info(waste_label)
#                 st.text("rabart: " + bot_response)

#             # Store the feedback data in Firestore
#             if "useremail" in st.session_state:
#                 store_feedback_data(
#                     st.session_state.useremail,
#                     uploaded_image_name,
#                     waste_label,
#                     confidence_score,
#                 )


# def get_waste_info(waste_label):
#     # Generate prompt based on the waste label
#     prompt = f"Provide information about {waste_label.strip()}."
#     try:
#         response = openai.Completion.create(
#             engine="gpt-3.5-turbo-instruct",
#             prompt=prompt,
#             max_tokens=100,
#             temperature=0.7,
#             stop="\n",
#         )
#         return response["choices"][0]["text"]
#     except Exception as e:
#         return f"Error: {e}"


# def store_feedback_data(useremail, uploaded_image_name, waste_label, confidence_score):
#     try:
#         feedback_ref = db.collection("waste_classifier").document()
#         feedback_ref.set(
#             {
#                 "useremail": useremail,
#                 "uploaded_image_name": uploaded_image_name,
#                 "waste_label": waste_label,
#                 "confidence_score": confidence_score,
#             }
#         )
#     except Exception as e:
#         st.error(f"Error submitting feedback: {e}")


# if __name__ == "__main__":
#     apps()


from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import openai
from firebase_admin import firestore
from firebase_setup import initialize_firebase

firebase_app = initialize_firebase()
if firebase_app is None:
    # Firebase app already initialized, use the existing app
    pass
else:
    # Use firebase_app for Firebase operations in this module
    pass
db = firestore.client()


openai.api_key = "OPENAI_KEY"


def apps():
    def classify_waste(img, uploaded_image_name):
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        model = load_model("keras_model.h5", compile=False)

        # Load the labels
        class_names = open("labels.txt", "r").readlines()

        # Create the array of the right shape to feed into the keras model
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = img.convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        waste_label = class_names[index]
        confidence_score = float(prediction[0][index])

        return waste_label, confidence_score

    def chat_with_gpt3(prompt):
        try:
            response = openai.Completion.create(
                engine="davinci-codex",
                prompt=prompt,
                max_tokens=100,
                temperature=0.7,
                stop=["\n", "User:"],  # Stop completion at newline or "User:" prompt
                echo=True,  # Echo user input in the bot response
            )
            return response["choices"][0]["text"]
        except Exception as e:
            return f"Error: {e}"

    st.title("Garbage Classification ")

    # Check if user is logged in
    if "useremail" in st.session_state:
        st.write(f"Logged in as: {st.session_state.useremail}")
    else:
        st.error("Please log in to use the application.")

    input_img = st.file_uploader(
        "Enter your image", type=["jpg", "png", "jpeg","webp"]
    )

    if input_img is not None:
        uploaded_image_name = input_img.name

        if st.button("Classify"):
            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                st.info("Your uploaded Image")
                st.image(input_img, use_column_width=True)

            with col2:
                st.info("Your Result")
                image_file = Image.open(input_img)
                waste_label, confidence_score = classify_waste(
                    image_file, uploaded_image_name
                )
                col4, col5 = st.columns([1, 1])
                if waste_label == "0 cardboard\n":
                    st.success(
                        f"The image is classified as CARDBOARD with confidence score {confidence_score:.2f}."
                    )
                    with col4:
                        st.image("Bins/1.png", use_column_width=True)
                    info_text = "Cardboard is recyclable and can be broken down into pulp to make new paper products."
                elif waste_label == "1 glass\n":
                    st.success(
                        f"The image is classified as GLASS with confidence score {confidence_score:.2f}."
                    )
                    with col4:
                        st.image("Bins/1.png", use_column_width=True)
                    info_text = "Glass is recyclable and can be melted down to make new glass products."
                elif waste_label == "2 trash\n":
                    st.success(
                        f"The image is classified as TRASH with confidence score {confidence_score:.2f}."
                    )
                    with col4:
                        st.image("Bins/4.png", use_column_width=True)
                    info_text = "Trash items are not recyclable and should be disposed of properly."
                elif waste_label == "3 paper\n":
                    st.success(
                        f"The image is classified as PAPER with confidence score {confidence_score:.2f}."
                    )
                    with col4:
                        st.image("Bins/1.png", use_column_width=True)
                    info_text = "Paper is recyclable and can be turned into new paper products."
                elif waste_label == "4 plastic\n":
                    st.success(
                        f"The image is classified as PLASTIC with confidence score {confidence_score:.2f}."
                    )
                    with col4:
                        st.image("Bins/2.png", use_column_width=True)
                    info_text = "Plastic is recyclable, but different types require different processes. Check local recycling guidelines."
                elif waste_label == "5 metal\n":
                    st.success(
                        f"The image is classified as METAL with confidence score {confidence_score:.2f}."
                    )
                    with col4:
                        st.image("Bins/1.png", use_column_width=True)
                    info_text = "Metal is recyclable and can be melted down to make new metal products."
                else:
                    st.error("The image is not classified as any relevant class.")
                    info_text = ""

            with col3:
                st.success("Information")
                if waste_label in ["0 cardboard\n", "1 glass\n", "2 trash\n","3 paper\n","4 plastic\n","5 metal\n"]:
                    st.write(info_text)
                else:
                    bot_response = get_waste_info(waste_label)
                    st.write(bot_response)

            # Store the feedback data in Firestore
            if "useremail" in st.session_state:
                store_feedback_data(
                    st.session_state.useremail,
                    uploaded_image_name,
                    waste_label,
                    confidence_score,
                )


def get_waste_info(waste_label):
    # Generate prompt based on the waste label
    prompt = f"Provide information about {waste_label.strip()}."
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            stop="\n",
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"Error: {e}"


def store_feedback_data(useremail, uploaded_image_name, waste_label, confidence_score):
    try:
        feedback_ref = db.collection("waste_classifier").document()
        feedback_ref.set(
            {
                "useremail": useremail,
                "uploaded_image_name": uploaded_image_name,
                "waste_label": waste_label,
                "confidence_score": confidence_score,
            }
        )
    except Exception as e:
        st.error(f"Error submitting feedback: {e}")


if __name__ == "__main__":
    apps()
