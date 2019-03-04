def report_error_undeclared_identifier(t):
    print("Parse Error [Line " + str(t.currentToken().line_number) + "]: Identifier '" + t.currentToken().key + "' has not been declared")
    exit()

def report_error_expected_expresion(t):
    print("Parse Error [Line " + str(t.currentToken().line_number) + "]: Expected an expression, but got: '" + t.currentToken().key + "'")
    exit()

def report_error_expected_eof(t):
    print("Parse Error [Line " + str(t.currentToken().line_number) + "]: Expected end of file, but got: '" + t.currentToken().key + "'")
    exit()

def report_error_expected_statement(t):
    print("Parse Error: [Line " + str(t.currentToken().line_number) + "] Expected statement but got: '" + t.currentToken().key + "'")
    exit()
