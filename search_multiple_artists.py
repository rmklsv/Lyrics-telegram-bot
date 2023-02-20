import re
from random import shuffle


def search_lyrics_artist1(text: str) -> set:
    with open('artist1_lyrics.txt', encoding='utf-8') as tasks:
        words = [word.lower() for word in text.split()]
        results = set()
        lyrics = tasks.readlines()
        for i, line in enumerate(lyrics):
            if len(words) == 1:
                if words[0] in re.sub(r'[^\w\s]', ' ', line.lower()).split():
                    if i > 0:
                        prev_line = lyrics[i-1]
                    else:
                        prev_line = ''
                    if i < len(lyrics) - 1:
                        next_line = lyrics[i+1]
                    else:
                        next_line = ''
                    if prev_line.strip() == '':
                        results.add(line.strip()
                                    + ' \n'
                                    + next_line.strip())
                    else:    
                        results.add(prev_line.strip()
                                    + ' \n'
                                    + line.strip()
                                    + ' \n'
                                    + next_line.strip())
            else:
                if re.search(r'\b'+text.lower()+r'\W', line.lower()):
                    if i > 0:
                        prev_line = lyrics[i-1]
                    else:
                        prev_line = ''
                    if i < len(lyrics) - 1:
                        next_line = lyrics[i+1]
                    else:
                        next_line = ''
                    if prev_line.strip() == '':
                        results.add(line.strip()
                                    + ' \n'
                                    + next_line.strip())
                    else:    
                        results.add(prev_line.strip()
                                    + ' \n'
                                    + line.strip()
                                    + ' \n'
                                    + next_line.strip())
        if len(results) > 0:
            random_results = list(results)
            shuffle(random_results)            
            return random_results[0]
        else:
            return None

def search_lyrics_artist2(text: str) -> set:
    with open('artist2_lyrics.txt', encoding='utf-8') as tasks:
        words = [word.lower() for word in text.split()]
        results = set()
        lyrics = tasks.readlines()
        for i, line in enumerate(lyrics):
            if len(words) == 1:
                if words[0] in re.sub(r'[^\w\s]', ' ', line.lower()).split():
                    if i > 0:
                        prev_line = lyrics[i-1]
                    else:
                        prev_line = ''
                    if i < len(lyrics) - 1:
                        next_line = lyrics[i+1]
                    else:
                        next_line = ''
                    if prev_line.strip() == '':
                        results.add(line.strip()
                                    + ' \n'
                                    + next_line.strip())
                    else:    
                        results.add(prev_line.strip()
                                    + ' \n'
                                    + line.strip()
                                    + ' \n'
                                    + next_line.strip())
            else:
                if re.search(r'\b'+text.lower()+r'\W', line.lower()):
                    if i > 0:
                        prev_line = lyrics[i-1]
                    else:
                        prev_line = ''
                    if i < len(lyrics) - 1:
                        next_line = lyrics[i+1]
                    else:
                        next_line = ''
                    if prev_line.strip() == '':
                        results.add(line.strip()
                                    + ' \n'
                                    + next_line.strip())
                    else:    
                        results.add(prev_line.strip()
                                    + ' \n'
                                    + line.strip()
                                    + ' \n'
                                    + next_line.strip())
        if len(results) > 0:
            random_results = list(results)
            shuffle(random_results)            
            return random_results[0]
        else:
            return None