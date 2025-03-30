import random
import matplotlib.pyplot as plt

def roulette():
    roll=random.randint(0,36)
    if roll<19:
        return False
    else:
        return True
    
def even_roulette():
    roll=random.randint(1,36)
    if roll<19:
        return False
    else:
        return True

##############################################################################

def simple_bettor(funds,initial_wager,wager_count,sample_size):
    simple_busts=0
    simple_profits=0
    for i in range(sample_size):
        value=funds
        wager=initial_wager
        X=[]
        Y=[]
        currentWager=1
        while currentWager<=wager_count:
            if roulette():
                value+=wager
                #print(value)
                X.append(currentWager)
                Y.append(value)
            else:
                value-=wager
                #if (value-wager)<0:
                    #wager=value
                #print(value)
                X.append(currentWager)
                Y.append(value)
            currentWager+=1
        if value<=0:
            value='broke'
            #broke_count+=1
            simple_busts+=1
        elif (type(value)==int) and (value>funds):
            simple_profits+=1
        #print('Funds:', value)
        plt.title('Roleta com aposta simples')
        plt.xlabel('Número de jogadas')
        plt.ylabel('Montante (€)')
        plt.plot(X,Y)
    print('Survival rate:', str(100-(simple_busts/float(sample_size)) * 100), '%')
    print('Simple bettor bust chances:',str((float(simple_busts)/sample_size)*100.))
    print('Simpler bettor profit chances:',str((float(simple_profits)/sample_size)*100.))

def doubler_bettor(funds,initial_wager,wager_count,sample_size):
    doubler_busts=0
    doubler_profits=0
    for i in range(sample_size):
        value=funds
        wager=initial_wager
        X=[]
        Y=[]
        currentWager=1
        previousWager='win'
        previousWagerAmount=initial_wager
        while currentWager<=wager_count:
            if previousWager=='win':
                if roulette():
                    value+=wager
                    #print(value)
                    X.append(currentWager)
                    Y.append(value)
                else:
                    value-=wager
                    previousWager='loss'
                    #print(value)
                    previousWagerAmount=wager
                    X.append(currentWager)
                    Y.append(value)
                    if value<=0:
                        #print('we went broke after',currentWager,'bets')
                        doubler_busts+=1
                        break
            elif previousWager=='loss':
                #print('we lost the last one, so we will be smart and double')
                if roulette():
                    wager=previousWagerAmount*2
                    if (value-wager)<0:
                        wager=value
                    #print('we won', wager)
                    value+=wager
                    #print(value)
                    wager=initial_wager
                    previousWager='win'
                    X.append(currentWager)
                    Y.append(value)
                else:
                    wager=previousWagerAmount*2
                    if (value-wager)<0:
                        wager=value
                    #print('we lost',wager)
                    value-=wager
                    previousWagerAmount=wager
                    X.append(currentWager)
                    Y.append(value)
                    if value<=0:
                        #print('we went broke after',currentWager,'bets')
                        doubler_busts+=1
                        break
                    #print(value)
                    previousWager='loss'
            currentWager+=1
        #print(value)
        plt.title('Roleta simples e dupla')
        plt.xlabel('Número de jogadas')
        plt.ylabel('Montante (€)')
        plt.plot(X,Y)
        if value>funds:
            doubler_profits+=1
    print('survival rate:', str(100-(doubler_busts/float(sample_size)) * 100), '%')
    #print('Doubler bettor bust chances:',str((float(doubler_busts)/sample_size)*100.))
    #print('Doubler bettor profit chances:',str((float(doubler_profits)/sample_size)*100.))

def multiple_bettor(funds,initial_wager,wager_count,sample_size):
    lower_bust=100.0
    higher_profit=0.0
    best_multiple=2
    for i in range(sample_size):
        multiple_busts=0
        multiple_profits=0
        random_multiple=random.uniform(0.1,10)
        for i in range(sample_size):
            value=funds
            wager=initial_wager
            currentWager=1
            previousWager='win'
            previousWagerAmount=initial_wager
            while currentWager<=wager_count:
                if previousWager=='win':
                    if roulette():
                        value+=wager
                    else:
                        value-=wager
                        previousWager='loss'
                        previousWagerAmount=wager
                        if value<=0:
                            multiple_busts+=1
                            break
                elif previousWager=='loss':
                    if roulette():
                        wager=previousWagerAmount*random_multiple
                        if (value-wager)<0:
                            wager=value
                        value+=wager
                        wager=initial_wager
                        previousWager='win'
                    else:
                        wager=previousWagerAmount*random_multiple
                        if (value-wager)<0:
                            wager=value
                        value-=wager
                        previousWagerAmount=wager
                        if value<=0:
                            multiple_busts+=1
                            break
                        previousWager='loss'
                currentWager+=1
            if value>funds:
                multiple_profits+=1
        if ((float(multiple_busts)/sample_size)*100.0<lower_bust) and ((multiple_profits/float(sample_size))*100.0>higher_profit):
            lower_bust=(multiple_busts/float(sample_size))*100.0
            higher_profit=(multiple_profits/float(sample_size))*100.0
            best_multiple=random_multiple
    print('Best multiple:',best_multiple,'\nBust rate:',lower_bust,'\nProfit rate:',higher_profit)
            
