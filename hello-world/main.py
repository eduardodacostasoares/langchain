from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
load_dotenv()

def main():
    print("Hello from langchain-course!")

    information = '''
    Malenia was one of the twin children born to Queen Marika the Eternal and her second Elden Lord, Radagon. As Empyreans, both Malenia and her elder twin brother, Miquella, were candidates to ascend as gods of a new age. However, due to the nature of their parentage, the twins were afflicted with dreadful curses. Miquella was doomed with eternal nascency, while Malenia's body was ravaged by the scarlet rot.
    The scarlet rot plagued Malenia from within, gradually consuming her and leaving her disfigured. Over time, she lost her eyes and several limbs to the rot. Despite her suffering, Malenia fought valiantly to suppress the rot’s influence, refusing to succumb to its ruinous nature.
    Miquella worked tirelessly to undo the curses they had both inherited. While unable to find a cure for his sister within the Golden Order, Miquella designed a needle of unalloyed gold to keep the rot at bay. He also crafted the prostheses that enabled her to continue fighting. At some point, Malenia encountered the legendary blind swordsman of the Flowing Curved Sword, who had long ago sealed away an Outer God of Rot. The swordsman became her master, enabling her to gain wings of unparalleled strength. Malenia eventually became a peerless warrior and her brother's sworn blade and protector. After the Elden Ring was shattered, Malenia claimed a shard of the fractured Elden Ring. She would attract loyal servants like her Cleanrot Knights, who vowed to fight next to her, despite the inevitable gradual putrefaction of their flesh.
    During the Shattering, Malenia led an army that marched south from the Haligtree down the Bellum Highway. She won many battles against the other Demigods, even humbling fellow shardbearer, Godrick the Grafted,[10] who groveled at her feet for mercy after first insulting her and then suffering defeat. Malenia and her half-brother Radahn would eventually be the last two demigods left standing in the conflict. Their forces clashed in the Caelid Wilds, and the two fought the Battle of Aeonia, a bitter duel to fulfill an unhonored vow. In the midst of the combat with Radahn, Malenia unleashes Scarlet Rot, resulting in her first rotflower bloom.
    The rot did not kill Radahn but robbed him of his wits, turning him feral. Malenia herself was left slumbering in a coma. She was rescued by one of her Cleanrot Knights, Finlay, who carried her across the Lands Between. When Malenia and Finlay took refuge at the Shaded Castle, Maleigh Marais, the sickly-born head of House Marais, was naturally drawn to the unconscious Demigod. He saw in her his personal goddess. Finlay carried Malenia back to the Haligtree, far north of the Erdtree.
    The unleashed scarlet rot devastated Caelid, leaving it a rotting wasteland, and created the Swamp of Aeonia. Malenia inadvertently brought forth the Scarlet Butterflies and Kindred of Rot. The pests, including Sage Gowry, who worshipped her as a goddess and hoped to cause her to bloom once again, believing that she would usher in a new age of rot.[16] However, Malenia rejected her fate and never embraced the Servants of Rot.
    Miquella had encased himself within the Haligtree in an effort to create a new Erdtree of his very own, hopefully granting him the power to cure both his and his sister’s curses. However, during Malenia's absence, Miquella was ripped from the womb of the tree and taken away by Mohg, Lord of Blood before he could emerge from his cocoon. Malenia dreamt while awaiting Miquella's return, and the scarlet rot seeped out from her and began infecting the Haligtree. Malenia's slumber is eventually disturbed by a Tarnished, who found their way to the roots of the Haligtree. The two fight and Malenia finally meets her match, but she suffers her first true defeat. However, in the end, Malenia succumbs to the Scarlet Rot and blossoms yet again, reborn as a nascent goddess. She unleashes her full fury against the invader, but falls short yet again, her dying words an apology to her vanished brother. Having bloomed twice, Malenia withdraws within her scarlet blossom.'''
    
    summary_template = '''
    Given the information {information}, about a videogame character I want you to create:
    1. a short summary
    2. 2 interest facts about them
    '''

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    #llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    logging.info(f"{response.content}")

if __name__ == "__main__":
    main()
