# Enter your code here. Read input from STDIN. Print output to STDOUT
while TRUE:
    try:
        N = int(raw_input().strip())

        if N == "done":
            break

        if N in range(1,21):
            for x in range(N):
                print (x**2)
        else:
            print(Input a number between 1 and 20.)
    except:
        print("Invalid number")
        continue
