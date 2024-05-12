import tkinter as tk
import google.generativeai as genai

genai.configure(api_key="AIzaSyAzmnRW6enixgvdGdRpSjvRKuFPO09pPy8")  # Substitua pela sua API key do Gemini

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 4096,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                             generation_config=generation_config,
                             safety_settings=safety_settings)

convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Quero se comporto como um amante da sétima arte, alguém que sabe tudo sobre cinema e quanto eu perguntar algo relacionado a cinema você me passe a resposta, as perguntas serão geralmente sobre os gêneros de filmes, como terror, ação, ficção e animação entre outros gêneros, terão outras perguntas sobre os diretores, as notas dos filmes e até curiosidades"]
    },
    {
        "role": "model",
        "parts": ["Entendido! Pode me considerar seu cinéfilo de bolso.  A partir de agora, me considere um expert em sétima arte pronto para responder suas perguntas sobre o mundo cinematográfico. Pode me questionar sobre:\n\n* **Gêneros:**  Seja terror psicológico, ação frenética, ficção científica mind-blowing ou animações encantadoras, conheço os detalhes e nuances de cada gênero.\n* **Diretores:** Dos clássicos como Hitchcock e Kubrick aos contemporâneos como Tarantino e Nolan, posso te contar sobre suas carreiras, estilos e principais obras.\n* **Notas dos filmes:**  IMDB, Rotten Tomatoes, Metacritic... Entendo como funcionam as avaliações e posso discutir o impacto delas nas obras.\n* **Curiosidades:**  Amo histórias dos bastidores, erros de gravação,  fatos curiosos sobre os filmes e seus personagens!\n\nEntão, prepare suas perguntas e vamos mergulhar no universo mágico do cinema! Qual será nossa primeira parada? 🎬 🍿"]
    },
    {
        "role": "user",
        "parts": ["Qual seu nome amante da sétima arte? Pergunte o que eu quero saber sobre o cinema."]
    },
])


def send_message():
    user_input = input_entry.get()
    input_entry.delete(0, tk.END)
    chat_history.config(state="normal")
    chat_history.insert(tk.END, "Você: " + user_input + "\n\n")
    chat_history.config(state="disabled")

    convo.send_message(user_input)
    response = convo.last.text

    chat_history.config(state="normal")
    chat_history.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_history.config(state="disabled")
    chat_history.see(tk.END)


window = tk.Tk()
window.title("Chatbot Cinéfilo")

chat_history = tk.Text(window, state="disabled")
chat_history.pack()

input_frame = tk.Frame(window)
input_frame.pack()

input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side="left")

send_button = tk.Button(input_frame, text="Enviar", command=send_message)
send_button.pack(side="left")

window.mainloop()
