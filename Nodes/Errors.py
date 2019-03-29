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

def report_error_match_consume(expected, t):
    print("Parse Error [Line " + str(t.currentToken().line_number) + "]: Expected: '" + expected + "', but got: '"+ t.currentToken().key + "" + "'")
    exit()

def report_error_uninitialized_identifier(id):
    print("Run-time Error: Identifier \'" + id.get_name() + "\' must be initialized before it can be used.")
    exit()

def report_error_duplicate_identifier(t):
    print("Parse Error: [Line " + str(t.currentToken().line_number) + "] Duplicate declaration of identifier: '" + t.currentToken().key + "'")
    exit()

def report_error_not_an_int(id, val):
    print("Run-time Error: Value of \'" + id.get_name() + "\' must be set to an int, not \'" + val + "\'")
    exit()
