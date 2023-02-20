def Lang(Syntax):
    with open("index.js", "w") as f:
        code = ""
        State = 0
        Token = ""
        String = ""
        OP_PR = 1
        for Char in Syntax:
            Token += Char
            if Token == " ":
                if State == 0:
                    Token = ""
 
            elif Token == "\n":
                Token = ""
 
            elif Token == "pr":
                OP_PR = 1
                Token = ""
    
            elif Token == "\"":
                if State == 0:
                    State = 1
                    Token = ""
    
                elif State == 1:
                    State = 0
                    if OP_PR == 1:
                        OP_PR = 0
                        code += f"console.log(\"{String}\");\n"
                        f.write(code)
                        
    
            elif State == 1:
                String += Token
                Token = ""
        print(code)
        f.write(code)
    
 
Content = open("Test.txt", "r").readlines()
for Line in Content:
    Lang(Line)
 