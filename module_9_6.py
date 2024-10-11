def all_variants(text):
    for text_size in range(len(text)):
        for start_index in range(len(text)-text_size):
            end_index = start_index + text_size + 1
            yield text[start_index:end_index]


a = all_variants("abc")
for i in a:
    print(i)
