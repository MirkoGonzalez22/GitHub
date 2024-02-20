import openai

# Configura tu clave de API
openai.api_key = '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'

# Define la función para generar el blog
def generate_blog(paragraph_topic):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3,
        n=1
    )

    retrieve_blog = response['choices'][0]['text']

    return retrieve_blog

# Prueba la función
print(generate_blog('Why NYC is better than your city.'))

