#a. POS Tagging 
import re


def fill_missing_tags(sentence):
    # Extract all existing tags
    tags = re.findall(r'/([A-Z]+)(?=\s|,|\.)', sentence)
    existing_tags = set(tags)
     
    # Split the sentence into tokens while preserving delimiters
    tokens = re.split(r'(\s|,|\.)', sentence)
     
    for i in range(len(tokens)):
        token = tokens[i]
        if '?' in token:
            # Split the word and the missing tag
            parts = token.split('/')
            word = parts[0]
            missing_tag = parts[1]
             
            # Determine the required tag length
            tag_length = len(missing_tag)
             
            # Find possible tags of the required length
            possible_tags = [tag for tag in existing_tags if len(tag) == tag_length]
             
            # Choose the most appropriate tag based on context
            if tag_length == 2:
                if word.lower() in ['system', 'star', 'computer', 'book', 'table']:
                    chosen_tag = 'NN'  # Noun
                elif word.lower() in ['is', 'am', 'are']:
                    chosen_tag = 'VB'  # Verb
                else:
                    chosen_tag = possible_tags[0] if possible_tags else 'NN'
            elif tag_length == 3:
                if word.lower() in ['caught', 'seen', 'done']:
                    chosen_tag = 'VBN'  # Past participle
                elif word.lower() in ['was', 'were']:
                    chosen_tag = 'VBD'  # Past tense verb
                else:
                    chosen_tag = possible_tags[0] if possible_tags else 'VBN'
             
            # Replace the missing tag
            tokens[i] = f"{word}/{chosen_tag}"
     
    # Reconstruct the sentence
    filled_sentence = ''.join(tokens)
    return filled_sentence


def main():
    # Sample input with missing tags
    sample_input = "She/PRP watched/??? the/DT movie/?? last/JJ night/NN, and/CC it/PRP was/VBD amazing/JJ."


    print("Input sentence:", sample_input)
   
    # Fill in the missing tags
    output_sentence = fill_missing_tags(sample_input)
   
    # Print the output
    print("\nOutput sentence:", output_sentence)


if __name__ == "__main__":
    main()