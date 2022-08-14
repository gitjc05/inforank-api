import spacy
import pytextrank

def ranker(text, sentence_lim):

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('textrank')
    
    sent_lim = int(sentence_lim)

    doc = nlp(text)
    half = ""

    for x in doc._.textrank.summary(limit_sentences=sent_lim):
        half += str(x) + " "

    second = ""
    result = ""

    l1 = half.split()

    for x in l1:
        second += x + " "
        if x[-1] == "." and x[-2] == x[-2].lower():
            result += second
            second = ""

    context = {
        'result': result,
        'sentence_limit': sent_lim
    }

    return context