def choice_bettor(funds,initial_wager,wager_count,sample_size,choice_multiple):
    choice_multiple_busts=0
    choice_multiple_profits=0
    for i in range(sample_size):
        value=funds
        wager=initial_wager
        X=[]
        Y=[]
        currentWager=1
        previousWager='win'
        previousWagerAmount=initial_wager
        while currentWager<=wager_count:
            if previousWager=='win':
                if roulette():
                    value+=wager
                    #print(value)
                    X.append(currentWager)
                    Y.append(value)
                else:
                    value-=wager
                    previousWager='loss'
                    #print(value)
                    previousWagerAmount=wager
                    X.append(currentWager)
                    Y.append(value)
                    if value<=0:
                        #print('we went broke after',currentWager,'bets')
                        choice_multiple_busts+=1
                        break
            elif previousWager=='loss':
                #print('we lost the last one, so we will be smart and double')
                if roulette():
                    wager=previousWagerAmount*choice_multiple
                    if (value-wager)<0:
                        wager=value
                    #print('we won', wager)
                    value+=wager
                    #print(value)
                    wager=initial_wager
                    previousWager='win'
                    #X.append(currentWager)
                    #Y.append(value)
                else:
                    wager=previousWagerAmount*choice_multiple
                    if (value-wager)<0:
                        wager=value
                    #print('we lost',wager)
                    value-=wager
                    previousWagerAmount=wager
                    #X.append(currentWager)
                    #Y.append(value)
                    if value<=0:
                        #print('we went broke after',currentWager,'bets')
                        choice_multiple_busts+=1
                        break
                    #print(value)
                    previousWager='loss'
            currentWager+=1
        #print(value)
        plt.title('Roleta com múltiplo:'+str(choice_multiple))
        plt.xlabel('Número de jogadas')
        plt.ylabel('Montante (€)')
        plt.plot(X,Y)
        if value>funds:
            choice_multiple_profits+=1
    #print('Choice bettor:', str(choice_bettor))
    #print('Choice bettor bust chances:',str((float(choice_multiple_busts)/sample_size)*100.))
    #print('Choice bettor profit chances:',str((float(choice_multiple_profits)/sample_size)*100.))     
            
def dAlembert(funds,initial_wager,wager_count,sample_size):
    global_invested=0.
    global_return_of_investment=0.
    global_da_busts=0.
    global_da_profits=0. 
    for i in range(sample_size):
        ret=0.
        da_busts=0.
        da_profits=0.
        total_invested=0. 
        for i in range(sample_size):
            value=funds
            wager=initial_wager
            currentWager=1
            previousWager='win'
            previousWagerAmount=initial_wager 
            while currentWager<=wager_count:
                if previousWager=='win':
                    if wager==initial_wager:
                        pass
                    else:
                        wager-=initial_wager
                    #print('current wager:',wager,'value',value)
                    if even_roulette():
                        value+=wager
                        #print('we won, current value:',value)
                        previousWagerAmount=wager
                    else:
                        value-=wager
                        previousWager='loss'
                        #print('we lost, current value:',value)
                        previousWagerAmount=wager
                        if value<=0:
                            da_busts+=1
                            break
                elif previousWager=='loss':
                    wager=previousWagerAmount+initial_wager
                    if(value-wager)<=0:
                        wager=value
                    #print('lost the last wager, current wager:',wager,'value',value)
                    if even_roulette():
                        value+=wager
                        #print('we won, current value:',value)
                        previousWagerAmount=wager
                        previousWager='win'
                    else:
                        value-=wager
                        #print('we lost, current value:',value)
                        previousWagerAmount=wager
                        if value<=0:
                            da_busts+=1
                            break
                    currentWager+=1
            if value>funds:
                da_profits+=1
            #print(value)
            ret+=value
        return_of_investment=ret-sample_size*funds
        total_invested=sample_size*funds
        #percent_return_of_investement=(return_of_investment/total_invested)*100.
        global_return_of_investment+=return_of_investment
        global_invested+=total_invested
        global_da_busts+=da_busts
        global_da_profits+=da_profits
        #print('Total invested:', sample_size*funds)
        #print('Total Return:',ret)
        #print('Return of investment:',return_of_investment)
        #print('Percent of return of investment:',percent_return_of_investement,'%')
        #print('Bust Rate:',(da_busts/sample_size)*100.00)
        #print('Profit rate:',(da_profits/sample_size)*100.00)
    percent_global_return_of_investement=(global_return_of_investment/global_invested)*100.00
    print('Percent of return of investment:',percent_global_return_of_investement,'%')
    print('Bust Rate:',(global_da_busts/(sample_size**2)*100.),'%')
    print('Profit rate:',(global_da_profits/sample_size**2)*100.,'%')
            
#simple_bettor(1000,10,100000,100)
#doubler_bettor(1000,10,100000,100)
#multiple_bettor(1000,10,100,100)
#choice_bettor(1000,10,1000,100,1.7045702822482716)
#dAlembert(1000,10,1000,1000)
#plt.axhline(y = 1000, color = 'k', linestyle = '-')
#plt.axhline(y = 0, color = 'r', linestyle = '-')
