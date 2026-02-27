ast = {
  "VariableDeclaration": {
    "TYPE": None,
    "VALUE": None,
    "NAME": None,
  },
  "BinaryExpression": {
    "LEFT": None,
    "RIGHT": None,
    "SYMBOL": None,
  },
  "FunctionCalls": {
    "FUNCTION": {
      "ARGUMENT": None,
      "NAME": None
    }
  }
}
types = ["int", "str", "bool", "list"]
ops = ["+", "-", "/", "*"]
identifiers = ["print"]
builtins = ["print", "scanf"]
def to_ast(line):
    line = line.split()
    operator = line[0]
    if operator in types:
      ast["VariableDeclaration"]["VALUE"] = "".join(line[3:])
      ast["VariableDeclaration"]["NAME"] = line[1]
      ast["VariableDeclaration"]["TYPE"] = line[0]
      print(ast["VariableDeclaration"])
    elif len(line) == 3:
      if line[1] in ops:
        ast["BinaryExpression"]["LEFT"] = line[0]
        ast["BinaryExpression"]["RIGHT"] = line[2]
        ast["BinaryExpression"]["SYMBOL"] = line[1]
        print(ast["BinaryExpression"])
    elif operator in identifiers:
      if operator.lower() in builtins:
        ast["FunctionCalls"]["FUNCTION"]["ARGUMENT"] = line[1]
        ast["FunctionCalls"]["FUNCTION"]["NAME"] = line[0]
        print(ast["FunctionCalls"])
    else:
      pass