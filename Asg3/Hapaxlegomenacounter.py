from nltk import word_tokenize
from nltk.probability import FreqDist

"""Returns the number of hapax legomena from the test, train, and validation sets"""
def count_words(filename):
    #Reads a file, counts the words, and saves the output in a dictionary
    infile = open(filename, 'r', encoding='utf-8')

    file = infile.read()

    infile.close()

    fdist = FreqDist(word.lower() for word in word_tokenize(file))

    return len(fdist.hapaxes())
    
  
      

print('Train DE: ', count_words('baseline/raw_data/train.de'))
print('Train EN: ', count_words('baseline/raw_data/train.de'))
print('Validation DE: ', count_words('baseline/raw_data/valid.de'))
print('Validation EN: ', count_words('baseline/raw_data/valid.en'))
print('Test DE: ', count_words('baseline/raw_data/test.de'))
print('Test EN: ', count_words('baseline/raw_data/test.en'))
