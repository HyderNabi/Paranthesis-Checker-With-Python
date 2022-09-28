#Paranthesis Checker Using Stack (Lists as Stack)


Expression =""" 
    int main(void){
            int arr[10]  = {2,3,4,5,6,7,8,9};
            for(int i=0;i<10;i++)
            {
                printf("%d",&arr[i]);
            }
    } """
#Input Expression"""
#Expression = "(()))"

Opening_Braces = ['{','[','(']      #Opening Braces
Closig_Braces = ['}',']',')']       #Closing Braces
flag = False;
print("The Expression is : " +Expression)
Stack = list()          #Initially the Stack is empty

for exp in Expression:  #for each character in the Expression
    if exp in Opening_Braces:
        Stack.append(exp)   #push onto the stack if the character is the left Paranthesis
    elif exp in Closig_Braces:
        if len(Stack) != 0:
            Brace = Stack.pop()        #pop the top of the stack and check whether the top of the stack and the incomming symbol is equal
            if exp == "{":
                 if Brace != "}":    #If incomming symbol is '{' then the top of the stack should be '}'
                     break;
            elif exp =="[":         #If the incomming symbol is '[' the the top of the stack should be ']'
                 if Brace != "]":
                     break;
            elif exp == "(":        #if the incomming symbol is '(' then the top of the stack should be ')'
                if Brace != ")":
                     break;
        else:
            flag = True;

if len(Stack) == 0 and flag is False:     #if the stack is empty
    print(Expression +" : is Correctly Parenthesized")
else:
    print(Expression +" : is not Correctly Parenthesized")