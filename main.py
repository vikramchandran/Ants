#!/Users/vikramchandran/anaconda3/bin/python
from cliparser.parser import Parser
from cliparser.security import Token




if __name__ == "__main__":
    # Resource owner's credentials
    parser = Parser()
    token = Token()
    parser.checkforupdate()
    parser.runparser()
    #acc_token = token.getacctoken()
    #token.tradeoff(acc_token)
