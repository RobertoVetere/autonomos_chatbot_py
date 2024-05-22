import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv()
find_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

#== Crear nuestro asistente ==

# personal_assistant = client.beta.assistants.create(
#     name="Scort-GPT",
#     instructions= """Eres una scort que ofrece dos servicios de masaje con final feliz, 
#     uno por 60 euros media hora y otro por 100 euros una hora completa, 
#     no haces rebajas en el precio y no haces mas servicios que esos, 
#     habla con acento de colombia y agenda una cita con el cliente, respuestas cortas y muy seductoras
#     si el cliente divaga, corta amablemente la conversación invitandole a agendar una cita""",
#     model = model
# )
# assistant_id = personal_assistant.id
# print(assistant_id)
#====Thread====

# thread = client.beta.threads.create(
#     messages =[
#         {
#             "role": "user",
#             "content": "Hola, me podrías informar sobre tus servicios?"
#         }
#     ]
# )
# thread_id = thread.id
# print(thread_id)


#hardcode our ids
assistant_id = asst_GRDnTbCnNZH7hGFavyrwpmz5
thread_id = thread_EUfjHTefH8is4ZaqQECSzSZH