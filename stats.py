def get_num_words(text):
    each_word = text.split()
    num_words = len(each_word)
    return num_words

def count_characters(text):
    dict_list = {}
    counter = 0
    for item in text:
        letter = item.lower()
        if letter in dict_list:
            dict_list[letter] +=1
        else:
            dict_list[letter] =1
    val_based_rev = {k: v for k, v in sorted(dict_list.items(), key=lambda item: item[1], reverse=True)}
    report = get_list(val_based_rev)
    return

    
def get_list(content_list):
    for key, value in content_list.items():
        print(f"{key}: {value}")
 
                


