from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
import os

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-' #use open ai api key

llm = OpenAI(temperature=0.9)

def generate_greatest_11(country):
    # Prompt to suggest team name
    prompt_template_name = PromptTemplate(
        input_variables=['country'],
        template='Suggest me a fancy National Cricket Team name for {country}'
    )
    team_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='team_name')

    # Prompt to suggest all-time greatest players
    prompt_template_items = PromptTemplate(
        input_variables=['team_name'],
        template='Suggest the ALL Time Greatest 11 players for Cricket team called {team_name}. Return in comma-separated values.'
    )
    player_name_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='players')

    # SequentialChain to run both prompts sequentially
    chain = SequentialChain(
        chains=[team_chain, player_name_chain],
        input_variables=['country'],
        output_variables=['team_name', 'players']
    )

    # Run the chain with the provided country
    result = chain.invoke({'country': country})

    # Debugging: print raw result
    print("Raw result:", result)

    # Extract and clean the first team name
    team_name = result['team_name'].strip()

    # Extract and clean the first set of players (11 players)
    players = result['players'].strip()

    return {
        'team_name': team_name,
        'players': players
    }


if __name__ == '__main__':
    output = generate_greatest_11('England')
    print(f"Team Name: {output['team_name']}")
    print(f"Greatest 11 Players: {output['players']}")
