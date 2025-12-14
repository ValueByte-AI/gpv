
from gpv import GPV

def main():
    
    texts = [
    "Today is a good day. I woke up early and went for a run in the park. The weather was perfect, and I felt energized. After my run, I had a healthy breakfast and spent some time reading a book. In the afternoon, I met up with some friends for lunch, and we had a great time catching up. I feel grateful for the wonderful day I had and look forward to more days like this...", # e.g., a blog post
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet, making it a popular choice for testing fonts and keyboard layouts. It's often used in typing practice and graphic design to showcase different typefaces. The phrase has been around since the late 19th century and continues to be a favorite among designers and typists alike...", # e.g., a pangram
    ]

    gpv = GPV(parsing_model_name="gpt-4o-mini", use_flash=True)
    results = gpv.parse_texts(texts)

    print(results)

if __name__ == "__main__":
    main()
