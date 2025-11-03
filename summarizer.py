import sys, re, math

def tokenize_sentences(text):
    # naive sentence splitter that handles ., !, ?
    # keeps periods in abbreviations from breaking (roughly)
    text = re.sub(r'\s+', ' ', text.strip())
    sents = re.split(r'(?<=[.!?])\s+', text)
    return [s for s in sents if s]

STOP = set("""a an the and or but if while to of in for on at from by with about as into like through after over between out against during without before under around among is are was were be been being have has had do does did will would should can could i you he she it we they them me my your his her our their this that these those not no""".split())

def word_score(text):
    words = [w.lower() for w in re.findall(r"[a-zA-Z']+", text)]
    freq = {}
    for w in words:
        if w in STOP: 
            continue
        freq[w] = freq.get(w, 0) + 1
    # log-scaled weights
    for w in list(freq):
        freq[w] = 1 + math.log(freq[w])
    return freq

def sentence_score(sent, weights):
    words = [w.lower() for w in re.findall(r"[a-zA-Z']+", sent)]
    if not words: 
        return 0.0
    return sum(weights.get(w, 0) for w in words) / len(words)

def summarize(text, n=3):
    sents = tokenize_sentences(text)
    weights = word_score(text)
    ranked = sorted(((sentence_score(s, weights), i, s) for i, s in enumerate(sents)), reverse=True)
    # keep original order among top-N
    top = sorted(ranked[:n], key=lambda x: x[1])
    return [s for _, _, s in top]

def main():
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    summary = summarize(text, n=3)
    for s in summary:
        print(s)

if __name__ == "__main__":
    main()
