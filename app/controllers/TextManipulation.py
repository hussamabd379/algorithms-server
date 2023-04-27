from app.core.Controller import Controller
from app.core.Response import Response
import logging
import json
import random
class TextManipulation(Controller):

    def calculateSimilarity(self,language,algorithm,firstText,firstTextType,firstTextSentencesCount,secondText,secondTextType,secondTextSentencesCount):

        responseBody = json.dumps({
            'success': True,
            'similarity_score' : random.randint(0,100),
            'similar_calculation_explination' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        })
        return Response(body=responseBody)