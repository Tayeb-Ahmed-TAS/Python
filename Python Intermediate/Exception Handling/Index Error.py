text = "Taskin"  # ? Here => T = 0 , a = 1 , s = 2 , k = 3 , i = 4 , n = 5 ;

n = int(input("Enter the index from 0 to 5 => "))

try:
    print(text[n])

except IndexError:
    print(f"Index Error ! Index {n} is not available !")

print("End")
