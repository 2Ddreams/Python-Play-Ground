import random

f_word = ""

pre = ["flying", "hero"]
post = ["bobcat", "panda"]

pre_gen = random.choice(pre)
post_gen = random.choice(post)

f_word = f"{pre_gen} {post_gen}"

print(f_word)