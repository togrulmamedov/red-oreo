import fasttext

class ModuleBuilder:

    def __init__(self):
        print "Initializing ModuleBuilder"

    def buildModel(self, filePath):
        model = fasttext.skipgram(filePath, 'model')
        return model

    def loadModel(self, model):
        return fasttext.load_model(model)

    def getVecOfTheWord(self, model, word):
        return model.words(word)

    def getWordsInDictionaty(self, model):
        return model.words




