import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from spellchecker import SpellChecker
from nltk.corpus import wordnet

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.spellchecker = SpellChecker()
        self.cached_synonyms = {}

    def preprocess_text(self, text):
        # Spell check and correct text
        corrected_text = ' '.join([self.spellchecker.correction(word) for word in text.split()])
        return corrected_text

    def vectorize_text(self, text):
        # Use TF-IDF for vectorization
        processed_text = self.preprocess_text(text)
        return self.vectorizer.fit_transform([processed_text]).toarray()

    def get_synonyms(self, word):
        if word in self.cached_synonyms:
            return self.cached_synonyms[word]
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        self.cached_synonyms[word] = synonyms
        return synonyms

    def expand_with_synonyms(self, text):
        words = text.split()
        expanded_words = set(words)
        for word in words:
            synonyms = self.get_synonyms(word)
            expanded_words.update(synonyms)
        return ' '.join(expanded_words)

    def diagnose(self, problem):
        problem_vector = self.vectorize_text(problem)
        best_match = None
        best_score = 0
        for issue in self.knowledge_base:
            expanded_issue = self.expand_with_synonyms(issue['problem'])
            issue_vector = self.vectorizer.transform([expanded_issue]).toarray()
            score = cosine_similarity(problem_vector, issue_vector)[0][0]
            if score > best_score:
                best_score = score
                best_match = issue
        return best_match['solution'] if best_match else "No solution found"

# Load knowledge base
def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from spellchecker import SpellChecker
from nltk.corpus import wordnet

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.spellchecker = SpellChecker()
        self.cached_synonyms = {}

    def preprocess_text(self, text):
        # Spell check and correct text
        corrected_text = ' '.join([self.spellchecker.correction(word) for word in text.split()])
        return corrected_text

    def vectorize_text(self, text):
        # Use TF-IDF for vectorization
        processed_text = self.preprocess_text(text)
        return self.vectorizer.fit_transform([processed_text]).toarray()

    def get_synonyms(self, word):
        if word in self.cached_synonyms:
            return self.cached_synonyms[word]
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        self.cached_synonyms[word] = synonyms
        return synonyms

    def expand_with_synonyms(self, text):
        words = text.split()
        expanded_words = set(words)
        for word in words:
            synonyms = self.get_synonyms(word)
            expanded_words.update(synonyms)
        return ' '.join(expanded_words)

    def diagnose(self, problem):
        problem_vector = self.vectorize_text(problem)
        best_match = None
        best_score = 0
        for issue in self.knowledge_base:
            expanded_issue = self.expand_with_synonyms(issue['problem'])
            issue_vector = self.vectorizer.transform([expanded_issue]).toarray()
            score = cosine_similarity(problem_vector, issue_vector)[0][0]
            if score > best_score:
                best_score = score
                best_match = issue
        return best_match['solution'] if best_match else "No solution found"

# Load knowledge base
def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
