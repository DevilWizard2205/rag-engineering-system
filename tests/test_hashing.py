from app.ingestion.utils import generate_content_hash


text_1 = "Retrieval Augmented Generation"

text_2 = "Retrieval Augmented Generation"

text_3 = "Something completely different"


hash_1 = generate_content_hash(text_1)
hash_2 = generate_content_hash(text_2)
hash_3 = generate_content_hash(text_3)


print("Hash 1:", hash_1)
print("Hash 2:", hash_2)
print("Hash 3:", hash_3)

print()
print("Same content:", hash_1 == hash_2)
print("Different content:", hash_1 != hash_3)