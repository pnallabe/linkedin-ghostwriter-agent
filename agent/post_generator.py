import datetime
from .rag_chain import get_rag_chain
from .config import TOPICS

def generate_post():
    day_idx = datetime.datetime.now().weekday() % len(TOPICS)
    topic = TOPICS[day_idx]
    chain = get_rag_chain()
    prompt = f"Write a 200 word professional, insightful LinkedIn post about '{topic}' using my background as context. Include a hook, body, and call-to-action."
    post = chain.run(prompt)

    print("\n[LinkedIn Post for Today]:\n")
    print(post)
    with open("output/linkedin_post.txt", "w") as f:
        f.write(post)
