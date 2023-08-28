#The purpose is to read in a file and calculate how much it cose to 
#purchase all the shares in the portfolio. 
# total_sum = 0
# with open ('Data/portfolio.dat','rb') as file:
#     for line in file:
#         columns = line.split()
#         product = int(columns[1])*float(columns[2])
#         total_sum = total_sum +product

# print(total_sum)

#now convert into a function
def portfolio_cost(file_name):
    total_sum = 0
    with open (file_name,'r')as file:
        for line in file:
            columns = line.split()
            try:
                product = int(columns[1])*float(columns[2])
                total_sum = total_sum +product
            except ValueError as e: 
                print("not parsed",repr(line))
                print('reason',e)
    return(total_sum)

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))

