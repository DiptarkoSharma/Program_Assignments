#Stacks Exercise
#Write a function that can reverse a string using Stacks.
from stacks import Stack

def main():

    try:

        line = input('Please enter a line >')
        if len(line.strip())==0:
            raise Exception('You cant enter a blank line')
        else:
            rev_str = ''
            st = Stack()
            for ch in line:
                st.push_one(ch)
            
            while st.size()!=0:
                rev_str+=st.pop_one()
            print(f'Rev String is {rev_str}')


            

    except Exception as e:
        print(f'Error is {e}')

if __name__ =='__main__':
    main()

